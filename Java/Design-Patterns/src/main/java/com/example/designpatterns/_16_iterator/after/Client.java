package com.example.designpatterns._16_iterator.after;

import com.example.designpatterns._16_iterator.before.Post;

import java.util.Collections;
import java.util.Iterator;
import java.util.List;

public class Client {

    public static void main(String[] args) {
        Board board = new Board();
        board.addPost("디자인 패턴");
        board.addPost("BTS");
        board.addPost("손흥민");

        // 들어간 순서대로
        List<Post> posts = board.getPosts();
        for (int i = 0; i < posts.size(); i++) {
            Post post = posts.get(i);
            System.out.println(post.getContent());
        }

        // 최신 글 순서대로
        Iterator<Post> recentPostIterator = board.getRecentPostIterator();
        while (recentPostIterator.hasNext()) {
            System.out.println(recentPostIterator.next().getContent());
        }
    }
}
