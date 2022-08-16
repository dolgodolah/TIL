package com.example.designpatterns._02_factorymethod.before;

public class AuthToken {

    private String passcode;
    private TokenType type;
    private int expireTime;

    public String getPasscode() {
        return passcode;
    }

    public void setPasscode(String passcode) {
        this.passcode = passcode;
    }

    public TokenType getType() {
        return type;
    }

    public void setType(TokenType type) {
        this.type = type;
    }

    public int getExpireTime() {
        return expireTime;
    }

    public void setExpireTime(int expireTime) {
        this.expireTime = expireTime;
    }

    @Override
    public String toString() {
        return "AuthToken{" +
                "passcode='" + passcode + '\'' +
                ", type=" + type +
                ", expireTime=" + expireTime +
                '}';
    }

    public enum TokenType {
        EMAIL, SMS;
    }
}
