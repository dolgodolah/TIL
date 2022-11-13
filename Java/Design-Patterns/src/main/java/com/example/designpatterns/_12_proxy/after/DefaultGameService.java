package com.example.designpatterns._12_proxy.after;

public class DefaultGameService implements GameService {
    @Override
    public void startGame() {
        System.out.println("게임 시작");
    }
}
