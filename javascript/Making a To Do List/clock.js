const clockContainer = document.querySelector(".js-clock"); //document에서 첫 js-clock 클래스의 자식들을 가져온다.
const clockTitle = clockContainer.querySelector("h1"); //clockContainer에서 첫 h1 태그 내용을 가져온다.


function getTime() {
    const date = new Date();
    const minutes = date.getMinutes();
    const hours = date.getHours();
    const seconds = date.getSeconds();

    //clockTitle의 내용을 로컬 시간으로 변경한다.
    clockTitle.innerText = `${hours < 10 ? `0${hours}` : hours}:${minutes < 10 ? `0${minutes}` : minutes}:${seconds < 10 ? `0${seconds}` : seconds}`;
}

function init() {
    getTime();
    setInterval(getTime, 1000); //getTime()를 1초에 한번씩 호출한다.
}



init()