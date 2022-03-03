# 0. Overview

지역 변수로 매번 `DateFormat dateFormat = new SimpleDateFormat("yyyyMMdd")`을 생성하길래 `static`으로 수정했다. 

```java
private static final DateFormat YYYYMMDD = new SimpleDateFormat("yyyyMMdd");
```

그 결과 `SimpleDateFormat.parse()`에서  `NumberFormatException` 런타임 에러가 발생했다.

이유는 `SimpleDateFormat`은 threadsafe 하지 않기 때문인데, 지역 변수로 매번 생성한 이유가 있었던 것이다.

그럼 `new SimpleDateFormat`으로 매번 인스턴스를 생성하는 방법밖에 없을까?

# 1. SimpleDateFormat

`SimpleDateFormat`은 threadsafe 하지 않아 전역 변수로 사용할 수는 없다.

하지만 Date를 String으로, String을 Date로 바꾸기 간편하기 때문에 많이 사용하고 있다.

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

# 2. FastDateFormat

`SimpleDateFormat`의 threadsafe 하지 않다는 단점을 보완하기 위해 `apache.commons`에서 `FastDateFormat`이 등장했다.

```
dependencies {
	implementation group: 'org.apache.commons', name: 'commons-lang3', version: '3.12.0'
}
```

```java
Date today = new Date();
FastDateFormat format1 = FastDateFormat.getInstance("yyyyMMdd");
FastDateFormat format2 = FastDateFormat.getInstance("yyyy-MM-dd");
FastDateFormat format3 = FastDateFormat.getInstance("yyyy년 MM월 dd일");
FastDateFormat format4 = FastDateFormat.getInstance("HH:mm:ss");
FastDateFormat format5 = FastDateFormat.getInstance("hh:mm:ss a");

System.out.println(format1.format(today));
System.out.println(format2.format(today));
System.out.println(format3.format(today));
System.out.println(format4.format(today));
System.out.println(format5.format(today));
System.out.println(format1.parse("20220302"));
```

# Reference

[https://stackoverflow.com/questions/21017502/numberformatexception-while-parsing-date-with-simpledateformat-parse/21021768](https://stackoverflow.com/questions/21017502/numberformatexception-while-parsing-date-with-simpledateformat-parse/21021768)