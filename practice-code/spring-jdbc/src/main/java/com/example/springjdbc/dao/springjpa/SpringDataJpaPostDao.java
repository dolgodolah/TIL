package com.example.springjdbc.dao.springjpa;

import com.example.springjdbc.dao.PostDao;
import com.example.springjdbc.entity.Post;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.Optional;

public interface SpringDataJpaPostDao extends JpaRepository<Post, Long>, PostDao {

    @Override
    Post save(Post post);

    @Override
    Optional<Post> findById(Long aLong);

    @Override
    Optional<Post> findByAuthor(String author);

    @Override
    List<Post> findAll();
}
