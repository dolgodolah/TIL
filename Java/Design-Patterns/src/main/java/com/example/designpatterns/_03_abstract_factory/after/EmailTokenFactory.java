package com.example.designpatterns._03_abstract_factory.after;

import com.example.designpatterns._02_factorymethod.after.AuthToken;
import com.example.designpatterns._02_factorymethod.after.DefaultAuthTokenFactory;
import com.example.designpatterns._02_factorymethod.after.EmailToken;

public class EmailTokenFactory extends DefaultAuthTokenFactory {

    private UserFactory userFactory;

    public EmailTokenFactory(UserFactory userFactory) {
        this.userFactory = userFactory;
    }

    @Override
    public AuthToken generate(String passcode) {
        AuthToken authToken = new EmailToken(passcode);
        authToken.setUser(userFactory.createUser());
        return authToken;
    }
}
