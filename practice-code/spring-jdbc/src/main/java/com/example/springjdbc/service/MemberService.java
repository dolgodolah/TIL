package com.example.springjdbc.service;

import com.example.springjdbc.dao.MemberDao;
import com.example.springjdbc.dto.MemberDto;
import com.example.springjdbc.entity.Member;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class MemberService {

    private final MemberDao memberDao;

    public MemberService(MemberDao memberDao) {
        this.memberDao = memberDao;
    }

    public Long join(MemberDto memberDto) {
        Member member = memberDao.save(memberDto.toEntity());
        return member.getId();
    }

    public Optional<Member> findById(Long id) {
        return memberDao.findById(id);
    }

    public Optional<Member> findByName(String name) {
        return memberDao.findByName(name);
    }
}
