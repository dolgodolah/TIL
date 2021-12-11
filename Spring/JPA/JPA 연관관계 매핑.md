# JPA 연관관계 매핑 방법

김영한님의 스프링 JPA 강의를 듣고 정리를 한 글입니다.

ORM을 통한 단방향 연관관계와 양방향 연관관계 매핑에 대해 알아보겠습니다.

## 연관관계 매핑을 사용하지 않을 경우

Member -> Team 의 참조없이 Member에서 Team의 기본키를 외래키로 사용합니다.

```java
//Member 클래스
@Entity
@Getter
@Setter
public class Member{
    @Id @GeneratedValue
    private Long id;
    private String name;
    private Long teamId; //FK로 사용
}

//Team 클래스
@Entity
@Getter
@Setter
@NoArgsConstructor
public class Team{
    @Id @GeneratedValue
    private Long id;
    private String name;
}

//팀 저장
Team team = new Team();
team.setName("teamA");
em.persist(team);

//멤버 저장
Member member = new Member();
member.setName("memberA");
member.setTeamId(team.getId());
em.persist(member);

//조회
Member findMember = em.find(Member.class, member.getId());
Long findTeamId = findMember.getTeamId();
Team findTeam = em.find(Team.class, findTeamdId);
//Member를 뽑고, Member를 통해 TeamId를 뽑고, TeamId를 통해 Team을 뽑습니다.
```

## 단방향 연관관계

Member에서 Team을 참조해보도록 설계해보겠습니다.

설계 과정에서는 웬만하면 단방향 관계 매핑을 권장한다고 합니다.

설계가 다 끝난 후 양방향 관계가 꼭 필요한 경우에만 수정을 합니다.

양방향으로 설계하지 않아도 join을 통한 FK로 양방향 조회를 할 수 있습니다.

```java
//member 클래스
@Entity
@Getter
@Setter
@NoArgsConstructor
public class Member{
    @Id @GeneratedValue(strategy=GenerationType.IDENTITY)
    private Long id;
    private String name;

    @ManyToOne
    @JoinColumn(name="TEAM_ID")
    private Team team; //Member -> Team
}

//team 클래스
@Entity
@Setter
@Getter
@NoArgsConstructor
public class Team{
    @Id @GeneratedValue(strategy=Generation.Type.IDENTITY)
    private Long id;
    private String name;
}

//팀 생성
Team team = new Team();
team.setName("teamA");
em.persist(team);

//멤버 생성
Member member = new Member();
member.setName("memberA");
member.setTeam(team);
em.persist(member);

//조회
Member findMember = em.find(Member.class, member.getId());
Team findTeam = em.find(Team.class, member.getTeam()); //Member가 Team을 참조하므로 멤버의 팀을 바로 조회할 수 있습니다.
```

## 양방향 연관관계

위 단방향 설계에 이어서 Team->Member를 참조하도록 Team 클래스를 수정하겠습니다.

```java
//Member 클래스
@Entity
@Getter
@Setter
@NoArgsConstructor
public class Member{
    @Id @GeneratedValue(strategy=Generation.Type.IDENTITY)
    private Long id;
    private String name;

    @ManyToOne
    @JoinColumn(name="TEAM_ID")
    private Team team; // Member -> Team
}

//Team 클래스
@Entity
@Getter
@Setter
@NoArgsConstructor
public class Team{
    @Id
    @GeneratedValue(strategy=Generation.Type.IDENTITY)
    private Long id;
    private String name;

    @OneToMany(mappedby="team")
    private List<Member> members = new ArrayList<>(); // Team -> Member
}

//팀 생성
Team team = new Team();
team.setName("teamA");
em.persist(team);

//멤버1 생성
Member member1 = new Member();
member1.setName("member1");
member1.setTeam(team);
//team.getMembers().add(member1);
em.persist(member1);

//멤버2 생성
Member member2 = new Member();
member2.setName("member2");
member2.setTeam(team);
//team.getMembers().add(member2);
em.persist(member2);

//Team -> Member 조회
Team findTeam = em.find(Team.class, team.getId());
List<Member> members = findTeam.getMembers(); // Team -> Member로 객체 그래프 탐색
for (Member m : members){
    System.out.println(m.getName());
}
```

Team -> Member 방향의 조회도 이처럼 양방향 연관관계를 통해 가능합니다.

여기서 몇 가지 주의할 점이 있습니다. 멤버1과 멤버2 생성하는 코드를 보면

멤버의 팀은 설정(member->team)했지만 팀의 멤버 추가(team->member)는 주석처리가 돼있습니다.

실제로 주석처리를 해도 관계형 디비를 확인해보면 정상작동하는 걸 볼 수 있습니다.

하지만 객체 관점에서도 입력해주어야 안전합니다.

양쪽 모두 값을 입력해주지 않으면 JPA를 사용하지 않은 순수한 객체 상태에서 문제가 발생할 수 있습니다.

다음은 양방향 매핑을 하기 위해 알아둬야할(명심해야할) 것들입니다.
- 두 객체의 관계 중 하나를 연관관계의 주인으로 지정하는데 FK를 가지고 있는 쪽을 주인으로 지정합니다.(Member가 주인)
- 즉, 연관관계의 주인만이 외래키를 관리(등록,수정)합니다.
- 주인이 아닌쪽은 mappedBy로 주인을 지정해줍니다.
- @OneToMany(mappedBy="team") -> 나는 team에 의해서 관리가 됩니다.
- 두 객체의 양방향 관계는 서로 다른 단방향 관계 2개입니다.

## 참고
[https://jyami.tistory.com/20](https://jyami.tistory.com/20)

[https://friends-aihaja.tistory.com/entry/5-%EC%96%91%EB%B0%A9%ED%96%A5-%EC%97%B0%EA%B4%80%EA%B4%80%EA%B3%84%EC%99%80-%EC%97%B0%EA%B4%80%EA%B4%80%EA%B3%84-%EC%A3%BC%EC%9D%B8](https://friends-aihaja.tistory.com/entry/5-%EC%96%91%EB%B0%A9%ED%96%A5-%EC%97%B0%EA%B4%80%EA%B4%80%EA%B3%84%EC%99%80-%EC%97%B0%EA%B4%80%EA%B4%80%EA%B3%84-%EC%A3%BC%EC%9D%B8)