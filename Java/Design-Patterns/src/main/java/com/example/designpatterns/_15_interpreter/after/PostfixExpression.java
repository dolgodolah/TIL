package com.example.designpatterns._15_interpreter.after;

import java.util.Map;

public interface PostfixExpression {

    int interpret(Map<Character, Integer> context);

    // 람다 버전
    static PostfixExpression plus(PostfixExpression left, PostfixExpression right) {
        return context -> left.interpret(context) + right.interpret(context);
    }

    // 익명 클래스 버전
    static PostfixExpression minus(PostfixExpression left, PostfixExpression right) {
        return new PostfixExpression() {
            @Override
            public int interpret(Map<Character, Integer> context) {
                return left.interpret(context) - right.interpret(context);
            }
        };
    }

    static PostfixExpression variable(Character c) {
        return context -> context.get(c);
    }
}
