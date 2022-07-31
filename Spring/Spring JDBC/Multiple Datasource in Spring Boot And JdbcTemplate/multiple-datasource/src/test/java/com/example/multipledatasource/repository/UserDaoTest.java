package com.example.multipledatasource.repository;

import com.example.multipledatasource.model.User;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import static org.assertj.core.api.Assertions.assertThat;


@SpringBootTest
@Transactional
class UserDaoTest {

    @Autowired
    private UserDao userDao;

    @Test
    void 전체회원조회() {
        /**
         * create table db1.user (
         *   `id` int(11) NOT NULL auto_increment,
         *   `nickname` varchar(100) NOT NULL default '',
         *   PRIMARY KEY (`id`)
         * ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
         *
         * create table db2.user (
         *   `id` int(11) NOT NULL auto_increment,
         *   `nickname` varchar(100) NOT NULL default '',
         *   PRIMARY KEY (`id`)
         * ) ENGINE=InnoDB AUTO_INCREMENT=10000 DEFAULT CHARSET=utf8;
         *
         *
         * insert db1.user (nickname) values ("nickname1");
         * insert db2.user (nickname) values ("nickname10000");
         */

        List<User> result = userDao.findAllUser();
        
        assertThat(result.size()).isEqualTo(2);
        assertThat(result.stream().anyMatch(e -> "nickname1".equals(e.getNickname())));
        assertThat(result.stream().anyMatch(e -> "nickname10000".equals(e.getNickname())));
    }
}