

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
            window.location.replace('/')
        }
    })
}


// Sign Up function 
function signup(){
    var first_name = document.querySelector('#first_name').value
    var last_name = document.querySelector('#last_name').value
    var email = document.querySelector('#email').value
    var username = document.querySelector('#create-Username').value
    var password = document.querySelector('#create-Password').value
    var confirm_password = document.querySelector('#confirm-create-Password').value

    

    // csrf token
    var csrf = document.querySelector('#csrf').value
    

    if(username == '' || password == ''){
        console.log("feilds must not be empty ")
        alert("Feilds must not be empty")
    }
    if (!password==confirm_password){
        console.log("Confirm Your Password again")
        alert("Confirm Your Password again !")

    }
    var data  = {
        'first_name':first_name,
        'last_name':last_name,
        'email':email,
        'username':username,
        'password':password

    }   
    
    fetch('api/signup/',{
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
            window.location.replace('/')
        }
    })
}


function logout(){
    // csrf token
    var csrf = document.querySelector('#csrf').value
    fetch('api/logout/',{
        method : 'POST',
        headers :{
            'Content-Type':'application/json',
            'X-CSRFToken': csrf
        },
        


    }).then(result => result.json())
    .then(response => {
        console.log(response)
        if(response.status == 200){
            window.location.replace('/')
        }
    })
}