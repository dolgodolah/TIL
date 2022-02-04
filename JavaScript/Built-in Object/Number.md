# Number

`Number`는 123이나 -9.25 같은 숫자를 표현하고 다룰 때 사용하는 **primitive wrapper object**이다.

JavaScript의 `Number` 타입은 Java의 double처럼 64bit로 숫자를 표현할 수 있다.

## 1. Literal syntax
JavaScript에서 123과 같은 숫자 리터럴은 정수가 아니라 부동 소수점 값이다.

```js
123;
123.0;
123 === 123.0; // true
```

`BigInt` 타입이 나왔지만 여전히 123은 `Number`로 표현된다.

## 2. Function syntax

`Number(value)`처럼 함수로 사용하면 문자열이나 다른 값을 `Number` 타입으로 변환한다. 만약 숫자로 변환할 수 없으면 NaN을 반환한다.

```js
Number('123'); // 숫자 123
Number('123') === 123; // true

Number('unicorn'); // NaN
Number(undefined); // NaN
```

## 3. Static properties

`Number.MAX_SAFE_INTEGER` : JavaScript에서 안전한 최대 정수 (2^53 - 1)

`Number.MIN_SAFE_INTEGER` : JavaScript에서 안전한 최소 정수 (-(2^53 - 1))

`Number.MAX_VALUE` : 표현 가능한 가장 큰 양수

`Number.MIN_VALUE` : 표현 가능한 가장 작은 양수

`Number.NaN` : "Not a Number"를 나타내는 값

`Number.POSITIVE_INFINITY` : 양의 무한대를 나타내는 특수 값 (오버플로우 시 반환)

`Number.NEGATIVE_INFINITY` : 음의 무한대를 나타내는 특수 값 (오버플로우 시 반환)

## 4. Static methods

`Number.isNaN()`
주어진 값이 NaN인지 확인합니다.

`Number.isFinite()`
주어진 값이 유한수 인지 확인합니다.

`Number.isInteger()`
주어진 값이 정수인지 확인합니다.

`Number.isSafeInteger()`
주어진 값이 안전한 정수(-(2^53 - 1)과 2^53 - 1 사이의 정수)인지 확인합니다.

## 5. Examples

### Number의 정수 범위

`Number` 객체가 표현할 수 있는 안전한 정수의 최소값과 최대값이다.

```js
const biggestInt = Number.MAX_SAFE_INTEGER; // (2^53 - 1) => 9007199254740991
const smallestInt = Number.MIN_SAFE_INTEGER; // -(2^53 - 1)) => -9007199254740991
```

**Json으로 데이터를 읽을 때, 위의 범위를 벗어나는 수는 `Number` 형변환 시 손상될 수 있다.**

실제로 브라우저 콘솔에 9007199254740993을 입력하면 다른 값이 나온다.

더 큰 수는 `BigInt` 타입을 사용하거나 `String`을 사용하는 것도 방법이다.

<br>

### Number를 이용해 Date 객체 숫자로 변환

Number를 함수로 사용하여 Date 객체를 숫자 값으로 변환할 수 있다.

```js
let d = new Date('December 17, 1995 03:24:00');
console.log(Number(d));
```