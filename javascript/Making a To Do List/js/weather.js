const weather = document.querySelector(".js-weather .weather__text");

const COORDS = "coords";
const API_KEY = "2a35e8f3a023c750aeb215e6c03d09b3";

function getWeather(lat, lon) {

    //fetch는 javascript의 비동기 통신을 위한 api이다.
    //날씨정보를 얻어오는 api가 정상적인 통신이 되어 날씨정보가 얻어지면 then 이하를 진행한다.
    fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`)
        .then(response => response.json())
        .then(json => {
            const temperature = json.main.temp;
            const place = json.name;
            weather.innerHTML = `${temperature}° @ ${place}`;
        });
}

function saveCoords(coordsObj) {
    localStorage.setItem(COORDS, JSON.stringify(coordsObj));
}

function handleGeoSuccess(position) {
    //javascript api를 통해 얻어진 position 데이터에서 latitude, longitude를 추출한다.
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;

    //저장을 위해서 하나의 객체로 만든다.
    const coordsObj = {
        latitude,
        longitude
    };
    saveCoords(coordsObj);

    //얻은 위도,경도 값으로 getWeather()를 호출한다.
    getWeather(latitude, longitude);
}

function handleGeoError() {
    console.log('Cant access geo location');
}

function askForCoords() {
    //javascript api로 현재 위치의 좌표값을 반환해준다.
    //정상적으로 좌표값이 얻어지면 handleGeoSuccess(), 아니면 handleGeoError()를 호출한다.
    navigator.geolocation.getCurrentPosition(handleGeoSuccess, handleGeoError);
}

function loadCoords() {
    const loadedCoords = localStorage.getItem(COORDS);
    //저장된 좌표값이 없으면 좌표값을 요청하고,
    //저장된 좌표값이 있다면 json형식으로 변환하고 getWeather에 필요한 값만 넘긴다.
    if (loadedCoords === null) {
        askForCoords();
    } else {
        const parsedCoords = JSON.parse(loadedCoords);
        getWeather(parsedCoords.latitude, parsedCoords.longitude);
    }
}

function init() {
    loadCoords()
}

init();