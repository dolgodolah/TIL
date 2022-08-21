package com.example.designpatterns._03_abstract_factory.after;

import com.example.designpatterns._02_factorymethod.after.Member;
import com.example.designpatterns._02_factorymethod.after.User;

public class MemberFactory implements UserFactory {
    @Override
    public User createUser() {
        return new Member();
    }
}
