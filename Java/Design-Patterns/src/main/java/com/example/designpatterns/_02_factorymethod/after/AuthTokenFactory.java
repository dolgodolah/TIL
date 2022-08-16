package com.example.designpatterns._02_factorymethod.after;

import com.example.designpatterns._02_factorymethod.after.AuthToken.TokenType;

public interface AuthTokenFactory {

    default AuthToken createAuthToken(TokenType type, String passcode) {
        validate(type, passcode);

        return generate(passcode);
    }

    AuthToken generate(String passcode);

//    자바 11부터 `interface`에 private method 가능함
//    private void validate(TokenType type, String passcode) {
//        if (type == null) {
//            throw new IllegalArgumentException("토큰 타입을 정해주세요");
//        }
//
//        if (passcode == null) {
//            throw new IllegalArgumentException("패스코드가 비어있어요.");
//        }
//    }

    void validate(TokenType type, String passcode);
}
