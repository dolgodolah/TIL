# SOLID 원칙

SOLID 원칙은 로버트 마틴의 좋은 객체 지향 설계 5가지 원칙 `SRP`, `OCP`, `LSP`, `ISP`, `DIP`을 말합니다.

서비스의 새로운 기능이 확장되거나 요구사항 변경이 있을 때 기존 코드의 변경이 많으면 좋은 설계가 아닙니다.

SOLID 원칙을 100% 실현하기에는 어렵지만 이 설계원칙을 인지하고 고려하면서 개발을 하면

기존 코드의 최소한의 변경만으로 새로운 요구사항이나 요구사항의 변경을 적용할 수 있습니다.

## 1. SRP(Single Responsibility Principle), 단일 책임 원칙

객체는 단 하나의 책임만 가질 수 있다는 원칙입니다. 이는 객체뿐 아니라 메소드에도 해당되는 원칙입니다.

객체가 하나의 책임을 가지게 되면 객체 간의 응집도는 높고 결합도가 낮아지게 됩니다.

```java
class Calculator {
  public add() {...};
  public subtraction() {...};
  public multiply() {...};
  public division() {...};
}
```

현재 Calculator 클래스는 사칙연산에 대한 책임만 가지고 있습니다. 단일 책임 원칙이 지켜진 코드입니다.

여기서 계산기에 알람 기능을 추가하기 위해서 Calculator에 alarm() 메소드를 추가하면

```java
class Calculator {
  public add() {...};
  public subtraction() {...};
  public multiply() {...};
  public division() {...};
  public alarm() {...};
}
```

이는 단일 책임 원칙이 지켜지지 않아 좋은 코드라고 보기 어렵습니다.
```java
class Calculator {
  public add() {...};
  public subtraction() {...};
  public multiply() {...};
  public division() {...};
}

class Alarm {
  public ring() {...};
  public setTime()() {...};
}
```

Calculator 클래스와 Alarm 클래스로 나눠 각각의 역할과 책임을 가지도록 하여 다시 단일 책임 원칙이 지켜지도록 수정했습니다.

객체마다 하나의 책임만 갖도록 잘 분배하면, 변화가 생기더라도 그 영향을 최소화 할 수 있습니다.

## 2. OCP(Open Closed Principle), 개방 폐쇄 원칙

소프트웨어는 확장에 대해서는 열려 있어야 하지만(Open), 변경에 대해서는 닫혀 있어야 한다(Closed)는 원칙입니다.

즉, 기존 코드를 변경하지 않고 확장을 할 수 있어야 한다는 의미입니다.

```java
public interface Animal {
  public void crying();
}

public class Dog implements Animal {
  @Override
  public void crying() {
    System.out.println("왈왈");
  }
}

public class Cat implements Animal {
  @Override
  public void crying() {
    System.out.println("야옹");
  }
}
```

Animal 인터페이스에 crying()을 정의해놓고 구현 클래스에서 crying()을 재정의하도록 하면

새로운 동물이 추가되어도 각 crying() 메소드들은 건드릴 필요없이 새로운 동물에 대한 crying()만 재정의하여 쉽게 확장할 수 있습니다.

## 3. LSP(Liskov Substitution Principle), 리스코프 치환 원칙

자식 클래스는 자신의 부모 클래스에서 하는 행위는 수행할 수 있어야 한다는 원칙입니다.

즉, 자식 클래스는 부모 클래스의 역할을 대체할 수 있어야 합니다.

```java
public interface Animal {
  public void crying();
}

public class Dog implements Animal {
  @Override
  public void crying() {
    System.out.println("왈왈");
  }
}

public class Cat implements Animal {
  @Override
  public void crying() {
    System.out.println("야옹");
  }
}
```
Animal 인터페이스에서 정의 해놓은 crying()을 Dog 클래스와 Cat 클래스에서 구현하도록 했습니다.

```java
public class AnimalHouse {
  public static void main(String[] args) {
    Dog doldol = new Dog();
    doldol.crying();
  }
}

public class AnimalHouse {
  public static void main(String[] args) {
    Animal doldol = new Dog();
    doldol.crying();
  }
}

public class AnimalHouse {
  public static void main(String[] args) {
    Animal doldol = new Cat();
    doldol.crying();
  }
}
```
Animal은 Dog의 부모 클래스이기 때문에 Dog doldol = new Dog();를 Animal doldol = new Dog(); 문제가 없습니다.

Cat의 부모 클래스도 Animal이기 때문에 doldol이라는 동물을 고양이로 바꿔도 문제가 발생하지 않습니다.

이는 리스코프 치환 원칙이 잘 지켜진 코드이기 때문입니다. (가장 베스트는 Override를 자제하는게 리스코프 치환 원칙을 가장 잘 지킨거라고 합니다.)

자식 클래스가 부모 클래스의 책임을 무시하거나 위배하는 코드는 리스코프 치환 원칙이 지켜지지 않은 코드입니다.



## 4. ISP(Interface Segregation Principle), 인터페이스 분리 원칙

자신이 사용하지 않는 인터페이스는 구현하지 말아야 한다는 설계 원칙입니다.

즉, 하나의 거대한 인터페이스보다는 여러 개의 구체적인 인터페이스를 설계해야한다는 뜻입니다.

```java
public interface People {
  // 가르치기
  // 채점하기
  // 수업듣기
  // 시험보기
}
```

학교에 있는 사람들을 People 인터페이스를 통해 정의했습니다.

기능을 자세히 보면 가르치기와 채점하기는 선생님의 역할이고, 수업듣기와 시험보기는 학생의 역할입니다.

하나의 People이라는 인터페이스보다 구체적인 Teacher와 Student 인터페이스로 설계를 해야 인터페이스 분리 원칙을 잘 지킨 코드입니다.

```java
public interface Teacher {
  // 가르치기
  // 채점하기
}

public interface Student {
  // 수업듣기
  // 시험보기
}
```

## 5. DIP(Dependency Inversion Principle), 의존 역전 원칙

구현클래스를 의존하는 것보다 인터페이스나 추상 클래스를 의존하는 것이 좋다라는 원칙입니다.

구현체보다 인터페이스나 추상 클래스에 의존해야 요구사항 변경이나 새로운 요구사항에 대한 기능 확장에 유리합니다.

객체끼리 의존관계를 맺을 때 구현체에 직접 접근하지 않고 인터페이스에 접근하도록 하여 의존 역전 원칙을 지킬 수 있습니다.
