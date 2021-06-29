   
//    Saving the data into local Storage and Creating Account
function saveData()
{
    let user={
        FirstName: document.getElementById("formReg").Firstname.value,
        LastName: document.getElementById("formReg").Surname.value,
        pass1: document.getElementById("formReg").pswd.value,
        email: document.getElementById("formReg").email.value,
        Phone: document.getElementById("formReg").phone.value,
        Address: document.getElementById("formReg").Address.value,
    };

    localStorage.setItem(user.email,JSON.stringify(user));
    document.getElementById("lblreg").innerText="Successfully Registered";
    
}

//    Deleting Account of Customer from local Storage
function unRegister()
{
    let Email=document.getElementById("formReg").email.value;
    if(localStorage.getItem(Email)!=undefined)
    {
        let passEntered=document.getElementById("formReg").pswd.value;
        let user=JSON.parse(localStorage.getItem(Email))

        if(passEntered==user.pass1)
        {
        localStorage.removeItem(Email);
        document.getElementById("lbllogin").innerText="We are sorry to see you go :(";
       
        }
        else{
        document.getElementById("lbllogin").innerText="Your account cannot be deleted; Wrong Password Entered";
        
        }
    }
    else{
    document.getElementById("lbllogin").innerText="Account does not exist!";
    
    }
}

//    Checking if password entered is same as password enter in the second password feild
function validatePassword()
{
    pass1=document.getElementById("formReg").pswd.value;
    pass2=document.getElementById("formReg").pswd1.value;

    if(pass1!=pass2)
    {
        document.getElementById("lblreg").innerText="Passwords do not match";
    }
    else
    {
        document.getElementById("lblreg").innerText="";
    }
}
   
// Checks if the Customer is logged in   
window.onload=function checkLog(){    
    for (let [key,value] of Object.entries(localStorage))
    {
    if (key=="loggedInUserName")
        {
            var  loggedUser=localStorage.getItem("loggedInUserName");
            var yourName=JSON.parse(localStorage.getItem(loggedUser));
            document.getElementById("message").innerText="Hello "+yourName.FirstName+"!";
        }
    }
}

//  Gets email from input and check if the user exists if yes it checks validity of password and adds to localstorage and session storage and logged in user else displays warning messages
function isUserRegistered()
{
    let Email=document.getElementById("formReg").email.value;
    if(localStorage.getItem(Email)!=undefined)
    {
        let user=JSON.parse(localStorage.getItem(Email));
        inputpassword=document.getElementById("formReg").pswd.value;
        if(user.pass1===inputpassword)
        {
            document.getElementById("message").innerText="Hello "+user.FirstName+"!";
            sessionStorage.loggedInUserName=user.email;

            localStorage.loggedInUserName=user.email;
            document.getElementById("lbllogin").innerText="";
        }
        else
            document.getElementById("lbllogin").innerText="incorrect password";
    }
        else 
             document.getElementById("lbllogin").innerText="no registered user";
}
    
//    Removes logged in user from local storage
     function logOut(){
         window.localStorage.removeItem('loggedInUserName');
    document.getElementById("message").innerText="Join Us";
    }