package com.example.springjdbc.dao;

import com.example.springjdbc.entity.Member;
import com.example.springjdbc.entity.Post;

import javax.persistence.EntityManager;
import java.util.List;
import java.util.Optional;

public class JpaPostDao implements PostDao {

    private final EntityManager em;

    public JpaPostDao(EntityManager em) {
        this.em = em;
    }

    @Override
    public Post save(Post post) {
        em.persist(post);
        return post;
    }

    @Override
    public Optional<Post> findById(Long id) {
        Post post = em.find(Post.class, id);
        return Optional.ofNullable(post);
    }

    @Override
    public Optional<Post> findByAuthor(String author) {
        List<Post> result = em.createQuery("select p from Post p where p.author = :author", Post.class)
                .setParameter("author", author)
                .getResultList();

        return result.stream().findAny();
    }

    @Override
    public List<Post> findAll() {
        return em.createQuery("select p from Post p", Post.class).getResultList();
    }
}
