package com.example.designpatterns._03_abstract_factory.after;

import com.example.designpatterns._02_factorymethod.after.User;

/**
 * 추상 팩토리
 */
public interface UserFactory {
    User createUser();
}
