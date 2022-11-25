package com.example.designpatterns._13_chain_of_responsibilities.before;

public class RequestHandler {

    public void handler(Request request) {
        // 인증, 인가 처리를 여기에 추가하게 되면 단일 책임 원칙이 지켜지지 않는다.
        // System.out.println("인증 처리");

        System.out.println(request.getBody());
    }
}
