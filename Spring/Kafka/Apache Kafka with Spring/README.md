# Practice Kafka with Spring

## 0. Overview

`Spring Framework` 기반 서버에 `Kafka`를 연결해보고, API를 통해 event를 Producing, Consuming 해본다.

## 1. Zookeeper & Kafka Install

- `Kafka`는 Message Broker 역할

- `Zookeeper`는 Broker를 관리하는 역할

`Kafka`를 운영하기 위해서는 `Zookeeper`가 구축되어 있어야 한다.

brew를 통한 설치 방법과, [Apache Kafka](https://kafka.apache.org/quickstart)에서 다운로드 받아 설치하는 방법이 있다.

(brew install을 통해 진행했다.)

- ### brew install
```bash
$ brew install kafka
$ brew install zookeeper

$ zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties # Start the ZooKeeper service
$ kafka-server-start /usr/local/etc/kafka/server.properties # Start the Kafka broker service
```

- ### Apache Kafka Download
```bash
# Download `https://kafka.apache.org/quickstart`

$ tar -xzf kafka_2.13-3.4.0.tgz
$ cd kafka_2.13-3.4.0

$ bin/zookeeper-server-start.sh config/zookeeper.properties # Start the ZooKeeper service
$ bin/kafka-server-start.sh config/server.properties # Start the Kafka broker service
```

## 2. Configuring Topics

`Topic`은 이벤트 메세지를 구분하는 단위이다. (저장소 이름정도로 생각하면 될 듯?)

커맨드라인으로 `Topic`을 생성 할 수 있지만, 여기서는 **KafkaAdmin Spring bean**을 통해서 `Topic`을 생성해본다.

- [코드](https://github.com/dolgodolah/TIL/blob/master/Spring/Kafka/Apache%20Kafka%20with%20Spring/src/main/kotlin/com/example/kafka/conf/KafkaTopicConfig.kt)

## 3. Consuming Messages

### 3.1 Consumer Configuration

이벤트 메세지를 Consuming 하기 위해 Consumer Configuration을 등록한다.

- [코드](https://github.com/dolgodolah/TIL/blob/master/Spring/Kafka/Apache%20Kafka%20with%20Spring/src/main/kotlin/com/example/kafka/conf/KafkaConsumerConfig.kt)

### 3.2 Consuming Messages

`@KafkaListener` 어노테이션을 통해 특정 토픽들에 대한 이벤트 메세지를 Consuming 할 수 있다.

- [코드](https://github.com/dolgodolah/TIL/blob/master/Spring/Kafka/Apache%20Kafka%20with%20Spring/src/main/kotlin/com/example/kafka/service/KafkaConsumerService.kt)

Producer 등록하기 전에 방금 Consumer로 설정한 스프링 서버를 실행시키고,

(현재는 스프링 서버에 Consumer만 등록된 상태)

kafka 커맨드라인을 통해 apple, banana 라는 메세지를 Producing 하게 되면


```bash
$ kafka-console-producer --broker-list localhost:9092 --topic [topickName]
> apple
> banana
```

스프링 서버에서 이 이벤트 메세지를 Consuming 하는 것을 확인할 수 있다.

```
receive message : apple
receive message : banana
```

## 4. Producing Messages

### 4.1 Producer Configuration


스프링 서버에 Producer Configuration도 등록해본다.

- [코드](https://github.com/dolgodolah/TIL/blob/master/Spring/Kafka/Apache%20Kafka%20with%20Spring/src/main/kotlin/com/example/kafka/conf/KafkaProducerConfig.kt)


### 4.2 Publishing Messages

먼저 간단한 API를 만들고,

- [코드](https://github.com/dolgodolah/TIL/tree/master/Spring/Kafka/Apache%20Kafka%20with%20Spring/src/main/kotlin/com/example/kafka/controller)

해당 API의 요청 DTO를 JSON 문자열로 치환하여, kafka에 메세지를 Publish 하도록 한다.

- [코드](https://github.com/dolgodolah/TIL/blob/master/Spring/Kafka/Apache%20Kafka%20with%20Spring/src/main/kotlin/com/example/kafka/service/KafkaProducerService.kt)

<br>

API 요청을 보내게 되면

```bash
$ curl -X POST http://localhost:8080/send \
  -H "Content-Type: application/json" \
  -d '{"name": "kim", "age": 27}'
```

`{"name":"kim","age":27}`라는 메세지가 발행 될 거고,

이 이벤트 메세지가 Consumer인 스프링 서버에 찍히는 것을 볼 수 있다.

```
receive message : {"name":"kim","age":27}
```

## 5. Async Producing

### TODO
- [ ] 이벤트 메세지 전송 결과를 기다리지 않도록 한다.

## 6. Consumer Commit & Offset

### TODO
- [ ] Commit, Offset 개념 정리
- [ ] 자동 커밋, 수동 커밋

## 6. Troubleshooting
`Apache kafka: Failed to acquire lock on file .lock in tmp/kafka-logs` - [해결법](https://stackoverflow.com/questions/37294996/apache-kafka-failed-to-acquire-lock-on-file-lock-in-tmp-kafka-logs)

## 7. Reference
https://www.baeldung.com/spring-kafka