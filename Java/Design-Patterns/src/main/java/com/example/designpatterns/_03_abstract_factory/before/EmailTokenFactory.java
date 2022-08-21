package com.example.designpatterns._03_abstract_factory.before;

import com.example.designpatterns._02_factorymethod.after.AuthToken;
import com.example.designpatterns._02_factorymethod.after.DefaultAuthTokenFactory;
import com.example.designpatterns._02_factorymethod.after.EmailToken;
import com.example.designpatterns._02_factorymethod.after.Member;

public class EmailTokenFactory extends DefaultAuthTokenFactory {
    @Override
    public AuthToken generate(String passcode) {
        AuthToken authToken = new EmailToken(passcode);

        // 사용자를 회원(Member) -> 비회원(Guest)로 바꾸려면 여기를 수정해야 한다.
        // 회원, 비회원 외에 또 다른 사용자가 추가된다면 바뀔 가능성이 더 생긴다.
        authToken.setUser(new Member());
        return authToken;
    }
}
