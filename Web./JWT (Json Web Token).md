# JWT (Json Web Token)

JWT (Json Web Token)는 정보를 담아 토큰을 발급할 수 있는 웹 토큰의 한 종류입니다.

Header, Payload, Signature 세 부분으로 구성되어 있고,

토큰을 이용하면 서버에서 사용자 상태를 기억하고 있는 stateful한 세션 방식의 인증과는 달리

stateless한 인증을 구현할 수 있기 때문에 수평적 확장에 있어 유리하여 최근 각광받고 있습니다.

## 1. 토큰 구조

### 1.1 Header

헤더에서는 두 가지 정보를 명시합니다.
- `typ` : 토큰의 타입을 나타내며 여기서는 당연히 JWT입니다.
- `alg` : 토큰을 검증할 때 signature를 해싱하기 위한 알고리즘을 지정합니다.

### 1.2 Payload

토큰에 담을 정보가 `Claim`이라는 단위로 들어있는 부분입니다.

`Claim`은 정보의 한 조각으로 `key`, `value`의 한 쌍으로 이뤄져있습니다.

이 클레임에는 세 가지 종류가 있습니다.

- 등록된 (registered) 클레임
   -  `iss`: 토큰 발급자 (issuer)
   -  `sub`: 토큰 제목 (subject)
   -  `aud`: 토큰 대상자 (audience)
   -  `exp`: 토큰의 만료시간 (expiraton)
   -  `nbf`: Not Before 를 의미하며, 토큰의 활성 날짜와 비슷한 개념
   -  `iat`: 토큰이 발급된 시간 (issued at)
   -  `jti`: JWT의 고유 식별자
- 공개 (public) 클레임
- 비공개 (private) 클레임

이미 등록된 클레임 외에도 공개, 비공개 클레임을 통해 정보를 추가할 수 있습니다.

### 1.3 Signature

토큰이 유효한지 판단하는 문자열입니다.

`Header` + `Payload` + `Secret Key`를 Header에서 명시한 알고리즘(HS256..)을 통해 해싱하여 생성합니다.

`Header`나 `Payload`에서 값이 변경되면 즉, 데이터가 변경되면 Signature가 완전히 달라지므로 토큰이 유효한지 검증할 수 있습니다.

Secret Key를 알지 못하면 복호화가 불가능하기 때문에 이 비밀키는 서버에서 잘 관리되어야 합니다.

## 2. JWT 방식의 로그인

보통 토큰은 HTTP Request에 `Authorization: <type> <credentials>`의 형태로 헤더에 담아 보내도록 합니다.

JWT의 경우 `Authorization: Bearer 토큰값`으로 요청 헤더에 담아 서버에 전송합니다.

### 2.1 Access Token

로그인을 통해 발급받은 Access Token을 요청 헤더에 담아 전송하여 토큰 검증이 유효할 경우 요청을 정상적으로 처리합니다.
  
`Authorization: <type> <credentials>`에서 type은 Bearer, credentials에는 Access Token을 넣습니다.
  
#### Access Token 동작방식
  
1. 클라이언트가 로그인 요청을 하면 Access Token을 발급받습니다.
2. 클라이언트는 발급받은 Access Token을 Local Storage(Cookie에 저장해도 되는 듯)에 저장합니다.
3. 다음 요청 시 헤더에 Access Token을 담아 보냅니다. `Authorization: Bearer AccessToken`
4. Access Token이 유효할 경우 클라이언트의 요청을 정삭적으로 처리합니다.
5. Access Token이 유효하지 않을 경우 클라이언트의 요청을 처리하지 않고 로그인 페이지로 리다이렉트합니다. 
  
### 2.2 Refresh Token

### 2.3 인증/인가 동작방식

