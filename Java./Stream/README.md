# java-8-streams

[테스트 코드](https://github.com/dolgodolah/TIL/blob/master/java/stream/src/test/java/com/example/stream/stream/StreamApplicationTests.java)로 Stream API 익히기

## Stream의 장점

- 기존 for문이 how 방식의 외부반복이었다면, stream을 통해 what 중심의 내부반복으로 작성하기 때문에 코드가 직관적이다.
    
```java
// 자바8(Stream) 이전
// 연봉을 어떻게 구해야하는지 하나하나 구현해야 했다.
// 때문에 sum, count와 같이 연봉과 관련없는 변수들이 사용된다.
int sum = 0;
int count = 0;
for (Employee emp : emps) {
        if (emp.getSalary() > 100000000) {
                sum += emp.getSalary();
                count++;
        }
}
double average = (double) sum / count;
```

```java
// 자바8(Stream) 이후
// 연산에 필요한 매개변수를 사용하지 않는다.
// Employee 객체에 무엇을 할 지 구현하기만 하면 된다.
double average = emps.stream()
        .filter(emp -> emp.getSalary() > 100000000)
        .mapToInt(Employee::getSalary)
        .average()
        .orElse(0);
```
    
- 변경 가능한 데이터들로 인해 생길 수 있던 부작용들을 방지할 수 있다.
    - 원본데이터로 연산을 수행하지 않기 때문에 원본데이터로 crud를 하지 않는 이상 원본데이터는 유지된다.
    - 예를 들어 `list.stream().sorted().collect(Collectors.toList())`를 통해 정렬해도 list의 순서는 유지된다.

- 스트림은 lazy 처리(결과가 필요하기 전에는 실행되지 않음)되기 때문에 성능상 이점을 볼 수 있다.
    - 여러 단어 중 가장 긴 단어 3개를 요청하면 filter 메소드는 3번째 값을 구한 후 필터링을 중단하고 결과를 반환한다.

# Reference

[https://www.baeldung.com/java-8-streams-introduction](https://www.baeldung.com/java-8-streams-introduction)

[https://www.baeldung.com/java-8-streams](https://www.baeldung.com/java-8-streams)