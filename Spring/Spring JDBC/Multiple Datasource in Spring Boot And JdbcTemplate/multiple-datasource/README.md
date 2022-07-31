# 사용 기술
- Spring Boot
- JdbcTemplate

# 테스트 방법

- db1, db2에 user 테이블 생성
```mysql
create table db1.user (
    `id` int(11) NOT NULL auto_increment,
    `nickname` varchar(100) NOT NULL default '',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

create table db2.user (
    `id` int(11) NOT NULL auto_increment,
    `nickname` varchar(100) NOT NULL default '',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10000 DEFAULT CHARSET=utf8;
```

- db1, db2에 데이터 추가
```mysql
insert db1.user (nickname) values ("nickname1");
insert db2.user (nickname) values ("nickname10000");
```

- 테스트 코드 검증 [Test Code]()

# Reference

[https://www.jackrutorial.com/2018/08/multiple-datasource-in-spring-boot.html](https://www.jackrutorial.com/2018/08/multiple-datasource-in-spring-boot.html)