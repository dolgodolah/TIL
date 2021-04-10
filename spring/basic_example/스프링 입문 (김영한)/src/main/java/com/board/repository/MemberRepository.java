package com.board.repository;

import java.util.List;
import java.util.Optional;

import com.board.domain.Member;

public interface MemberRepository {
	Member save(Member member);
	//Optional : null을 처리하는 방법
	Optional<Member> findById(Long id);
	Optional<Member> findByName(String name);
	List<Member> findAll();
}
