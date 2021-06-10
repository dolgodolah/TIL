## git add 취소하기

```bash
git reset HEAD <file> 
```

파일명이 없으면 add한 파일 전체를 취소합니다.

## git commit 취소하기

1. commit을 취소하고 해당 파일들은 stage 상태로 워킹 디렉토리에 보존

```bash
git reset --soft HEAD^
```

2. commit을 취소하고 해당 파일들은 unstage 상태로 워킹 디렉토리에 보존

```bash
git reset --mixed HEAD^ // 기본옵션
git reset HEAD^ // 위와 동일
git reset HEAD~2 // 마지막 2개의 커밋을 취소
```

3. commit을 취소하고 해당 파일들은 unstage 상태로 워킹 디렉토리에서 삭제

```bash
git reset --hard HEAD^
```

## git push 취소하기
되돌아간 commit 이후의 모든 commit 정보가 모두 사라지므로 협업 프로젝트에서는 사용하지말자!!

1. 가장 최근의 commit을 취소합니다.
```bash
git reset HEAD^
```

2. 원하는 시점으로 워킹 디렉토리를 되돌립니다.
```bash
git reset [commit id]
```

3. 되돌려진 상태에서 다시 commit 합니다.
```bash
git commit -m "commit messages"
```

4. 원격 저장소에 강제로 push 합니다.
```bash
git push -f origin [branch name]
```


## 출처
[https://velog.io/@hidaehyunlee/Git-add-commit-push-%EC%B7%A8%EC%86%8C%ED%95%98%EA%B8%B0](https://velog.io/@hidaehyunlee/Git-add-commit-push-%EC%B7%A8%EC%86%8C%ED%95%98%EA%B8%B0)