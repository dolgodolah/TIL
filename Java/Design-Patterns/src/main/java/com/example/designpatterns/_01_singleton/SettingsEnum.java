package com.example.designpatterns._01_singleton;

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
