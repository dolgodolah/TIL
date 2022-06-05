package com.example.springjdbc.dao;

import com.example.springjdbc.entity.Member;
import com.example.springjdbc.entity.MemberType;
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
class JdbcMemberDaoTest {

    private static final String NAME = "홍길동";
    private static final Integer AGE = 25;
    @Autowired MemberDao memberDao;

    @Test
    void 회원가입() {
        Member member = new Member();
        member.setName(NAME);
        member.setAge(AGE);
        member.setMemberType(MemberType.USER);
        
        Member result = memberDao.save(member);

        assertThat(result.getName()).isEqualTo(member.getName());
        assertThat(result.getAge()).isEqualTo(member.getAge());
        assertThat(result.getMemberType()).isEqualTo(member.getMemberType());
    }

    @Test
    void ID로_회원찾기() {
        Member member = new Member();
        member.setName(NAME);
        member.setAge(AGE);
        member.setMemberType(MemberType.USER);
        Member saveMember = memberDao.save(member);

        Optional<Member> result = memberDao.findById(saveMember.getId());

        assertThat(result).isNotNull();
        assertThat(result.get().getId()).isEqualTo(saveMember.getId());
        assertThat(result.get().getName()).isEqualTo(saveMember.getName());
        assertThat(result.get().getAge()).isEqualTo(saveMember.getAge());
        assertThat(result.get().getMemberType()).isEqualTo(saveMember.getMemberType());
    }

    @ParameterizedTest
    @ValueSource(strings = {"홍길동", "김수한무", "거북이"})
    void NAME으로_회원찾기(String input) {
        Member member = new Member();
        member.setName(input);
        member.setAge(AGE);
        member.setMemberType(MemberType.ADMIN);
        Member saveMember = memberDao.save(member);

        Optional<Member> result = memberDao.findByName(input);

        assertThat(result).isNotNull();
        assertThat(result.get().getId()).isEqualTo(saveMember.getId());
        assertThat(result.get().getName()).isEqualTo(saveMember.getName());
        assertThat(result.get().getAge()).isEqualTo(saveMember.getAge());
        assertThat(result.get().getMemberType()).isEqualTo(saveMember.getMemberType());
    }

    @ParameterizedTest
    @CsvSource(value = {"1:1", "2:2", "3:3", "4:4", "10:10"}, delimiter = ':')
    void 전체회원찾기(int input, int expected) {
        for (int i = 0; i < input; i++) {
            Member member = new Member();
            member.setName(NAME + i);
            member.setMemberType(MemberType.USER);
            memberDao.save(member);
        }

        List<Member> members = memberDao.findAll();

        assertThat(members.size()).isEqualTo(expected);
    }

    @Test
    void 회원가입_후_회원탈퇴() {
        Member member = new Member();
        member.setName(NAME);
        member.setAge(AGE);
        Member saveMember = memberDao.save(member);

        memberDao.deleteById(saveMember.getId());

        Optional<Member> result = memberDao.findById(saveMember.getId());

        assertThat(result).isEmpty();
    }
}