# Filter, Interceptor, AOP

진행중인 프로젝트에 대해 리뷰를 받던 중 유저 세션값을 가져와 로그인 여부를 확인하는

반복적인 코드를 제거하면 좋겠다는 조언을 받았습니다.

반복적인 코드 제거? 당연히 AOP라고 생각했는데 Filter, Interceptor, AOP의 차이를 알고있냐는 질문을 받았습니다.

AOP에 대해서만 알고있던지라 답변을 제대로 하지 못했습니다.

그래서 Filter, Interceptor, AOP의 차이에 대해 공부하고 내용을 정리해보겠습니다.

## 공통 관심사항, 공통 작업에 대한 처리

개발을 하다보면 공통적으로 처리해야 할 작업들이 많습니다.

예를 들어 로그인 세션 확인, 권한 확인, XSS 방어, PC와 모바일의 분기처리, 로깅, 페이지 인코딩 변환 등이 있습니다.

이런 공통 관심사항에 관련된 코드를 모든 페이지마다 작성한다면 중복된 코드가 많아지게 되고

프로젝트 규모가 커질수록 유지보수에 어려움이 생깁니다.

즉, 공통 관심사항은 빼서 따로 관리하는게 좋습니다. 이를 활용할 수 있는 것이 3가지 있습니다.

`Filter`, `Interceptor`, `AOP`

이 세가지 기능 모두 무슨 행동(비지니스 로직)을 하기전에 먼저 실행하거나, 실행한 후에 추가적인 행동을 할 때 사용되는 기능들입니다.

차이점은 실행되는 위치(시점)가 다릅니다. 하나씩 알아보겠습니다.

## Filter

DispatcherServlet 이전에 실행이 되어 요청과 응답을 거르는 정제 역할을 합니다.

요청 내용을 변경하거나 여러가지 체크를 수행할 수 있습니다. 응답내용에 대해서도 변경하는 처리를 할 수 있습니다.

일반적으로 인코딩 변환 처리, XSS방어 등의 요청에 대한 처리로 사용됩니다.

**필터의 실행메서드**
- init() : 필터 인스턴스 초기화
- doFilter() : 전/후 처리
- destroy() : 필터 인스턴스 종료

## Interceptor

요청에 대한 작업 전/후로 가로챈다고 보면 됩니다.

필터는 스프링 컨텍스트 외부에 존재하여 스프링과 무관한 자원에 대해 동작하지만,

인터셉터는 스프링의 [DispatcherServlet이 Controller를 호출](https://github.com/dolgodolah/TIL/blob/master/spring/Spring%20MVC.md#dispatcherservlet)하기 전/후로 끼어들기 때문에

스프링 컨텍스트 내부에서 Controller에 관한 요청과 응답에 대해 처리합니다.

스프링의 모든 Bean에 접근할 수 있습니다.

인터셉터는 로그인 체크, 권한 체크, 프로그램 실행시간 계산, 로그확인 등의 대한 처리로 사용됩니다.

**인터셉터의 실행메서드**
- preHandler() : 컨트롤러 메서드가 실행되기 전
- postHandler() : 컨트롤러 메서드가 실행된 후 view에 렌더링되기 전
- afterCompletion() : view가 렌더링 되고 난 후

## AOP

OOP에서 중복을 줄이기 위한 프로그래밍 방법입니다. 

Interceptor나 Filter와 달리 메소드 전후의 지점에 자유롭게 설정이 가능합니다.

Interceptor와 Filter는 주소를 대상으로 구분해서 걸러내는 반면 AOP는 주소, 파라미터, 애노테이션 등 다양한 방법으로 대상을 지정할 수 있습니다.

AOP의 Advice와 HandlerInterceptor의 가장 큰 차이는 파라미터의 차이입니다.

Advice의 경우 JoinPoint나 ProceedingJoinPoint 등을 활용해서 호출합니다.

반면 HandlerInterceptor는 Filter와 유사하게 HttpServletRequest, HttpServletResponse를 파라미터로 사용합니다.

주로 로깅, 트랜잭션, 에러 처리 등 비지니스 로직에서 조금 더 세밀하게 조정하고 싶을 때 사용합니다.


**AOP의 포인트컷**

@Before: 대상 메서드의 수행 전

@After: 대상 메서드의 수행 후

@After-returning: 대상 메서드의 정상적인 수행 후

@After-throwing: 예외발생 후

@Around: 대상 메서드의 수행 전/후


## 출처
[https://goddaehee.tistory.com/154](https://goddaehee.tistory.com/154)