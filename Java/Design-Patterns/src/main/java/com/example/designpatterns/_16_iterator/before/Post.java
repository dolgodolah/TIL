package com.example.designpatterns._16_iterator.before;

import java.time.LocalDateTime;

public class Post {

    private String content;
    private LocalDateTime createdDateTime;

    public Post(String content) {
        this.content = content;
        this.createdDateTime = LocalDateTime.now();
    }

    public String getContent() {
        return content;
    }

    public LocalDateTime getCreatedDateTime() {
        return createdDateTime;
    }
}
