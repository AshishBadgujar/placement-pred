const form = document.querySelector('form');
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const formProps = Object.fromEntries(formData);

    let obj = {}
    obj.role = formProps.role;
    obj.duration = formProps.duration;
    obj.company = formProps.company

    delete (formProps.role)
    delete (formProps.duration)
    delete (formProps.company)

    formProps.internship = obj

    console.log(formProps)
    try {
        let fetchResponse = await fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formProps)
        })
        let data = await fetchResponse.json()
        console.log("response=", data)
        if (data.success) {
            document.getElementById('submit-btn').classList.add('display-none')
            let div = document.getElementById('success')
            div.classList.remove("display-none");
        } else {
            document.getElementById('submit-btn').classList.add('display-none')
            let div = document.getElementById('fail')
            div.classList.remove("display-none");
        }

    } catch (error) {
        console.log(error)
    }
})