package com.example.springjdbc.entity;

public class Member {

    private Long id;
    private String name;

    public Long getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Member(String name) {
        this.name = name;
    }

    public Member() {
    }
}
