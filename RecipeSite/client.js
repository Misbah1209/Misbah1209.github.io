window.onload=display;

var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("slide");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "block";
}

// this function displays home page sections
function display(){
  document.getElementById("hidden").style.display = "block";
  document.getElementById("hidden2").style.display = "block";
  document.getElementById("add").style.visibility="hidden";
  document.getElementById("profilePage").style.display = "none";
 // document.getElementById("food").innerHTML="";
  //allRecipe();
  document.getElementById('fud').style.display='none';
}

// this function displays Add recpe page and hides home page sections
function profile(){
  document.getElementById("hidden").style.display = "none";
  document.getElementById("hidden2").style.display = "none";
  document.getElementById("profilePage").style.display = "block";
}

// This function checks the password input to ensure both are same.
function validatePswd(){
  pass1=document.getElementById("pswd").value;
  pass2=document.getElementById("pswd1").value;

  if(pass1!=pass2)
  {
      document.getElementById("regMessage").innerText="Passwords do not match";
  }
  else
  {
      document.getElementById("regMessage").innerText="";
  }
}

/*user registration funtion */
function addUser() {
  //Set up XMLHttpRequest
  let xhttp = new XMLHttpRequest();

  //Extract user data
  let firstName = document.getElementById("fname").value;
  let lastName = document.getElementById("lname").value;
  let nationality = document.getElementById("place").value;
  let DOB = document.getElementById("dob").value;
  let email = document.getElementById("email").value;
  let password = document.getElementById("pswd").value;
  
  //Create object with user data
  let user = {
    firstName: firstName,
    lastName:lastName,
    nationality:nationality,
    birthday:DOB,
    email: email,
    password:password
  };
  
    //Send new user data to server
    xhttp.open("POST", "/user", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send( JSON.stringify(user) );

  //Set up function that is called when reply received from server
  xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("regMessage").innerHTML="Successful Registration";
      }
      else {
        document.getElementById("regMessage").innerHTML="Unsuccessful Registration";
      }
    };
    return false;
 }

 /*user login and checking login funtion */
 function login()
{
  //Set up XMLHttpRequest
  let xhttp = new XMLHttpRequest();

  //Extract login user data
  let firstName = document.getElementById("uname").value;
  let password = document.getElementById("psw").value;
  
  //Create object with user data
  let userLog = {
    firstName: firstName,
    password:password
  };

 //Set up function that is called when reply received from server
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) 
    {
      if(xhttp.responseText=="false")
      {
        document.getElementById("logMessage").innerHTML="Unsuccessful Login";
      }
    else 
      {
        document.getElementById("logMessage").innerHTML="Successful Login";
        let usrArr = JSON.parse(xhttp.responseText);
        let logId=usrArr[0].username;
        document.getElementById("user").innerHTML=logId;
        document.getElementById("add").style.visibility="visible";
      }
    }
  };

    //Send new user data to server
    xhttp.open("POST", "/login", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send( JSON.stringify(userLog) );
   

 return false;
}

/*user logout funtion */
function logout(){
  //Set up XMLHttpRequest
  let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = () => {//Called when data returns from server
    if (xhttp.readyState == 4 && xhttp.status == 200) {
      if(xhttp.responseText=="LoggedOut")
      {
        document.getElementById("logMessage").innerHTML="You have been logged out";
        document.getElementById("user").innerHTML="";
        document.getElementById("add").style.visibility="hidden";
      }
      else{document.getElementById("logMessage").innerHTML="Error Logging out"+xhttp.responseText;}
    }
  };

  //Request data for all customers
  xhttp.open("GET", "/logout", true);
  xhttp.send();
  return false;
}

function addRecipe(){
  //Set up XMLHttpRequest
  let xhttp = new XMLHttpRequest();

  //Extract user data
  let userId = document.getElementById("user").innerHTML;
  let name = document.getElementById("title").value;
  let time = document.getElementById("time").value;
  let veg = document.getElementById("veg").value;
  let cuisine = document.getElementById("cuisine").value;
  let course = document.getElementById("course").value;
  let img = document.getElementById("img").value;
  let description = document.getElementById("desc").value;
  let Ingredients = document.getElementById("items").value;
  let Howto = document.getElementById("step").value;

  //Create object with user data
  let recipe = {
    userId: userId,
    name: name,
    time:time,
    veg:veg,
    cuisine:cuisine,
    course: course,
    img:img,
    description:description,
    Ingredients: Ingredients,
    Howto:Howto
  };
  
    //Send new user data to server
    xhttp.open("POST", "/recipe", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send( JSON.stringify(recipe) );

  //Set up function that is called when reply received from server
  xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("lblfood").innerHTML="Successful Added";
      }
      else {
        document.getElementById("lblfood").innerHTML="Unsuccessful Try again";
        console.log(xhttp.responseText);
      }
    };
    return false;
}

function allRecipe(){
  let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = () => {//Called when data returns from server
    if (xhttp.readyState == 4 && xhttp.status == 200) 
    {
      //Convert JSON to a JavaScript object
      let usrArr = JSON.parse(xhttp.responseText);

      //Return if no recipes
      if(usrArr.length === 0)
        return;

      let htmlStr="";
      //Build string with recipe data
      for(let i=0; i<usrArr.length; ++i){
        htmlStr += '<div class="recipeColumn">';
        htmlStr += '<div class="recipeCard">';
        htmlStr += '<div class="recipeColumn">';
        htmlStr += '<img src="'+ usrArr[i].img +'" alt="food" >';
        htmlStr += '</div><br>';
        htmlStr += '<h3>"'+ usrArr[i].name +'" </h3><br>';
        htmlStr += '<p>'+ usrArr[i].description +'</p><br>';
        htmlStr += '<p>Cook Time:'+ usrArr[i].time +'</p><br>';
        htmlStr += '<button onclick=\'showCard('+usrArr[i].Id+')\'>View</button>';
        htmlStr += '</div>';
        htmlStr += '</div>';
        htmlStr += '</div>';
      }
      //Add recipe to page.
      document.getElementById("food").innerHTML += htmlStr;           
    }
  };

  //Request data for all recipe
  xhttp.open("GET", "/allrecipe", true);
  xhttp.send();
}

function showCard(Id){

  let xhttp = new XMLHttpRequest();
  let flist={Id:Id};

 //Request data for all recipe
 xhttp.open("POST", "/thisRecipe", true);
 xhttp.setRequestHeader("Content-type", "application/json");
 xhttp.send(JSON.stringify(flist) );

  xhttp.onreadystatechange = () => {//Called when data returns from server
    if (xhttp.readyState == 4 && xhttp.status == 200) 
    {
      //Convert JSON to a JavaScript object
      let rList = JSON.parse(xhttp.responseText);

      //Return if no recipes
      if(rList.length === 0)
        return;     
      
      let htmlStr="";

      //Build string with recipe data
       for(let i=0; i<rList.length; ++i){
        htmlStr += '<form id="myfood"  class="reg-modal-content animate">';
        htmlStr += ' <br><h1 style="text-align:center;">'+ rList[i].name +'</h1>';
        htmlStr += '<div class="imgcontainer">';
        htmlStr += '<span onclick='+'document.getElementById("fud").style.display="none" class="close" title="Close Modal">&times;</span>';
        htmlStr += '<img src="'+ rList[i].img +'" alt="food" class="yummy">';
        htmlStr += ' <hr style=" border-top: 3px dotted black;">';
        htmlStr += ' </div><div class="container">';
        htmlStr += ' <div class="sign">';
        htmlStr += ' <div style="text-align: justify;text-justify: inter-word;" class="reg1">';
        htmlStr += ' <h1>Ingredients</h1><br>';
        htmlStr += rList[i].Ingredients ;
        htmlStr += ' <br><h1>Cuisine</h1>:'+ rList[i].cuisine;
        htmlStr += ' <br><h1>Course</h1>:'+ rList[i].course;
        htmlStr += ' </div><div  style="text-align: justify;text-justify: inter-word;" class="reg1">';
        htmlStr += ' <h1>Direction</h1> ';
        htmlStr += rList[i].Howto ;  
        htmlStr += ' </div></div></div></form>';   
      }
      //Add recipe to page.
      document.getElementById("fud").innerHTML += htmlStr;
      document.getElementById("fud").style.display='block' ;
  }
};
}

function Soup(){
  let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = () => {//Called when data returns from server
    if (xhttp.readyState == 4 && xhttp.status == 200) 
    {
      //Convert JSON to a JavaScript object
      let usrArr = JSON.parse(xhttp.responseText);

      //Return if no recipes
      if(usrArr.length === 0)
        return;
      document.getElementById("food").innerHTML = ""; 
      let htmlStr="";
      //Build string with recipe data
      for(let i=0; i<usrArr.length; ++i){
        htmlStr += '<div class="recipeColumn">';
        htmlStr += '<div class="recipeCard">';
        htmlStr += '<div class="recipeColumn">';
        htmlStr += '<img src="'+ usrArr[i].img +'" alt="food" >';
        htmlStr += '</div><br>';
        htmlStr += '<h3>"'+ usrArr[i].name +'" </h3><br>';
        htmlStr += '<p>'+ usrArr[i].description +'</p><br>';
        htmlStr += '<p>Cook Time:'+ usrArr[i].time +'</p><br>';
        htmlStr += '<button onclick=\'showCard('+usrArr[i].Id+')\'>View</button>';
        htmlStr += '</div>';
        htmlStr += '</div>';
        htmlStr += '</div>';
      }
      //Add recipe to page.
      document.getElementById("food").innerHTML += htmlStr;           
    }
  };

  //Request data for all recipe
  xhttp.open("GET", "/soup", true);
  xhttp.send();
}

function Entre(){
  let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = () => {//Called when data returns from server
    if (xhttp.readyState == 4 && xhttp.status == 200) 
    {
      //Convert JSON to a JavaScript object
      let usrArr = JSON.parse(xhttp.responseText);

      //Return if no recipe
      if(usrArr.length === 0)
        return;
      document.getElementById("food").innerHTML = ""; 
      let htmlStr="";
      //Build string with recipe data
      for(let i=0; i<usrArr.length; ++i){
        htmlStr += '<div class="recipeColumn">';
        htmlStr += '<div class="recipeCard">';
        htmlStr += '<div class="recipeColumn">';
        htmlStr += '<img src="'+ usrArr[i].img +'" alt="food" >';
        htmlStr += '</div><br>';
        htmlStr += '<h3>"'+ usrArr[i].name +'" </h3><br>';
        htmlStr += '<p>'+ usrArr[i].description +'</p><br>';
        htmlStr += '<p>Cook Time:'+ usrArr[i].time +'</p><br>';
        htmlStr += '<button onclick=\'showCard('+usrArr[i].Id+')\'>View</button>';
        htmlStr += '</div>';
        htmlStr += '</div>';
        htmlStr += '</div>';
      }
      //Add recipe to page.
      document.getElementById("food").innerHTML += htmlStr;           
    }
  };

  //Request data for all recipe
  xhttp.open("GET", "/Entre", true);
  xhttp.send();
}

function MainC(){
  let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = () => {//Called when data returns from server
    if (xhttp.readyState == 4 && xhttp.status == 200) 
    {
      //Convert JSON to a JavaScript object
      let usrArr = JSON.parse(xhttp.responseText);

      //Return if no recipe
      if(usrArr.length === 0)
        return;
      document.getElementById("food").innerHTML = ""; 
      let htmlStr="";
      //Build string with recipe data
      for(let i=0; i<usrArr.length; ++i){
        htmlStr += '<div class="recipeColumn">';
        htmlStr += '<div class="recipeCard">';
        htmlStr += '<div class="recipeColumn">';
        htmlStr += '<img src="'+ usrArr[i].img +'" alt="food" >';
        htmlStr += '</div><br>';
        htmlStr += '<h3>"'+ usrArr[i].name +'" </h3><br>';
        htmlStr += '<p>'+ usrArr[i].description +'</p><br>';
        htmlStr += '<p>Cook Time:'+ usrArr[i].time +'</p><br>';
        htmlStr += '<button onclick=\'showCard('+usrArr[i].Id+')\'>View</button>';
        htmlStr += '</div>';
        htmlStr += '</div>';
        htmlStr += '</div>';
      }
      //Add recipe to page.
      document.getElementById("food").innerHTML += htmlStr;           
    }
  };

  //Request data for all recipe
  xhttp.open("GET", "/MainC", true);
  xhttp.send();
}