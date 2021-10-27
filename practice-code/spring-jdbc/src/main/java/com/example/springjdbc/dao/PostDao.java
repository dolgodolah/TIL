package com.example.springjdbc.dao;

import com.example.springjdbc.entity.Post;

import java.util.List;
import java.util.Optional;

public interface PostDao {
    Post save(Post post);
    Optional<Post> findById(Long id);
    Optional<Post> findByAuthor(String author);
    List<Post> findAll();
}
