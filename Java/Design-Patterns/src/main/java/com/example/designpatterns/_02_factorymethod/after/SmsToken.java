package com.example.designpatterns._02_factorymethod.after;

public class SmsToken extends AuthToken {

    public SmsToken(String passcode) {
        setType(TokenType.SMS);
        setExpireTime(3 * 60);
        setPasscode(passcode);
    }
}
