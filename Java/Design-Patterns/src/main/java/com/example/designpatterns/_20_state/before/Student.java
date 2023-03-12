package com.example.designpatterns._20_state.before;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

public class Student {
    private String name;
    private Set<OnlineCourse> onlineCourses = new HashSet<>();

    public Student(String name) {
        this.name = name;
    }

    public void addPrivateCourse(OnlineCourse onlineCourse) {
        this.onlineCourses.add(onlineCourse);
    }

    public String getName() {
        return name;
    }

    public Set<OnlineCourse> getOnlineCourses() {
        return onlineCourses;
    }

    @Override
    public String toString() {
        return "Student{" +
                "name='" + name + '\'' +
                '}';
    }
}
