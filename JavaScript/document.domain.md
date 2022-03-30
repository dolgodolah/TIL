# 1. document.domain 이란?

같은 사이트이지만 서로 다른 서버 간의 통신이 필요한 경우 `document.domain`을 통해 iframe이나 windown 간에 통신이 가능하게 할 수 있다.

- 예를 들어 `parent.abc.com`에서 `child.abc.com`을 새 창으로 띄우고
- `child.abc.com`에서 입력받은 값을 `parent.abc.com`에 전달하려면
- `document.domain = 'abc.com'`처럼 `document.domain`에 서버의 hostname을 설정하면 된다.

하지만 https://developer.chrome.com/blog/immutable-document-domain 을 보면 알 수 있듯이

보안상의 문제로 document.domain이 deprecated 되었다는 것을 알 수 있다.

# 2. document.domain 대체방법

## 2.1 postMessage()

## 2.2 Channel Messaging API