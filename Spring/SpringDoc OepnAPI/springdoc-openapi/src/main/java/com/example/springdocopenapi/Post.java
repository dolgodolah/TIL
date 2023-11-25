package com.example.springdocopenapi;

import java.util.Collections;
import java.util.List;

public class Post {
    private Long id;
    private String author;
    private String title;
    private String content;
    private List<Comment> comments;

    public Post(Long id, String author, String title, String content) {
        this.id = id;
        this.author = author;
        this.title = title;
        this.content = content;
        this.comments = Collections.emptyList();
    }

    public Long getId() {
        return id;
    }

    public String getAuthor() {
        return author;
    }

    public String getTitle() {
        return title;
    }

    public String getContent() {
        return content;
    }

    public List<Comment> getComments() {
        return comments;
    }
}