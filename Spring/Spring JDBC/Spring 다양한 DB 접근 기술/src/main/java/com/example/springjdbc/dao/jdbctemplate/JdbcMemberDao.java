package com.example.springjdbc.dao.jdbctemplate;

import com.example.springjdbc.dao.MemberDao;
import com.example.springjdbc.entity.Member;
import com.example.springjdbc.entity.MemberType;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.jdbc.core.namedparam.MapSqlParameterSource;
import org.springframework.jdbc.core.simple.SimpleJdbcInsert;

import javax.sql.DataSource;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;

public class JdbcMemberDao implements MemberDao {

    private final JdbcTemplate jdbcTemplate;
    private final SimpleJdbcInsert jdbcInsert;

    public JdbcMemberDao(DataSource dataSource) {
        this.jdbcTemplate = new JdbcTemplate(dataSource);
        this.jdbcInsert = new SimpleJdbcInsert(dataSource)
                .withTableName("member")
                .usingGeneratedKeyColumns("id");
    }

    @Override
    public Member save(Member member) {
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("name", member.getName());
        parameters.put("age", member.getAge());
        parameters.put("member_type", member.getMemberType());

        Number key = jdbcInsert.executeAndReturnKey(new MapSqlParameterSource(parameters));
        member.setId(key.longValue());
        return member;
    }

    @Override
    public Optional<Member> findById(Long id) {
        List<Member> result = jdbcTemplate.query("select * from member where id = ?", memberRowMapper(), id);
        return result.stream().findAny();
    }

    @Override
    public Optional<Member> findByName(String name) {
        List<Member> result = jdbcTemplate.query("select * from member where name = ?", memberRowMapper(), name);
        return result.stream().findAny();
    }

    @Override
    public List<Member> findAll() {
        return jdbcTemplate.query("select * from member", memberRowMapper());
    }

    @Override
    public int getAllMemberCount() {
        return jdbcTemplate.queryForObject("select count(*) from member", Integer.class);
    }

    @Override
    public void deleteById(Long id) {
        jdbcTemplate.update("delete from member where id = ?", id);
    }

    private RowMapper<Member> memberRowMapper() {
        return new RowMapper<Member>() {
            @Override
            public Member mapRow(ResultSet rs, int rowNum) throws SQLException {
                Member member = new Member();
                member.setId(rs.getLong("id"));
                member.setName(rs.getString("name"));
                member.setAge(rs.getInt("age"));
                member.setMemberType(MemberType.valueOf(rs.getString("member_type")));
                /*
                Enum을 String으로 저장했을 땐 valueOf()로 캐스팅
                Enum을 int로 저장했을 땐 values()에서 index를 통해 캐스팅해야 됨
                member.setMemberType(MemberType.values()[rs.getInt("member_type") - 1]);
                 */

                return member;
            }
        };
    }
}
