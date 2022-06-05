package com.example.springjdbc.dao;

import com.example.springjdbc.dao.springjpa.SpringDataJpaPostDao;
import com.example.springjdbc.entity.Post;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.ValueSource;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;

import static org.assertj.core.api.Assertions.*;

@SpringBootTest
@Transactional
class SpringDataJpaPostDaoTest {

    private static final String AUTHOR = "홍길동";
    private static final String CONTENT = "오늘 날씨 맑음 내일 날씨 흐림";

    @Autowired
    SpringDataJpaPostDao springDataJpaPostDao;

    @Test
    void 등록하기() {
        Post post = new Post();
        post.setAuthor(AUTHOR);
        post.setContent(CONTENT);

        Post result = springDataJpaPostDao.save(post);

        assertThat(result.getAuthor()).isEqualTo(post.getAuthor());
        assertThat(result.getContent()).isEqualTo(post.getContent());
    }

    @Test
    void ID로_조회하기() {
        Post post = new Post();
        post.setAuthor(AUTHOR);
        post.setContent(CONTENT);
        Post savePost = springDataJpaPostDao.save(post);

        Optional<Post> result = springDataJpaPostDao.findById(savePost.getId());

        assertThat(result).isNotNull();
        assertThat(result.get().getAuthor()).isEqualTo(savePost.getAuthor());
        assertThat(result.get().getContent()).isEqualTo(savePost.getContent());
    }

    @ParameterizedTest
    @ValueSource(strings = {"홍길동", "김수한무", "거북이"})
    void AUTHOR로_조회하기(String input) {
        Post post = new Post();
        post.setAuthor(input);
        post.setContent(CONTENT);
        Post savePost = springDataJpaPostDao.save(post);

        Optional<Post> result = springDataJpaPostDao.findByAuthor(input);

        assertThat(result).isNotNull();
        assertThat(result.get().getAuthor()).isEqualTo(savePost.getAuthor());
        assertThat(result.get().getContent()).isEqualTo(savePost.getContent());
    }

    @ParameterizedTest
    @CsvSource(value = {"1:1", "2:2", "3:3", "4:4", "10:10"}, delimiter = ':')
    void 전체조회하기(int input, int expected) {
        for (int i = 0; i < input; i++) {
            Post post = new Post();
            post.setAuthor(AUTHOR + i);
            post.setContent(CONTENT);
            springDataJpaPostDao.save(post);
        }

        List<Post> posts = springDataJpaPostDao.findAll();

        assertThat(posts.size()).isEqualTo(expected);
    }
}
