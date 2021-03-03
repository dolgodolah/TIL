# JPA 복합키 설정 방법

## 기본키(PK) 설정 방법

```java
@Id
```
어노테이션 @Id 를 통해서 기본키 설정을 할 수 있다. 


## 복합키 설정 방법

기본키를 나타내는 @Id는 한 클래스에 한번만 사용할 수 있다. 하지만 여러 개의 기본키로 구성된 복합키를 이용할 때는 어떻게 해야할까?

```java
@Embeddable
class LikeId implements Serializable {

@Column
private Long id;

@Column
private String userIp;
}

```
복합키를 나타내는 클래스를 생성하여 Serializable 인터페이스를 구현한다. 그리고 @Embeddable 어노테이션을 추가한다.

복합키 클래스를 생성하면 이를 엔티티와 결합해야 한다.

```java
@Entity
public class 클래스이름 {

@EmbeddedId
private LikeId likeId;

private String name;
}
```

@EmbeddedId 어노테이션을 통해 결합할 수 있다.


## 참고
[https://lng1982.tistory.com/286](https://lng1982.tistory.com/286)