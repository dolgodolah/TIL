# @NotNull vs @Column(nullable = false)

평소 `@Column(nullable = false)`을 통해 해당 컬럼에 제약조건을 걸었는데 어떤 코드에는 `@NotNull` 어노테이션이 사용된다.

```java
@Column(nullable = false)
private String title;
```

```java
@NotNull
private String title;
```

딱 봐도 기능은 비슷해보이는데 무슨 차이가 있는거지?

## 

- 기능은 실제로 비슷하지만 유효성 검사를 하는 접근이 다르다.

- @NotNull은 DB에 쿼리를 보내기 전에 Bean Validation에 의해 검사된다.

- @Column(nullable = false)은 DB에서 유효성 검사를 다룬다.

- 스프링에서는 @NotNull 사용을 지향하고 있다.

## 참고 링크
[https://www.baeldung.com/hibernate-notnull-vs-nullable](https://www.baeldung.com/hibernate-notnull-vs-nullable)
