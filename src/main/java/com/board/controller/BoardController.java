package com.board.controller;


import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import com.board.dto.BoardDTO;
import com.board.service.BoardService;


@Controller
public class BoardController {
	private BoardService boardService;

	public BoardController(BoardService boardService) {
		this.boardService = boardService;
	}

	@GetMapping("/list")
	public String list() {
		return "board/list";
	}
	
	@GetMapping("/post")
	public String post() {
		return "board/post";
	}
	
	@PostMapping("/post")
	public String write(BoardDTO boardDTO) {
		boardService.savePost(boardDTO);
		return "redirect:/";
	}
	
	
	
//	@GetMapping(value = "/board/write.do")
//	public String openBoardWrite(@RequestParam(value = "idx", required = false) Long idx, Model model) {
//		if (idx == null) {
//			model.addAttribute("board", new BoardDTO());
//		} else {
//			BoardDTO board = boardService.getBoardDetail(idx);
//			if (board == null) {
//				return "redirect:/board/list.do";
//			}
//			model.addAttribute("board", board);
//		}
//
//		return "board/write";
//	}
//	
//	@PostMapping(value = "/board/register.do")
//	public String registerBoard(final BoardDTO params) {
//		try {
//			boolean isRegistered = boardService.registerBoard(params);
//			if (isRegistered == false) {
//				// TODO => 게시글 등록에 실패하였다는 메시지를 전달
//			}
//		} catch (DataAccessException e) {
//			// TODO => 데이터베이스 처리 과정에 문제가 발생하였다는 메시지를 전달
//
//		} catch (Exception e) {
//			// TODO => 시스템에 문제가 발생하였다는 메시지를 전달
//		}
//
//		return "redirect:/board/list.do";
//	}
//	
//	@GetMapping(value="/board/list.do") 
//	public String openBoardList(Model model) {
//		List boardList = boardService.getBoardList();
//		model.addAttribute("boardList", boardList);
//		return "board/list";
//	}
}
