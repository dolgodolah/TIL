package com.example.designpatterns._02_factorymethod.after;

public class AuthToken {

    private String passcode;
    private TokenType type;
    private int expireTime;
    private User user;

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

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
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
