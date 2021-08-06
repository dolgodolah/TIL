
서버에서 요청을 받고 응답을 하지않고 대기한다?

응답을 어떻게 늦게 보내지?

변경 감지는 어떻게 하지?

인증됐다는 사실을 어떻게 로그인 화면에 알리지?



# 기존 HTTP 통신
http는 절대 절대 절대 양방향 통신이 될 수 없습니다. request와 response 형태의 단방향 통신만 가능합니다.

Client 요청이 있을 때만 Server가 응답을 하여 해당 정보를 전송하고 곧바로 연결을 종료하는 방식입니다. 

즉, http는 Server에서 원하는 타이밍에 Client에게 데이터를 보낼 수 없습니다.

그럼 로그인 화면 대기 상태에서 계속 기다렸다가 어떻게 인증 여부를 판단하고 로그인을 진행할까요?



Client와 Server가 양방향 통신을 할 수 있으면 됩니다. 하지만 http프로토콜을 뜯어 고치지 않는한 http는 양방향 통신이 불가능합니다^^

그래서 양방향으로 통신하는 것처럼 느끼게 할 수 있는 방법을 생각 해냅니다. 가장 초기모델이 바로 polling입니다.



# Polling
http통신은 양방향 통신이 될 수 없으나 양방향처럼 보이게는 할 수 있습니다.

주기적으로 요청을 보내면 됩니다. 주기적으로 요청을 보내게 되면 응답도 마찬가지로 주기적으로 받게되고

사용자입장에서는 마치 양방향 통신을 하는것처럼 느껴집니다.

![image](https://user-images.githubusercontent.com/75430912/127518310-af3cf32b-016a-479a-a88c-7a150de6746c.png)


Server에서 원하는 타이밍에 응답을 보낼 수는 없지만 주기적으로 요청응답이 이뤄지기때문에 이벤트 발생을 Server에서 Client로 알릴 수 있습니다.

요청의 간격이 짧아지면 짧아질 수록 실시간처럼 보입니다. 하지만 간격이 짧을수록 요청량이 많이지기 때문에 Server와 Client 모두에게 부담입니다.

그렇다고 간격을 길게 하면 실시간성이 떨어집니다..

그래서 새롭게 생각해낸 방식이 Long Polling 방식입니다.

# Long Polling

![image](https://user-images.githubusercontent.com/75430912/127518449-c7bbc0db-f6a2-4b2b-8f6b-1b978fb0d679.png)


Client에서 요청을 하게되면 바로 응답이 오는게 아니라 이벤트가 발생할 때까지 기다렸다가 이벤트 발생 시 응답을 보내는 방식입니다.

기다렸다가 Server에서 이벤트가 발생하면 응답을 보내기때문에 실시간성이 매우 좋습니다.

하지만 Long Polling도 단점이 있습니다. Server에서 발생하는 이벤트가 많다면?

결국 Long Polling도 기본 Polling방식과 마찬가지로 통신량이 많아져 비용이 많이 들고,

일정 간격인 Polling 방식보다 더 많은 통신량을 초래할 수도 있습니다.

- jQuery 롱폴링 예제 https://stackoverflow.com/questions/6835835/jquery-simple-polling-example

- java and spring 롱폴링으로 채팅 예제 https://www.bemyaficionado.com/long-polling-with-java-and-spring-boot/

- java and spring 롱폴링 기본 구조 https://pythonq.com/so/javascript/1382842

# Socket
Client와 Server가 특정 Port를 통해 실시간으로 양방향 통신을 하는 방식입니다.

Socket통신은 Http 통신과 달리 Server와 Client가 특정 Port를 통해 연결을 성립하고 있어 실시간으로 양방향 통신을 하는 방식입니다.

Client만 필요한 경우에 요청을 보내는 Http 통신과 달리 Socket 통신은 Server 역시 Client로 요청을 보낼 수 있으며,

계속 연결을 유지하는 연결지향형 통신이기 때문에 실시간 통신이 필요한 경우에 자주 사용됩니다.

예를 들면, 실시간 Streaming 중계나 실시간 채팅과 같이 즉각적으로 정보를 주고받는 경우에 사용합니다.

만약 실시간 동영상 Streaming 서비스를 Http 통신으로 구현하였다고 가정해보면,

이러한 경우에 사용자가 서버로 동영상을 요청하기 위해서는 동영상이 종료되는 순간까지 계속해서 Http 통신을 보내야 하게 됩니다.

이러한 구조는 계속 연결을 요청하기 때문에 부하가 걸리게 됩니다.

그러므로 이러한 경우에는 Socket을 통해 구현하는 것이 적합합니다.

- 스프링부트 웹소켓으로 채팅 예제 https://kouzie.github.io/spring/Spring-Boot-%EC%8A%A4%ED%94%84%EB%A7%81-%EB%B6%80%ED%8A%B8-WebSocket/#tomcat-%EC%9B%B9%EC%86%8C%EC%BA%A3-%EC%98%88%EC%A0%9C

