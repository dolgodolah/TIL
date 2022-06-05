package com.example.springjdbc.dao;

import com.example.springjdbc.entity.Member;

import java.util.List;
import java.util.Optional;

public interface MemberDao {
    Member save(Member member);
    Optional<Member> findById(Long id);
    Optional<Member> findByName(String name);
    List<Member> findAll();
    int getAllMemberCount();
    void deleteById(Long id);
}
