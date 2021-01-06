package com.board.service;
import org.springframework.stereotype.Service;

import com.board.domain.repository.BoardRepository;
import com.board.dto.BoardDTO;

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
}