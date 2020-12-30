package com.board;

import java.util.List;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import com.board.domain.BoardDTO;
import com.board.mapper.BoardMapper;
import com.board.service.BoardService;

@SpringBootTest
public class ServiceTest implements BoardService{
	@Autowired
	private BoardMapper boardMapper;

	@Test
	public boolean registerBoard(BoardDTO params) {
		// TODO Auto-generated method stub
		int queryResult = 0;
		if (params.getIdx()==null) {
			queryResult = boardMapper.insertBoard(params);
		}else {
			queryResult = boardMapper.updateBoard(params);
		}
		return (queryResult == 1) ? true : false;
	}
	
	@Test
	public void testOfRegister() {
		BoardDTO params = boardMapper.selectBoardDetail((long)2);
		System.out.println(registerBoard(params));
	}
	

	@Override
	public BoardDTO getBoardDetail(Long idx) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public boolean deleteBoard(Long idx) {
		// TODO Auto-generated method stub
		return false;
	}

	@Override
	public List<BoardDTO> getBoardList() {
		// TODO Auto-generated method stub
		return null;
	}
	
	
}
