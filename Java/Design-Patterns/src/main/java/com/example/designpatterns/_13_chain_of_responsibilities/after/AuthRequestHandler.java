package com.example.designpatterns._13_chain_of_responsibilities.after;

import com.example.designpatterns._13_chain_of_responsibilities.before.Request;

public class AuthRequestHandler extends RequestHandler {

    public AuthRequestHandler(RequestHandler nextHandler) {
        super(nextHandler);
    }

    @Override
    public void handle(Request request) {
        System.out.println("인증 처리");
        System.out.println("권한 확인");
        super.handle(request);
    }
}
