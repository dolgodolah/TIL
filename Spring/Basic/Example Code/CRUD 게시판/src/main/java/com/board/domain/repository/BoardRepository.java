package com.board.domain.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.board.domain.entity.Board;

public interface BoardRepository extends JpaRepository<Board, Long> {
}