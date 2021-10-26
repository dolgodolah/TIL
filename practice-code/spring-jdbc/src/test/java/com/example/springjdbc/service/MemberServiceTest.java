package com.example.springjdbc.service;

import com.example.springjdbc.dao.MemberDao;
import com.example.springjdbc.dto.MemberDto;
import com.example.springjdbc.entity.Member;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.transaction.annotation.Transactional;

import java.util.Optional;

import static org.assertj.core.api.Assertions.*;

@SpringBootTest
@Transactional
class MemberServiceTest {

    private static final String NAME = "홍길동";

    @Autowired MemberService memberService;
    @Autowired MemberDao memberDao;

    @Test
    public void 회원가입() {
        MemberDto memberDto = new MemberDto();
        memberDto.setName(NAME);
        Long memberId = memberService.join(memberDto);

        Optional<Member> member = memberDao.findById(memberId);
        assertThat(member.get().getId()).isEqualTo(memberId);
    }

    @Test
    public void ID로_회원찾기() {
        MemberDto memberDto = new MemberDto();
        memberDto.setName(NAME);
        Long memberId = memberService.join(memberDto);
        Optional<Member> member = memberService.findById(memberId);

        assertThat(member.get().getId()).isEqualTo(memberId);
        assertThat(member.get().getName()).isEqualTo(NAME);
    }

    @Test
    public void NAME으로_회원찾기() {
        MemberDto memberDto = new MemberDto();
        memberDto.setName(NAME);
        Long memberId = memberService.join(memberDto);

        Optional<Member> member = memberService.findByName(NAME);

        assertThat(member.get().getId()).isEqualTo(memberId);
        assertThat(member.get().getName()).isEqualTo(NAME);
    }
}