package com.example.designpatterns._01_singleton;

public class App {

    public static void main(String[] args) {

        Settings settings1 = Settings.getInstance();
        Settings settings2 = Settings.getInstance();
        System.out.println(settings1 == settings2); // true

        settings1.up();
        settings2.up();
        System.out.println(settings1.getValue() == 2); // true
        System.out.println(settings2.getValue() == 2); // true

        //

        SettingsEnum settings3 = SettingsEnum.INSTANCE;
        SettingsEnum settings4 = SettingsEnum.INSTANCE;

        System.out.println(settings3 == settings4); // true

        settings3.up();
        settings4.up();
        System.out.println(settings3.getValue() == 2); // true
        System.out.println(settings4.getValue() == 2); // true

    }
}
