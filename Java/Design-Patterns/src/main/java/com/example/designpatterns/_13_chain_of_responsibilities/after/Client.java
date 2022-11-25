package com.example.designpatterns._13_chain_of_responsibilities.after;

import com.example.designpatterns._13_chain_of_responsibilities.before.Request;

public class Client {

    private RequestHandler requestHandler;

    public Client(RequestHandler requestHandler) {
        this.requestHandler = requestHandler;
    }

    public void execute() {
        Request request = new Request("이번 놀이는 뽑기입니다.");
        requestHandler.handle(request);
    }
    public static void main(String[] args) {
        RequestHandler chain = new LoggingRequestHandler(new AuthRequestHandler(new PrintRequestHandler(null)));
        Client client = new Client(chain);
        client.execute();
    }
}
