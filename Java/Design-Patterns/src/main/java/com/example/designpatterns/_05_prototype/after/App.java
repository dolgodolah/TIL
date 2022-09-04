package com.example.designpatterns._05_prototype.after;

public class App {

    public static void main(String[] args) throws CloneNotSupportedException {
        GithubRepository repository = new GithubRepository();
        repository.setUser("dolgodolah");
        repository.setName("TIL");

        GithubIssue githubIssue = new GithubIssue(repository);
        githubIssue.setId(1);
        githubIssue.setTitle("디자인 패턴: 프로토타입 패턴");

        String url = githubIssue.getUrl();
        System.out.println(url);


        GithubIssue clone = (GithubIssue) githubIssue.clone();
        System.out.println(clone.getUrl());

        repository.setName("test");

        System.out.println(clone != githubIssue); // true
        System.out.println(clone.equals(githubIssue)); // true
        System.out.println(clone.getClass() == githubIssue.getClass()); // true
        System.out.println(clone.getRepository() == githubIssue.getRepository()); // shallow copy 일 경우 true, deep copy 일 경우 false
    }
}
