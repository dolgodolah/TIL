# Bean Validation을 이용한 요청 값 검증

회원가입할 때 비밀번호 입력하는 부분을 보면 최소 *자 이상을 입력하라고 하는 것을 본 적이 있다. 회원가입과 로그인 기능 구현에서 이와 같은 제한사항을 구현하기 위해 찾아보니 Bean Validation을 통해 구현할 수 있었다.

## gradle DI

build.gradle에 spring-boot-starter-validation를 추가했다.

```
implementation 'org.springframework.boot:spring-boot-starter-validation'
```

## 주요 어노테이션

```java
/**
* 문자열을 다룰 때 사용
*/
@NotNull // null 불가능
@NotEmpty // null, 빈 문자열(스페이스 포함X) 불가
@NotBlank // null, 빈 문자열, 스페이스만 포함한 문자열 불가
@Size(min=?, max=?) // 최소 길이, 최대 길이 제한
@Null // null만 가능 
​
/**
* 숫자를 다룰 때 사용
*/
@Positive // 양수만 허용
@PositiveOrZero // 양수와 0만 허용
@Negative // 음수만 허용
@NegativeOrZero // 음수와 0만 허용
@Min(?) // 최소값 제한
@Max(?) // 최대값 제한
​
/** 
* 정규식 관련
*/
@Email // 이메일 형식만가능 (기본 제공)
@Pattern(regexp="?") // 직접 정규식을 쓸 수 있음
```

## 참고
[https://shinsunyoung.tistory.com/43](https://shinsunyoung.tistory.com/43)