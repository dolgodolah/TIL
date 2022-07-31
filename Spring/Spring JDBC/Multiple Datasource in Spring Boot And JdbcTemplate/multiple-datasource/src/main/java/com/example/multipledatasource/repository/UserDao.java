package com.example.multipledatasource.repository;

import com.example.multipledatasource.model.User;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;
import java.util.Optional;

@Repository
public class UserDao {

    private JdbcTemplate main;
    private JdbcTemplate sub;

    public UserDao(@Qualifier("mainJdbcTemplate") JdbcTemplate main,
                   @Qualifier("subJdbcTemplate") JdbcTemplate sub) {
        this.main = main;
        this.sub = sub;
    }

    public List<User> findAllUser() {
        List<User> result = main.query("select * from user", userRowMapper());
        result.addAll(sub.query("select * from user", userRowMapper()));

        return result;
    }

    private RowMapper<User> userRowMapper() {
        return new RowMapper<User>() {
            @Override
            public User mapRow(ResultSet rs, int rowNum) throws SQLException {
                User user = new User();
                user.setId(rs.getInt("id"));
                user.setNickname(rs.getString("nickname"));

                return user;
            }
        };
    }
}
