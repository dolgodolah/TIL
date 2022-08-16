package com.example.designpatterns._02_factorymethod.before;

public class Client {

    public static void main(String[] args) {
        Client client = new Client();


        AuthToken smsToken = AuthTokenFactory.createAuthToken(AuthToken.TokenType.SMS, "123456");
        System.out.println(smsToken);

        AuthToken emailToken = AuthTokenFactory.createAuthToken(AuthToken.TokenType.EMAIL, "654321");
        System.out.println(emailToken);
    }
}
