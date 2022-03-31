# 1. document.domain 이란?

Document 인터페이스의 domain 속성은 **동일 출처 정책에서 사용하는 현재 문서의 출처에서 도메인 부분을 설정하거나 가져옵니다.**
> https://developer.mozilla.org/ko/docs/Web/API/Document/domain

<br>

예를 들어 server1.kakao.com(부모 페이지)에서 server2.kakao.com(자식 페이지)을 팝업 혹은 iframe으로 띄웠다고 가정할 때, 이 두 페이지는 `sub domain`이 달라 동일 출처 정책(same-origin policy)으로 인해 리소스 공유가 되지 않는다.

이럴 때 `document.domain`을 설정하여 동일 출처 정책을 통과할 수 있다.

1. naver.com(부모)에서 m.naver.com(자식) 팝업 띄움
<img width="1102" alt="스크린샷 2022-03-31 오후 9 54 47" src="https://user-images.githubusercontent.com/75430912/161064959-625cef77-b035-42a7-bbd3-5ac9cbe146bf.png">

2. m.naver.com(자식)에서 naver.com(부모) 페이지를 reload 해보지만 cross-origin으로 인한 동일 출처 정책 위반
<img width="1102" alt="스크린샷 2022-03-31 오후 9 55 04" src="https://user-images.githubusercontent.com/75430912/161064955-e0df6275-5c82-44b4-93e4-89cc1e0d4c74.png">

3. naver.com(부모)와 m.naver.com(자식)의 document.domain을 루트 도메인인 'naver.com'로 설정
<img width="1102" alt="스크린샷 2022-03-31 오후 9 55 37" src="https://user-images.githubusercontent.com/75430912/161064951-6e1e65dd-15dc-442f-aa94-480b835d4258.png">
<img width="1102" alt="스크린샷 2022-03-31 오후 9 55 44" src="https://user-images.githubusercontent.com/75430912/161064946-32a10f61-c015-49bc-b896-2f1e1093e041.png">

4. m.naver.com(자식)에서 naver.com(부모) 페이지를 다시 reload 해보면 성공
<img width="1102" alt="스크린샷 2022-03-31 오후 9 55 55" src="https://user-images.githubusercontent.com/75430912/161064927-206f6f83-5a15-43a1-987b-7476adced87d.png">






하지만 https://developer.chrome.com/blog/immutable-document-domain 을 보면 알 수 있듯이

보안상의 문제로 `document.domain`이 deprecated 되었기 때문에 사용을 지양해야 한다.

# 2. document.domain 대체방법

## 2.1 postMessage()

## 2.2 Channel Messaging API
