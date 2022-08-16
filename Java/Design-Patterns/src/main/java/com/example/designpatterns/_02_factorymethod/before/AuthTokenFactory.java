package com.example.designpatterns._02_factorymethod.before;

import com.example.designpatterns._02_factorymethod.before.AuthToken.TokenType;
import org.springframework.util.StringUtils;

public class AuthTokenFactory {

    public static AuthToken createAuthToken(TokenType type, String passcode) {
        // validate
        if (type == null) {
            throw new IllegalArgumentException("토큰 타입을 정해주세요");
        }

        if (!StringUtils.hasText(passcode)) {
            throw new IllegalArgumentException("패스코드가 비어있어요.");
        }

        AuthToken authToken = new AuthToken();
        authToken.setType(type);

        // set expireTime
        if (type == TokenType.EMAIL) {
            authToken.setExpireTime(5 * 60);
        }

        if (type == TokenType.SMS) {
            authToken.setExpireTime(3 * 60);
        }

        // set passcode
        authToken.setPasscode(passcode);

        return authToken;
    }
}
