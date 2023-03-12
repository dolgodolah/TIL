package com.example.designpatterns._20_state.before;

public class Client {

    public static void main(String[] args) {
        Student lee = new Student("Lee");
        Student kim = new Student("Kim");
        OnlineCourse onlineCourse = new OnlineCourse();
        kim.addPrivateCourse(onlineCourse);

        onlineCourse.addStudent(lee);
        onlineCourse.changeState(OnlineCourse.State.PRIVATE);
        onlineCourse.addStudent(kim);
        onlineCourse.addReview("good course", lee);

        System.out.println(onlineCourse.getState());
        System.out.println(onlineCourse.getStudents());
        System.out.println(onlineCourse.getReviews());
    }
}
