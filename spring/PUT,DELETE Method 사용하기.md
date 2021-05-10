# PUT, DELETE Method를 사용하여 RESTful한 API 만들기

기본적으로 form 태그의 method는 get, post만 지원하기 때문에 put, delete 방식으로 자원을 전송하고 싶으면 아래와 같이 작성한다.

``` html
<form action="#" method="post">
    <input type="hidden" name="_method" value="put" />
    <button type="submit">수정</button>
</form>
```

아니 근데 안된다...
서버 쪽 Controller의 @PutMapping이 작동하질 않는다.

답은 HiddenHttpMethodFilter이다.
HiddenHttpMethodFilter는 Hidden 타입의 input 태그의 속성들을 읽어서 HttpServletRequestWrapper.getMethod() 반환 값을 변경해 요청된 HTTP 메소드의 타입을 PUT, DELETE, PATCH로 변경해주는 필터이다.

Application의 main클래스에 hiddenHttpMethodFilter()를 추가해주면 된다.

```java
@SpringBootApplication
public class HelloApplication{
    public static void main(String[] args){
        SpringApplication.run(HelloApplication.class, args);
    }

    @Bean
    public HiddenHttpMethodFilter hiddenHttpMethodFilter(){
        return new HiddenMethodFilter();
    }
}
```

이후에는 Controller에서 get, post뿐만 아니라 put, delete도 사용가능해진다.

[https://imbf.github.io/spring/2020/05/03/Spring-HiddenHttpMethodFilter.html](https://imbf.github.io/spring/2020/05/03/Spring-HiddenHttpMethodFilter.html)