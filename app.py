from flask import Flask, render_template, request,jsonify
import pickle
import pymongo

app = Flask(__name__)

client=pymongo.MongoClient("mongodb://root:example@mongo:27017")
db=client.placement

model=pickle.load(open('model.pkl','rb'))

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        data=request.get_json()
 
        qa=float(data['qa'])
        lr=float(data['lr'])
        va=float(data['va'])
        programming=float(data['programming'])
        cn=float(data['cn'])/10
        dsa=float(data['dsa'])/10
        ml=float(data['ml'])/10
        os=float(data['os'])/10
        oop=float(data['oop'])/10
        dbms=float(data['dbms'])/10
        cgpa=float(data['cgpa'])
        activeBacklog=int(data['activeBacklogs'])
        deadBacklog=int(data['deadBacklogs'])

        if db.students.find_one({"email":data['email']}): 
            db.students.update_one({'email':data['email']},{"$set":data})
        else:
            db.students.insert_one(data)

        result = model.predict([[qa,lr,va,programming,cn,dsa,ml,os,oop,dbms,cgpa]])
        if result[0] == 1:
            print("yes")
            return jsonify({"success":True}),200
        if result[0]==0:
            print("no")
            return jsonify({"success":False}),200
        return jsonify({"error":"failed"}),400
    else:
        return render_template('index.html')

if __name__ == '__main__':
	app.run()
