# JPA, Hibernate, Spring Data JPA 개념 정리

기존에 Spring Data JPA를 이용해 프로젝트를 진행해왔습니다.

JPA와 Hibernate, Spring Data JPA의 차이에 대해 어림짐작 알고있었지만 이번 공부를 통해서 이 셋의 차이에 대해 정확히 짚어보겠습니다. 

## JPA

JPA는 Java Persistence API의 약자로, `자바에서 관계형 데이터베이스를 사용하는 방식을 정의한 인터페이스`입니다.

기술명세서같은 인터페이스일 뿐 특정 기능을 수행하는 라이브러리가 아닙니다.

JPA를 정의한 javax.persistence 패키지를 보면 대부분 interface, enum, Exception, Annotation으로 이루어져 있는걸 볼 수 있습니다.


## Hibernate

위에서 언급한 인터페이스의 `구현체 역할`이 바로 Hibernate입니다.

javax.persistence.EntityManager와 같은 인터페이스를 직접 구현한 라이브러리입니다. 


반드시 Hibernate를 사용할 필요는 없습니다.

실제로 다른 구현체인 DataNuclues, EclipseLink 등이 있지만

Hibernate가 굉장히 성숙한 라이브러리이기 때문에 대부분 Hibernate를 사용하고 있다고 합니다.      

## Spring Data JPA

Spring Data JPA는 `JPA를 쓰기 편하게 만들어 놓은 모듈`입니다.

Spring Data JPA를 사용하기 전에는 repository 개발을 위해 EntityManager를 이용하여 직접 구현하여야 합니다.

```java
@PersistenceContext
private EntityManager em;

public void save(Member member){
    em.persist(member);
}

.
.
```

하지만 Spring Data JPA는 정해진 규칙에 맞게 메소드를 입력하면 자동으로 메소드 이름에 해당하는 쿼리를 날리는 구현체를 만들어 등록해줍니다.

```java
@Transactional
public Long join(User user) {
	return userRepository.save(user).getId();
}
```

정해진 규칙에 맞게 메소드를 추가할 수도 있습니다.

```java
public interface UserRepository extends JpaRepository<User, Long> {
	Optional<User> findByEmail(String email);

}
```





## 출처
[https://suhwan.dev/2019/02/24/jpa-vs-hibernate-vs-spring-data-jpa/](https://suhwan.dev/2019/02/24/jpa-vs-hibernate-vs-spring-data-jpa/)