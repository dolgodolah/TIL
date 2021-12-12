# Git 파일(폴더)명 대소문자 변경

git은 운영체제의 파일시스템에 의존하는데 Windows나 macOS의 파일 시스템에서는 파일 이름의 대소문자가 달라도 같은 파일로 인식한다.

즉 파일 이름의 대소문자를 변경해도 스테이지에 변경이 나타나지 않는다.

## 해결 방법

기본적으로 파일명을 바꾸는 명령어는 다음과 같다.

```
git mv <oldName> <newName>

git mv rails spring
```

하지만 첫 글자만 대문자에서 소문자(혹은 그 반대)로 변경하는 경우에는 invalid argument가 발생한다.

이럴 때는 임시로 다른 파일명으로 바꿨다가 다시 원하는 이름으로 바꾸면 된다.

```
git mv <oldName> <tempName>
git mv <tempName> <newName>

git mv spring tmp
git mv tmp Spring
```



