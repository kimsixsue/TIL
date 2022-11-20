# Git_Advanced

>  https://git-scm.com/book

`git restore {filename} `

- 수정한 파일을 수정 전(직전 커밋)으로 되돌리기
- 이미 git에 등록되어, 버전 관리가 되는 파일만 되돌리기 가능
- 해당 내용을 복원할 수 없으니 주의할 것



`git stash {filename}`  : 수정한 파일을 stash 공간으로 옮겨 임시 보관

- `git stash apply` : stash의 내용을 불러오기



`git add` 를 잘못한 경우 되돌리기

- `git rm --cached {filename}`
  - root-commit 이 없는 경우, 한 번도 커밋 안 한 경우
    - git에서 더 이상 관리하고 싶지 않은 file인 경우에도 사용
- `git restore --staged {filename}`
  - root-commit 이 있는 경우, 커밋이 한 번이라도 있을 때 사용
  - HEAD(최근 commit된 곳)로 되돌릴 때 사용



`git commit --amend` 

- commit 내용을 수정하지 않아도 hash 값이 변경되므로, 팀으로 작업해서 사용할 때는 주의해야 한다.

- 이전 커밋을 완전히 고쳐서 새 커밋으로 변경하므로, 이전 커밋은 일어나지 않은 일이 되며 히스토리에도 남지 않음을 주의할 것

- 상황별로 두 가지 기능으로 나뉨

  - 새로 올라온 내용이 없다면, 직전 commit의 메시지만 수정
  - 새로 올라온 내용이 있다면, 직전 commit을 덮어쓰기
    - 동시에 같이 관리되어야 할 파일이 별도로 관리 될 때, 함께 관리할 파일과 같이 새롭게 commit

- `vim 모드` 로 들어가게 됨

  - `i` 입력 모드 문서 편집 가능

  - `esc` 명령 모드
    - 저장 및 종료 `:wq`
      - 강제 종료 `:q!`



`git reset [option] {commit ID}`

- 프로젝트를 특정 커밋 버전 상태로 되돌림

- `commit ID` 는 되돌아가고 싶은 버전 시점의 `commit ID` (hash) 를 작성

- 특정 커밋으로 되돌아갔을  때, 해당 커밋 이후로 쌓았던 커밋 내역들은 전부 사라짐

  - `—-soft` : 해당 커밋 바로 직전으로 돌아가는 옵션
  - `–-mixed` : 해당 커밋 버전으로 돌아가는 옵션. default

  - `--hard`: 해당 커밋 버전으로 돌아가는 옵션.

    - 되돌아간 커밋 이후의 파일들은 모두 Working Directory에서 삭제

    - 기존의 Untracked 파일은 사라지지 않고 Untracked로 남아있음



`git reflog` 

- `git reset --hard {commit ID}` 하기 전의 과거 커밋 해쉬 명세를 모두 조회 가능

- 이후 `git reset --hard {commit ID}` 하면, 삭제된 파일도 복구 가능



`git revert {commit id}`

- 취소하고 싶은 commit id를 되돌리며, 커밋 취소했다는 commit 기록으로 남김

- 과거를 없었던 일처럼 만드는 행위로, 이전 커밋을 취소한다는 새로운 커밋 기록을 생성
- 팀 협업할 때 커밋 명세의 차이로 인한 충돌 방지 가능



## git branch

- 브랜치는 나뭇가지라는 뜻으로 여러 갈래로 작업공간을 나누어 독립적으로 작업할 수 있도록 도와주는 git의 도구

- 브랜치는 독립 공간을 형성하기 때문에, master 원본에 대해 안전함

  - 서비스가 정상 동작 가능하게, 배포할 수 있도록 유지

- 하나의 작업은 하나의 브랜치로 나누어 진행되므로, 체계적인 개발이 가능함

- git은 브랜치를 만드는 속도가 굉장히 빠르고, 적은 용량을 소모함



- **조회**
  - `git branch` : 로컬 저장소의 브랜치 목록 확인
  - `git branch -r` : 원격 저장소의 브랜치 목록 확인

- **생성**
  - `git branch {branch name}` : 새로운 브랜치 생성
  - `git branch {branch name} {commit ID}` : 특정 커밋 기준으로 브랜치 생성

- **삭제**
  - `git branch -d {branch name}` : merge 병합이 완료된 브랜치만 삭제 가능

  - `git branch -D {branch name}` : 강제 삭제
- 진행 흐름
  - branch 생성 > 새로운 기능 개발 완료 > merge 완료 > branch 삭제



## git switch

현재 브랜치에서 다른 브랜치로 이동하는 명령어

해당 브랜치의 변경 사항을 반드시 커밋 후, switch 하자

- `git switch {branch name}` : 다른 브랜치로 이동
- `git switch -c {branch name}` : 브랜치를 새로 생성하고 이동
- `git switch -c {branch name} {commit ID}` : 특정 커밋 기준으로 브랜치 생성 및 이동



`cat.git/HEAD` : 현재 브랜치가 어디인지 확인 가능

`git log --oneline`

`git log --oneline --all`

`git log --oneline --all --graph`



`git merge {합칠 브랜치 이름}`: 분기된 브랜치 들을 하나로 합치는 명령어

- 브랜치를 합치려고 하는, 즉 메인 브랜치로 switch 후, master가 선택된 상태에서, 다른 branch를 부름
- master 브랜치가 상용이므로 주로 master 브랜치에 병합, 병합 후에는 꼭 브랜치 삭제해주자
  - **Fast-Forward**
    - 마치 빨리 감기처럼, 브랜치가 가리키는 커밋을 앞으로 이동시키는 방법
    - master에는 변화 없고 다른 브랜치의 변화만 있어서, 해당 commit으로 HEAD가 이동하는 것 처럼 보임
    - `git merge hotfix`
  - **3-way Merge**
    - 각 브랜치의 커밋 두 개와 공통 조상 하나를 사용하여 병합하는 방법
    - `git merge hotfix` 하면 커밋메세지 수정란이 나옴
  - **Merge Conflict**
    - 두 브랜치에서 보통 같은 파일의 같은 부분을 수정했을 때 자주 발생함
    - Git은 사용자에게 해결 방법을 선택하라고 요청, 충돌이 발생했을 때 이를 해결하며 병합하는 방법



**Git workflow : 브랜치와 원격 저장소를 이용해 협업**



**(중요) 원격 저장소 소유권이 있는 경우: shared repository model**

- 원격 저장소가 자신의 소유이거나 Collaborator로 등록된 경우
- master 브랜치에 직접 개발하는 것이 아니라, 기능별로 브랜치를 따로 만들어 개발
- Pull Request를 사용하여 팀원 간 변경 내용에 대한 소통 진행
- 작업 순서
  1. repository 를 각자 `clone` 받는다
  2. 각자 기능별로 branch 생성하기
  3. 기능 구현이 완료되면, 해당 branch에 `push` 를 한다
  4. pull request 기능을 통해, master에 각각의 기능 브랜치들을 반영 요청
  5. 병합이 완료된 브랜치는 불필요하므로 원격 저장소에서 삭제
  6. 원격 저장소에서 병합이 완료되면 사용자는 로컬에서 master 브랜치로 switch
  7. 병합으로 인해 변경된 원격 저장소의 master 내용을 로컬에 Pull
  8. 원격 저장소 master를 받았으므로, 기존 로컬 브랜치는 삭제 (한 사이클 종료)
  9. 새 기능 추가를 위해 새로운 브랜치를 생성하며 지금까지의 과정을 반복



원격 저장소 소유권이 없는 경우

fork & pull model

- 오픈 소스 프로젝트와 같이, 자신의 소유가 아닌 코드에 개발자로서 기여하고 싶을 때

- 원본 원격 저장소를 그대로 내 원격 저장소에 복제(Fork)

- 기능 완성 후 복제한 내 원격 저장소에 Push

- 이후 Pull Request를 통해 원본 원격 저장소에 반영 요청

- 작업 순서

  1. 소유권이 없는 원격 저장소를 Fork를 통해 내 원격 저장소에 clone

  2. 이후에 로컬 저장소와 원본 원격 저장소를 동기화하기 위해 연결

     `git remote add upstream [원본 URL]`

  3. branch해서 기능 개발 진행

  4. 기능 개발 완료 후, 원본 원격 저장소에 해당 브랜치를 `push`

  5. pull request를 통해, origin의 브랜치를 upstream에 반영해달라는 요청을 보냄

  6. 좋은 코드면 upstream에 브랜치가 병합.

  7. 내 원격 저장소에서 브랜치 삭제 후, 병합된 코드 `pull` 받기

  8. 새로운 기능 추가를 위해 새로운 브랜치를 생성하며 위 과정을 반복



git branch 전략

Git Flow 

- 브랜치를 자주 생성하는 것을 강력히 권장한다.
- 대규모 프로젝트에 적합한 브랜치 전략
- 5개의 브랜치로 나누어 소스 코드를 관리
  - `master` : 제품으로 당장 출시할 수 있는 브랜치

  - `develop` : 다음 출시 버전을 개발하는 브랜치

  - `feature` : 기능을 개발하는 브랜치

  - `release` : 이번 출시 버전을 준비하는 브랜치

  - `hotfix` : 출시 버전에서 발생한 버그를 수정하는 브랜치



## 2. Git의 기초

### 수정하고 저장소에 저장하기

파일 삭제하기

Staging Area에서만 제거하고 워킹 디렉토리에 있는 파일은 지우지 않고 남겨둘 수 있다. 다시 말해서 있는 파일은 그대로 두고 Git만 추적하지 않게 한다. 이것은 `.gitignore` 파일에 추가하는 것을 빼먹었거나 대용량 로그 파일이나 컴파일된 파일인 `.a` 파일 같은 것을 실수로 추가했을 때 쓴다. `--cached` 옵션을 사용하여 명령을 실행한다.

`git rm --cached filename`

### 커밋 히스토리 조회하기

`git log [<options>]`

Git에는 히스토리를 조회하는 명령어인 `git log` 가 있다. 특별한 아규먼트 없이 `git log` 명령을 실행하면 저장소의 커밋 히스토리를 시간순으로 보여준다. 즉, 가장 최근의 커밋이 가장 먼저 나온다.

`--oneline` 

- 각 커밋을 **한 라인으로 보여준다**. 많은 커밋을 한 번에 조회할 때 유용하다.

`--all` 

- Pretend as if **all** the refs in `refs/`, along with `HEAD`, are listed on the command line as `<commit>`.

`--graph` 

- Draw a text-based **graphical** representation of the commit **history** on the left hand side of the output. This may cause extra lines to be printed in between commits, in order for the **graph history** to be drawn properly.

```bash
$ git log --pretty=format:"%h %s" --graph
* 2d3acf9 Ignore errors from SIGCHLD on trap
*  5e3ee11 Merge branch 'master' of git://github.com/dustin/grit
|\
| * 420eac9 Add method for getting the current branch
* | 30e367c Timeout code and tests
* | 5a09431 Add timeout protection to grit
* | e1193f8 Support for heads with slashes in them
|/
* d6016bc Require time for xmlschema
*  11d191e Merge branch 'defunkt' into local
```

### 되돌리기

만약 마지막으로 커밋하고 나서 수정한 것이 없다면(커밋하자마자 바로 이 명령을 실행하는 경우) 조금 전에 한 커밋과 모든 것이 같다. 이때는 **커밋 메시지만 수정한다.**

편집기가 실행되면 이전 커밋 메시지가 자동으로 포함된다. 메시지를 수정하지 않고 그대로 커밋해도 **기존의 커밋을 덮어쓴다.**

이렇게 `--amend` 옵션으로 커밋을 고치는 작업은, 추가로 작업한 일이 작다고 하더라도 **이전의 커밋을 완전히 새로 고쳐서 새 커밋으로 변경**하는 것을 의미한다. 이전의 커밋은 일어나지 않은 일이 되는 것이고 당연히 히스토리에도 남지 않는다.

Git으로 *커밋* 한 모든 것은 언제나 복구할 수 있다. 삭제한 브랜치에 있었던 것도, `--amend` 옵션으로 다시 커밋한 것도 복구할 수 있다. 하지만 커밋하지 않고 잃어버린 것은 절대로 되돌릴 수 없다.

> https://git-scm.com/docs/git-restore

`git restore {file}`

- Restore working tree files. Restore specified paths in the working tree with some contents from a restore source. **If a path is tracked but does not exist in the restore source, it will be removed to match the source.**

`git restore --staged {file}`

- Specify the restore location. If neither option is specified, by default the working tree is restored. Specifying `--staged` will only restore the index. Specifying both restores both. The command can also be used to restore the content in the index with `--staged` By default, if `--staged` is given, the **contents are restored** from `HEAD`, otherwise from the index.

### 리모트 저장소

리모트 저장소 추가하기

- 기존 워킹 디렉토리에 새 리모트 저장소를 쉽게 추가할 수 있는데 `git remote add <단축이름> <url>` 명령을 사용한다.

리모트 저장소를  Pull 하기

- 그냥 쉽게 `git pull` 명령으로 리모트 저장소 브랜치에서 데이터를 가져올 뿐만 아니라 자동으로 로컬 브랜치와 Merge 시킬 수 있다. 먼저 `git clone` 명령은 자동으로 로컬의 master 브랜치가 리모트 저장소의 master 브랜치를 추적하도록 한다(물론 **리모트 저장소**에 master 브랜치가 있다는 가정에서). 그리고 `git pull` 명령은 Clone 한 서버에서 데이터를 가져오고 그 데이터를 자동으로 현재 작업하는 코드와 Merge 시킨다.

리모트 저장소에 Push 하기

- 프로젝트를 공유하고 싶을 때 **Upstream 저장소에 Push** 할 수 있다. 이 명령은 `git push <리모트 저장소 이름> <브랜치 이름>`으로 단순하다. master 브랜치를 `origin` 서버에 Push 하려면(다시 말하지만 Clone 하면 보통 자동으로 origin 이름이 생성된다) `git push origin master` 로 서버에 Push 한다.

- **Clone 한 리모트 저장소에 쓰기 권한이 있고**, Clone 하고 난 이후 아무도 Upstream 저장소에 Push 하지 않았을 때만 사용할 수 있다. 다시 말해서 Clone 한 사람이 여러 명 있을 때, 다른 사람이 Push 한 후에 Push 하려고 하면 Push 할 수 없다. 먼저 다른 사람이 작업한 것을 가져와서 **Merge 한 후에 Push** 할 수 있다.

## 3. Git 브랜치

### 브랜치란 무엇인가

모든 버전 관리 시스템은 브랜치를 지원한다. 개발을 하다 보면 코드를 **여러 개로** 복사해야 하는 일이 자주 생긴다. 코드를 통째로 복사하고 나서 원래 코드와는 상관없이 **독립적으로 개발을 진행**할 수 있는데, 이렇게 **독립적**으로 개발하는 것이 브랜치다.

사람들은 브랜치 모델이 Git의 최고의 장점이라고, Git이 다른 것들과 구분되는 특징이라고 말한다. 당최 어떤 점이 그렇게 특별한 것일까. Git의 브랜치는 매우 가볍다. **순식간에 브랜치를 새로 만들고** 브랜치 사이를 이동할 수 있다. 다른 버전 관리 시스템과는 달리 Git은 브랜치를 만들어 작업하고 나중에 Merge 하는 방법을 권장한다. 심지어 하루에 수십 번씩해도 괜찮다. Git 브랜치에 능숙해지면 개발 방식이 완전히 바뀌고 다른 도구를 사용할 수 없게 된다.

Git의 브랜치는 커밋 사이를 가볍게 이동할 수 있는 어떤 포인터 같은 것이다. 기본적으로 Git은 `master` 브랜치를 만든다. 처음 커밋하면 이 `master` 브랜치가 생성된 커밋을 가리킨다. 이후 커밋을 만들면 `master` 브랜치는 자동으로 가장 마지막 커밋을 가리킨다.

Git 버전 관리 시스템에서 “master” 브랜치는 특별하지 않다. 다른 브랜치와 다른 것이 없다. 다만 모든 저장소에서 “master” 브랜치가 존재하는 이유는 `git init` 명령으로 초기화할 때 자동으로 만들어진 이 브랜치를 애써 다른 이름으로 변경하지 않기 때문이다.

**새 브랜치 생성하기**

`git branch {branch name}`

새로 만든 브랜치도 지금 작업하고 있던 마지막 커밋을 가리킨다.

지금 작업 중인 브랜치가 무엇인지 Git은 어떻게 파악할까. 다른 버전 관리 시스템과는 달리 Git은 'HEAD’라는 특수한 포인터가 있다. 이 포인터는 지금 작업하는 로컬 브랜치를 가리킨다. 브랜치를 새로 만들었지만, Git은 아직 `master` 브랜치를 가리키고 있다. `git branch` 명령은 브랜치를 만들기만 하고 브랜치를 옮기지 않는다.

`git log` 명령으로 쉽게 확인할 수 있다. 현재 브랜치가 가리키고 있는 히스토리가 무엇이고 어떻게 갈라져 나왔는지 보여준다. `git log --oneline --decorate --graph --all` 이라고 실행하면 히스토리를 출력한다.

```bash
$ git log --oneline --decorate --graph --all
* c2b9e (HEAD, master) made other changes
| * 87ab2 (testing) made a change
|/
* f30ab add feature #32 - ability to add new formats to the
* 34ac2 fixed bug #1328 - stack overflow under certain conditions
* 98ca9 initial commit of my project
```

실제로 Git의 브랜치는 어떤 한 커밋을 가리키는 40글자의 SHA-1 체크섬 파일에 불과하기 때문에 만들기도 쉽고 지우기도 쉽다. 새로 브랜치를 하나 만드는 것은 41바이트 크기의 파일을(40자와 줄 바꿈 문자) 하나 만드는 것에 불과하다.

브랜치가 필요할 때 프로젝트를 통째로 복사해야 하는 다른 버전 관리 도구와 Git의 차이는 극명하다. 통째로 복사하는 작업은 프로젝트 크기에 따라 다르겠지만 수십 초에서 수십 분까지 걸린다. 그에 비해 **Git은 순식간이다.** 게다가 커밋을 할 때마다 이전 커밋의 정보를 저장하기 때문에 Merge 할 때 어디서부터(Merge Base) 합쳐야 하는지 안다. 이런 특징은 개발자들이 수시로 브랜치를 만들어 사용하게 한다.

> https://git-scm.com/docs/git-switch

`git switch (-c|-C) <branch-name> [<start-point>]`

- **Switch to a specified branch**. The working tree and the index are updated to match the branch. All new commits will be added to the tip of this branch.

- `git switch -c <new-branch-name>` : **Create a new branch and switch to it**

- The `-c` flag stands for **create**
  - If you want to **create a new branch** to retain commits you create, you may do so (now or later) by using **-c with the switch** command.

- `<start-point>` : **You can grow a new branch from any commit**.

```bash
$ git switch -c fixup HEAD~3
Switched to a new branch 'fixup'
```

### 브랜치와 Merge 의 기초

실제 개발과정에서 겪을 만한 예제를 하나 살펴보자. 브랜치와 Merge는 보통 이런 식으로 진행한다.

1. 웹사이트가 있고 뭔가 작업을 진행하고 있다.
2. 새로운 이슈를 처리할 새 Branch를 하나 생성한다.
3. 새로 만든 Branch에서 작업을 진행한다.

이때 중요한 문제가 생겨서 그것을 해결하는 `Hotfix`를 먼저 만들어야 한다. 그러면 아래와 같이 할 수 있다.

1. 새로운 이슈를 처리하기 이전의 운영(Production) 브랜치로 이동한다.
2. `Hotfix` 브랜치를 새로 하나 생성한다.
3. 수정한 `Hotfix` 테스트를 마치고 운영 브랜치로 Merge 한다.
4. 다시 작업하던 브랜치로 옮겨가서 하던 일 진행한다.

브랜치의 기초

- 운영 환경에 적용하려면 문제를 제대로 고쳤는지 테스트하고 최종적으로 운영환경에 배포하기 위해 `hotfix` 브랜치를 `master` 브랜치에 합쳐야 한다. `git merge` 명령으로 아래와 같이 한다.

```bash
$ git checkout master
$ git merge hotfix
Updating f42c576..3a0874c
Fast-forward
 index.html | 2 ++
 1 file changed, 2 insertions(+)
```

- **Merge** 메시지에서 “**fast-forward**” 가 보이는가. `hotfix` 브랜치가 가리키는 `C4` 커밋이 `C2` 커밋에 기반한 브랜치이기 때문에 브랜치 포인터는 Merge 과정 없이 그저 최신 **커밋으로 이동한다.** 이런 Merge 방식을 “**Fast forward**” 라고 부른다. 다시 말해 A 브랜치에서 다른 B 브랜치를 Merge 할 때 B 브랜치가 A 브랜치 이후의 커밋을 가리키고 있으면 그저 A 브랜치가 B 브랜치와 동일한 커밋을 가리키도록 이동시킬 뿐이다.

- 이제 `hotfix`는 `master` 브랜치에 포함됐고 운영환경에 적용할 수 있는 상태가 되었다고 가정해보자.

- 급한 문제를 해결하고 `master` 브랜치에 적용하고 나면 다시 일하던 브랜치로 돌아가야 한다. 이제 더 이상 필요없는 `hotfix` **브랜치는 삭제한다**. `git branch` 명령에 `-d` 옵션을 주고 **브랜치를 삭제한다.**

```bash
$ git branch -d hotfix
Deleted branch hotfix (3a0874c).
```

Merge 의 기초

53번 이슈를 다 구현하고 master 브랜치에 Merge 하는 과정을 살펴보자. `iss53` 브랜치를 `master` 브랜치에 Merge 하는 것은 앞서 살펴본 `hotfix` 브랜치를 Merge 하는 것과 비슷하다. `git merge` 명령으로 합칠 브랜치에서 합쳐질 브랜치를 Merge 하면 된다.

```bash
$ git merge iss53
Merge made by the 'recursive' strategy.
index.html |    1 +
1 file changed, 1 insertion(+)
```

`hotfix` 를 Merge 했을 때와 메시지가 다르다. 현재 브랜치가 가리키는 커밋이 Merge 할 브랜치의 조상이 아니므로 Git은 'Fast-forward’로 Merge 하지 않는다. 이 경우에는 Git은 각 브랜치가 가리키는 커밋 두 개와 공통 조상 하나를 사용하여 **3-way Merge**를 한다.

단순히 브랜치 포인터를 최신 커밋으로 옮기는 게 아니라 **3-way Merge** 의 결과를 별도의 커밋으로 만들고 나서 해당 브랜치가 그 커밋을 가리키도록 이동시킨다. 그래서 이런 커밋은 부모가 여러 개고 Merge 커밋이라고 부른다.

충돌의 기초

가끔씩 3-way Merge가 실패할 때도 있다. Merge 하는 **두 브랜치에서 같은 파일의 한 부분을 동시에 수정하고** Merge 하면 Git은 해당 부분을 Merge 하지 못한다. 예를 들어, 53번 이슈와 `hotfix` 가 같은 부분을 수정했다면 Git은 Merge 하지 못하고 아래와 같은 **충돌(Conflict)** 메시지를 출력한다.

```bash
$ git merge iss53
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.
```

Git은 자동으로 Merge 하지 못해서 새 커밋이 생기지 않는다. 변경사항의 충돌을 개발자가 해결하지 않는 한 Merge 과정을 진행할 수 없다. Merge 충돌이 일어났을 때 Git이 어떤 파일을 Merge 할 수 없었는지 살펴보려면 `git status` 명령을 이용한다.

```bash
$ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")

Unmerged paths:
  (use "git add <file>..." to mark resolution)

    both modified:      index.html

no changes added to commit (use "git add" and/or "git commit -a")
```

충돌이 일어난 파일은 unmerged 상태로 표시된다. Git은 충돌이 난 부분을 표준 형식에 따라 표시해준다. 그러면 개발자는 **해당 부분을 수동으로 해결한다.** 충돌 난 부분은 아래와 같이 표시된다.

```bash
<<<<<<< HEAD:index.html
<div id="footer">contact : email.support@github.com</div>
=======
<div id="footer">
 please contact us at support@github.com
</div>
>>>>>>> iss53:index.html
```

**`=======` 위쪽의 내용은 `HEAD` 버전(merge 명령을 실행할 때 작업하던 `master` 브랜치)의 내용이고** 아래쪽은 `iss53` 브랜치의 내용이다. 충돌을 해결하려면 위쪽이나 아래쪽 내용 중에서 고르거나 새로 작성하여 Merge 한다. 아래는 아예 새로 작성하여 충돌을 해결하는 예제다.

```bash
<div id="footer">
please contact us at email.support@github.com
</div>
```

충돌한 양쪽에서 조금씩 가져와서 새로 수정했다. **그리고 `<<<<<<<`, `=======`, `>>>>>>>`가 포함된 행을 삭제했다. 이렇게 충돌한 부분을 해결하고 `git add` 명령으로 다시 Git에 저장한다.**

충돌을 해결하고 나서 해당 파일이 Staging Area에 저장됐는지 확인했으면 **`git commit`** 명령으로 Merge 한 것을 커밋한다.

어떻게 충돌을 해결했고 좀 더 확인해야 하는 부분은 무엇이고 왜 그렇게 해결했는지에 대해서 자세하게 기록한다. 자세한 기록은 나중에 이 Merge 커밋을 이해하는데 도움을 준다.

### 브랜치 관리

`git branch` 명령은 단순히 브랜치를 만들고 삭제하는 것이 아니다. 아무런 옵션 없이 실행하면 **브랜치의 목록을 보여준다.**

``` bash
$ git branch
  iss53
* master
  testing
```

`iss53` 브랜치는 앞에서 이미 Merge 했기 때문에 목록에 나타난다. `*` 기호가 붙어 있지 않은 브랜치는 **`git branch -d` 명령으로 삭제해도 되는 브랜치다. 이미 다른 브랜치와 Merge 했기 때문에 삭제해도** 정보를 잃지 않는다.

위에는 없었던 다른 브랜치가 보인다. 아직 Merge 하지 않은 커밋을 담고 있기 때문에 `git branch -d` 명령으로 삭제되지 않는다.

```bash
$ git branch -d testing
error: The branch 'testing' is not fully merged.
If you are sure you want to delete it, run 'git branch -D testing'.
```

Merge 하지 않은 브랜치를 **강제로 삭제**하려면 `-D` 옵션으로 삭제한다.

### 브랜치 워크플로

Long-Running 브랜치

Git은 꼼꼼하게 3-way Merge를 사용하기 때문에 장기간에 걸쳐서 한 브랜치를 다른 브랜치와 여러 번 Merge 하는 것이 쉬운 편이다. 그래서 개발 과정에서 필요한 용도에 따라 브랜치를 만들어 두고 계속 사용할 수 있다. 그리고 정기적으로 브랜치를 다른 브랜치로 Merge 한다.

이런 접근법에 따라서 Git 개발자가 많이 선호하는 워크플로가 하나 있다. 배포했거나 **배포할 코드만 `master` 브랜치에 Merge 해서** 안정 버전의 코드만 `master` 브랜치에 둔다. **개발을 진행하고 안정화하는 브랜치는 `develop`** 이나 `next` 라는 이름으로 추가로 만들어 사용한다. 이 브랜치는 언젠가 안정 상태가 되겠지만, 항상 안정 상태를 유지해야 하는 것이 아니다. 테스트를 거쳐서 안정적이라고 판단되면 `master` 브랜치에 Merge 한다. 토픽 브랜치(앞서 살펴본 `iss53` 브랜치 같은 짧은 호흡 브랜치)에도 적용할 수 있는데, 해당 토픽을 처리하고 테스트해서 버그도 없고 안정적이면 그때 Merge 한다.

사실 우리가 얘기하는 것은 커밋을 가리키는 포인터에 대한 얘기다. 커밋 포인터를 만들고 수정하고 분리하고 합치는지에 대한 것이다. 개발 브랜치는 공격적으로 히스토리를 만들어 나아가고 안정 브랜치는 이미 만든 히스토리를 뒤따르며 나아간다.

토픽 브랜치

토픽 브랜치는 프로젝트 크기에 상관없이 유용하다. 토픽 브랜치는 **어떤 한 가지 주제나 작업을 위해 만든** 짧은 호흡의 브랜치다. 다른 버전 관리 시스템에서는 이런 브랜치를 본 적이 없을 것이다. Git이 아닌 다른 버전 관리 도구에서는 브랜치를 하나 만드는 데 큰 비용이 든다. Git에서는 매우 일상적으로 브랜치를 만들고 Merge 하고 삭제한다.

앞서 사용한 `iss53` 이나 `hotfix` 브랜치가 토픽 브랜치다. 우리는 브랜치를 새로 만들고 어느 정도 커밋하고 나서 다시 `master` 브랜치에 Merge 하고 브랜치 삭제도 해 보았다. 보통 주제별로 브랜치를 만들고 각각은 독립돼 있기 때문에 매우 쉽게 컨텍스트 사이를 옮겨 다닐 수 있다. 묶음별로 나눠서 일하면 내용별로 검토하기에도, 테스트하기에도 더 편하다. 각 작업을 하루든 한 달이든 유지하다가 `master` 브랜치에 Merge 할 시점이 되면 순서에 관계없이 그때 Merge 하면 된다.

`master` 브랜치를 checkout 한 상태에서 어떤 작업을 한다고 해보자. 한 이슈를 처리하기 위해서 `iss91` 브랜치를 만들고 해당 작업을 한다. 같은 이슈를 다른 방법으로 해결해보고 싶을 때도 있다. `iss91v2` 브랜치를 만들고 다른 방법을 시도해 본다. 확신할 수 없는 아이디어를 적용해보기 위해 다시 `master` 브랜치로 되돌아가서 `dumbidea` 브랜치를 하나 더 만든다. 지금까지 말했던 커밋 히스토리는 아래 그림 같다.

### 리모트 브랜치

브랜치 추적

리모트 트래킹 브랜치를 로컬 브랜치로 Checkout 하면 자동으로 “트래킹(Tracking) 브랜치” 가 만들어진다 (트래킹 하는 대상 브랜치를 “**Upstream** 브랜치” 라고 부른다). 트래킹 브랜치는 리모트 브랜치와 직접적인 연결고리가 있는 로컬 브랜치이다. 트래킹 브랜치에서 `git pull` 명령을 내리면 리모트 저장소로부터 데이터를 내려받아 연결된 리모트 브랜치와 자동으로 Merge 한다.

서버로부터 **저장소를 Clone**을 하면 Git은 자동으로 `master` 브랜치를 `origin/master` 브랜치의 트래킹 브랜치로 만든다. 트래킹 브랜치를 직접 만들 수 있는데 리모트를 `origin` 이 아닌 다른 리모트로 할 수도 있고, 브랜치도 `master` 가 아닌 다른 브랜치로 추적하게 할 수 있다. 

## 5. 분산 환경에서의 Git

### 분산 환경에서의 워크플로

### Integration-Manager 워크플로

Git을 사용하면 **리모트 저장소**를 여러 개 운영할 수 있다. 다른 개발자는 읽기만 가능하고 자신은 쓰기도 가능한 **공개 저장소**를 만드는 워크플로도 된다. 이 Workflow에는 보통 프로젝트를 대표하는 공식 저장소가 있다. **기여자는 우선 공식 저장소를 하나 Clone 하고** 수정하고 나서 **자신의 저장소에 Push 한다.** 그 다음에 프로젝트 Integration-Manager에게 새 저장소에서 **Pull 하라고 요청한다.** 그러면 그 Integration-Manager는 기여자의 저장소를 리모트 저장소로 등록하고, 로컬에서 기여물을 테스트하고, 프로젝트 메인 브랜치에 **Merge 하고**, 그 내용을 다시 프로젝트 메인 저장소에 Push 한다.

1. 프로젝트 Integration-Manager는 프로젝트 메인 저장소에 Push를 한다.
2. 프로젝트 기여자는 메인 저장소를 Clone 하고 수정한다.
3. 기여자는 자신의 저장소에 Push 하고 Integration-Manager가 접근할 수 있도록 공개해 놓는다.
4. 기여자는 Integration-Manager에게 변경사항을 적용해 줄 것을 이메일로 요청한다.
5. Integration-Manager는 기여자의 저장소를 리모트 저장소로 등록하고 수정사항을 Merge 하여 테스트한다.
6. Integration-Manager는 Merge 한 사항을 메인 저장소에 Push 한다.

이 방식은 GitHub나 GitLab 같은 Hub 사이트를 통해 주로 사용하는 방식이다. 프로젝트를 Fork 하고 수정사항을 반영하여 다시 모두에게 공개하기 좋은 구조로 돼 있다. 이 방식의 장점은 기여자와 Integration-Manager가 각자의 사정에 맞춰 프로젝트를 유지할 수 있다는 점이다. 기여자는 자신의 저장소와 브랜치에서 수정 작업을 계속해 나갈 수 있고 수정사항이 프로젝트에 반영되도록 기다릴 필요가 없다. 관리자는 여유를 가지고 기여자가 Push 해 놓은 커밋을 적절한 시점에 Merge 한다.

### 프로젝트에 기여하기

공개 프로젝트 Fork

비공개 팀을 운영하는 것과 공개 팀을 운영하는 것은 약간 다르다. 공개 팀을 운영할 때는 모든 개발자가 프로젝트의 공유 저장소에 직접적으로 쓰기 권한을 가지지는 않는다. 그래서 프로젝트의 관리자는 몇 가지 일을 더 해줘야 한다. Fork를 지원하는 Git 호스팅에서 Fork를 통해 프로젝트에 기여하는 법을 예제를 통해 살펴본다. Git 호스팅 사이트(GitHub, BitBucket, repo.or.cz 등) 대부분은 Fork 기능을 지원하며 프로젝트 관리자는 보통 Fork 하는 것으로 프로젝트를 운영한다. 다른 방식으로 이메일과 Patch를 사용하는 방식도 있는데 뒤이어 살펴본다.

우선 처음 할 일은 메인 저장소를 Clone 하는 것이다. 그리고 나서 토픽 브랜치를 만들고 일정 부분 기여한다. 그 순서는 아래와 같다.

일단 프로젝트의 웹사이트로 가서 “Fork” 버튼을 누르면 원래 프로젝트 저장소에서 갈라져 나온, 쓰기 권한이 있는 저장소가 하나 만들어진다. 그러면 로컬에서 수정한 커밋을 원래 저장소에 Push 할 수 있다. 그 저장소를 로컬 저장소의 리모트 저장소로 등록한다. 예를 들어 `myfork`로 등록한다.

```bash
$ git remote add myfork <url>
```

자 이제 등록한 리모트 저장소에 Push 한다. 작업하던 것을 로컬 저장소의 `master` 브랜치에 Merge 한 후 Push 하는 것보다 리모트 브랜치에 바로 Push를 하는 방식이 훨씬 간단하다. 이렇게 하는 이유는 관리자가 토픽 브랜치를 프로젝트에 포함시키고 싶지 않을 때 토픽 브랜치를 Merge 하기 이전 상태로 `master` 브랜치를 되돌릴 필요가 없기 때문이다. 다시 관리자의 저장소를 Pull 할 때는 토픽 브랜치의 내용이 들어 있을 것이다.

### 프로젝트 관리하기

기여물 통합하기

Merge 하는 워크플로

바로 `master` 브랜치에 Merge 하는 것이 가장 간단하다. 이 워크플로에서는 `master` 브랜치가 안전한 코드라고 가정한다. 토픽 브랜치에서 작업을 하고 작업이 끝나면 토픽 브랜치를 검증하고 `master` 브랜치로 Merge 한 후 토픽 브랜치를 삭제하는 과정을 반복한다.

개발자가 많고 규모가 큰 프로젝트에서는 최소한 두 단계로 Merge 하는 것이 좋다. 살펴볼 예에서는 Long-Running 브랜치를 두 개를 유지한다. `master` 브랜치는 아주 안정적인 버전을 릴리즈하기 위해서 사용한다. `develop` 브랜치는 새로 수정된 코드를 통합할 때 사용한다. 그리고 두 브랜치를 모두 공개 저장소에 Push 한다. 우선 develop 브랜치에 토픽 브랜치를 같이 Merge 한다. 그 후에 릴리즈해도 될만한 수준이 되면 master 브랜치를 develop 브랜치까지 Fast-forward시킨다

이 워크플로를 사용하면 프로젝트 저장소를 Clone 하고 나서 개발자가 안정 버전이 필요하면 master 브랜치를 빌드하고 안정적이지 않더라도 좀 더 최신 버전이 필요하면 develop 브랜치를 Checkout 하여 빌드한다. 이 개념을 좀 더 확장해서 사용할 수 있다. 토픽 브랜치를 검증하기 위한 `integrate` 브랜치를 만들어 Merge 하고 토픽 브랜치가 검증되면 develop 브랜치에 Merge 한다. 그리고 `develop` 브랜치에서 충분히 안정하다는 것이 증명되면 그때 `master` 브랜치에 Fast-forward Merge 한다.

> https://git-scm.com/book/en/v2/Distributed-Git-Maintaining-a-Project

## 6. GitHub

### GitHub 프로젝트에 기여하기

프로젝트 Fork 하기

참여하고 싶은 프로젝트가 생기면 아마 그 프로젝트에 Push 할 권한은 없을 테니까 “Fork” 해야 한다. “Fork” 하면 GitHub이 프로젝트를 통째로 복사해준다. 그 복사본은 사용자 네임스페이스에 있고 Push 할 수도 있다.

이 방식에서는 사람들을 프로젝트에 추가하고 Push 권한을 줘야 할 필요가 없다. 사람들은 프로젝트를 “Fork” 해서 Push 한다. 그리고 Push 한 변경 내용을 원래 저장소로 보내 기여한다. 이것을 Pull Request라고 부른다.

GitHub 플로우

GitHub은 Pull Request가 중심인 협업 워크플로를 위주로 설계됐다. 이 워크플로는 Fork 해서 프로젝트에 기여하는 것인데 단일 저장소만 사용하는 작은 팀이나 전 세계에서 흩어져서 일하는 회사, 혹은 한 번도 본 적 없는 사람들 사이에서도 유용하다. Git 브랜치 에서 토픽 브랜치 중심으로 일하는 방식이다.

보통은 아래와 같이 일한다.

1. 프로젝트를 `Fork` 한다.
2. `master` 기반으로 토픽 브랜치를 만든다.
3. 뭔가 수정해서 커밋한다.
4. 자신의 GitHub 프로젝트에 브랜치를 Push 한다.
5. GitHub에 Pull Request를 생성한다.
6. 토론하면서 그에 따라 계속 커밋한다.
7. 프로젝트 소유자는 Pull Request를 Merge 하고 닫는다.

이 방식은 기본적으로 Integration-Manager 워크플로와 같다.

### GitHub 프로젝트 관리하기

동료 추가하기

저장소에 커밋 권한을 주고 싶은 동료가 있으면 “Collaborator” 로 추가해야 한다. Ben과 Jeff, Louise라는 동료가 있는데 그들이 내 저장소에 Push 할 수 있도록 하고 싶으면 내 프로젝트에 GitHub 계정들을 추가해야 한다. 계정이 추가된 사람은 해당 프로젝트와 Git 저장소에 “Push” 할 수 있을 뿐만 아니라 읽고 쓰기도 가능하다.

오른쪽 밑에 있는 ``Settings` ` 링크를 클릭한다.

왼쪽 메뉴에서 “Collaborators” 를 선택한다. 텍스트 박스에 사용자이름을 입력하고 “Add collaborator” 를 클릭한다. 필요한 사람을 모두 추가할 때까지 반복한다. 그리고 오른쪽에 있는 “X” 를 클릭하면 권한이 회수된다.

Pull Request로 함께 일하기

Pull Request를 만든 사람과 토론할 수 있다. GFM을 사용하여 특정 커밋을 선택하거나, 특정 라인을 지정하거나, 혹은 전체 Pull Request 자체에도 코멘트를 남길 수 있다.

일단 대화에 참여하고 나면 누군가 코멘트할 때마다 이메일 알림이 계속 온다. 그 이메일에는 Pull Request 페이지의 링크가 포함돼 있기 때문에 어떤 일이 일어나고 있는지 쉽게 알 수 있다. 그리고 답 메일을 보내면 Pull Request의 코멘트로 달린다.

보내온 코드가 마음에 들어서 Merge 하고 싶다면 로컬에 가져와서 Merge 할 수 있다. `git pull <url> <branch>` 명령으로 Merge 하면 되는데 먼저 Fork 한 저장소를 리모트로 추가하고 Fetch 해서 Merge 한다.

GitHub 사이트에서 “Merge” 버튼을 누르는 것으로 간편하게 Merge 할 수 있다(Trivial Merge). “fast-forward” 가 가능할 때도 “non-fast-forward” Merge를 하기 때문에 Merge 커밋이 생긴다. 그래서 “Merge” 버튼을 클릭해서 Merge 하면 항상 Merge 커밋이 생긴다. 여기서 어떻게 해야 하는지 'command line' 힌트 링크를 클릭하면 알려준다.

만약 Pull Request를 Merge 하지 않기로 했다면 그냥 닫으면 된다. 그러면 그 Pull Request를 보낸 사람에게 알림이 간다.

Pull Request 이어가기

Pull Request를 Merge 할 브랜치는 `master` 가 아니어도 된다. 주 브랜치를 고를 수도 있고 Pull Request를 열 때 다른 브랜치를 골라도 된다. 심지어 다른 Pull Request를 고를 수도 있다.

착착 잘 진행하는 어떤 Pull Request가 있는데 거기에 뭔가 아이디어를 더하고 싶다는 생각이 들었다. 좋은 아이디어라는 확신도 부족하고 무엇보다 Merge 될 브랜치에 Push 권한이 없다. 이럴 땐 Pull Request에 Pull Request를 보낼 수 있다.

Pull Request를 만들러 가면 페이지 위쪽에 어떤 저장소의 브랜치를 어떤 저장소의 브랜치로 요청하는 것인지를 보여주는 박스가 있다. “Edit” 버튼을 누르면 Fork 한 저장소 중 하나로 저장소를 변경하고 해당 저장소의 브랜치로 변경할 수 있다.

쉽게 다른 Fork 저장소나 Pull Request의 브랜치를 골라 Pull Request를 열 수 있다.

## 7. Git 도구

### 리비전 조회하기

RefLog로 가리키기

Git은 자동으로 브랜치와 HEAD가 지난 몇 달 동안에 가리켰었던 커밋을 모두 기록하는데 이 로그를 “Reflog” 라고 부른다.

`git reflog` 를 실행하면 Reflog를 볼 수 있다.

```bash
$ git reflog
734713b HEAD@{0}: commit: fixed refs handling, added gc auto, updated
d921970 HEAD@{1}: merge phedders/rdocs: Merge made by the 'recursive' strategy.
1c002dd HEAD@{2}: commit: added some blame and merge stuff
1c36188 HEAD@{3}: rebase -i (squash): updating HEAD
95df984 HEAD@{4}: commit: # This is a combination of two commits.
1c36188 HEAD@{5}: rebase -i (squash): updating HEAD
7e05da5 HEAD@{6}: rebase -i (pick): updating HEAD
```

Git은 브랜치가 가리키는것이 달라질 때마다 그 정보를 임시 영역에 저장한다. 그래서 예전에 가리키던 것이 무엇인지 확인해 볼 수 있다.

### Stashing과 Cleaning

당신이 어떤 프로젝트에서 한 부분을 담당하고 있다고 하자. 그리고 여기에서 뭔가 작업하던 일이 있고 다른 요청이 들어와서 잠시 브랜치를 변경해야 할 일이 생겼다고 치자. 그런데 이런 상황에서 아직 완료하지 않은 일을 커밋하는 것이 껄끄럽다는 것이 문제다. 커밋하지 않고 나중에 다시 돌아와서 작업을 다시 하고 싶을 것이다. 이 문제는 `git stash` 라는 명령으로 해결할 수 있다.

Stash 명령을 사용하면 워킹 디렉토리에서 수정한 파일들만 저장한다. Stash는 Modified이면서 Tracked 상태인 파일과 Staging Area에 있는 파일들을 보관해두는 장소다. 아직 끝내지 않은 수정사항을 스택에 잠시 저장했다가 나중에 다시 적용할 수 있다(브랜치가 달라져도 말이다).

Git은 Stash에 저장할 때 수정했던 파일들을 복원해준다. 복원할 때의 워킹 디렉토리는 Stash 할 때의 그 브랜치이고 워킹 디렉토리도 깨끗한 상태였다. 하지만 꼭 깨끗한 워킹 디렉토리나 Stash 할 때와 같은 브랜치에 적용해야 하는 것은 아니다. 어떤 브랜치에서 Stash 하고 다른 브랜치로 옮기고서 거기에 Stash를 복원할 수 있다. 그리고 꼭 워킹 디렉토리가 깨끗한 상태일 필요도 없다. 워킹 디렉토리에 수정하고 커밋하지 않은 파일들이 있을 때도 Stash를 적용할 수 있다. 만약 충돌이 있으면 알려준다.

### 히스토리 단장하기

마지막 커밋을 수정하기

히스토리를 단장하는 일 중에서는 마지막 커밋을 수정하는 것이 가장 자주 하는 일이다. 기본적으로 두 가지로 나눌 수 있는데 하나는 단순히 커밋 메시지만를 수정하는 것이고 다른 하나는 나중에 수정한 파일을 마지막 커밋 안에 밀어넣는 것이다.

커밋 메시지를 수정하는 방법은 매우 간단하다.

```bash
$ git commit --amend
```

이 명령은 자동으로 텍스트 편집기를 실행시켜서 마지막 커밋 메시지를 열어준다. 여기에 메시지를 바꾸고 편집기를 닫으면 편집기는 바뀐 메시지로 마지막 커밋을 수정한다.

반대로 커밋 메시지가 아니라 프로젝트 내용을 수정한 경우가 있다. 커밋하고 난 후 새로 만든 파일이나 수정한 파일을 가장 최근 커밋에 집어넣을 수 있다. 기본적으로 방법은 같다. 파일을 수정하고 `git add` 명령으로 Staging Area에 넣는다. 그리고 `git commit --amend` 명령으로 커밋하면 커밋 자체가 수정되면서 추가로 수정사항을 밀어넣을 수 있다.

이때 SHA-1 값이 바뀌기 때문에 과거의 커밋을 변경할 때 주의해야 한다. Rebase와 같이 이미 Push 한 커밋은 수정하면 안 된다.

### Reset 명확히 알고 가기

HEAD

HEAD는 현재 브랜치를 가리키는 포인터이며, 브랜치는 브랜치에 담긴 커밋 중 가장 마지막 커밋을 가리킨다. 지금의 HEAD가 가리키는 커밋은 바로 다음 커밋의 부모가 된다. 단순하게 생각하면 HEAD는 *현재 브랜치 마지막 커밋의 스냅샷*이다.

트리를 조작하는 동작은 세 단계 이하로 이루어진다.

`reset` 명령은 정해진 순서대로 세 개의 트리를 덮어써 나가다가 옵션에 따라 지정한 곳에서 멈춘다.

1. HEAD가 가리키는 브랜치를 옮긴다. *(`--soft` 옵션이 붙으면 여기까지)*
2. Index를 HEAD가 가리키는 상태로 만든다. *(`--hard` 옵션이 붙지 않았으면 여기까지)*
3. 워킹 디렉토리를 Index의 상태로 만든다.

1 단계: HEAD 이동

`reset` 명령이 하는 첫 번째 일은 HEAD 브랜치를 이동시킨다. `checkout` 명령처럼 HEAD가 가리키는 브랜치를 바꾸지는 않는다. HEAD는 계속 현재 브랜치를 가리키고 있고, 현재 브랜치가 가리키는 커밋을 바꾼다. HEAD가 `master` 브랜치를 가리키고 있다면(즉 `master` 브랜치를 Checkout 하고 작업하고 있다면) `git reset 9e5e6a4` 명령은 `master` 브랜치가 `9e5e6a4`를 가리키게 한다.

`reset` 명령에 커밋을 넘기고 실행하면 언제나 이런 작업을 수행한다. `reset --soft` 옵션을 사용하면 딱 여기까지 진행하고 동작을 멈춘다.

이제 위의 다이어그램을 보고 어떤 일이 일어난 것인지 생각해보자. `reset` 명령은 가장 최근의 `git commit` 명령을 되돌린다. `git commit` 명령을 실행하면 Git은 새로운 커밋을 생성하고 HEAD가 가리키는 브랜치가 새로운 커밋을 가리키도록 업데이트한다. `reset` 명령 뒤에 `HEAD~` (HEAD의 부모 커밋)를 주면 Index나 워킹 디렉토리는 그대로 놔두고 브랜치가 가리키는 커밋만 이전으로 되돌린다. Index를 업데이트한 다음에 `git commit` 명령를 실행하면 `git commit --amend` 명령의 결과와 같아진다

2 단계: Index 업데이트 (--mixed)

여기서 `git status` 명령을 실행하면 Index와 `reset` 명령으로 이동시킨 HEAD의 다른 점이 녹색으로 출력된다.

`reset` 명령은 여기서 한 발짝 더 나아가 Index를 현재 HEAD가 가리키는 스냅샷으로 업데이트할 수 있다.

`--mixed` 옵션을 주고 실행하면 `reset` 명령은 여기까지 하고 멈춘다. `reset` 명령을 실행할 때 아무 옵션도 주지 않으면 기본적으로 `--mixed` 옵션으로 동작한다(예제와 같이 `git reset HEAD~` 처럼 명령을 실행하는 경우).

위의 다이어그램을 보고 어떤 일이 일어날지 한 번 더 생각해보자. 가리키는 대상을 가장 최근의 `커밋` 으로 되돌리는 것은 같다. 그러고 나서 *Staging Area* 를 비우기까지 한다. `git commit` 명령도 되돌리고 `git add` 명령까지 되돌리는 것이다.

3 단계: 워킹 디렉토리 업데이트 (--hard)

`reset` 명령은 세 번째로 워킹 디렉토리까지 업데이트한다. `--hard` 옵션을 사용하면 `reset` 명령은 이 단계까지 수행한다.

이 과정은 어떻게 동작하는지 가늠해보자. `reset` 명령을 통해 `git add` 와 `git commit` 명령으로 생성한 마지막 커밋을 되돌린다. **그리고** 워킹 디렉토리의 내용까지도 되돌린다.

이 `--hard` 옵션은 매우 매우 중요하다. `reset` 명령을 위험하게 만드는 유일한 옵션이다. Git에는 데이터를 실제로 삭제하는 방법이 별로 없다. 이 삭제하는 방법은 그 중 하나다. `reset` 명령을 어떻게 사용하더라도 간단히 결과를 되돌릴 수 있다. 하지만 `--hard` 옵션은 되돌리는 것이 불가능하다. 이 옵션을 사용하면 워킹 디렉토리의 파일까지 강제로 덮어쓴다. 이 예제는 파일의 **v3**버전을 아직 Git이 커밋으로 보관하고 있기 때문에 `reflog` 를 이용해서 다시 복원할 수 있다. 만약 커밋한 적 없다면 Git이 덮어쓴 데이터는 복원할 수 없다.

### 고급 Merge

Git의 Merge은 진짜 가볍다. Git에서는 브랜치끼리 몇 번이고 Merge 하기가 쉽다. 오랫동안 합치지 않은 두 브랜치를 한 번에 Merge 하면 거대한 충돌이 발생한다. 조그마한 충돌을 자주 겪고 그걸 풀어나감으로써 브랜치를 최신으로 유지한다.

하지만, 가끔 까다로운 충돌도 발생한다. 다른 버전 관리 시스템과 달리 Git은 충돌이 나면 모호한 상황까지 해결하려 들지 않는다. Git의 철학은 Merge가 잘될지 아닐지 판단하는 것을 잘 하자이다. 충돌이 나도 자동으로 해결하려고 노력하지 않는다. 오랫동안 따로 유지한 두 브랜치를 Merge 하려면 몇 가지 해야 할 일이 있다.

이 절에서는 어떤 Git 명령을 사용해서 무슨 일을 해야 하는지 알아보자. 그 외에도 특수한 상황에서 사용하는 Merge 방법과 Merge를 잘 마무리하는 방법을 소개한다.

Merge 충돌

Git은 복잡한 Merge 충돌이 났을 때 필요한 도구도 가지고 있다. 무슨 일이 일어났고 어떻게 해결하는 게 나은지 알 수 있다.

Merge 할 때는 충돌이 날 수 있어서 Merge 하기 전에 워킹 디렉토리를 깔끔히 정리하는 것이 좋다. 워킹 디렉토리에 작업하던 게 있다면 임시 브랜치에 커밋하거나 Stash 해둔다. 그래야 어떤 일이 일어나도 다시 되돌릴 수 있다. 작업 중인 파일을 저장하지 않은 채로 Merge 하면 작업했던 일부를 잃을 수도 있다.

Combined Diff 형식

Merge가 성공적으로 끝난 파일은 Staging Area에 올려놓았다. 이 상태에서 충돌 난 파일들이 그대로 있을 때 `git diff` 명령을 실행하면 충돌 난 파일이 무엇인지 알 수 있다. 어떤 걸 더 고쳐야 하는지 아는 데에 도움이 된다.

Merge 하다가 충돌이 났을 때 `git diff` 명령을 실행하면 꽤 생소한 Diff 결과를 보여준다.

```bash
$ git diff
diff --cc hello.rb
index 0399cd5,59727f0..0000000
--- a/hello.rb
+++ b/hello.rb
@@@ -1,7 -1,7 +1,11 @@@
  #! /usr/bin/env ruby

  def hello
++<<<<<<< HEAD
 +  puts 'hola world'
++=======
+   puts 'hello mundo'
++>>>>>>> mundo
  end

  hello()
```

이런 형식을 “Combined Diff” 라고 한다. 각 라인은 두 개의 컬럼으로 구분할 수 있다. 첫 번째 컬럼은 “ours” 브랜치와 워킹 디렉토리의 차이(추가 또는 삭제)를 보여준다. 두 번째 컬럼은 “theirs” 와 워킹 디렉토리사이의 차이를 나타낸다.

이 예제에서 `<<<<<<<` 와 `>>>>>>>` 충돌 마커 표시는 어떤 쪽에도 존재하지 않고 추가된 코드라는 것을 알 수 있다. 이 표시는 Merge 도구가 만들어낸 코드이기 때문이다. 물론 이 표시는 지워야 하는 라인이다.

Merge 되돌리기

지금까지 Merge 하는 방법을 배웠으나 Merge 할 때 실수할 수도 있다. Git에서는 실수해도 된다. 실수해도 (대부분 간단하게) 되돌릴 수 있다.

Merge 커밋도 예외는 아니다. 토픽 브랜치에서 일을 하다가 `master` 로 잘못 Merge 했다고 생각해보자. 커밋 히스토리는 아래와 같다.

접근 방식은 원하는 결과에 따라 두 가지로 나눌 수 있다.

Refs 수정

실수로 생긴 Merge 커밋이 로컬 저장소에만 있을 때는 브랜치를 원하는 커밋을 가리키도록 옮기는 것이 쉽고 빠르다. 잘못 Merge 하고 나서 `git reset --hard HEAD~` 명령으로 브랜치를 되돌리면 된다.

 `reset --hard` 명령은 아래의 세 단계로 수행한다.

1. HEAD의 브랜치를 지정한 위치로 옮긴다. 이 경우엔 `master` 브랜치를 Merge 커밋(`C6`) 이전으로 되돌린다.
2. Index를 HEAD의 내용으로 바꾼다.
3. 워킹 디렉토리를 Index의 내용으로 바꾼다.

이 방법의 단점은 히스토리를 다시 쓴다는 것이다. 다른 사람들과 공유된 저장소에서 히스토리를 덮어쓰면 문제가 생길 수 있다. 간단히 말해 다시 쓰는 커밋이 이미 다른 사람들과 공유한 커밋이라면 `reset` 하지 않는 게 좋다. 이 방법은 Merge 하고 나서 다른 커밋을 생성했다면 제대로 동작하지 않는다. HEAD를 이동시키면 Merge 이후에 만든 커밋을 잃어버린다.

커밋 되돌리기

브랜치를 옮기는 것을 할 수 없는 경우는 모든 변경사항을 취소하는 새로운 커밋을 만들 수도 있다. Git에서 이 기능을 “revert” 라고 부른다. 지금의 경우엔 아래처럼 실행한다.

```bash
$ git revert -m 1 HEAD
[master b1d8379] Revert "Merge branch 'topic'"
```

`-m 1` 옵션은 부모가 보호되어야 하는 “mainline” 이라는 것을 나타낸다. `HEAD` 로 Merge를 했을 때(`git merge topic1`) Merge 커밋은 두 개의 부모 커밋을 가진다. 첫 번째 부모 커밋은 `HEAD` (`C6`)이고 두 번째 부모 커밋은 Merge 대상 브랜치(`C4`)이다. 두 번째 부모 커밋(`C4`)에서 받아온 모든 변경사항을 되돌리고 첫 번째 부모(`C6`)로부터 받아온 변경사항은 남겨두고자 하는 상황이다.

> https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging

This can often be useful to basically trick Git into thinking that a branch is already merged when doing a merge later on. For example, say you branched off a `release` branch and have done some work on it that you will want to merge back into your `master` branch at some point. In the meantime some bugfix on `master` needs to be backported into your `release` branch. You can merge the bugfix branch into the `release` branch and also `merge -s ours` the same branch into your `master` branch (even though the fix is already there) so when you later merge the `release` branch again, there are no conflicts from the bugfix.

## 10. Git의 내부

### Git Refs

**HEAD**

`git branch <branch>` 명령을 실행할 때 Git은 어떻게 마지막 커밋의 SHA-1 값을 아는 걸까? **HEAD** 파일은 현 브랜치를 가리키는 간접(symbolic) Refs다.

간접 Refs라서 다른 것과 다르다. 이 Refs는 다른 Refs를 가리키는 것이라서 SHA-1 값이 없다. 파일을 열어 보면 아래와 같이 생겼다.

**현재 HEAD가 어떤 브랜치를 가리키는지 알 수 있음**

```bash
$ cat .git/HEAD
ref: refs/heads/master
```

### 운영 및 데이터 복구

데이터 복구

보통 `git reflog` 명령을 사용하는 게 가장 쉽다. HEAD가 가리키는 커밋이 바뀔 때마다 Git은 남몰래 자동으로 그 커밋이 무엇인지 기록한다. 새로 커밋하거나 브랜치를 바꾸면 Reflog도 늘어난다. `git reflog` 명령만 실행하면 언제나 발자취를 돌아볼 수 있다.

```bash
$ git reflog
1a410ef HEAD@{0}: reset: moving to 1a410ef
ab1afef HEAD@{1}: commit: modified repo.rb a bit
484a592 HEAD@{2}: commit: added repo.rb
```

개체 삭제

`git rm --cached filename` 명령으로 삭제한다. 디스크에서 삭제하는 것이 아니라 Index에서 삭제하는 것이다. 이렇게 하는 이유는 속도가 빠르기 때문이다.