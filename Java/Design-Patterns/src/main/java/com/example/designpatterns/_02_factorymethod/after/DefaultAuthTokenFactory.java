package com.example.designpatterns._02_factorymethod.after;

import org.springframework.util.StringUtils;

// 자바 8은 `interface`에 private method 불가능하기 때문에 추상 클래스를 둬서 구현해준다.
public abstract class DefaultAuthTokenFactory implements AuthTokenFactory {

    @Override
    public void validate(AuthToken.TokenType type, String passcode) {
        if (type == null) {
            throw new IllegalArgumentException("토큰 타입을 정해주세요");
        }

        if (!StringUtils.hasText(passcode)) {
            throw new IllegalArgumentException("패스코드가 비어있어요.");
        }
    }
}
