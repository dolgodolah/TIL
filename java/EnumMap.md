# 1. EnumMap이란?

EnumMap은 Map 인터페이스에서 키를 특정 enum 타입만을 사용하도록 하는 구현체이다.

HashMap처럼 해시를 만들고 해시 충돌에 대응하는 작업이 필요없기 때문에 성능적으로 유리하다.

# 2. EnumMap 사용법

### enum 구현

```java
public enum Day {
    MON, TUE, WED, THU, FRI, SAT, SUN;
} 
```

### EnumMap 생성

enum 타입을 인자로 넘겨 생성할 수 있다.

```java
Map<Day, String> plan = new EnumMap<>(Day.class);

plan.put(Day.MON, "TV보기");
plan.put(Day.TUE, "공부하기");

System.out.println(plan.toString()); // {MON=TV보기, TUE=공부하기}
```

<br>

혹은 같은 enum 타입을 key로 사용하던 HashMap을 인자로 넘겨 생성할 수도 있다.

```java
Map<Day, String> map = new HashMap<>();
map.put(Day.MON, "공부하기"); // Map이 비어있으면 Specified map is empty 예외 발생

Map<Day, String> plan = new EnumMap<>(map);
plan.put(Day.MON, "영화보기");

System.out.println(plan.toString()); // {MON=공부하기, TUE=영화보기}
```

# 3. 결론

HashMap의 경우 일정량 이상의 자료가 저장되면 자체적으로 resize를 하지만

EnumMap은 시작부터 데이터의 사이즈가 enum으로 제한되기 때문에 해당 작업이 필요없다.

**즉, HashMap보다 성능상 이점이 있기 때문에 Enum 타입의 키를 사용할 때는 EnumMap을 사용하자.**

# Reference

[https://www.baeldung.com/java-enum-map](https://www.baeldung.com/java-enum-map)
