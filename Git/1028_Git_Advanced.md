# Git_Advanced

## GIT undoing

- Git 작업 되돌리기
  - working directory 작업 단계

### working directory

- **git restore**

  > https://git-scm.com/docs/git-restore

  - 수정한 파일을 수정 전으로 되돌리기

  - 이미 버전 관리가 되는 파일만 되돌리기 가능

  - git restore를 통해 되돌리면, 해당 내용을 복원할 수 없으니 주의할 것

    `git restore {filename}`

- **git stash**

  > https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-Stashing%EA%B3%BC-Cleaning

  - 수정한 파일을 stash 영역(임시 공간)으로 옮긴 후에
  - 수정한 부분 초기화

### staging area 작업 단계 되돌리기

- git  add 를 잘못한 경우 되돌리기
- root-commit 이 없는 경우 : `git rm --cached filename`
  - 한 번도 커밋 안 한 경우
  - git 으로 관리 되는 file -> 더는 관리하고 싶지 않을 때, `gitignore`에 등록해야 하는데 commit 됐을 때
- root-commit 이 있는 경우 : `git restore --stage filename`
  - 커밋이 한 번이라도 있을 때 사용

### Repository 작업 단계 되돌리기

> https://git-scm.com/book/ko/v2/Git%EC%9D%98-%EA%B8%B0%EC%B4%88-%EB%90%98%EB%8F%8C%EB%A6%AC%EA%B8%B0

- `git commit --amend`

  > https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-%ED%9E%88%EC%8A%A4%ED%86%A0%EB%A6%AC-%EB%8B%A8%EC%9E%A5%ED%95%98%EA%B8%B0

- 상황별로 두 가지 기능으로 나뉨

  - 직전 커밋의 메시지만 수정
  - 직전 커밋을 덮어쓰기

- 이전 커밋을 완전히 고쳐서 새 커밋으로 변경하므로, 이전 커밋은 일어나지 않은 일이 되며 히스토리에도 남지 않음을 주의할 것!

- 팀으로 작업해서 사용할 때는 주의해야 한다. 

  - 문제 발생: 계속 커밋 해시값이 변경되면 해시값이 두 개로 나뉘면서 기존이랑 충돌

- 이전에 a파일 커밋, 새로운 b파일, a와 b 같이 커밋하고 싶을 때 이 명령어 사용

- vim 간단 사용법

  - i 입력 모드 문서 편집 가능
  - esc 명령 모드
    - 저장 및 종료 `:wq`
    - 강제 종료 `:q!`

### git reset/revert

- 둘 다 특정 시간으로 되돌리기

- commit 기록을 하느냐 하지 않느냐? 차이점

- **git reset**

  - 마치 과거로 돌리는 듯한 행위로, 프로젝트를 특정 커밋 버전 상태로 되돌림

  - 특정 커밋으로 되돌아갔을  때 해당 커밋 이후로 쌓았던 커밋들은 전부 사라짐

  - `git reset [option] {commit ID}`

    > https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-Reset-%EB%AA%85%ED%99%95%ED%9E%88-%EC%95%8C%EA%B3%A0-%EA%B0%80%EA%B8%B0
    >
    > https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-%EB%A6%AC%EB%B9%84%EC%A0%84-%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0
    >
    > https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-%EB%8C%80%ED%99%94%ED%98%95-%EB%AA%85%EB%A0%B9
    >
    > https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-%ED%9E%88%EC%8A%A4%ED%86%A0%EB%A6%AC-%EB%8B%A8%EC%9E%A5%ED%95%98%EA%B8%B0

    - 옵션: soft, mixed, hard 중 하나를 작성

    - soft: 해당 커밋으로 되돌아가고, 되돌아간 커밋 이후 파일들은 staging area로 넣어둠. 돌려둠

      - c2 커밋 바로 직전으로 돌아가는 옵션
      - `git reset --soft HEAD~1`

    - mixed: 옵션을 정하지 않으면 기본

      - 되돌아간 커밋 이후의 파일들은 working directory로 돌려놓음
      - `git reset --mixed 3daf666`

    - hard

      > https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-%EA%B3%A0%EA%B8%89-Merge

      - 되돌아간 커밋 이후 파일들은 모두 working directory에서 삭제

        - 따라서 사용 시 주의할 것
          - 복구는 가능 `reflog`

      - `git reset --hard 0785b4a`

        `HEAD is now at 0785b4a commit 01 - 이 커밋은 수정되었습니다.`

      - ls 해보면 다 삭제됨

      - `git reflog`

        > https://git-scm.com/book/ko/v2/Git%EC%9D%98-%EB%82%B4%EB%B6%80-%EC%9A%B4%EC%98%81-%EB%B0%8F-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%B3%B5%EA%B5%AC

        - hard 옵션으로 삭제했을 때
        - `git reflog` 명령어를 사용하면 reset 하기 전의 과거 커밋 명세를 모두 조회 가능
        - `git reflog`
        - 가장 위쪽이 최근
        - 아래쪽으로 갈수록 옛날
        - 그러고 `git reset --hard` 하면 복구 가능
        - `git reset –hard 1fe67b2`

    - 커밋ID는 되돌아가고 싶은 시점의 커밋 ID를 작성

- **git revert**

  > https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-%EA%B3%A0%EA%B8%89-Merge

  - 해당 commit을 취소시키고, 취소시킨 걸 기록으로 남기는 것이다.
  - 과거를 없었던 일로 만드는 행위로, 이전 커밋을 취소한다는 뜻. 새로운 커밋을 생성
  - `git revert {commit ID}`
  - 새로운 커밋이 하나 증가함 커밋 삭제했다는 커밋이 증가하는 것임.
  - GitHub을 이용해 팀 협업할 때 커밋 명세의 차이로 충돌 방지

- 문법적 차이

  - `git reset 5sd2f42`라고 작성하면 커밋으로 되돌린다는 뜻
  - `git revert 5sd2f42`라고 작성하면 5sd2f42 라는 커밋 한 개를 취소한다는 뜻

## git branch

> https://git-scm.com/book/ko/v2/Git-%EB%B8%8C%EB%9E%9C%EC%B9%98-%EB%B8%8C%EB%9E%9C%EC%B9%98%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80

- 브랜치는 나뭇가지라는 뜻으로 여러 갈래로 작업공간을 나누어 독립적으로 작업할 수 있도록 도와주는 git의 도구

- 독립적인 작업 공간

- 브랜치는 독립 공간을 형성하기 때문에 master 원본에 대해 안전함

  - master: 동작이 정상적 서비스가 가능한 배포할 수 있는	

- 하나의 작업은 하나의 브랜치로 나누어 진행되므로 체계적인 개발이 가능함

- git은 브랜치를 만드는 속도가 굉장히 빠르고, 적은 용량을 소모함

- **조회**

  - `git branch`: 로컬 저장소의 브랜치 목록 확인
  - `git branch -r`: 원격 저장소의 브랜치 목록 확인

- **생성**

  - `git branch {branch name}`: 새로운 브랜치 생성
  - `git branch {branch name} {commit ID}`: 특정 커밋 기준으로 브랜치 생성

- **삭제**

  - `git branch -d {branch name}`: merge 병합이 완료된 브랜치만 삭제 가능

  - `git branch -D {branch name}`: 강제 삭제

    > https://git-scm.com/book/ko/v2/Git-%EB%B8%8C%EB%9E%9C%EC%B9%98-%EB%B8%8C%EB%9E%9C%EC%B9%98-%EA%B4%80%EB%A6%AC

1. 기능 개발 완료 2. merge OK 3. branch 삭제

## git switch

> https://git-scm.com/docs/git-switch

- `git switch {branch name}`: 다른 브랜치로 이동
  - `git switch hj`
- `git switch -c {branch name}`: 브랜치를 새로 생성하고 이동
  - `git switch -c hj`
- `git switch -c {branch name} {commit ID}`: 특정 커밋 기준으로 브랜치 생성 및 이동
- switch 하기 전에, 해당 브랜치의 변경 사항을 반드시 커밋해야함을 주의할 것
- **커밋하고 스위치 하자**
  - 커밋 안 하면 서로 레파지토리에 영향을 미침

## git merge

> https://git-scm.com/book/ko/v2/Git-%EB%B8%8C%EB%9E%9C%EC%B9%98-%EB%B8%8C%EB%9E%9C%EC%B9%98%EC%99%80-Merge-%EC%9D%98-%EA%B8%B0%EC%B4%88

- 분기된 브랜치 들을 하나로 합치는 명령어

- master 브랜치가 상용이고 주로 master 브랜치에 병합

- `git merge {합칠 브랜치 이름}`

  - 병합하기 전에 브랜치를 합치려고 하는, 즉 **메인 브랜치로 switch 해야 함**

  - 병합에는 세 종류가 존재

    - **Fast-Forward**

      - 마치 빨리 감기처럼 브랜치가 가리키는 커밋을 앞으로 이동시키는 방법
      - 가장 쉬운 방식 master 가서 merge 명령어 치기
      - 명령어 `(master) git merge hotfix`

    - **3-way Merge**

      - master도 분기가 됐고, hotfix도 분기가 된 상태
      - 가장 최근 부분들(master에서도 최근 것 + hotfix에서도 최근 것) 합쳐지기
      - git switch master 로 master에서 작업
      - 명령어 git merge hotfix 하면 커밋메세지 수정란이 나옴
      - 깃이 알아서 fast-forward 인지 3-way-merge인지 알아서 선택해줌

    - **Merge Conflict**

      > https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-%EA%B3%A0%EA%B8%89-Merge

      - 두 브랜치에서 같은 부분을 수정한 경우 발생

      - 보통 같은 파일의 같은 부분을 수정했을 때 자주 발생함

      - 충돌이 발생했을 때 이를 해결 (사용자에게 선택하라고 함)하며 병합하는 방법

      - `error: CONFLICT (content): Merge conflict in {file name}`

        - 무조건 해결 해야 함. 파일 이름 해당하는 파일 열어서 수정해야 함

          ```bash
          Hello
          world
          <<<<<<< HEAD (master에서 수정한 부분)
          rabbit
          bunny
          =======
          login
          logout
          >>>>>>> login(login에서 수정한 부분)
          ```

        - 수정은 그냥 없애고 싶은 부분 없애면 됨 **>>>> 부분들**

        - **conflict 해결 후에 git add . > git commit 하고 vim 나가면 끝**

        - (master | MERGING) > (master)로 변경되면 해결된 상황임

## workflow

> https://git-scm.com/book/ko/v2/Git-%EB%B8%8C%EB%9E%9C%EC%B9%98-%EB%B8%8C%EB%9E%9C%EC%B9%98-%EC%9B%8C%ED%81%AC%ED%94%8C%EB%A1%9C
>
> https://git-scm.com/book/ko/v2/%EB%B6%84%EC%82%B0-%ED%99%98%EA%B2%BD%EC%97%90%EC%84%9C%EC%9D%98-Git-%EB%B6%84%EC%82%B0-%ED%99%98%EA%B2%BD%EC%97%90%EC%84%9C%EC%9D%98-%EC%9B%8C%ED%81%AC%ED%94%8C%EB%A1%9C

- 원격 저장소를 이용해 협업하는 두 가지 방법

  - **(중요) 원격 저장소 소유권이 있는 경우: shared repository model**

    > https://git-scm.com/book/ko/v2/GitHub-GitHub-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EA%B4%80%EB%A6%AC%ED%95%98%EA%B8%B0

    - collaborator로 등록된 경우

    - master 브랜치에 직접 개발하는 것이 아니라, 기능별로 브랜치를 따로 만들어 개발

    - `git push origin branchname`

      > https://git-scm.com/book/ko/v2/Git-%EB%B8%8C%EB%9E%9C%EC%B9%98-%EB%A6%AC%EB%AA%A8%ED%8A%B8-%EB%B8%8C%EB%9E%9C%EC%B9%98

    - `Pull Request를 사용하여 팀원 간 변경 내용에 대한 소통 진행`

    - 원격 저장소에

      1. clone 받기

      2. 각자 branch 생성하기

      3. master가 아니라 본인 branch에 push를 한다

      4. pull request 기능을 통해 각각의 기능들을 merge 시킨다

      5. merge가 끝나면 master로 돌아가서

      6. 그다음 병합이 완료된 master를 pull 받기

      7. 그다음 개발 완료한 branch는 삭제해 주기

         ------- 7번 단계까지 1사이클

      8. 새로운 기능을 추가하려면 새로운 branch 생성

      9. 반복

  - 원격 저장소 소유권이 없는 경우: fork & pull model

    > https://git-scm.com/book/ko/v2/GitHub-GitHub-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%EC%97%90-%EA%B8%B0%EC%97%AC%ED%95%98%EA%B8%B0

    - 특정 오픈 소스나, django, kakao 등등 소유권 없는 코드에 코더로서 개발자로서 기여하고 싶을 때

      1. fork를 한다.

      2. git remote add upstream [원본 URL]

         > https://git-scm.com/book/ko/v2/Git%EC%9D%98-%EA%B8%B0%EC%B4%88-%EB%A6%AC%EB%AA%A8%ED%8A%B8-%EC%A0%80%EC%9E%A5%EC%86%8C
         >
         > https://git-scm.com/book/ko/v2/%EB%B6%84%EC%82%B0-%ED%99%98%EA%B2%BD%EC%97%90%EC%84%9C%EC%9D%98-Git-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%EC%97%90-%EA%B8%B0%EC%97%AC%ED%95%98%EA%B8%B0

         - 동기화하기 위해서

      3. branch해서 기능 개발

      4. 기능 개발 완료 후 나의 원격 저장소에 해당 브랜치를 push

      5. pull request를 원본에 요청함

      6. 좋은 코드면 병합함

      7. 병합되면 병합된 코드 pull 받고 branch 삭제

- git branch 전략

  - git-flow

    - 다음과 같이 5개의 브랜치로 나누어 소스 코드를 관리

      - master: 제품으로 출시될 수 있는 브랜치

      - develop: 다음 출시 버전을 개발하는 브랜치

        > https://git-scm.com/book/ko/v2/%EB%B6%84%EC%82%B0-%ED%99%98%EA%B2%BD%EC%97%90%EC%84%9C%EC%9D%98-Git-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EA%B4%80%EB%A6%AC%ED%95%98%EA%B8%B0
        >
        > https://git-scm.com/book/ko/v2/Git-%EB%B8%8C%EB%9E%9C%EC%B9%98-%EB%B8%8C%EB%9E%9C%EC%B9%98%EC%99%80-Merge-%EC%9D%98-%EA%B8%B0%EC%B4%88

      - feature: 기능을 개발하는 브랜치

      - release: 이번 출시 버전을 준비하는 브랜치

      - hotfix: 출시 버전에서 발생한 버그를 수정하는 브랜치

    - 대규모 프로젝트에 적합한 브랜치 전략

  - GitHub-flow

    - GitHub에서 사용하는 방식

      > https://git-scm.com/book/ko/v2/GitHub-GitHub-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%EC%97%90-%EA%B8%B0%EC%97%AC%ED%95%98%EA%B8%B0

  - gitlab flow

    > https://git-scm.com/book/ko/v2/%EB%B6%84%EC%82%B0-%ED%99%98%EA%B2%BD%EC%97%90%EC%84%9C%EC%9D%98-Git-%EB%B6%84%EC%82%B0-%ED%99%98%EA%B2%BD%EC%97%90%EC%84%9C%EC%9D%98-%EC%9B%8C%ED%81%AC%ED%94%8C%EB%A1%9C

    - gitlab에서 사용하는 방식
    - pre-production

  - 결국 어떤 브랜치 전략은 팀에서 전략을 정한다

  - **브랜치는 자주 생성하는 것을 강력히 권장**

  - **main으로 만들어서 하는 작업을 지양**

기타 명령어

> https://git-scm.com/book/ko/v2/Git%EC%9D%98-%EA%B8%B0%EC%B4%88-%EC%BB%A4%EB%B0%8B-%ED%9E%88%EC%8A%A4%ED%86%A0%EB%A6%AC-%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0

- git log --oneline: 깃 로그 한 줄로 보기

- git log --oneline --all: 로그 전부 다 볼 수 있음

- git log --oneline --all --graph: 그래프로 로그기록 확인 가능

- `cat .git/HEAD`: 현재 HEAD가 어떤 브랜치를 가리키는지 알 수 있음

  > https://git-scm.com/book/ko/v2/Git%EC%9D%98-%EB%82%B4%EB%B6%80-Git-Refs

- **무조건 머지 후에 branch 사용하지 않으면 삭제해줘야 함**