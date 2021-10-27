package com.example.springjdbc;

import com.example.springjdbc.dao.JdbcMemberDao;
import com.example.springjdbc.dao.JpaPostDao;
import com.example.springjdbc.dao.MemberDao;
import com.example.springjdbc.dao.PostDao;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import javax.persistence.EntityManager;
import javax.sql.DataSource;

@Configuration
public class SpringConfig {

    private DataSource dataSource;
    private EntityManager em;

    public SpringConfig(DataSource dataSource, EntityManager em) {
        this.dataSource = dataSource;
        this.em = em;
    }

    @Bean
    public MemberDao memberDao() {
        return new JdbcMemberDao(dataSource);
        // DB 접근 방법을 JDBC -> JPA로 변경하여 JpaMemberDao를 구현하고 이처럼 갈아 끼우면
        // 기존 MemberDao(JdbcMemberDao)는 단 하나의 수정도 없이 갈아 끼울수 있다.
        // return new JpaMemberDao(em);
    }

    @Bean
    public PostDao postDao() {
        return new JpaPostDao(em);
    }
}
