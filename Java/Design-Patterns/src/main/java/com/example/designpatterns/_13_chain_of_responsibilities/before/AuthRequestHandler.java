package com.example.designpatterns._13_chain_of_responsibilities.before;

public class AuthRequestHandler extends RequestHandler {

    /**
     * 인증, 인가 처리를 분리함으로써 단일 책임 원칙은 지켜진다.
     * (하지만 해당 핸들러에 다른 처리나 기능이 추가되어야 한다면?)
     */
    @Override
    public void handler(Request request) {
        System.out.println("인증 확인");
        System.out.println("권한 확인");
        super.handler(request);
    }
}
