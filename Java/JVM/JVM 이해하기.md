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


# 2. JVM 구조
