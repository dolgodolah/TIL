const toDoForm = document.querySelector(".js-toDoForm");
const toDoInput = toDoForm.querySelector("input");
const toDoList = document.querySelector(".js-toDoList");

const TODOS_LS = 'toDos';
let toDos = [];

function deleteToDo(event) {
    const btn = event.target;
    const li = btn.parentNode;
    toDoList.removeChild(li);

    //toDo.id가 li.id(삭제된 id)와 다른 것만 cleanToDos에 담는다.
    const cleanToDos = toDos.filter(function(toDo) {
        return toDo.id !== parseInt(li.id);
    });

    //새로 만들어진 cleanToDos를 toDos에 대입
    toDos = cleanToDos;
    saveToDos();
}

function saveToDos() {
    localStorage.setItem(TODOS_LS, JSON.stringify(toDos));
}

function paintToDo(text) {

    //html 구조 생성
    //  <li>
    //      <button>❌</button>
    //      <span>text</span>
    //  </li>
    const li = document.createElement("li");
    const delBtn = document.createElement("button");
    const span = document.createElement("span");
    const newId = toDos.length + 1;

    //delBtn은 click되면 deleteToDo를 호출한다.
    delBtn.innerText = "❌";
    delBtn.addEventListener("click", deleteToDo);

    span.innerText = text;
    li.appendChild(delBtn);
    li.appendChild(span);
    li.id = newId;
    toDoList.appendChild(li);

    //toDo를 하나의 객체로 만들어 toDos 리스트에 push
    const toDoObj = {
        text: text,
        id: newId
    };
    toDos.push(toDoObj);
}


function handleSubmit(event) {
    event.preventDefault(); //submit 발생 시 기본적으로 발생하는 이벤트를 막는다.
    const currentValue = toDoInput.value;
    paintToDo(currentValue);
    saveToDos();
    toDoInput.value = "";
}

function loadToDos() {
    //localStorage로부터 key가 TODOS_LS(="toDos")인것들을 불러온다.
    const loadedtoDos = localStorage.getItem(TODOS_LS);

    //저장된 것들이 있으면 paintToDo를 호출한다.
    if (loadedtoDos !== null) {
        const parsedToDos = JSON.parse(loadedtoDos);

        //(key,text)쌍의 json으로 파싱된 toDos들의 text들을 하나씩 paintToDo 한다.
        parsedToDos.forEach(function(toDo) {
            paintToDo(toDo.text);
        })
    }
}

function init() {
    loadToDos();

    //toDos가 load된 후에는 submit을 기다린다. submit 발생 시 handleSubmit 호출.
    toDoForm.addEventListener("submit", handleSubmit);
}

init();