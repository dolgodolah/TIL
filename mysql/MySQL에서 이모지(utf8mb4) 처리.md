# MySQL에서 Emoji(이모지) 데이터 처리하기



## 이슈

insert 시 문자에 이모지가 있으면 에러가 발생했습니다. MySQL 의 UTF-8 은 3 byte 로 표현되는 범위내의 캐릭터만 입력할 수 있지만 이모지처럼 4 byte 로 표현되는 문자가 들어와서 발생한 현상입니다.

따라서 가변 4bytes의 문자열을 저장할 수 있는 utf8mb4를 사용하면 이모지를 저장할 수 있습니다.


## 해결방법

- utf8mb4 로 database 생성

```mysql
CREATE DATABASE myplaylists CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
```



- utf8 database 를 utf8mb4 로 변경
```mysql
ALTER DATABASE myplaylists CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

```
## License
[https://www.lesstif.com/java/java-+-mysql-+-utf8mb4-emoji-51283094.html](https://www.lesstif.com/java/java-+-mysql-+-utf8mb4-emoji-51283094.html)

[https://artiiicy.tistory.com/31](https://artiiicy.tistory.com/31) AWS RDS에서 변경법