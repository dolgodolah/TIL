# HTTPS 적용하기
제 인스턴스(AWS EC2 - Amazon Linux 2)에 https를 적용하는 과정(시행착오)에서 학습한 내용을 정리했습니다.

## HTTPS란?
HTTPS = `HTTP(Hypertext Transfer Protocol)` + `Secure`

일반 HTTP의 문제점은 서버와 클라이언트 사이에 전송되는 정보가 암호화되지 않아 데이터가 감청당하기 매우 쉽습니다.

예를들어 로그인을 위해서 서버로 비밀번호를 전송하거나, 또는 중요한 기밀 문서를 열람하는 과정에서

악의적인 감청이나 데이터의 변조등이 일어날 수 있다는 것인데, 이를 보안한 것이 HTTPS입니다.

HTTPS를 적용하기 위해서는 SSL 인증서를 발급받아야 합니다.

유료 인증서나, Let's Encrypt같은 무료 인증서를 발급받아 적용할 수 있는데

Let's Encrypt의 경우 인증서 유효기간(3개월)마다 갱신해주어야 합니다. 

letsencrypt 인증서를 발급받기에 앞서 nginx를 설치해야합니다.

nginx를 설치하는 방법에 대해 알아보겠습니다.

## Nginx

### 왜 Nginx?



Nginx는 Apache와 같은 서버로 Apache보다 서버부담이 비교적 적어 Nginx로 갈아타는 추세라고 합니다.

여기서 Nginx를 설치하는 이유는 `reverse-proxy`를 통해 리다이렉팅을 하기 위함입니다. 

reverse-proxy란 외부의 요청을 받아 뒷단 서버로 요청을 전달하는 행위를 말하는데

이런 리버스 프록시 서버(Nginx)는 요청을 전달하고, 실제 요청에 대한 처리는 뒷단의 웹 서버들이 처리합니다.

무중단 배포를 할 때도 이를 이용하는데 이번에는 https 적용을 위해서 nginx를 설치해보겠습니다.


### Nginx 설치

EC2에 접속해 Nginx를 설치합니다.

```
sudo yum install nginx
```

설치가 완료되고 Nginx를 실행해봅니다.

```
sudo service nginx start
```

설치가 잘 되고 정상적으로 실행이 되었다면 EC2 Public DNS을 브라우저 url에 입력했을 때

Nginx에서 기본으로 설정해놓은 페이지가 열리게 됩니다. 이제 이 페이지를 실행중인 프로젝트를 바라볼 수 있도록

설정하면 됩니다.


참고
[https://opentutorials.org/course/228/4894](https://opentutorials.org/course/228/4894)

[https://velog.io/@teveloper/nginx-nginx%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%B4-AWS-EC2%EC%97%90-https-%EC%A0%81%EC%9A%A9%ED%95%98%EA%B8%B0-%EB%AC%B4%EB%A3%8C-SSL-%EC%9D%B8%EC%A6%9D%EC%84%9C-%EB%B0%9C%EA%B8%89](https://velog.io/@teveloper/nginx-nginx%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%B4-AWS-EC2%EC%97%90-https-%EC%A0%81%EC%9A%A9%ED%95%98%EA%B8%B0-%EB%AC%B4%EB%A3%8C-SSL-%EC%9D%B8%EC%A6%9D%EC%84%9C-%EB%B0%9C%EA%B8%89)