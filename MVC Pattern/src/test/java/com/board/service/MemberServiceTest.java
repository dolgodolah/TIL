package com.board.service;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;

import com.board.domain.Member;
import com.board.repository.MemoryMemberRepository;

public class MemberServiceTest {

	MemoryMemberRepository repository = new MemoryMemberRepository();
	MemberService service = new MemberService();
	
	
	@Test
	public void join() {
		Member member = new Member();
		member.setName("김규범");
		Member member2 = new Member();
		member2.setName("김규범");
		Member member3 = new Member();
		member3.setName("홍길동");
		System.out.println(service.join(member2));
		System.out.println(service.join(member3));
		System.out.println(service.join(member));
	}
}
