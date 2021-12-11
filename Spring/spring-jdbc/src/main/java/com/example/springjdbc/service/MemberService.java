package com.example.springjdbc.service;

import com.example.springjdbc.dao.MemberDao;
import com.example.springjdbc.entity.Member;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;

@Service
public class MemberService {

    private final MemberDao memberDao;

    public MemberService(MemberDao memberDao) {
        this.memberDao = memberDao;
    }

    @Transactional
    public Long join(Member member) {
        memberDao.save(member);
        return member.getId();
    }

    public Optional<Member> findById(Long id) {
        return memberDao.findById(id);
    }

    public Optional<Member> findByName(String name) {
        return memberDao.findByName(name);
    }

    public List<Member> findAll() {
        return memberDao.findAll();
    }
}
