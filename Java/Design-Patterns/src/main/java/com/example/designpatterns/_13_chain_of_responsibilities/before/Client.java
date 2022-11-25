package com.example.designpatterns._13_chain_of_responsibilities.before;

public class Client {

    public static void main(String[] args) {
        Request request = new Request("무궁화 꽃이 피었습니다.");

        // 1. 기본 버전
        RequestHandler requestHandler1 = new RequestHandler();
        requestHandler1.handler(request);

        // 2. 인증, 인가 추가 버전
        RequestHandler requestHandler2 = new AuthRequestHandler();
        requestHandler2.handler(request);

        // 3. 로깅도 추가 하고 싶다면?? 그럼 인증, 인가 처리는?
        // LoggingRequestHandler -> AuthRequestHandler -> RequestHandler 순으로 상속??
        // 클라이언트가 사용해야 되는 핸들러를 직접 명시를 해야되기 때문에 이러한 구조는 문제가 있다.
        RequestHandler requestHandler3 = new LoggingRequestHandler();
        requestHandler3.handler(request);
    }
}
