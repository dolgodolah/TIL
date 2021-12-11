# Overview

평소 Lombok 덕분에 생성자 생성, 빌더 패턴, Getter, Setter 등을 편리하게 구현했다.

편의성을 제공해주는만큼 잘못 사용하기 쉬운데 실용적으로 올바르게 Lombok을 사용하는 방법을 알아본다.

# 바람직한 롬복 사용법

```java
@Entity
@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@EntityListeners(AuditingEntityListener.class)
@EqualsAndHashCode(of = {"id"})
public class Member {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String email;
    private String name;

    @CreatedDate
    private LocalDateTime createdDate;

    @UpdatedDate
    prviate LocalDateTime updatedDate;

    @Builder
    public Member(String email, String name) {
        this.email = email;
        this.name = name;
    }
}
```

롬복에 관한 어노테이션에 대해서만 설명하겠다.

## 1. @Getter

```java
public Long getId() { return id; }
public String getEmail() { return email; }
public String getName() { return name; }
        ...
```

위 코드를 `@Getter` 한 줄로 생략할 수 있다.

```java
@Getter
public class Member {
```

`@Setter`의 경우 무분별한 사용을 하게 되면 객체의 일관성이 무너지기 때문에 지양한다.

## 2. @NoArgsConstructor(access = AccessLevel.PROTECTED)

`@Builder` 사용을 위해서는 매개변수가 없는 기본 생성자가 있어야 한다.

`@NoArgsConstructor`가 바로 매개변수를 받지 않는 기본 생성자를 생성하는 어노테이션이다.

```java
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class Member {
```

`@Builder` 사용을 위한 기본 생성자일뿐 굳이 외부에서 생성되도록 열어둘 필요가 없기 때문에

`access = AccessLevel.PROTECTED`를 설정했다.

이는 Member 객체 생성을 위해서는 빌더를 통한 생성으로만 제한할 수 있다.

## 3. EqualsAndHashCode(of = {"id"})

```java
@EqualsAndHashCode(of = {"id"})
public class Member {
```

equals()와 hashCode()를 생성해준다.

default는 static이나 transient를 제외한 모든 필드들이 대상이 된다.

of를 통해 특정 필드들을 명시할 수 있고, exclude를 통해 특정 필드를 제외할 수 있다.

## 4. @Builder

빌더 패턴을 통해 객체 생성을 위해서는 [Builder 생성자에 대한 구현](https://github.com/dolgodolah/TIL/blob/master/java/%EC%9D%B4%ED%8E%99%ED%8B%B0%EB%B8%8C%20%EC%9E%90%EB%B0%94/%EC%95%84%EC%9D%B4%ED%85%9C2.%20%EC%83%9D%EC%84%B1%EC%9E%90%EC%97%90%20%EB%A7%A4%EA%B0%9C%EB%B3%80%EC%88%98%EA%B0%80%20%EB%A7%8E%EB%8B%A4%EB%A9%B4%20%EB%B9%8C%EB%8D%94%EB%A5%BC%20%EA%B3%A0%EB%A0%A4%ED%95%98%EB%9D%BC.md) 이 필요하다.

이를 `@Builder` 로 대신할 수 있다.

```java
@Builder
public class Member {
```

클래스에 `@Builder`를 명시하게 되면 해당 클래스의 모든 필드들을 매개변수로 받는 빌더를 생성하게 되는데

Member 클래스의 경우 `id`, `createdDate`, `updatedDate`를 매개변수로 받을 필요가 없다.

```java
public class Member {
    ...
    
    @Builder
    public Member(String email, String name) {
        this.email = email;
        this.name = name;
    }
}

```

즉, 위의 예시 코드처럼 필요한 매개변수를 받는 생성자를 작성하고 그 생성자에 `@Builder`를 명시하는게 바람직하다.


