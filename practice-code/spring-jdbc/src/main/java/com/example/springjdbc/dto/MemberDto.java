package com.example.springjdbc.dto;

import com.example.springjdbc.entity.Member;

public class MemberDto {
    private String name;

    public void setName(String name) {
        this.name = name;
    }

    public Member toEntity() {
        Member member = new Member();
        member.setName(name);
        return member;
    }
}
