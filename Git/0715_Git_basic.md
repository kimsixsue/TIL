# Git basic

* Git은 분산 **버전 관리** 프로그램
* 특정 상태들을 관리하는 것
* 최종본과 변경사항만을 관리
  * 언제 어디가 어떻게 바뀐지를 commit message에 기록
* 한 곳이 아닌 각 컴퓨터에서 버전 관리 Sync
  * 버전 관리 기준은 Git
* Git기반의 저장소 서비스: GitLab, GitHub, Bitbucket

------

## Git bash 기본 명령어

* touch == 파일 생성
* mkdir == make directory
* ls == show list
* cd == change directory
* start == 폴더/파일을 여는 명령어
* rm == 파일 삭제
  * -rf 옵션을 주면 폴더 삭제 가능

-----

## 상대 경로

* ./ == 현재 작업중인 폴더
* ../ == 현재 작업중인 폴더의 상위 경로

-----

## Markdown

> https://www.markdownguide.org/cheat-sheet/

* README.md 파일

* 다양한 에디터가 지원함

* h1은 #로 시작

* 리스트는 *로 시작
  
  ```
  코드블럭은 
  ```을 
  씀
  ```

* 링크는 [title] (https://www.example.com)

* 구분선은 ---

----

## Git 기본기

* README.md
  
  * 프로젝트에서 가장 먼저 보는 문서

* Repository : 특정 디렉토리를 버전 관리하는 **저장소**
  
  * **git init** 명령어로 로컬 저장소를 생성
  * .git 디렉토리에 **버전 관리에 필요한 모든 것**이 들어있음
  * remote : Github, Gitlab
  * local : PC

* Commit은 3가지 영역을 바탕으로 동작
  
  1. Workig Directory
     * 작업중인 실제 디렉토리
  2. Staging Area
     * **커밋**으로 남기고 싶은 **특정 버전으로** 관리하고 싶은 파일이 있는 곳
  3. Repository
     * **커밋**들이 저장되는 곳

---

## Git 실전

```python
# 처음 Git 이용 시, Run
git config --global user.email "깃메일" # 주로 지메일
git config --global user.name "깃닉네임"
```

```python
git clone {remote_repo} # 최초로 local 복사. 설정 (remote 주소 포함) 포함 복제
git commit -m "add something"
git push origin master
```

```python
git init # name convention = origin
git remote add <repo_name> {remote_repo} # remote_repo는 repository 주소
git add . # 끝에 붙은 .은 모든 것을 의미
git commit -m "commit_message" # 자세하게
git push <repo_name> <local branch> # local -> remote 업로드
```

```python
git pull <repo_name> <local branch> # git에 버전을 맞춥니다.
```

```python
git status # Git으로 관리중인 파일 상태
```

```python
git log # Git commit history
```

```python
git diff # 두 commit 간 차이
```

```python
git stash # 수정 사항을 stash 공간으로 이동하고, 가장 최근버전으로 복원
```

* .gitignore 파일은 일종의 블랙리스트를 작성
  
  * 그러나 이미 git에서 관리중인 경우, 해당 파일에 작동하지 않음

----

![토끼 사진](./img/Oryctolagus_cuniculus_Tasmania_2.jpg)