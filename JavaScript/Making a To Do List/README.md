# What I Learned

- Vanilla JS로 To Do List를 제작했습니다.

- 사용자의 현재 위치를 가져옵니다.

```
navigator.geolocation.getcurrentposition(success,fail);
```
- Open API 활용하여 날씨 정보 가져옵니다.
- Javascript는 fetch를 통해 비동기 통신을 할 수 있습니다.
```javascript
// url과 통신하여 얻어진 json 데이터를 출력한다.
fetch(url)
.then(response => response.json())
.then(json => console.log(json))
```

- Math.random()을 통해 수를 랜덤으로 생성합니다.
