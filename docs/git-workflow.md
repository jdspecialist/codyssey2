\# Git Clone \& Pull 실습 보고서



\## 1. 개요

원격 저장소와 로컬 저장소 간의 변경 사항 동기화 과정을 실습하기 위해 `git clone`과 `git pull`을 수행하였습니다.



\## 2. 실습 과정 및 실행 결과



\### (1) 저장소 클론 (Clone)

다른 디렉토리에서 원격 저장소를 복제하였습니다.

```bash

C:\\codyssey2>git clone https://github.com/jdspecialist/codyssey2.git codyssey2-clone

Cloning into 'codyssey2-clone'...

remote: Enumerating objects: 58, done.

remote: Counting objects: 100% (58/58), done.

remote: Compressing objects: 100% (41/41), done.

remote: Total 58 (delta 25), reused 43 (delta 16), pack-reused 0 (from 0)

Receiving objects: 100% (58/58), 18.56 KiB | 1.16 MiB/s, done.

Resolving deltas: 100% (25/25), done.





C:\\codyssey2\\codyssey2-clone>git add README.md



C:\\codyssey2\\codyssey2-clone>git commit -m "Docs: README 수정 및 clone/pull 실습"

On branch main

Your branch is up to date with 'origin/main'.



nothing to commit, working tree clean



C:\\codyssey2\\codyssey2-clone>git push origin main

Everything up-to-date



C:\\codyssey2>git pull origin main

From https://github.com/jdspecialist/codyssey2

&#x20;\* branch            main       -> FETCH\_HEAD

Already up to date.





