# JpaRepository 사용법

스프링부트에서는 Entity의 기본적인 CRUD가 가능하도록 JpaRepository 인터페이스를 제공한다.

## interfate 형식

Spring Data JPA에서 제공하는 JpaRepository 인터페이스를 상속하기만 해도 되며, 인터페이스에 따로 @Repository등의 어노테이션을 추가할 필요가 없다.

JpaRepository를 상속받을 때는 사용될 Entity 클래스와 ID 값이 들어가게 된다. 즉, JpaRepository<T, ID> 가 된다.


```java
public interface MemberRepository extends JpaRepository<Member, Long> {
```

## 기본 기능

save() : 레코드 저장 (insert, update)

findOne() : primary key로 레코드 한건 찾기

findAll() : 전체 레코드 불러오기. 정렬(sort), 페이징(pageable) 가능

count() : 레코드 갯수

delete() : 레코드 삭제

## 기능 추가
기능을 추가하기 위해서는 규칙에 맞는 메서드를 작성해야 한다.

- And : 여러 필드를 and로 검색
```java
findByEmailAndUserId(String email, String userId)
```

- Or : 여러필드를 or 로 검색
```java
findByEmailOrUserId(String email, String userId)
```

- Between : 필드의 두 값 사이에 있는 항목 검색
```java
findByCreatedAtBetween(Date fromDate, Date toDate)
```


- LessThan : 작은 항목 검색
```java
findByAgeGraterThanEqual(int age)
```
 

- GreaterThanEqual : 크거나 같은 항목 검색
```java
findByAgeGraterThanEqual(int age)
```
 

- IsNull : null 인 항목 검색
```java
findByJobIsNull()
```
 

- In : 여러 값중에 하나인 항목 검색
```java
findByJob(String … jobs)
```
 
- OrderBy : 검색 결과를 정렬하여 전달
```java
findByEmailOrderByNameAsc(String email)
```

- Like : like 검색
```java
findByNameLike(String name)
```

- Containing : like 검색
```java
findByTitleContaining(String keyword);
```
 
 findByNameLike("%in%")와 findByNameContaining("in")은 같은 결과를 가진다.
 (Like는 와일드카드 문자를 포함해야 Containing과 같은 결과를 가진다.)

## 참고
[https://jobc.tistory.com/120](https://jobc.tistory.com/120)