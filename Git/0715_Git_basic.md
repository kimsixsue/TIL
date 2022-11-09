- [Git basic](#git-basic)
  * [상대 경로](#상대-경로)
  * [Markdown](#markdown)
  * [Git 기본기](#Git-기본기)
  * [Git bash 기본 명령어](#Git-bash-기본-명령어)
  * [Git 실전](#Git-실전)
  * [Contribution activity](#contribution-activity)

# Git basic

## 상대 경로

  `./` 현재 작업중인 폴더

`../` 현재 작업중인 폴더의 상위 경로

## Markdown

다양한 에디터가 지원함

> https://www.markdownguide.org/cheat-sheet/

| Element         | Markdown Syntax                    |
| :-------------- | ---------------------------------- |
| Heading         | `#`                                |
| Unordered List  | `-`                                |
| Horizontal Rule | `---`                              |
| Link            | `[title](https://www.example.com)` |

## Git 기본기

Git은 분산 **버전 관리** 프로그램

- 특정 상태들을 관리하는 것

- 최종본과 변경사항만을 관리, 언제 어디가 어떻게 바뀐지를 commit message에 기록

- 한 곳이 아닌 각 컴퓨터에서 버전 관리 Sync, 버전 관리 기준은 Git

Git 기반의 저장소 서비스

- [GitHub](https://github.com/), [GitLab](https://gitlab.com/), [Bitbucket](https://bitbucket.org/)

**3가지 영역**을 바탕으로 Commit이 동작

1. Workig Directory: 작업중인 실제 디렉토리

2. Staging Area: **커밋**으로 남기고 싶은 **특정 버전으로** 관리하고 싶은 파일이 있는 곳

3. Repository: **커밋**들이 저장되는 곳


Repository : 특정 디렉토리를 버전 관리하는 **저장소**

* `.git` 디렉토리에 **버전 관리에 필요한 모든 것**이 들어있음

* remote : Github, Gitlab

* local : PC

`README.md` 는 프로젝트에서 가장 먼저 보는 Markdown 문서

`.gitignore` 파일은 일종의 블랙리스트를 작성

* 그러나 이미 git에서 관리중인 경우, 해당 파일에 작동하지 않음

## Git bash 기본 명령어

| 명령어   |                         |
| :------- | ----------------------- |
| `touch`  | 파일 생성               |
| `mkdir`  | make directory          |
| `ls`     | show list               |
| `cd`     | change directory        |
| `start`  | 폴더/파일을 여는 명령어 |
| `rm`     | 파일 삭제               |
| `rm -rf` | 폴더 삭제 가능          |

## Git 실전
```python
# 처음 Git 이용 시, Run
git config --global user.email "git@mail"   # gmail
git config --global user.name "git nickname"
# 만약 프로젝트마다 다른 이름과 이메일 주소를 사용하고 싶으면
git config user.email "git@mail"
git config user.name "git nickname"
```
```python
# 최초로 local 복사. 설정 (remote 주소 포함) 포함 복제
git clone {url}  # {remote_repository_name} 기본값은 origin
git commit -m "commit_message"  # ex) 'add something'
git push {remote_repository_name} {branch_name}  # 서버에 Push
# github에서 생성한 repository의 {branch_name} 기본값은 main
```
```python
# git에서 생성한 repository의 {branch_name} 기본값은 master
git init  # name convention = origin
git remote add <단축이름> <url>  # name, remote repository
git add *  # 끝에 붙은 *은 모든 것을 의미
git commit -m "commit_message"  # ex) 'initial project version'
git push <remote_repository_name> <branch_name>  # local -> remote 업로드
```

| 명령어                                            |                                                              |
| ------------------------------------------------- | ------------------------------------------------------------ |
| `git clone <url>`                                 | 기존 저장소를 Clone해서 Git 저장소를 쓰기 시작한다. remote name은 origin |
| `git init`                                        | 로컬 저장소를 생성, master branch가 자동으로 만들어진다.     |
| `git remote add <단축이름> <url>`                 | 기존 워킹 디렉토리에 새 리모트 저장소를 추가할 수 있다.      |
| `git add`                                         | 워킹 디렉토리에서 Staging Area(“index”)로 컨텐트를 추가      |
| `git commit`                                      | `git add`로 Staging Area에 넣은 모든 파일을 커밋한다.        |
| `git push {remote_repository_name} {branch_name}` | 서버에 Push                                                  |

| 명령어                                |                                                             |
| ------------------------------------- | ----------------------------------------------------------- |
| `git pull <repo_name> <local branch>` | Git에 버전을 맞춥니다.                                      |
| `git status`                          | 파일 상태를 확인할 수 있다.                                 |
| `git log`                             | 저장소의 히스토리를 조회한다.                               |
| `git diff`                            | 어떤 라인을 추가했고 삭제했는지 알 수 있다.                 |
| `git stash`                           | 수정 사항을 stash 공간으로 이동하고, 가장 최근버전으로 복원 |

## Contribution activity
> https://github.com/kimsixsue?tab=overview&from=2022-08-14&to=2022-08-20

와 같은 주소를 통해, 해당 기간의 Contribution activity를 확인할 수 있다.

## GitLab

```bash
remote: "The project you were looking for could not be found or you don't have permission to view it"
```

https://coding-log.tistory.com/180?category=981518

https://velog.io/@likefeb16220/Git-Error-Warning#error-the-project-you-were-looking-for-could-not-be-found-or-you-dont-have-permission-to-view-it
