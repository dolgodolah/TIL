# Thymeleaf 문법

반복해서 사용해봐야 손에 익을텐데, 시간 남을 때 조금씩 하다보니 매번 타임리프 문법을 구글링해서 찾아본다. 익숙해지기 전까지는 자주 찾아볼것 같아서 기록해둔다.

[모든 문법](https://noritersand.github.io/java/java-%ED%83%80%EC%9E%84%EB%A6%AC%ED%94%84-thymeleaf-%EA%B8%B0%EB%B3%B8/)

## 표현식

```
th:[속성]="서버 전달 받은 값 또는 조건식"
```

## 자주 사용하는 문법

기본문법
```html
<span th:text="${user.name}"></span> <!-- 텍스트 내용 -->

<input type="text" th:value="${title}" /> <!--element value값, checkbox, input 등 -->

<p th:if="${user.authType}=='web'" th:text="${user.authType}"></p> <!-- 조건문 -->

<p th:unless="${user.authType}=='facebook'" th:text="'not '+ ${user.authType}"></p> <!-- else -->

<div th:each="user : ${users}">
    <p th:text="${user.name}"></p>
    <!-- th:each 반복 상태를 추척할 수 있는 status 변수, 반복대상명 + "Stat" -->
    <p th:text="${userStat.index}"></p> <!-- 0부터 시작 -->
    <p th:text="${userStat.count}"></p> <!-- 1부터 시작 -->
    <p th:text="${userStat.even}"></p> <!-- 현재 반복이 짝수인지 여부 (boolean) -->
    <p th:text="${userStat.odd}"></p> <!-- 현재 반복이 홀수인지 여부 -->
    <p th:text="${userStat.first}"></p> <!-- 현재 반복이 첫번째인지 여부 -->
    <p th:text="${userStat.last}"></p> <!-- 현재 반복이 마지막인지 여부 -->
</div> <!-- 반복문 -->

<li th:classappend="${condition} == 1 ? 'active'"><a href="/"></a> <!-- condition이 1이면 "/" 링크를 가진 'active' 클래스 추가 -->
<li th:classappend="${condition} == 2 ? 'active'"><a href="/about"></a> <!-- 상황에 따라 동적으로 class 추가 -->
```

HttpServlet의 Attribute 값 가져오기

```java
HttpServletRequest request;
request.setAttribute("errorMessage", "비밀번호 일치하지 않음");
```

```html
<span th:text="${#request.getAttribute('errorMessage')}"></span> <!-- HttpServletRequest object의 'errorMessage'를 반환 -->
```

th:each를 통한 체크박스 생성
```java
@ModelAttribute("regions")
public Map<String, String> regions() {
    Map<String, String> regions = new LinkedHashMap<>();
    regions.put("SEOUL", "서울");
    regions.put("BUSAN", "부산");
    regions.put("JEJU", "제주");
    return regions;
}

```

```html
<div th:each="region : ${regions}" class="form-check form-check-inline">
    <input type="checkbox" th:field="*{regions}" th:value="${region.key}"
        class="form-check-input">
    <label th:for="${#ids.prev('regions')}" th:text="${region.value}" class="form-check-label">region</label>
</div>
```


## 참고 링크
[https://eblo.tistory.com/55](https://eblo.tistory.com/55)
[https://ifuwanna.tistory.com/200](https://ifuwanna.tistory.com/200)