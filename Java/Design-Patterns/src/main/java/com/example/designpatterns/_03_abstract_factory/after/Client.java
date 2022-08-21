package com.example.designpatterns._03_abstract_factory.after;

import com.example.designpatterns._02_factorymethod.after.AuthToken;

public class Client {

    public static void main(String[] args) {
        EmailTokenFactory emailTokenFactory = new EmailTokenFactory(new GuestFactory());
        AuthToken authToken = emailTokenFactory.createAuthToken(AuthToken.TokenType.EMAIL, "123456");
        System.out.println(authToken.getUser().getClass()); // Guest

        EmailTokenFactory emailTokenFactory2 = new EmailTokenFactory(new MemberFactory());
        AuthToken authToken2 = emailTokenFactory2.createAuthToken(AuthToken.TokenType.EMAIL, "123456");
        System.out.println(authToken2.getUser().getClass()); // Member
    }
}
