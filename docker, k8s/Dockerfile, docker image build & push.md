# Dockerfile

Dockerfile이란 도커이미지를 만들기 위한 파일입니다.

jdk 버전이나 gradle, maven 사용 여부에 따라 Dockerfile 작성하는 방법이 조금씩 다릅니다. (저는 jdk 1.8, gradle 사용)

스프링 부트 프로젝트의 jar파일을 실행하도록 하는 docker image를 build하기 위해 Dockerfile을 작성했습니다.

## Dockerfile 작성
```bash
FROM openjdk:8-jdk-alpine
ARG JAR_FILE=build/libs/*.jar
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java","-jar","/app.jar"]
```

### FROM
Dockerfile로 이미지를 만들기 위한 기반이 되는 이미지가 필요합니다.

FROM openjdk:8-jdk-alpine의 의미는 '이 이미지는 알파인 리눅스에서 사용되는 JDK 8버전을 기반으로 만듭니다' 입니다.


### ARG
image build 시에 사용되는 변수를 정의합니다.

ARG JAR_FILE=build/libs/*.jar의 의미는

JAR_FILE 변수에 build/libs/*.jar라는 값을 넣었다고 생각하면 됩니다. (build/libs/*.jar는 gradle 빌드 환경에서 빌드된 jar파일 저장 위치입니다.)

docker build 명령어를 사용할 때 --build-arg 옵션으로 오버라이딩 할 수 있습니다.



### COPY
파일이나 디렉토리를 복사하여 컨테이너 디렉토리에 추가해주는 역할을 합니다.

COPY <복사할 경로> <이미지에 추가할 경로> 형식으로 작성됩니다.

COPY ${JAR_FILE} app.jar는 JAR_FILE변수에 저장된 jar파일을 컨테이너의 app.jar경로에 추가한다는 의미입니다.



### ENTRYPOINT
해당 컨테이너가 시작되었을 때 수행할 명령어들을 정의합니다.

ENTRYPOINT ["java","-jar","/app.jar"]는 컨테이너가 시작되면 java -jar /app.jar 명령어를 실행한다는 걸 의미합니다.

가끔 예제에 /dev/urandom을 엔트리포인트에 추가하는 경우가 있는데 자바 8 이상부터는 필요하지않습니다.

To reduce Tomcat startup time, we used to add a system property pointing to /dev/urandom as a source of entropy. This is not necessary anymore with JDK 8 or later.

https://spring.io/guides/gs/spring-boot-docker/


# docker image build & push

Dockerfile 작성 후 docker build -t <IMAGE ID> . 을 통해 도커 이미지를 빌드합니다. (반드시 Dockerfile이 위치하는 루트 경로에서 실행)

빌드 명령어에서 -t는 이미지의 이름을 지정해주는 옵션입니다.

이 이미지를 docker hub repository에 push함으로써 도커 이미지 생성 및 푸시까지 진행하였습니다.
