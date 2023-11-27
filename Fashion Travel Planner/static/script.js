window.onload = admin;

//fucntion to switch tab for forms in register and list pages
const toggleForm = () => {
  const formContainer = document.querySelector('.form_container');
  formContainer.classList.toggle('active');
};

//weather function
const apiKey = "b142cf15080064a844f6c6ec97d25af5";
const apiUrl = "https://api.openweathermap.org/data/2.5/weather?units=metric&q=";

const searchBox = document.querySelector('.searchInput');
const searchBtn = document.querySelector('.searchButton');
const weatherIcon = document.querySelector('.weather_icon');

async function checkWeather(city) {
  //get city entered and get api key
  const response = await fetch(apiUrl + city + "&appid=" + apiKey);
  var data = await response.json();

  //change display icon as per json response
  if (data.weather[0].main == "Clouds") {
    weatherIcon.src = "/static/images/icons/clouds.png";
  } else if (data.weather[0].main == "Clear") {
    weatherIcon.src = "/static/images/icons/clear.png";
  } else if (data.weather[0].main == "Thunderstorm") {
    weatherIcon.src = "/static/images/icons/thunderstorm.png";
  } else if (data.weather[0].main == "Rain") {
    weatherIcon.src = "/static/images/icons/rain.png";
  } else if (data.weather[0].main == "Drizzle") {
    weatherIcon.src = "/static/images/icons/drizzle.png";
  } else if (data.weather[0].main == "Snow") {
    weatherIcon.src = "/static/images/icons/snow.png";
  } else if (data.weather[0].main == "Mist") {
    weatherIcon.src = "/static/images/icons/mist.png";
  } else {
    weatherIcon.src = "/static/images/icons/clear.png";
  }
  //display the response on the html
  document.querySelector('.weather_place').innerHTML = data.name;
  document.querySelector('.humidity').innerHTML = data.main.humidity + "%";
  document.querySelector('.weather_temp').innerHTML = Math.round(data.main.temp) + "°C";
  document.querySelector('.wind').innerHTML = data.wind.speed.toFixed(1) + " km/h";
  document.querySelector('.rainy').innerText = data.rain && data.rain["1h"] ? data.rain["1h"] : "0" + "mm";

  document.getElementById('temperature').value = Math.round(data.main.temp);
  document.getElementById('rain').value = data.rain && data.rain["1h"] ? data.rain["1h"] : "0";

}

searchBtn.addEventListener("click", () => {
  checkWeather(searchBox.value);
})

//function to provide admin access 
function admin() {
  adminName = document.getElementById("nametag").innerText;

  if (adminName == "Hey misbah!") {
    document.getElementById("admintag").style.display = "block";
  }
  else {
    document.getElementById("admintag").style.display = "none";
  }
}

