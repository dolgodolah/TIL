const nameContainer = document.querySelector(".js-name");

function saveName(text) {
    localStorage.setItem("username", text);
}

function handleSubmit(event) {
    //form에서 submit이 처리될 때 기본적으로 새로고침되는 것을 막는다.
    event.preventDefault();
    const form = event.target;
    const input = form.querySelector("input");
    const value = input.value;

    //form에서 input을 통해 받은 값을 value에 넣고
    //localStorage에 저장하는 saveName(), value를 출력해주는 paintName()을 호출한다.
    saveName(value);
    paintName(value);
}

function askForName() {

    //<input></input>을 생성한다.
    const input = document.createElement("input");
    input.placeholder = "What is your name?";
    input.type = "text";
    input.className = "name__input";

    //<form></form>을 생성하여 위의 <input>을 삽입한다.
    const form = document.createElement("form");
    //<form>은 submit 발생 시 handleSubmit()을 호출한다.
    form.addEventListener("submit", handleSubmit);
    form.appendChild(input);

    //nameContainer에 위에서 만든 form을 추가한다.
    nameContainer.appendChild(form);
}

function paintName(text) {
    //nameContainer의 내부를 비우고, 인사말 span을 삽입한다.
    //<form><input></input></form>  --> <span></span>
    nameContainer.innerHTML = "";
    const span = document.createElement("span");
    span.className = "name__text";
    span.innerText = `Hello ${text}`;
    nameContainer.appendChild(span);
}

function loadName() {
    //localStorage로 부터 'username'을 가져온다.
    const currentUser = localStorage.getItem("username");

    //null값이면 currentUser의 입력을 요청하는 askForName()을 호출, 값이 있다면 paintName()을 호출한다.
    if (currentUser === null) {
        askForName();
    } else {
        paintName(currentUser);
    }
}

function init() {
    loadName();
}

init();