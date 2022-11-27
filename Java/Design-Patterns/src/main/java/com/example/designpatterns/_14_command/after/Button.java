package com.example.designpatterns._14_command.after;

import com.example.designpatterns._14_command.before.Light;

public class Button {

    private Command command;

    public Button(Command command) {
        this.command = command;
    }

    public void press() {
        command.execute();
    }

    public static void main(String[] args) {
        Button button = new Button(new LightOnCommand(new Light()));
        button.press();
        button.press();

        Button button2 = new Button(new LightOffCommand(new Light()));
        button2.press();
        button2.press();
    }
}
