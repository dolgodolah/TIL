# 스프링 DB 접근 기술

### 사용 기술
- Spring Boot
- JdbcTemplate
- JPA
- 스프링 데이터 JPA


### 의존 라이브러리
```
implementation 'org.springframework.boot:spring-boot-starter-jdbc'
implementation 'org.springframework.boot:spring-boot-starter-web'
runtimeOnly 'com.h2database:h2'
```

## JdbcTemplate

순수 JDBC와 동일한 환경설정을 하면 된다.

스프링 JdbcTemplate과 MyBatis 같은 라이브러리는 순수 Jdbc의 반복 코드를 대부분 제거해준다.

하지만 SQL은 직접 작성해야 한다.