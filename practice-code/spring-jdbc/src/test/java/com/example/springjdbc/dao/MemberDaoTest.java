package com.example.springjdbc.dao;

import com.example.springjdbc.entity.Member;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.ValueSource;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;

import static org.assertj.core.api.Assertions.assertThat;

@SpringBootTest
@Transactional
class MemberDaoTest {

    private static final String NAME = "홍길동";
    @Autowired MemberDao memberDao;

    @Test
    void 회원가입() {
        Member member = new Member();
        member.setName(NAME);
        Member result = memberDao.save(member);

        assertThat(result.getName()).isEqualTo(NAME);
    }

    @Test
    void ID로_회원찾기() {
        Member member = new Member();
        member.setName(NAME);
        Member saveMember = memberDao.save(member);

        Optional<Member> result = memberDao.findById(saveMember.getId());

        assertThat(result).isNotNull();
        assertThat(result.get().getId()).isEqualTo(saveMember.getId());
        assertThat(result.get().getName()).isEqualTo(saveMember.getName());
    }

    @ParameterizedTest
    @ValueSource(strings = {"홍길동", "김수한무", "거북이"})
    void NAME으로_회원찾기(String input) {
        Member member = new Member();
        member.setName(input);
        Member saveMember = memberDao.save(member);

        Optional<Member> result = memberDao.findByName(input);

        assertThat(result).isNotNull();
        assertThat(result.get().getId()).isEqualTo(saveMember.getId());
        assertThat(result.get().getName()).isEqualTo(saveMember.getName());
    }

    @ParameterizedTest
    @CsvSource(value = {"1:1", "2:2", "3:3", "4:4", "10:10"}, delimiter = ':')
    void 전체회원찾기(int input, int expected) {
        for (int i = 0; i < input; i++) {
            Member member = new Member();
            member.setName(NAME + i);
            memberDao.save(member);
        }

        List<Member> members = memberDao.findAll();

        assertThat(members.size()).isEqualTo(expected);
    }
}