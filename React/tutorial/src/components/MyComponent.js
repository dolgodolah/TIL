import React from 'react'


/*
ES6의 화살표 함수
기존 function 을 이용한 함수 선언 방식을 아예 대체하지는 않는다.
이 문법은 주로 함수를 파라미터로 전달할 때 유용하다.

기존 function
setTimeout(function() {
    console.log('hello');
}, 1000);

화살표 함수
setTimeout(() => {
    console.log('hello');
}, 1000);
 */

const MyComponent = () => {
    return <div>새로운 컴포넌트</div>
}

function BlackDog() {
    this.name = '흰둥이';
    return {
        name: '검둥이',
        // 기존 function
        bark: function() {
            console.log(this.name + ': 멍멍!');
        }
    }
}

// 화살표 function
function WhiteDog() {
    this.name = '검둥이';
    return {
        name: '검둥이',
        // 화살표 function
        bark: () => {
            console.log(this.name + ': 멍멍!');
        }
    }
}

const blackDog = new BlackDog();
blackDog.bark(); // 검둥이 : 멍멍!

const whiteDog = new WhiteDog();
whiteDog.bark(); // 흰둥이 : 멍멍!

/*
기존 function 은 자신이 종속된 객체를 this로 가리키고,
화살표 function 은 자신이 종속된 인스턴스를 this로 가리킨다.
 */


// 화살표 함수를 사용하면 가독성을 높일 수 있다.
const triple = (value) => value * 3;

/*
이처럼 기존 function과 화살표 function에는 차이가 있지만 함수형 컴포넌트를 선언할 때는 큰 차이가 없다.
어떤 방식을 선택할지는 취향이다.
 */

export default MyComponent;