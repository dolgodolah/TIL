# 스프링 DB 접근 기술

### 사용 기술
- Spring Boot
- JdbcTemplate
- JPA
- 스프링 데이터 JPA

# 1. JdbcTemplate

## 1.1 의존 라이브러리

순수 JDBC와 동일한 환경설정을 하면 된다.

```
dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-jdbc'
    runtimeOnly 'com.h2database:h2'
}
```

## 1.2 사용 방법

```properties
spring.datasource.url=jdbc:h2:tcp://localhost/~/test
spring.datasource.driver-class-name=org.h2.Driver
spring.datasource.username=sa
```

```java
@Repository
public class JdbcMemberDao implements MemberDao{

    private final JdbcTemplate jdbcTemplate;

    public JdbcMemberDao(DataSource dataSource) {
        this.jdbcTemplate = new JdbcTemplate(dataSource);
    }
    
    ...
}
```

JdbcTemplate을 사용하기 위해서는 JdbcTemplate 생성자에 `application.properties`에 정의한 dataSource가 주입돼야 한다.

## 1.3 특징
- 스프링 JdbcTemplate과 MyBatis 같은 라이브러리는 순수 Jdbc의 반복 코드를 대부분 제거해준다.

- 하지만 SQL은 직접 작성해야 한다.

```java
@Override
public Optional<Member> findById(Long id) {
    List<Member> result = jdbcTemplate.query("select * from member where id = ?", memberRowMapper(), id);
    return result.stream().findAny();
}
```

<br>

# 2. JPA

## 2.1 의존 라이브러리

```
dependencies {
    // implementation 'org.springframework.boot:spring-boot-starter-jdbc'
    implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
    runtimeOnly 'com.h2database:h2'
}
```

`spring-boot-starter-data-jpa` 내부에 jdbc 관련 라이브러리를 포함하기 때문에 jdbc는 제거해도 된다.

## 2.2 사용 방법

DB 테이블과 매핑시킬 클래스에 `@Entity`를 명시해야 한다.

```java
@Entity
public class Post {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String author;
    private String content;
    ...
}
```

<br>

JPA는 EntityManager를 이용해 DB를 접근하기 때문에 EntityManager를 주입받아야 한다.

```java
@Repository
public class JpaPostDao implements PostDao {

    private final EntityManger em;

    public JpaPostDao(EntityManager em) {
        this.em = em;
    }
    
    ...
}
```

## 2.3 특징

- JPA는 순수 Jdbc의 반복 코드는 물론이고, 기본적인 sql문도 자동으로 만들어서 실행해준다.

```java
Post post = em.find(Post.class, id);
```
<br>

- 하지만 pk 기반이 아닐 때는 JPQL을 작성해야 한다.

````java
em.createQuery("select p from Post p", Post.class).getResultList();
````
<br>

- 객체 중심의 설계에 집중할 수 있게 하여 개발 생산성을 높일 수 있다.

<br>

# 3. Spring Data JPA

JPA 기술을 스프링에서 한번 감싸서 제공하는 기술로 pk 기반이 아니어도 JPQL을 작성하지 않아도 된다.

#### 빈을 등록하는 방법은 3가지가 있다.
- 컴포넌트 스캔 : 위 코드처럼 `@Repository`를 통해 의존관계 설정
- 직접 스프링 빈 등록 : [실제 작성한 코드](https://github.com/dolgodolah/TIL/blob/master/practice-code/spring-jdbc/src/main/java/com/example/springjdbc/SpringConfig.java)는 직접 스프링 빈을 등록함
    - JdbcMemberDao, JpaMemberDao 등을 코드 변경없이 갈아 끼우기 위해서는 직접 등록하는 게 좋다.
- xml : 잘 사용되지 않는 방법이라고 함
