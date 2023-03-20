# 0. Overview

지역 변수로 매번 `DateFormat dateFormat = new SimpleDateFormat("yyyyMMdd")`을 생성하길래 `static`으로 수정했다. 

```java
private static final DateFormat YYYYMMDD = new SimpleDateFormat("yyyyMMdd");
```

그 결과 `SimpleDateFormat.parse()`에서  `NumberFormatException` 런타임 에러가 발생했다.

이유는 `SimpleDateFormat`은 threadsafe 하지 않기 때문인데, 지역 변수로 매번 생성한 이유가 있었던 것이다.

그럼 `new SimpleDateFormat`으로 매번 객체를 생성하는 방법 밖에 없을까?

# 1. SimpleDateFormat

자바 내장 라이브러리에서 `Date` <-> `String` 변환을 간편하게 할 수 있는 클래스이기 때문에 많이 사용하고 있다.

## 1.1 사용법

```java
Date today = new Date();
DateFormat format1 = new SimpleDateFormat("yyyyMMdd");
DateFormat format2 = new SimpleDateFormat("yyyy-MM-dd");
DateFormat format3 = new SimpleDateFormat("yyyy년 MM월 dd일");
DateFormat format4 = new SimpleDateFormat("HH:mm:ss");
DateFormat format5 = new SimpleDateFormat("hh:mm:ss a");

System.out.println(format1.format(today)); // 20220302
System.out.println(format2.format(today)); // 2022-03-02
System.out.println(format3.format(today)); // 2022년 03월 02일
System.out.println(format4.format(today)); // 19:31:31
System.out.println(format5.format(today)); // 07:31:31 오후

System.out.println(format1.parse("20220302")); // Wed Mar 02 00:00:00 KST 2022
System.out.println(format1.parse("20220302").getClass()); // class java.util.Date
```

## 1.2 문제점

- ### thread safe 하지 않다.

SimpleDateFormat은 thread safe 하지 않기 때문에 multi-thread 환경에서 static으로 선언해서는 안된다.

```java
class DateFormatTest {
    private static final SimpleDateFormat SIMPLE_DATE_FORMAT = new SimpleDateFormat("yyyyMMdd");

    @Test
    void 멀티스레드환경에서_SimpleDateFormat() {
        assertThrows(NumberFormatException.class, this::task);
    }

    private boolean task() {
        String dateStr = "20220101";

        IntStream.range(0, 1000).parallel().forEach(e -> {
            try {
                SIMPLE_DATE_FORMAT.parse(dateStr);
            } catch (ParseException parseException) {
            }
        });

        return true;
    }
}
```

따라서 비즈니스 로직 안에서 매번 인스턴스로 생성하여 사용해야 한다.

- ### lenient 하다.

실제로 없는 날짜 (20221504)를 입력했을 때 Exception을 던지지 않고, 다음 날짜 (20230304)로 자동 보정되게 된다.

이는 원하지 않은 날짜로 데이터가 설정되어 저장될 수 있기 때문에 문제가 될 수 있다.

`format.setLenient(false)`를 통해 잘못된 날짜를 입력했을 때 Exception을 던지도록 할 수는 있다.


# 2. FastDateFormat

`SimpleDateFormat`의 threadsafe 하지 않다는 단점을 보완하기 위해 `apache.commons`의 `FastDateFormat`이 등장했다.

## 2.1 사용법

```
dependencies {
	implementation group: 'org.apache.commons', name: 'commons-lang3', version: '3.12.0'
}
```

```java
@Test
public void Date_To_String() {
    Date date = new Date();

    String simpleDateFormat = SIMPLE_DATE_FORMAT.format(date);
    String fastDateFormat = FAST_DATE_FORMAT.format(date);

    assertEquals(simpleDateFormat, fastDateFormat);
}

@Test
public void String_To_Date() throws ParseException {
    String dateStr = "20220101";

    Date simpleDateFormat = SIMPLE_DATE_FORMAT.parse(dateStr);
    Date fastDateFormat = FAST_DATE_FORMAT.parse(dateStr);

    assertEquals(simpleDateFormat, fastDateFormat);
}
```

## 2.2 static 예제

```java
public class Person {

    private static final FastDateFormat YYYYMMDD = FastDateFormat.getInstance("yyyyMMdd");

    private String name;
    private String birthday;

    public Person(String name, String birthday) {
        this.name = name;
        this.birthday = birthday;
    }

    public boolean isSameBirthday(Date other) throws ParseException {
        return getBirthday().equals(other);
    }

    private Date getBirthday() throws ParseException {
        return YYYYMMDD.parse(birthday);
    }
}
```

## 2.3 장점

- ### thread safe 하다.

`FastDateFormat`은 thread safe 하기 때문에 전역변수로 선언해도 괜찮다.

```java
public class DateFormatTest {

    private static final FastDateFormat YYYYMMDD = FastDateFormat.getInstance("yyyyMMdd");

    @Test
    void 멀티스레드환경에서_FastDateFormat() {
        assertEquals(true, task());
    }

    private boolean task() {
        String dateStr = "20220101";

        IntStream.range(0, 1000).parallel().forEach(e -> {
            try {
                SIMPLE_DATE_FORMAT.parse(dateStr);
            } catch (ParseException parseException) {
            }
        });

        return true;
    }
```

- ### SimpleDateFormat과 사용법이 유사하기 때문에 쓰기 편하다.

`FastDateFormat` 역시 `Date` <-> `String` 변환을 위해 만들어진 클래스이기 때문에 기존에 사용하던 `SimpleDateFormat`과 사용법이 유사하다.

## 2.4 단점

`apache.commons.lang3`라는 외부 라이브러리에 의존해야 한다.

# 3. DateTimeFormatter

자바8에서 지원하는 `DateTimeFormatter`를 통해서도 `Date` <-> `String` 전환을 할 수 있다.

## 3.1 사용법

```java
@Test
public void Date_To_String() {
    Date date = new Date();

    String simpleDateFormat = SIMPLE_DATE_FORMAT.format(date);
    String dateTimeFormatter = DATE_TIME_FORMATTER.withZone(ZoneId.systemDefault()).format(date.toInstant());

    assertEquals(simpleDateFormat, dateTimeFormatter);
}

@Test
public void String_To_Date() throws ParseException {
    String dateStr = "20220101";

    Date simpleDateFormat = SIMPLE_DATE_FORMAT.parse(dateStr);
    LocalDateTime localDateTime = LocalDate.parse(dateStr, DATE_TIME_FORMATTER).atStartOfDay();
    Date dateTimeFormatter = Date.from(localDateTime.atZone(ZoneId.systemDefault()).toInstant());

    assertEquals(simpleDateFormat, dateTimeFormatter);
}
```

## 3.2 장점

- ### thread safe 하다.

`DateTimeFormatter`도 thread safe 하기 때문에 전역변수로 선언해도 괜찮다.

- ### Java8 내장 라이브러리이다.

외부 라이브러리의 의존없이 일반 jdk에서 수행할 수 있다.

## 3.3 단점

애초에 `DateTimeFormatter`는 `Date` <-> `String` 변환이 아닌 `LocalDateTie(LocalDate)` <-> `String` 변환을 위한 클래스라서

`Date` <-> `String` 변환을 위해 사용하기에는 불편한 느김이 있다.

<br>

# 4. 결론

`SimpleDateFormat`은 별도의 라이브러리 설치없이 간편하게 사용 가능하지만 thread safe 하지 않다는 단점 때문에 불필요하게 매번 새로운 객체를 생성해야 한다.

따라서 apache.common.lang의 `FastDateFormat`을 사용하거나,

Java8 에서 지원하는 `DateTimeFormatter`을 사용하도록 리팩토링하는 것이 좋다.



# Reference

- [SimpleDateFormat thread-unsafe](https://stackoverflow.com/questions/21017502/numberformatexception-while-parsing-date-with-simpledateformat-parse/21021768)

- [SimpleDateFormat setLenient](https://stackoverflow.com/questions/1905551/make-simpledateformat-parse-fail-on-invalid-dates-e-g-month-is-greater-than)

- [Java SimpleDateFormat 을 쓰지 말아야 할 이유](https://techlog.myoa-universe.com/archives/786)

- `withResolverStyle(ResolverStyle.STRICT)` 설정한 이유 
  -  존재하지 않는 날짜가 자동 보정되지 않도록 함 - [링크](https://howtodoinjava.com/java/date-time/resolverstyle-strict-date-parsing/)

- yyyy 대신 uuuu를 사용한 이유
  - `withResolverStyle(ResolverStyle.STRICT)` 설정하고 yyyy 사용하면 에러 발생함 (기원전 이슈) - [링크](https://stackoverflow.com/questions/26393594/using-new-java-8-datetimeformatter-to-do-strict-date-parsing)
  - 애초에 uuuu 사용을 권장한다고 함 (SimpleDateFormat은 하위호환때문에 쩔수 없이 못바꿨다는 얘기가 있네요) - [링크](https://stackoverflow.com/questions/41177442/uuuu-versus-yyyy-in-datetimeformatter-formatting-pattern-codes-in-java/41178418)
