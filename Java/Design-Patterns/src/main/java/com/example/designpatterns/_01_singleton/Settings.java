package com.example.designpatterns._01_singleton;

public class Settings {

    private static final Settings INSTANCE = new Settings();

    private int value;

    private Settings() {
    }

    public static Settings getInstance() {
        return INSTANCE;
    }

    public void up() {
        value++;
    }

    public int getValue() {
        return value;
    }
}
