package com.example.designpatterns._13_chain_of_responsibilities.before;

public class LoggingRequestHandler extends AuthRequestHandler {
    @Override
    public void handler(Request request) {
        System.out.println("로깅");
        super.handler(request);
    }
}
