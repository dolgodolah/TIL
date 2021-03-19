# Thymeleaf 문법

반복해서 사용해봐야 손에 익을텐데, 시간 남을 때 조금씩 하다보니 매번 타임리프 문법을 구글링해서 찾아본다. 익숙해지기 전까지는 자주 찾아볼것 같아서 기록해둔다.

## 표현식


```
th:[속성]="서버 전달 받은 값 또는 조건식"
```

## 자주 사용하는 문법

```html
<span th:text="${user.name}"></span> <!-- 텍스트 내용 -->

<input type="text" th:value="${title}" /> <!--element value값, checkbox, input 등 -->

<p th:if="${user.authType}=='web'" th:text="${user.authType}"></p> <!-- 조건문 -->

<p th:unless="${user.authType}=='facebook'" th:text="'not '+ ${user.authType}"></p> <!-- else -->

<p th:each="user : ${users}" th:text="${user.name}"></p> <!-- 반복문 -->

<li th:classappend="${condition} == 1 ? 'active'"><a href="/"></a> <!-- condition이 1이면 "/" 링크를 가진 'active' 클래스 추가 -->
<li th:classappend="${condition} == 2 ? 'active'"><a href="/about"></a> <!-- 상황에 따라 동적으로 class 추가 -->
```

## 그 외 정보


input은 th:value, textareas는 th:text를 사용한다.

```html
<input type="text" name="writer" th:value="${post.writer}">
<textarea type="text" name="content" th:text="${post.content}"></textarea>
```

## 참고 링크
[https://eblo.tistory.com/55](https://eblo.tistory.com/55)