# 1. document.domain 이란?

Document 인터페이스의 domain 속성은 **동일 출처 정책에서 사용하는 현재 문서의 출처에서 도메인 부분을 설정하거나 가져옵니다.**
> https://developer.mozilla.org/ko/docs/Web/API/Document/domain

<br>

예를 들어 server1.kakao.com(부모 페이지)에서 server2.kakao.com(자식 페이지)을 팝업 혹은 iframe으로 띄웠다고 가정할 때, 이 두 페이지는 `sub domain`이 달라 동일 출처 정책(same-origin policy)으로 인해 리소스 공유가 되지 않는다.

이럴 때 `document.domain`을 설정하여 동일 출처 정책을 통과할 수 있다.

하지만 https://developer.chrome.com/blog/immutable-document-domain 을 보면 알 수 있듯이

보안상의 문제로 `document.domain`이 deprecated 되었기 때문에 사용을 지양해야 한다.

# 2. document.domain 대체방법

## 2.1 postMessage()

## 2.2 Channel Messaging API