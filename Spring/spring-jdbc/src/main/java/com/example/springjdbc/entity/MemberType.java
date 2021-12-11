package com.example.springjdbc.entity;

public enum MemberType {
    USER(1), ADMIN(2);

    private final int value;

    MemberType(int value) {
        this.value = value;
    }

}
