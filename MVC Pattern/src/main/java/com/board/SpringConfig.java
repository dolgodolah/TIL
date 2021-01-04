package com.board;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import com.board.repository.MemberRepository;
import com.board.repository.MemoryMemberRepository;
import com.board.service.MemberService;

@Configuration
public class SpringConfig {
	@Bean
	public MemberService memberService() {
		return new MemberService(memberRepository());
	}
	
	@Bean
	public MemberRepository memberRepository() {
		return new MemoryMemberRepository();
	}
}
