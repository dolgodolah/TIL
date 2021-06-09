# [TCP] 3-way handsahke, 4-way handshake

TCP의 개념 및 특징과 3-way handshake, 4-way handshake에 대해 공부하면서 정리한 글입니다.

## TCP(Transmission Control Protocol)

#### TCP란?
TCP는 네트워크 계층 중 전송 계층에서 사용하는 프로토콜로 신뢰성을 보장하는 연결형 서비스입니다.

#### TCP의 특징
**연결형 서비스**로 가상 회선 방식을 제공합니다. `3-way handshake 과정을 통해 연결을 설정`하고, `4-way handshake 과정을 통해 연결을 해제`합니다.

데이터 송신하는 곳과 수신하는 곳의 데이터 처리 속도를 조절하여 버퍼 오버 플로우를 방지하는 **흐름제어**, 네트워크 내의 패킷 수가 넘치지 않도록 하는 **혼잡제어**를 제공합니다.

높은 신뢰성을 보장하지만 UDP보다 속도가 느리기 때문에 연속성보다 신뢰성있는 전송이 중요할 때 사용됩니다.

## TCP의 연결 설정 및 해제 과정

- SYN : synchronize sequence number
- ACK : acknowledgement

### 3-way handshake
TCP통신을 이용하여 데이터를 전송하기 위해 `네트워크 연결을 설정`하는 과정입니다.

양쪽 모두 데이터를 전송할 준비가 되었다는 것을 보장합니다.

즉, TCP/IP 프로토콜을 이용해서 통신을 하는 응용 프로그램이 데이터를 전송하기 전에 먼저 정확한 전송을 보장하기 위해 상대방과 연결을 수립하는 과정을 의미합니다.

1. 클라이언트는 서버에 접속을 요청하는 `SYN(a)` 요청 메세지를 보냅니다.
2. 서버는 클라이언트의 요청인 SYN(a) 패킷을 받고 클라이언트에게 요청을 수락한다는 `ACK(a+1)`과 `SYN(b)`이 설정된 패킷을 보냅니다.
3. 클라이언트는 서버의 수락 응답인 ACK(a+1)과 SYN(b) 패킷을 받고, `ACK(b+1)`을 서버로 보내면 **연결이 성립**됩니다.

[3-way handshake 이미지](https://gmlwjd9405.github.io/images/network/3-way-handshaking.png)

### 4-way handshake
TCP의 `연결을 해제`하는 과정입니다.

1. 클라이언트가 연결을 종료하겠다는 `FIN플래그`를 전송합니다.
2. 서버는 클라이언트의 요청(FIN)을 받고 확인메세지로 `ACK`를 보냅니다. 데이터를 모두 보낼 때까지 `TIME_OUT` 상태가 됩니다.
3. 데이터를 모두 보내고 통신이 끝났으면 연결이 종료되었다고 클라이언트에게 `FIN플래그`를 보냅니다.
4. 클라이언트는 FIN플래그를 확인했다는 메시지로 `ACK`를 보내고 아직 서버로부터 받지 못한 데이터가 있을 것을 대비해 일정 시간동안 세션을 남겨 놓고 패킷을 기다리는 과정 `TIME_WAIT`을 거칩니다.
5. ACK를 받은 서버는 CLOSED 됩니다.

[4-way handshake 이미지](https://gmlwjd9405.github.io/images/network/4-way-handshaking.png)


## License
[https://asfirstalways.tistory.com/356](https://asfirstalways.tistory.com/356)

[https://gmlwjd9405.github.io/2018/09/19/tcp-connection.html](https://gmlwjd9405.github.io/2018/09/19/tcp-connection.html)