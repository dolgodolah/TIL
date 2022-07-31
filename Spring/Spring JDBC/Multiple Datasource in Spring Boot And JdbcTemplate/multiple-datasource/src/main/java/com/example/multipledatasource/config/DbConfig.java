package com.example.multipledatasource.config;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.boot.jdbc.DataSourceBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;
import org.springframework.jdbc.core.JdbcTemplate;

import javax.sql.DataSource;

@Configuration
public class DbConfig {

    @Bean(name = "mainDb")
    @ConfigurationProperties(prefix = "spring.datasource")
    @Primary
    public DataSource mainDataSource() {
        return DataSourceBuilder.create().build();
    }

    @Bean(name = "mainJdbcTemplate")
    public JdbcTemplate mainJdbcTemplate(@Qualifier("mainDb") DataSource dataSource) {
        return new JdbcTemplate(dataSource);
    }

    @Bean(name = "subDb")
    @ConfigurationProperties(prefix = "spring.second-db")
    public DataSource subDataSource() {
        return DataSourceBuilder.create().build();
    }

    @Bean(name = "subJdbcTemplate")
    public JdbcTemplate subJdbcTemplate(@Qualifier("subDb") DataSource dataSource) {
        return new JdbcTemplate(dataSource);
    }
}
