package com.example.designpatterns._02_factorymethod.after;

// 자바 11부터 `interface`에 private method 가능하기 때문에 추상 클래스를 상속받도록 함
// public class SmsTokenFactory implements AuthTokenFactory {
public class SmsTokenFactory extends DefaultAuthTokenFactory {
    @Override
    public AuthToken generate(String passcode) {
        return new SmsToken(passcode);
    }
}
