package com.board.service;
import org.springframework.stereotype.Service;

import com.board.domain.entity.Board;
import com.board.domain.repository.BoardRepository;
import com.board.dto.BoardDTO;

import java.util.ArrayList;
import java.util.List;

import javax.transaction.Transactional;

@Service
public class BoardService {
    private BoardRepository boardRepository;

    public BoardService(BoardRepository boardRepository) {
        this.boardRepository = boardRepository;
    }

    @Transactional
    public Long savePost(BoardDTO boardDTO) {
        return boardRepository.save(boardDTO.toEntity()).getId();
    }
    
    @Transactional
    public List<BoardDTO> getBoardList(){
    	//db에 있는 게시물 전부 찾아 boardList에 저장
    	List<Board> boardList = boardRepository.findAll();
    	//찾은 게시물을 담을 boardDTOList 생성
    	List<BoardDTO> boardDTOList = new ArrayList<>();
    	
    	for(Board board : boardList) {
    		BoardDTO boardDTO = BoardDTO.builder()
    				.id(board.getId())
    				.author(board.getAuthor())
    				.title(board.getTitle())
    				.content(board.getContent())
    				.createdDate(board.getCreatedDate())
    				.build();
    		boardDTOList.add(boardDTO);
    	}
    	return boardDTOList;
    }
    
    @Transactional
    public BoardDTO getPost(Long id) {
    	Board board = boardRepository.findById(id).get();
    	
    	BoardDTO boardDTO = BoardDTO.builder()
    			.id(board.getId())
    			.author(board.getAuthor())
    			.title(board.getTitle())
    			.content(board.getContent())
    			.createdDate(board.getCreatedDate())
    			.build();
    	return boardDTO;
    }
}