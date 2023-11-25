package com.example.springdocopenapi;

public class Comment {
    private Long id;
    private Long postId;
    private String author;
    private String content;

    public Comment(Long id, Long postId, String author, String content) {
        this.id = id;
        this.postId = postId;
        this.author = author;
        this.content = content;
    }
}