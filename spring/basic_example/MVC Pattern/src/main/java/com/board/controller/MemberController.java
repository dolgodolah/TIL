package com.board.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import com.board.domain.Member;
import com.board.service.MemberService;

@Controller
public class MemberController {
	private final MemberService memberService;

	@Autowired
	public MemberController(MemberService memberService) {
		this.memberService = memberService;
	}
	
	
	// localhost:8080/members/new로 들어오게 되면 createForm()에 매핑된다.
	@GetMapping("/members/new")
	public String createForm() {
		return "members/createMemberForm";
	}
	
	// localhost:8080/members/new에서 Post를 받게 되면 create()에 매핑된다.
	@PostMapping("/members/new")
	public String create(MemberForm form) { //입력받은 name을 form에 저장하고
		Member member = new Member();
		member.setName(form.getName()); //form의 name을 member의 이름으로 설정한다.
		
		memberService.join(member); //해당 member를 서비스로직을 통해 가입시킨다.
		
		return "redirect:/"; // localhost:8080/로 변경된다. <-> forward는 주소는 그대로고 내용만 localhost:8080/의 내용으로 바뀐다.
	}
	
	
	@GetMapping("/members")
	public String list(Model model) {
		List<Member> members = memberService.findMembers();
		model.addAttribute("members", members);
		return "members/memberList";
	}
	
}
