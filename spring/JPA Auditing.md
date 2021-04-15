# JPA Auditing
JPA Auditing을 이용하여 해당 Entity의 생성일/수정일 자동화를 할 수 있다.


## 사용 방법
Auditing 기능을 사용할 Entity클래스에 @EntityListeners(AuditingEntityListener.class), @CreatedDate, @LastModifiedDate를 추가해준다.

```java
@EntityListeners(AuditingEntityListener.class) /* JPA에게 해당 Entity는 Auditiong 기능을 사용함을 알립니다. */
public class Board {

    // ...

    @CreatedDate
    private LocalDateTime createdDate;

    @LastModifiedDate
    private LocalDateTime modifiedDate;

    // ...

}
```

JPA Auditing 어노테이션 활성화를 위해서는 Application 클래스(main)에 활성 어노테이션 @EnableJpaAuditing을 추가해야한다.

```java
@EnableJpaAuditing
@SpringBootApplication
public class BoardApplication {

	public static void main(String[] args) {
		SpringApplication.run(BoardApplication.class, args);
	}
}
```


## 참고
[https://velog.io/@conatuseus/2019-12-06-2212-%EC%9E%91%EC%84%B1%EB%90%A8-1sk3u75zo9](https://velog.io/@conatuseus/2019-12-06-2212-%EC%9E%91%EC%84%B1%EB%90%A8-1sk3u75zo9)

[https://craftdeveloper.tistory.com/16](https://craftdeveloper.tistory.com/16)