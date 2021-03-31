const form = document.querySelector(".js-form");
const input = form.querySelector("input");
const greeting = document.querySelector(".js-greetings");

const SHOWING_CN = "showing";
const USER_LS = "currentUser";

function saveName(text) {
    localStorage.setItem(USER_LS, text);
}

function handleSubmit(event) {
    //form에서 submit이 처리될 때 기본적으로 새로고침되는 것을 막는다.
    event.preventDefault();

    //form에서 input을 통해 받은 값을 currentValue에 넣고
    //localStorage에 저장하는 saveName(), currentValue를 출력해주는 paintGreeting()을 호출한다.
    const currentValue = input.value;
    saveName(currentValue);
    paintGreeting(currentValue);
}

function askForName() {
    //css에서 기본적으로 form의 display를 none으로 처리했기 때문에 form이 나타나지 않는다.
    //askForName()이 호출됐을 때만 나타나게 하기 위해 form의 클래스에 SHOWING_CN(showing)을 추가한다.
    //css에서 showing의 display를 block으로 했기 때문에 form이 나타난다.
    form.classList.add(SHOWING_CN);

    //해당 form에서의 submit이 들어올 때 handleSubmit()를 호출한다.
    form.addEventListener("submit", handleSubmit);
}

function paintGreeting(text) {
    form.classList.remove(SHOWING_CN);
    greeting.classList.add(SHOWING_CN);
    greeting.innerText = `Hello ${text}`;
}

function loadName() {
    //localStorage로 부터 USER_LS(currentUser)를 가져온다.
    const currentUser = localStorage.getItem(USER_LS);

    //null값이면 currentUser의 입력을 요청하는 askForName을 호출, 값이 있다면 paintGreeting을 호출한다.
    if (currentUser === null) {
        askForName();
    } else {
        paintGreeting(currentUser);
    }
}

function init() {
    loadName();
}

init();