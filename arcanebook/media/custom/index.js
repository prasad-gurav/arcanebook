// LogIn function 
function login(){
    var username = document.querySelector('#Username').value
    var password = document.querySelector('#Password').value
    var csrf = document.querySelector('#csrf').value
    
    if(username == '' || password == ''){
        console.log("feilds must not be empty ")
        alert("Feilds must not be empty")
    }

    var data  = {
        'username':username,
        'password':password

    }   
    
    fetch('api/login/',{
        method : 'POST',
        headers :{
            'Content-Type':'application/json',
            'X-CSRFToken': csrf
        },
        'body':JSON.stringify(data)


    }).then(result => result.json())
    .then(response => {
        console.log(response)
        if(response.status == 200){
            window.location('/')
        }
    })
}