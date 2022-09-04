package com.example.designpatterns._05_prototype.before;

import java.util.ArrayList;
import java.util.List;

public class App {

    public static void main(String[] args) {
        GithubRepository repository = new GithubRepository();
        repository.setUser("dolgodolah");
        repository.setName("TIL");

        GithubIssue githubIssue = new GithubIssue(repository);
        githubIssue.setId(1);
        githubIssue.setTitle("디자인 패턴: 프로토타입 패턴");

        String url = githubIssue.getUrl();
        System.out.println(url);



        GithubIssue githubIssue2 = new GithubIssue(repository);
        githubIssue2.setId(2);
        githubIssue2.setTitle("디자인 패턴: 빌더 패턴");

        String url2 = githubIssue2.getUrl();
        System.out.println(url2);


        List<String> test = new ArrayList<>();
        test.add("1");

        List<String> test2 = new ArrayList<>(test);

    }
}
