package com.board.service;

import java.util.List;
import java.util.Optional;

import com.board.domain.Member;
import com.board.repository.MemberRepository;
import com.board.repository.MemoryMemberRepository;

public class MemberService {

	private final MemberRepository memberRepository = new MemoryMemberRepository();
	
	public Long join(Member member) {
		validateDuplicateMember(member); //중복 회원 확인
		memberRepository.save(member);
		return member.getId();
	}

	private void validateDuplicateMember(Member member) {
		memberRepository.findByName(member.getName())
			.ifPresent(m->{
				throw new IllegalStateException("이미 존재하는 회원입니다.");
			});
	}
	
	
	public List<Member> findMembers(){
		return memberRepository.findAll();
	}
	
	public Optional<Member> findOne(Long memberId){
		return memberRepository.findById(memberId);
	}
}
