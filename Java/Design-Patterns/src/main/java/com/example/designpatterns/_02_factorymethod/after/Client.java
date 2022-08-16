package com.example.designpatterns._02_factorymethod.after;

public class Client {

    public static void main(String[] args) {
        Client client = new Client();
        client.print(new SmsTokenFactory(), AuthToken.TokenType.SMS, "123456");
        client.print(new EmailTokenFactory(), AuthToken.TokenType.EMAIL, "654321");

    }

    private void print(AuthTokenFactory authTokenFactory, AuthToken.TokenType type, String passcode) {
        System.out.println(authTokenFactory.createAuthToken(type, passcode));
    }
}
