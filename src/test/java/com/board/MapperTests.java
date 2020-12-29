package com.board;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import com.board.domain.BoardDTO;
import com.board.mapper.BoardMapper;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.core.io.JsonEOFException;
import com.fasterxml.jackson.databind.ObjectMapper;

@SpringBootTest
class MapperTests {

	@Autowired
	private BoardMapper boardMapper;

	@Test
	public void testOfInsert() {
		BoardDTO params = new BoardDTO();
		params.setTitle("1번 게시글 제목");
		params.setContent("1번 게시글 내용");
		params.setWriter("테스터");

		int result = boardMapper.insertBoard(params);
		System.out.println("결과는 " + result + "입니다.");
	}
	
	@Test
	public void  testOfSelectDetail() {
		BoardDTO board = boardMapper.selectBoardDetail((long) 1);
		try {
			String boardJson = new ObjectMapper().writeValueAsString(board);
			System.out.println("==============");
			System.out.println(boardJson);
			System.out.println("==============");
		}catch(JsonProcessingException e) {
			e.printStackTrace();
		}
	}
	
	@Test
	public void testOfUpdate() {
		BoardDTO params = new BoardDTO();
		params.setTitle("1번 게시글 제목을 수정");
		params.setContent("1번 게시글 내용 수정");
		params.setWriter("홍길동");
		params.setIdx((long) 1);
		
		int result = boardMapper.updateBoard(params);
		if (result==1) {
			BoardDTO board = boardMapper.selectBoardDetail(params.getIdx());
			try {
				String boardJson = new ObjectMapper().writeValueAsString(board);
				System.out.println("==============");
				System.out.println(boardJson);
				System.out.println("==============");
			}catch(JsonProcessingException e) {
				e.printStackTrace();
			}
		}
	}

}