# JVM(Java Virtual Machine)과 GC(Garbage Collection)

JVM과 GC에 대해 공부하면서 배운 내용을 정리한 글입니다.

## JVM이란?

JVM(Java Virtual Machine)은 Java가 `OS에 구애받지 않고 재사용`을 가능하게 해주며 `메모리 관리`, `Garbage Collector`을 수행하는 자바 가상 머신입니다.

한정된 메모리를 효율적으로 사용하여 최고의 성능을 내기 위해 JVM에 대해 공부하여야 합니다.

JVM의 구조는 크게 `Class Loader`, `Execution Engine`, `Garbage Collector`, `Runtime Data Area`로 나뉩니다.

가장 일반적인 상호작용은 힙과 스택의 메모리 사용을 확인하는 것입니다.

이 글에서 다룰 Garbage Collector는 밑에서 자세히 다루도록 하고 나머지 구조에 대해 간단히 알아보겠습니다.

## Class Loader

a.java 파일이 생성되면 자바컴파일러(javac)가 컴파일하여 a.class같은 클래스 파일(바이트코드)로 변환해줍니다.

이러한 class파일들을 모아서 JVM이 OS로부터 할당받은 메모리 영역(Runtime Data Area)에 적재하는 역할을 합니다.

## Execution Engine

Execution Engine은 Class Loader에 의해 적재된 클래스들을 기계어로 번역해 명령어 단위로 실행하는 역할을 합니다. 

## Runtime Data Area

JVM의 메모리 영역으로 자바 애플리케이션 실행 시 사용되는 데이터들을 적재하는 공간입니다.

Runtime Data Area는 Method Area, Heap Area, Stack Area, PC register, Native Method Area로 구분됩니다.




## GC(Garbage Collection)
자바 이전에는 개발자가 모든 프로그램 메모리를 관리했지만 자바에서는 JVM이 프로그램 메모리를 관리해줍니다.

JVM의 가비지 컬렉터를 통해 동적으로 할당한 메모리 영역 중 사용하지 않은 영역을 탐지하여 해제합니다. 

### 메모리 영역

GC의 과정을 알아보기 전에 메모리 영역에 대해 간단히 알아보겠습니다.

***Stack*** : 정적으로 할당한 메모리 영역
원시타입의 데이터가 값과 함께 할당, Heap 영역에 생성된 Object 타입의 데이터 참조 값 할당

***Heap*** : 동적으로 할당한 메모리 영역
모든 Object 타입의 데이터가 할당


```java
public class Main {
    public static void(String[] args){
        int num1 = 10;
        int num2 = 5;
        String name = "홍길동";
    }
}
```

위 프로그램의 메인 메서드가 실행되면 스택에 num1, num2, name이 밑에서부터 차례대로 쌓이게 됩니다.

여기서 중요한 점은 name은 String 객체를 생성므로 힙에 String 객체("홍길동")를 할당하고 스택의 name에는 이 객체를 참조하는 값이 담기게 됩니다.

이 메서드가 끝나게 되면 스택에 있는 데이터들이 모두 pop되어 날아가고 힙영역의 객체 타입의 데이터(Unreachable Object)만 남게 됩니다.

즉, 이 객체 데이터들이 GC의 대상이 됩니다.


### GC 과정

1. Garbage Collector가 Stack의 모든 변수를 스캔하며 어떤 객체를 참조하고 있는지 찾아(Reachable Object) 마킹합니다. (Mark)

2. Reachable Object가 참조하고 있는 객체도 찾아서 마킹합니다. (Mark)

3. 최종적으로 마킹되지 않은 객체를 Heap에서 제거합니다. (Sweep)

### GC 종류

Heap 영역에는 `New Generation`과 `Old Generation`으로 나뉩니다.

1. New Generation에서 일어나는 GC가 Minor GC,

2. Old Generation에서 일어나는 GC가 Major GC가 됩니다.

***Minor GC***

New Generation은 Eden + Survival 0 + Survival 1으로 구성돼있습니다.

새로 생성된 객체는 Eden 영역에 생성되고 이 Eden 영역이 가득 찰 경우 GC가 발생(Mark and Sweep)됩니다.

여기서 살아남은 Reachable 객체는 Survival 0으로 옮겨집니다.

위 과정이 반복되어 Survival 0가 가득찰 경우 GC가 발생됩니다.

Survival 0에서 살아남은 Reachable 객체는 Survival 1으로 옮겨집니다.

Survival에서의 GC가 발생할 때는 Reachable 객체에 대해 Age 값을 증가시킵니다. 

현재 상태를 정리해보면 Survival 0에 객체가 가득 차 GC가 발생하여 살아남은 Reachable 객체를 aging하면서 Survival 1으로 옮긴 상태입니다.

또 Eden 영역이 가득 차 GC가 발생하면 Reachable 객체를 Survival 1으로 옮기게 됩니다. (Survival 0와 Survival 1 중 객체가 이미 있는 곳으로)

위 과정을 계속해서 반복하게 되면(Survival 0과 Survival 1 사이의 이동) age 값이 증가하여

특정 age 값을 넘어가게 되면 Old Generation 영역으로 Promotion하게 됩니다.



즉, `Survival 0와 Survival 1 중 하나는 항상 비어있는 상태가 유지`되어야 합니다.

***Major GC***

Minor GC로 인해 Old Generation 영역도 가득 차게 되면 GC가 발생하는데 이를 Major GC라고 합니다.



## 출처
[https://velog.io/@hono2030/JVM%EC%9D%98-%EA%B5%AC%EC%A1%B0](https://velog.io/@hono2030/JVM%EC%9D%98-%EA%B5%AC%EC%A1%B0)

[https://www.itworld.co.kr/news/110837](https://www.itworld.co.kr/news/110837)

[https://asfirstalways.tistory.com/158](https://asfirstalways.tistory.com/158)

[https://www.youtube.com/watch?v=vZRmCbl871I](https://www.youtube.com/watch?v=vZRmCbl871I)