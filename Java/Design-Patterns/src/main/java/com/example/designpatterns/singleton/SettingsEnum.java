package com.example.designpatterns.singleton;

public enum SettingsEnum {

    INSTANCE;

    private int value;

    public void up() {
        value++;
    }

    public int getValue() {
        return value;
    }

}
