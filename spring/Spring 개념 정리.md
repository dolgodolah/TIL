# Spring 개념 정리

스프링 프레임워크에 대해서 공부하면서 배운 내용들을 정리했습니다.

## Spring Framework란?

>스프링 프레임워크는 자바 플랫폼을 위한 오픈 소스 애플리케이션 프레임워크로서 간단히 스프링(Spring)이라고도 한다. 동적인 웹 사이트를 개발하기 위한 여러 가지 서비스를 제공하고 있다. 대한민국 공공기관의 웹 서비스 개발 시 사용을 권장하고 있는 전자정부 표준프레임워크의 기반 기술로서 쓰이고 있다.


## Spring의 특징

### 1. IOC

IOC는 Inversion of Control의 약자로 제어의 역전이라는 뜻입니다. 지금까지 객체 지향적인 프로그래밍은 각 객체들이 프로그램의 흐름을 결정하고 각 객체를 구성하는 작업에 직접적으로 참여했습니다. 즉, `모든 작업을 개발자가 제어하는 구조`인 것입니다.

하지만 IOC에서는 이 흐름의 구조를 바꿨습니다. 제어의 흐름을 개발자가 컨트롤 하지 않고, 프레임워크 컨테이너가 제어를 하게 됩니다. 즉, `객체의 생성부터 생명주기 등 모든 객체에 대한 제어권이 넘어간 것`입니다.

#### DI (Dependency Injection) : 의존성 주입

IOC의 구성요소 중 대표적으로 DI가 있습니다. 

일단 의존성이라는 것은 클래스 A가 또 다른 클래스 B 없이는 제 기능을 할 수 없을 때 클래스 A가 클래스 B에 대한 의존성이 있다(의존을 하고 있다)라고 표현할 수 있습니다.

DI, 의존성 주입은 이러한 클래스 B를 객체로 생성하여 `외부에서 클래스 A에 주입시켜주는 것을 말합니다.`

의존성 주입을 하게 되면 객체들간의 결합도를 낮추면서 유연성과 확장성은 향상시킬 수 있습니다.

- 객체를 직접 생성했을 때
```java
public class bookService{
    public void getPrice(){
        BookRepository book = new Spring();
        book.price();
    }
}

public static void main(String[] args){
    bookService.getPrice();
}
```

bookService 클래스에 가격을 알 수 있는 getPrice 메소드가 있습니다.

getPrice 메소드에서는 Spring 객체를 직접 생성하였습니다.

스프링책이 아닌 자바책의 가격을 구하고 싶으면 bookService를 찾아가 new SpringBook()을 `BookRepository book = new Java();`로 바꿔야합니다.

- 객체를 외부에서 주입했을 때
```java
public class BookService{
    private BookRepository bookRepository;
    public BookService(BookRepository bookRepository){ 
        this.bookRepository=bookRepository; //주입!
    }

    public void getPrice(){
        bookRepository.price();
    }
}

public static void main(String[] args){
    BookRepository book = new Spring();
    BookService bookService = new BookService(book);
    bookService.getPrice();
}
```

객체를 외부에서 주입하게 되면 스프링 책에서 자바 책의 가격을 알고 싶을 때

bookService를 수정할 필요 없이 book의 객체를 new Java()로 하면 됩니다.


### 2. POJO

POJO는 Plain Old Java Object로 평범한 자바 오브젝트라는 뜻입니다.

이전 EJB(Enterprise JavaBeans)는 확장 가능하고 재사용이 가능한 로직을 개발하기 위해 사용 되었었는데

EJB는 한가지 기능을 위해 불필요한 복잡한 로직이 과도하게 들어가는 단점이 있었습니다.

그래서 다시 조명을 받은게 POJO입니다. POJO를 사용함으로써 코드를 심플하게 작성할 수 있고, 그로인해 테스트 하기에 더 좋으며, 유연하고, 요구사항에 따라 기술적 선택을 바꿀수 있습니다.

### 3. AOP

AOP는 Aspect Oriented Programming로 관점 지향 프로그래밍입니다.

자바 언어를 이용한 프로그래밍은 OOP(Object Oriented Programming)입니다.

객체 지향 프로그래밍 과정 중에 중복된 코드가 많아져 가독성, 확장성, 유지보수성이 떨어질 수 있습니다.

이를 보완하기 위해 핵심 비즈니스 로직과 공통 기능(보안, 트랜잭션 등)을 분리시켜

핵심 비즈니스 로직에 반복적인 공통 기능들을 끼워넣는 식의 AOP가 등장합니다.

Spring에서는 AOP를 편리하게 사용할 수 있도록 지원하고 있습니다.


### 4. MVC

MVC는 Model + View + Controller의 합성어로 소프트웨어 디자인 패턴입니다.

Model은 실제로 처리되는 데이터를 말하고,

View는 화면의 표시, 입력 등을 처리하여 model의 상태를 표시합니다.

Controller는 해당 요청에 근거하여 model과 view의 처리를 제어합니다.

이처럼 기능별로 작업을 분리함으로써 유지보수가 쉬워집니다.