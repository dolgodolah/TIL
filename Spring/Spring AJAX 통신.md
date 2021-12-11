# 스프링 AJAX 통신


## ajax란?

asynchronous Javascript and XML의 줄임말로 자바스크립트를 이용하여 비동기 식으로 서버와 통신을 한다. 비동기통신이기 때문에 서버에 요청이 가더라도 화면의 깜빡 거림이나 화면이 이동 된다는 느낌을 주지 않고 상당히 자연스럽고 빠르게 클라이언트의 화면을 변화 시켜준다고 한다.


## 준비
ajax 통신을 하기 위해서는 jQuery 라이브러리를 이용해야한다.

```html
<script src="https://code.jquery.com/jquery-latest.js"></script>
```

## 기본 예제
- 클라이언트 (javascript)
```javascript
    $('#btn1').on('click', function(){
        var form = {
                name: "jamong",
                age: 23
        }
        $.ajax({
            url: "requestObject",
            type: "POST",
            data: form,
            success: function(data){
                $('#result').text(data);
            },
            error: function(){
                alert("simpleWithObject err");
            }
        });
    });

```
- 서버 (Spring)
```java
@PostMapping("/requestObject")
@ResponseBody
public String simpleWithObject(Jamong jamong) {
        //필요한 로직 처리
        return jamong.getName() + jamong.getAge();
} 
```
- 뷰 (html)

```html
<body>
    <button id="btn1">버튼</button>
    <div id="result"></div>
</body>
```
## 참고
[https://myjamong.tistory.com/17](https://myjamong.tistory.com/17)

[https://dion-ko.tistory.com/59](https://dion-ko.tistory.com/59)