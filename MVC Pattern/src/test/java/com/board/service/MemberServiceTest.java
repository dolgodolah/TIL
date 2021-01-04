package com.board.service;

import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.fail;

import java.util.List;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import com.board.domain.Member;
import com.board.repository.MemoryMemberRepository;

public class MemberServiceTest {

	MemoryMemberRepository repository;
	MemberService service;
	@BeforeEach
	public void beforeEach() {
		//Dependency Injection
		repository = new MemoryMemberRepository();
		service = new MemberService(repository);
	}
	
	@AfterEach
	public void afterEach() {
		repository.clearStore();
	}
	
	@Test
	public void 회원가입() {
		//given
		Member member = new Member();
		member.setName("spring");
		//when
		Long saveId = service.join(member);
		//then
		Member result = service.findOne(saveId).get();
		Assertions.assertThat(member.getName()).isEqualTo(result.getName());
	}
	
	@Test
	public void 중복_회원_예외() {
		//given
		Member member1 = new Member();
		Member member2 = new Member();
		member1.setName("spring");
		member2.setName("spring");
		//when
		service.join(member1);
		IllegalStateException e = assertThrows(IllegalStateException.class, () -> service.join(member2));
		System.out.println(e);
//		try {
//			service.join(member2);
//			fail();
//		}catch(IllegalStateException e) {
//			Assertions.assertThat(e.getMessage()).isEqualTo("이미 존재하는 회원입니다.");
//		}
		
		//then
	}
	
	@Test
	public void findMembers() {
		Member member = new Member();
		member.setName("김규범");
		Member member2 = new Member();
		member2.setName("홍길동");
		service.join(member2);
		service.join(member);
		List<Member> result = service.findMembers();
		System.out.println(result.get(0).getName());
	}
	
	@Test
	public void findOne() {
		Member member = new Member();
		member.setName("김규범");
		Member member2 = new Member();
		member2.setName("홍길동");
		service.join(member2);
		service.join(member);
		System.out.println(service.findOne((long) 1).get().getName());
	}
}
