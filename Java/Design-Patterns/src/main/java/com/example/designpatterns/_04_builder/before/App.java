package com.example.designpatterns._04_builder.before;

import java.time.LocalDate;

public class App {
    public static void main(String[] args) {
        TourPlan cancunTrip = new TourPlan();
        cancunTrip.setTitle("칸쿤 여행");
        cancunTrip.setNights(2);
        cancunTrip.setDays(3);
        cancunTrip.setStartDate(LocalDate.of(2022, 12, 9));
        cancunTrip.setWhereToStay("리조트");
        cancunTrip.addPlan(0, "체크인 이후 짐풀기");
        cancunTrip.addPlan(0, "저녁 식사");
        cancunTrip.addPlan(1, "조식 부페에서 식사");
        cancunTrip.addPlan(1, "해변가 산책");
        cancunTrip.addPlan(1, "점심은 수영장 근처 음식점에서 먹기");
        cancunTrip.addPlan(1, "리조트 수영장에선 놀기");
        cancunTrip.addPlan(1, "저녁은 BBQ 식당에서 스테이크");
        cancunTrip.addPlan(2, "조식 부페에서 식사");
        cancunTrip.addPlan(2, "체크아웃");

        // 객체를 생성하는 일관된 프로세스가 없다.
        TourPlan longBeachTrip = new TourPlan();
        longBeachTrip.setTitle("오레곤 롱비치 여행");
        longBeachTrip.setStartDate(LocalDate.of(2023, 8, 1));

        // days 설정 시 nights 설정이 되어야 하는데 이를 강제할 수가 없다.
        longBeachTrip.setDays(0);
        longBeachTrip.setNights(0); // 실수로 누락될 수 있음.

        // 강제하려면 생성자가 많아질 수 있다. -> 어떤 생성자를 사용해야하는지 헷갈릴 수 있다.
        // 그리고 필요없는 필드에 null 을 넣어야 한다.
        new TourPlan("오레곤 롱비치 여행", 2, 3, LocalDate.of(2023, 8, 1), "리조트");
        new TourPlan("오레곤 롱비치 여행", 2, 3, LocalDate.of(2023, 8, 1));

    }
}
