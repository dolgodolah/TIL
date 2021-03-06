# ORM (Object Relational Mapping)

ORM, 객체 관계 매핑에 대해 공부하면서 정리한 글입니다.

## 영속성

데이터를 생성한 프로그램이 종료되더라도 `사라지지 않는 데이터의 특성`을 말합니다.

영속성이 없는 데이터는 단지 메모리에만 존재하므로 프로그램 종료 시 없어집니다.

메모리 상의 데이터를 관계형 데이터베이스 등에 영구적으로 저장해 영속성을 부여할 수 있습니다.

이러한 영속성을 부여해주는 Persistence Framework에 SQL Mapper(Mybatis)와 ORM(Hibernate, JPA)가 있습니다.

## ORM이란?

객체와 관계형 데이터베이스 간의 데이터에 대해 객체를 바탕으로 자동 매핑시켜주는 기술을 말합니다.

객체 지향은 클래스를 사용하고, 관계형 데이터베이스에서는 테이블을 사용하기 때문에 데이터 불일치가 존재할 수 있습니다.

하지만 ORM을 통해 객체 간의 관계를 바탕으로 SQL을 자동으로 생성하여 불일치를 해결할 수 있습니다.


### 장점

객체 지향적인 코드로 인해 더 직관적이고 `비지니스 로직에 더 집중`할 수 있습니다.

ORM은 독립적으로 작성되어 있고, 해당 객체들을 재활용할 수 있습니다.

### 단점

완전히 ORM 으로만 서비스를 구현하기가 어렵습니다.

잘못 구현된 경우 속도 저하 및 심각할 경우 일관성이 무너질 수 있습니다.


## [연관관계](https://github.com/dolgodolah/TIL/blob/master/spring/JPA%20%EC%97%B0%EA%B4%80%EA%B4%80%EA%B3%84%20%EB%A7%A4%ED%95%91.md)







## License
[https://gmlwjd9405.github.io/2019/02/01/orm.html](https://gmlwjd9405.github.io/2019/02/01/orm.html)