# 0. 개요

지역 변수로 매번 `DateFormat dateFormat = new SimpleDateFormat("yyyyMMdd")`을 생성하길래 `static`으로 수정했다. 

```java
private static final DateFormat YYYYMMDD = new SimpleDateFormat("yyyyMMdd");
```

그 결과 `SimpleDateFormat.parse()`에서  `NumberFormatException` 런타임 에러가 발생했다.

이유는 `SimpleDateFormat`은 threadsafe 하지 않기 때문인데, 지역 변수로 매번 생성한 이유가 있었던 것이다.

그럼 `SimpleDateFormat`으로 매번 객체를 생성하는 방법밖에 없을까?

# 1. SimpleDateFormat
<!-- TODO -->

# 2. FastDateFormat
<!-- TODO -->


# 참조

[https://stackoverflow.com/questions/21017502/numberformatexception-while-parsing-date-with-simpledateformat-parse/21021768](https://stackoverflow.com/questions/21017502/numberformatexception-while-parsing-date-with-simpledateformat-parse/21021768)