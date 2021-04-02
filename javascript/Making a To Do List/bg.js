const body = document.querySelector("body");
const IMG_NUMBER = 4;

function handleImgLoad() {

}

function paintImage(imgNumber) {
    const image = new Image();
    image.src = `images/${imgNumber + 1}.jpg`;
    image.classList.add("bgImage");

    //append -> 뒤에 추가, prepend -> 맨앞에 추가
    body.prepend(image)
}

function generateRandom() {
    const number = Math.floor(Math.random() * IMG_NUMBER);
    return number;
}

function init() {
    const randomNumber = generateRandom();
    paintImage(randomNumber);
}

init();