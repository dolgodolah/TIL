package com.example.designpatterns._11_fliyweight.after;

public class Client {
    public static void main(String[] args) {
        FontFactory fontFactory = new FontFactory();
        Character c1 = new Character('h', "white", fontFactory.getFont("nanum:12")); // cache miss 최초 인스턴스 생성
        Character c2 = new Character('e', "white", fontFactory.getFont("nanum:12")); // cache hit
        Character c3 = new Character('l', "white", fontFactory.getFont("nanum:12")); // cache hit
        Character c4 = new Character('l', "white", fontFactory.getFont("nanum:12")); // cache hit
        Character c5 = new Character('o', "white", fontFactory.getFont("nanum:12")); // cache hit

    }
}
