package com.example.designpatterns._02_factorymethod.after;

public class EmailToken extends AuthToken {
    public EmailToken(String passcode) {
        setPasscode(passcode);
        setExpireTime(5 * 60);
        setType(TokenType.EMAIL);
    }
}
