# HTTPS 적용하기
제가 구축한 인스턴스(AWS EC2 - Amazon Linux 2)에 https를 적용하는 과정(시행착오)에서 학습한 내용을 정리했습니다.

`Amazon Linux2` + `Nginx` + `Let's Encrypt`의 구성으로 진행중이라면 이 글이 조금이나마 도움이 될 것 같습니다.

## HTTPS란?
HTTPS = `HTTP(Hypertext Transfer Protocol)` + `Secure`

일반 HTTP의 문제점은 서버와 클라이언트 사이에 전송되는 정보가 암호화되지 않아 데이터가 감청당하기 매우 쉽습니다.

예를들어 로그인을 위해서 서버로 비밀번호를 전송하거나, 또는 중요한 기밀 문서를 열람하는 과정에서

악의적인 감청이나 데이터의 변조등이 일어날 수 있다는 것인데, 이를 보완한 것이 HTTPS입니다.

`HTTPS를 적용하기 위해서는 SSL 인증서를 발급`받아야 합니다. 유료 인증서나, Let's Encrypt같은

무료 인증서를 발급받아 적용할 수 있는데 Let's Encrypt의 경우 인증서 유효기간(3개월)마다 갱신해주어야 합니다. 

letsencrypt 인증서를 발급받기에 앞서 nginx를 설치하도록 하겠습니다.

## Nginx

### 왜 Nginx?

Nginx는 Apache와 같은 서버로 Apache보다 비용 부담이 비교적 적어 Nginx로 갈아타는 추세라고 합니다.

여기서 Nginx를 설치하는 이유는 `reverse-proxy`를 통해 `리다이렉트`를 하기 위함입니다. 

reverse-proxy란 외부의 요청을 받아 뒷단 서버로 요청을 전달하는 행위를 말하는데

이런 리버스 프록시 서버(Nginx)는 요청을 전달하고, 실제 요청에 대한 처리는 뒷단의 웹 서버들이 처리합니다.

[무중단 배포](https://jojoldu.tistory.com/267?category=635883)를 할 때도 이를 이용하는데 이번에는 https 적용을 위해서 nginx를 설치해보겠습니다.


### Nginx 설치

일단 `Nginx를 설치해 80포트를 8080포트로 리다이렉트하는 방법`에 대해 알아보겠습니다.

EC2에 접속해 Nginx를 설치합니다.

```
sudo yum install nginx
```

### Nginx 실행

설치가 완료되고 Nginx를 실행해봅니다.

```
sudo service nginx start
```

설치가 잘 되고 정상적으로 실행이 되었다면 도메인을 브라우저 url에

입력했을 때 Nginx에서 기본으로 설정해놓은 페이지가 열리게 됩니다.

이제 이 페이지를 실행중인 프로젝트를 바라볼 수 있도록 설정하면 됩니다.

### Nginx 설정

nginx 설정파일을 열어

```
sudo vi /etc/nginx/nginx.conf
```

`server` 내의 `location /` 부분에 아래 내용을 추가합니다.

    server {
        listen       80;
        listen       [::]:80;
        server_name  내 도메인

        location /{
                proxy_pass http://localhost:8080;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header Host $http_host;
        }


nginx 재시작 

```
sudo service nginx restart
```

을 하고 설정이 제대로 되었다면

브라우저를 통해 도메인명(:80)을 접속할 때 스프링 프로젝트(:8080)가 접속되는 걸 볼 수 있습니다.

이제 SSL을 발급받으면 http(80 포트)를 https(443 포트)로 리다이렉트하고,

https(443 포트)를 스프링 프로젝트(:8080)로 리다이렉트하면 됩니다.

이 과정은 SSL 인증서를 발급받은 후 설정하기로 합니다.

## letsencrypt SSL 인증서 발급 방법

### certbot 설치

개인적으로 이 과정이 매우 까다로웠습니다. (몇 시간동안 삽질...)

일단 letsencrypt 인증서를 받으려면 사용할 [ACME 클라이언트 소프트웨어](https://letsencrypt.org/ko/docs/client-options/) 일부를 선택해야 합니다.

대부분의 경우 certbot으로 시작하는 것을 권장한다고 하므로 certbot을 사용하겠습니다.

하지만 certbot은 Amazon Linux 2에서 공식적으로 지원되지 않는다고 하므로 `certbot 설치`를 하겠습니다. 

certbot에 필요한 종속성을 공급하는 `EPEL(Extra Packages for Enterprise Linux) 7 리포지토리 패키지를 먼저 다운`받아야 합니다.

다음 명령들을 순서대로 작성해 설치해줍니다.

```
sudo wget -r --no-parent -A 'epel-release-*.rpm' https://dl.fedoraproject.org/pub/epel/7/x86_64/Packages/e/
sudo rpm -Uvh dl.fedoraproject.org/pub/epel/7/x86_64/Packages/e/epel-release-*.rpm
sudo yum-config-manager --enable epel*
sudo yum repolist all
```

위의 마지막 명령어를 통해 EPEL이 활성화되었는지 확인할 수 있습니다. 이제 `certbot을 설치`해보겠습니다.

```
sudo yum install -y certbot
sudo yum install certbot-nginx
```

### certbot 실행 및 letsencrypt 인증서 발급 요청

이제 드디어 certbot을 실행시켜 `letsencrypt 인증서 발급 요청을 진행`해보겠습니다.

발급 방법에도 여러가지가 있다고하는데 하나만 소개하고 나머지는 [여기](https://happist.com/573990/%EC%B5%9C%EC%8B%A0-lets-encrypt-ssl-%EC%9D%B8%EC%A6%9D%EC%84%9C-%EB%B0%9C%EA%B8%89-%EB%B0%A9%EB%B2%95-3%EA%B0%80%EC%A7%80-%EC%A0%95%EB%A6%AC)를 참고바랍니다.

인증서 발급 요청 전에 인바운드 규칙에서 80포트와 443포트가 허용돼있는지 확인합니다.

허용이 되어있다면 SSL 인증서 발급을 진행합니다.

```
sudo certbot --nginx -d 도메인명
```

### 이슈 발생

인증서 발급이 완료되면 남은 과정으로는

80포트 -> 443포트, 443포트 -> 8080포트 리다이렉트 설정과 인증서 자동 갱신 설정입니다.

하지만 저는 여기서 진행을 중단했습니다. letsencrypt 인증서 발급을 진행하는 도중

'The ACME server refuses to issue a certificate for this domain name, because it is forbidden by policy'라는

에러가 발생했고 도메인명이 거절당했다는 걸 알 수 있습니다.

저는 EC2 인스턴스를 생성하고 ~.amazon.com과 같은 형태인 퍼블릭 IPv4 DNS를 그대로 사용하였는데

letsencrypt에서는 이를 [high-risk domain names로 판단하여 blacklist로 설정](https://community.letsencrypt.org/t/policy-forbids-issuing-for-name-on-amazon-ec2-domain/12692)했기 때문에 계속 거절당했던 겁니다.

그리하여 제가 진행하고 있는 프로젝트 서버를 적절한 도메인으로 설정한다면

이 글을 수정하여 남은 리다이렉트 과정과 자동 갱신 방법에 대해서 알아보겠습니다.

(이 방법에 대해서는 아래 링크를 참고하시면 나와있습니다.)



## 참고

[https://happist.com/573990/%EC%B5%9C%EC%8B%A0-lets-encrypt-ssl-%EC%9D%B8%EC%A6%9D%EC%84%9C-%EB%B0%9C%EA%B8%89-%EB%B0%A9%EB%B2%95-3%EA%B0%80%EC%A7%80-%EC%A0%95%EB%A6%AC](https://happist.com/573990/%EC%B5%9C%EC%8B%A0-lets-encrypt-ssl-%EC%9D%B8%EC%A6%9D%EC%84%9C-%EB%B0%9C%EA%B8%89-%EB%B0%A9%EB%B2%95-3%EA%B0%80%EC%A7%80-%EC%A0%95%EB%A6%AC)

[https://opentutorials.org/course/228/4894](https://opentutorials.org/course/228/4894)

[https://velog.io/@infoqoch/AWS-linux2%EC%97%90%EC%84%9C-Nginx%EB%A1%9C-Lets-Encrypt-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0#aws%EC%97%90%EC%84%9C-nginx%EC%9D%98-%ED%99%9C%EC%9A%A9](https://velog.io/@infoqoch/AWS-linux2%EC%97%90%EC%84%9C-Nginx%EB%A1%9C-Lets-Encrypt-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0#aws%EC%97%90%EC%84%9C-nginx%EC%9D%98-%ED%99%9C%EC%9A%A9)