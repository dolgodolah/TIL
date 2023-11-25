package com.example.springdocopenapi;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicLong;
import java.util.stream.Collectors;

@RestController
public class BlogController {

    private final Map<Long, Post> posts = new ConcurrentHashMap<>();
    private final Map<Long, Comment> comments = new ConcurrentHashMap<>();

    private AtomicLong postIdGenerator = new AtomicLong(1);
    private AtomicLong commentIdGenerator = new AtomicLong(1);

    @GetMapping("/posts/{postId}")
    public ResponseEntity<Post> getPost(@PathVariable Long postId) {
        Post post = posts.get(postId);

        if (post == null) {
            return ResponseEntity.notFound().build();
        }

        return ResponseEntity.ok(post);
    }

    @GetMapping("/posts")
    public ResponseEntity<List<Post>> getPosts(@RequestParam(defaultValue = "true") boolean desc) {
        if (desc) {
            List<Post> values = posts.values().stream()
                    .sorted(Collections.reverseOrder(Comparator.comparing(Post::getId)))
                    .collect(Collectors.toList());

            return ResponseEntity.ok(values);
        }

        List<Post> values = new ArrayList<>(posts.values());
        return ResponseEntity.ok(values);
    }

    @PostMapping("/posts")
    public ResponseEntity<Void> createPost(@RequestBody CreatePostDTO createPostDTO) {
        long id = postIdGenerator.getAndIncrement();
        Post post = new Post(id, createPostDTO.author, createPostDTO.title, createPostDTO.content);
        posts.put(id, post);
        return ResponseEntity.ok().build();
    }


    static class CreatePostDTO {
        private String author;
        private String title;
        private String content;

        public String getAuthor() {
            return author;
        }

        public String getTitle() {
            return title;
        }

        public String getContent() {
            return content;
        }
    }

}
