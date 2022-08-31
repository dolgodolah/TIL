package com.example.designpatterns._04_builder.after;

import com.example.designpatterns._04_builder.before.TourPlan;

import java.time.LocalDate;

public class App {
    public static void main(String[] args) {

        /**
         * DefaultTourBuilder 사용
         */
        TourPlanBuilder builder = new DefaultTourBuilder();
        TourPlan cancunTrip = builder.title("칸쿤 여행")
                .nightsAndDays(2, 3)
                .startDate(LocalDate.of(2023, 8, 1))
                .whereToStay("리조트")
                .addPlan(0, "체크인하고 짐풀기")
                .addPlan(0, "저녁 식사")
                .getPlan();
        System.out.println(cancunTrip);


        TourPlanBuilder builder2 = new DefaultTourBuilder();
        TourPlan longBeachTrip = builder2.title("롱비치")
                .startDate(LocalDate.of(2022, 12, 30))
                .getPlan();
        System.out.println(longBeachTrip);


        /**
         * TourDirector 사용
         */
        TourDirector director = new TourDirector(new DefaultTourBuilder());
        TourPlan tourPlan = director.cancunTrip();
        System.out.println(tourPlan);

        TourDirector director2 = new TourDirector(new DefaultTourBuilder());
        TourPlan tourPlan2 = director2.longBeachTrip();
        System.out.println(tourPlan2);
    }
}
