package com.example.designpatterns._15_interpreter.after;

import java.util.Stack;

public class PostfixParser {

    public static PostfixExpression parse(String expression) {
        Stack<PostfixExpression> stack = new Stack<>();
        for (char c : expression.toCharArray()) {
            stack.push(getExpression(c, stack));
        }

        return stack.pop();
    }

    private static PostfixExpression getExpression(char c, Stack<PostfixExpression> stack) {
        switch (c) {
            case '+':
                return PostfixExpression.plus(stack.pop(), stack.pop());
            case '-':
                PostfixExpression right = stack.pop();
                PostfixExpression left = stack.pop();
                return PostfixExpression.minus(left, right);
            default:
                return PostfixExpression.variable(c);
        }
    }
}
