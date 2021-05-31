# JPA 연관관계 매핑 방법

김영한님의 스프링 JPA 강의를 듣고 정리를 한 글입니다.

ORM을 통한 단방향 연관관계와 양방향 연관관계 매핑에 대해 알아보겠습니다.

## 단방향 연관관계
설계 과정에서는 웬만하면 단방향 관계 매핑을 권장한다고 합니다.

설계가 다 끝난 후 양방향 관계가 꼭 필요한 경우에만 수정을 합니다.

양방향으로 설계하지 않아도 join을 통한 FK로 양방향 조회를 할 수 있습니다.

Member 클래스
```java
@Entity
@Getter
@NoArgsConstructor
public class Member{
    @Id
    @GeneratedValue(strategy=GenerationType.IDENTITY)
    @Column
    private Long id;
    private String username;

    @ManyToOne
    @JoinColumn(name="TEAM_ID")
    // Member테이블의 team_id는 Team테이블을 참조한다.
    // 즉, Member테이블에 외래키(FK)가 있다.
    private Team team; //Member -> Team

    @Builder
    private Member(Long id, String username, Team team){
        this.id=id;
        this.username=username;
        this.team=team;
    }
}
```
Team 클래스
```java
@Entity
@Getter
@NoArgsConstructor
public class Team{
    @Id
    @GeneratedValue(strategy=Generation.Type.IDENTITY)
    private Long id;
    private String name;

    @Builder
    private Team(Long id, String name){
        this.id=id;
        this.name=name;
    }
}
```

## 양방향 연관관계

위 단방향 설계에서 양방향으로 설계하기 위해서는 Team 클래스를 수정합니다.

Team 클래스
```java
@Entity
@Getter
@NoArgsConstructor
public class Team{
    @Id
    @GeneratedValue(strategy=Generation.Type.IDENTITY)
    private Long id;
    private String name;

    @OneToMany(mappedBy="team")
    private List<Member> members = new Arraylist<>(); // Team -> Member

    @Builder
    private Team(Long id, String name){
        this.id=id;
        this.name=name;
    }
}
```
양방향 매핑에서 주의해야할 규칙들입니다.
- 두 객체의 관계 중 하나를 연관관계의 주인으로 지정하는데 FK를 가지고 있는 쪽을 주인으로 지정합니다.(Member가 주인)
- 즉, 연관관계의 주인만이 외래키를 관리(등록,수정)합니다.

- 주인이 아닌쪽은 mappedBy로 주인을 지정해줍니다.
- @OneToMany(mappedBy="team") -> 나는 team에 의해서 관리가 된다. -> Member 객체의 team 변수에 의해 관리가 됩니다.

- 두 객체의 양방향 관계는 사실 서로 다른 단방향 관계 2개인 것입니다.

## 참고
[https://jyami.tistory.com/20](https://jyami.tistory.com/20)

[https://friends-aihaja.tistory.com/entry/5-%EC%96%91%EB%B0%A9%ED%96%A5-%EC%97%B0%EA%B4%80%EA%B4%80%EA%B3%84%EC%99%80-%EC%97%B0%EA%B4%80%EA%B4%80%EA%B3%84-%EC%A3%BC%EC%9D%B8](https://friends-aihaja.tistory.com/entry/5-%EC%96%91%EB%B0%A9%ED%96%A5-%EC%97%B0%EA%B4%80%EA%B4%80%EA%B3%84%EC%99%80-%EC%97%B0%EA%B4%80%EA%B4%80%EA%B3%84-%EC%A3%BC%EC%9D%B8)