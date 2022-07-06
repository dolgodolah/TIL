# JPA Auditing
JPA Auditing을 이용하여 해당 Entity의 생성일/수정일 자동화를 할 수 있다.


## 사용 방법
Auditing을 사용할 Entity클래스에 `@EntityListeners(AuditingEntityListener.class)`, `@CreatedDate`, `@LastModifiedDate`를 추가해준다.

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

그리고 JPA Auditing 어노테이션 활성화를 위해 Application 클래스(main)에 활성 어노테이션 @EnableJpaAuditing을 추가해준다.

```java
@EnableJpaAuditing
@SpringBootApplication
public class BoardApplication {

	public static void main(String[] args) {
		SpringApplication.run(BoardApplication.class, args);
	}
}
```

## 응용 (@MappedSuperclass)

`@MappedSuperclass`를 이용하면 생성일, 수정일이 필요한 모든 클래스마다 `@EntityListeners(AuditingEntityListener.class)`, `@CreatedDate`, `@LastModifiedDate`를 명시하지 않아도 된다.

 부모 클래스(BaseTime)를 만들어 생성일, 수정일이 추가하고 `@MappedSuperclass`를 명시해준다.

```java
@MappedSuperclass
@EntityListeners(AuditingEntityListener::class)
class BaseTime {
    @CreatedDate
    private LocalDateTime createdDate;

    @LastModifiedDate
    private LocalDateTime modifiedDate;
}
```

생성일, 수정일이 필요한 클래스는 위 BaseTime 클래스를 상속받게 하여 따로 생성일, 수정일 속성 추가를 하지 않아도 된다.

```java
class User extends BaseTime {

    private String name;
    ...
    // createdDate, modifiedDate는 따로 추가할 필요없다.
}
```


## 참고
[https://velog.io/@conatuseus/2019-12-06-2212-%EC%9E%91%EC%84%B1%EB%90%A8-1sk3u75zo9](https://velog.io/@conatuseus/2019-12-06-2212-%EC%9E%91%EC%84%B1%EB%90%A8-1sk3u75zo9)

[https://craftdeveloper.tistory.com/16](https://craftdeveloper.tistory.com/16)