package com.example.springjdbc;

import com.example.springjdbc.dao.JdbcMemberDao;
import com.example.springjdbc.dao.MemberDao;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import javax.sql.DataSource;

@Configuration
public class SpringConfig {

    private DataSource dataSource;

    public SpringConfig(DataSource dataSource) {
        this.dataSource = dataSource;
    }

    @Bean
    public MemberDao memberDao() {
        return new JdbcMemberDao(dataSource);
    }
}
