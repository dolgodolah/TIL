# REST란?

## 한줄요약

- HTTP의 URL구조를 사용해서 데이터를 변경, 추출, 생성하는 구조이다.
- HTTP URI(Uniform Resource Identifier)를 통해 자원(Resource)을 명시하고, HTTP Method(POST, GET, PUT, DELETE)를 통해 해당 자원에 대한 CRUD Operation을 적용하는 것을 의미한다.



## 

스프링을 공부하다보면 REST, REST API, RESTful이라는 단어를 수없이 많이 본다. CRUD를 적용한 게시판을 만드는 과정 자체가 REST를 이용한다는건 느낌적으로 알고있다. 하지만 이 용어가 많이 등장하는만큼 중요하다는 것이고, 누군가 물어보면 느낌을 말하는게 아니라 교과서처럼 말할 수 있어야한다고 생각한다. (물론 실무적용이 가장 중요하겠지만)


## RESTful 하지 못한 경우
- CRUD 기능을 모두 POST로만 처리하는 API
- route에 resource, id 외의 정보가 들어가는 경우 (/students/updateName)

RESTful한 API를 구현하는 근본적인 목적이 성능 향상에 있는 것이 아니라 API의 이해도 및 호환성을 높이는 것이 주 동기이니, 성능이 중요한 상황에서는 굳이 RESTful한 API를 구현할 필요는 없다.

## 참고 문서, 참고 링크
- [https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html](https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html)
- 스프링부트 프로그래밍 입문 (김완섭 옮김)