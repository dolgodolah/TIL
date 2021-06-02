# Spring MVC

Spring MVC와 DispatcherServlet에 대해 공부하며 정리한 글입니다.

## MVC 패턴

스프링 프레임워크는 기본적으로 MVC 패턴을 지원합니다.

MVC 패턴이란 `Model`, `View`, `Controller` 세 부분으로 구분하여 개발하는 패턴을 말하는데

`Model`은 처리되는 모든 데이터들,

`View`는 데이터에 대한 입력과 출력,

`Controller`는 model에 대한 처리와 view 반환을 담당하는 구조입니다.

MVC는 MVC1과 MVC2으로 나뉘게 되는데 스프렝 프레임워크의 경우 MVC2에 해당합니다.

MVC1은 model, view, controller을 한페이지에서 담당합니다.

구조가 간단하기 때문에 쉽고 빠르게 개발할 수 있다는 장점이 있지만, 규모가 커질수록 유지보수가 어려워집니다.

반면 MVC2는 요청, 응답, 비니지스 로직 처리를 분리하여 담당하는 구조로

다소 개발하는데 시간이 걸리고 어려움이 있을 수 있으나 유지보수에 용이하고 확장성에 좋습니다.

## DispatcherServlet

Spring MVC에는 dispatcherservlet이 존재합니다.

기존에는 mvc패턴을 위해 모든 서블릿에 대해 url 매핑을 하려 web.xml에 모두 등록해줘야 했지만

dispatcherservlet이 등장함으로써 해당 애플리케이션으로 들어오는 모든 요청에 대해 핸들링해줍니다.

다음은 Spring 서버에 요청이 들어왔을 때 dispatcherservlet의 동작 과정입니다.

1. URL로 접근하여 정보를 요청 (Client→DispatcherServlet)

2. 해당 요청을 매핑한 컨트롤러가 있는지 검색 (DispatcherServlet→HandlerMapping)

3. 처리요청 (HandlerMapping→Controller)

4. 클라이언트의 요청 처리하고 결과 출력할 view의 이름을 리턴(Controller→DispatcherServlet)

5. 컨트롤러에서 보내온 view 이름을 검색 (DispatcherServlet→ViewResolver)

6. 처리결과를 view에 송신 (ViewResolver→View)

7. 처리결과과 포함된 view를 송신 (View→DispatcherServlet)

8. 최종결과 출력 (DispatcherServlet→Client)


