# 1. document.domain

"Document 인터페이스의 domain 속성은 **동일 출처 정책에서 사용하는 현재 문서의 출처에서 도메인 부분을 설정하거나 가져옵니다.**"
> https://developer.mozilla.org/ko/docs/Web/API/Document/domain

<br>

`server1.kakao.com`(부모 페이지)에서 `server2.kakao.com`(자식 페이지)을 팝업 혹은 iframe으로 띄웠다고 가정할 때 이 두 페이지는 `sub-domain`이 달라 동일 출처 정책(same-origin policy)에 의해 리소스 공유가 되지 않는다.

이럴 때 `document.domain`을 설정하면 동일 출처 정책을 통과할 수 있다.

## 재현

1. naver.com(부모)에서 m.naver.com(자식) 팝업 띄움
<img width="1102" alt="스크린샷 2022-03-31 오후 9 54 47" src="https://user-images.githubusercontent.com/75430912/161064959-625cef77-b035-42a7-bbd3-5ac9cbe146bf.png">

2. m.naver.com(자식)에서 naver.com(부모) 페이지를 reload 해보지만 cross-origin으로 인한 동일 출처 정책 위반
<img width="1102" alt="스크린샷 2022-03-31 오후 9 55 04" src="https://user-images.githubusercontent.com/75430912/161064955-e0df6275-5c82-44b4-93e4-89cc1e0d4c74.png">

3. naver.com(부모)와 m.naver.com(자식)의 document.domain을 루트 도메인인 'naver.com'로 설정
<img width="1102" alt="스크린샷 2022-03-31 오후 9 55 37" src="https://user-images.githubusercontent.com/75430912/161064951-6e1e65dd-15dc-442f-aa94-480b835d4258.png">
<img width="1102" alt="스크린샷 2022-03-31 오후 9 55 44" src="https://user-images.githubusercontent.com/75430912/161064946-32a10f61-c015-49bc-b896-2f1e1093e041.png">

4. m.naver.com(자식)에서 naver.com(부모) 페이지를 다시 reload 해보면 성공
<img width="1102" alt="스크린샷 2022-03-31 오후 9 55 55" src="https://user-images.githubusercontent.com/75430912/161064927-206f6f83-5a15-43a1-987b-7476adced87d.png">


## document.domain 은 취약하다

하지만 위 재현에서 보았듯이 `document.domain`은 공격자에 의해서도 설정이 될 수 있다. Chrome에서는 이러한 보안상의 문제로 `document.domain` 수정이 금지될 예정이라고 한다.

<br>

# 2. document.domain 대체방법

Chrome뿐 아니라 다른 브라우저들에서도 `document.domain`을 수정하지 못하도록 할 예정이라고 하니 앞으로 `document.domain`을 수정하는 코드는 작성을 지양해야 하며, 기존에 `document.domain`을 수정함으로써 리소스 공유를 하던 서비스들 또한 기능이 작동되지 않게 되기 때문에 대응을 해야 한다.

Chrome에서는 `document.domain`을 대체할 수 있는 방법으로 `postMessage()` 또는 `Channel Messaging API`를 제안하고 있다.

## postMessage()

`postMessage()`를 통해 부모 페이지와 자식 페이지 간에 메세지를 주고 받을 수 있다.

자식 페이지에서 특정 액션을 수행하고 결과값을 `postMessage()`로 부모 페이지에 전달하게 되면, 부모 페이지에서는 이 메세지를 따른 적절한 처리를 하면 된다.

`postMessage()`로 부모 페이지를 reload 시키려면 다음과 같은 구조로 코드를 작성하면 된다.

- In iframe or popup:
```js
window.parent.postMessage("loaded", "*");
```

- In parent
```js
window.addEventListener("loaded", receiveMessage, false);

function receiveMessage(event) {
   // do reload
   window.location.reload();
}
```

### 주의해야 할 보안 사항

`event listener`를 통해 메세지를 받을 때 항상 신뢰된 사이트에서만 메세지가 온다라는 보장이 없기 때문에 검증 과정없이 아무 메세지를 다 받게 되면 XSS 공격에 취약하다.

그러므로 메세지를 받을 때는 받은 메세지의 출처가 어디인지 도메인 등과 같은 정보가 신뢰할 수 있는 값인지 검증하는 과정이 있어야 한다.

`postMessage()`를 통해 메세지를 보내는 쪽도 주의해야 할 보안 사항은 있다. `postMeesage()`의 두번째 인자에 항상 `*`가 아닌 특정 도메인들을 명시해야 한다.

`*`를 넣게 되면 모든 도메인에 대해 메세지를 보내도록 허용함을 의미하는데 이럴 경우 악성 사이트에서도 해당 메세지를 받을 수 있음을 의미하고 메세지를 통해 전달되는 데이터를 가로챌 수 있게 되기 때문이다.

## Channel Messaging API


# Ref

https://developer.mozilla.org/ko/docs/Web/API/Document/domain

https://developer.chrome.com/blog/immutable-document-domain

https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage