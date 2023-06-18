# 1. JVM vs JDK vs JRE
## JVM (Java Virtual Machine)
- 자바 바이트 코드(.class 파일)를 실행시키는 표준 방법이다.
- 인터프리터, JIT(Just In Time) 컴파일러를 통해 자바 바이트 코드를 OS에 특화된 코드로 변환하여 실행한다.
- HelloJava.java > (컴파일) > HelloJava.class > (인터프리터, JIT) > OS에 특화된 머신 코드
```
$ javap -c HelloJava
Compiled from "HelloJava.java"
public class HelloJava {
  public HelloJava();
    Code:
       0: aload_0
       1: invokespecial #1                  // Method java/lang/Object."<init>":()V
       4: return

  public static void main(java.lang.String[]);
    Code:
       0: getstatic     #2                  // Field java/lang/System.out:Ljava/io/PrintStream;
       3: ldc           #3                  // String Hello Java
       5: invokevirtual #4                  // Method java/io/PrintStream.println:(Ljava/lang/String;)V
       8: return
}
```
- JVM 스펙(https://docs.oracle.com/javase/specs/jvms/se11/html/) 에 맞춰 오라클, 아마존, Azul, ... 등에서 구현하여 구현체는 다양하다.
- JVM은 홀로 제공되지 않고, 최소 제공 단위는 JRE이다.

## JRE (Java Runtime Enviroment)
- 자바 애플리케이션을 실행할 수 있도록 구성된 배포판이다.
- JVM + 핵심 라이브러리
- 개발 관련 도구는 포함되지 않는다.

## JDK (Java Development Kit)
- JRE + 개발에 필요한 툴
- 오라클은 자바 11부터 JRE를 따로 제공하지 않고, JDK만 제공한다.

<br>

# 2. JVM 구조
![jvm-3](https://github.com/dolgodolah/TIL/assets/75430912/41ddcb51-97ca-4030-a2ad-ad507dcdca31)

## 클래스 로더
- 아래 세 과정을 통해 `.class` 파일에서 바이트 코드를 읽고 메모리에 저장한다.
- `로딩` : 클래스 읽어오는 과정
- `링크` : 레퍼런스 연결하는 과정
- `초기화` : static 값들 초기화 및 변수 할당
## 메모리
- `메소드 영역`에는 클래스 수준의 정보 (클래스 이름, 부모 클래스 이름, 메소드, 변수)를 저장하고, 공유 자원이다.
- `힙 영역`에는 객체를 저장하고, 공유 자원이다.
- `스택 영역`에는 런타임 스택을 만들고, 메소드 호출을 스택 프레임이라 부르는 블럭으로 쌓는다. 쓰레드마다 영역을 가지고 쓰레드 종료 시 런다임 스택도 사라진다.
- `PC(Program Counter) 레지스터`에는 쓰레드마다 현재 실행할 스택 프레임을 가리키는 포인터가 생성된다.
- `네이티브 메소드 스택`은 네이티브 메소드 호출할 때 사용하는 별도의 메소드 스택이다.
## 실행 엔진
- `인터프리터`로 바이트 코드를 한줄 씩 실행한다.
- `JIT 컴파일러`는 인터프리터의 효율을 높이기 위해 반복되는 코드를 모두 네이티브 코드로 바꿔둔다.
- `GC(Garbage Collector)`는 더 이상 참조되지 않는 객체를 모아서 정리한다.
## JNI(Java Native Interface)
- 자바 애플리케이션에서 C, C++, 어셈블리로 작성된 함수를 사용할 수 있는 인터페이스를 제공한다.
- Native 키워드를 사용해 메소드를 호출한다. (ex. `Thread.currentThread()`)
## 네이티브 메소드 라이브러리(Java Method Libraries)
- C, C++, 어셈블리로 작성된 라이브러리다.
