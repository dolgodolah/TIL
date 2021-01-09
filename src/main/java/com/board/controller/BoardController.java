package com.board.controller;


import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;

import com.board.dto.BoardDTO;
import com.board.service.BoardService;


@Controller
public class BoardController {
	private BoardService boardService;

	public BoardController(BoardService boardService) {
		this.boardService = boardService;
	}

	@GetMapping("/list")
	public String list(Model model) {
		List<BoardDTO> boardList = boardService.getBoardList();
		model.addAttribute("postList",boardList);
		return "board/list";
	}
	
	@GetMapping("/post")
	public String post() {
		return "board/post";
	}
	
	@PostMapping("/post")
	public String write(BoardDTO boardDTO) {
		boardService.savePost(boardDTO);
		return "redirect:/list";
	}
	
	@GetMapping("/post/{id}")
	public String detail(@PathVariable("id") Long id, Model model) {
		BoardDTO boardDTO = boardService.getPost(id);
		model.addAttribute("post", boardDTO);
		return "board/detail";
	}
	
	@GetMapping("/post/edit/{id}")
	public String edit(@PathVariable("id") Long id, Model model) {
		BoardDTO boardDTO = boardService.getPost(id);
		model.addAttribute("post", boardDTO);
		return "board/edit";
	}
	
	@PutMapping("/post/edit/{idx}")
	public String update(BoardDTO boardDTO) {
		boardService.savePost(boardDTO);
		return "redirect:/post/" + boardDTO.getId();
		
	}
}
