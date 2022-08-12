# String

## 문자의 표현

컴퓨터에서의 문자표현
    - 숫자, 비트맵, 메모리 낭비가 심하다, 대응, 숫자를 정해 놓고
    - 52, 6
코드체계
네트워크, 달리 해석, 문제
표준안, 만들기
ASCII, 문자 인코딩 표준
7bit, 128문자, 표현, 33, 제어문자, 95개의 출력 가능한 문자
ASCII 32 공백, ASCII 65 A, ASCII 97 a
악센트 문자, 도형 문자

- 1Byte, 8bit, 모두 사용, 표현

ASCII형식
코드체계

- 조합형, 완성형, 두 종류
  ASCII, 국가간에 정보를 주고 받을 때 발생
  자국, 타 국가가 가지고 있지 않으면 정보를 잘못 해석 할 수 밖에 없었다.
  다국어 처리, 표준, 유니코드
  변수의 크기를 정의
  바이트 순서, 표준화
  UCS-2 UCS-4, 인식하고, 다르게 구현
  유니 코드의 적당한 외부 인코딩이 필요
  UTF-8 in web, 1 Byte, 16, windows, java, 2 Byte, 32, 4 Byte
  2.x 버전, `#-*- coding: utf-8 -*-`, 명시
  3.x, 유니코드 UTF-8, 생략 가능

### 문자열

fixed length, variable length, length controlled, java, c언어

클래스

널문자('`\0`')

텍스트 데이터의 취급방법이 통일

홑따옴표, 쌍따옴표, 홑따옴표 3개, 쌍따옴표 3개

`+`

문자열, 문자열, 이어 붙여주는

`*`

문자열 `*` 수, 반복

문자열, 시퀀스 자료형으로 분류, 인덱싱, 슬라이싱, 있음

문자열, 요소값을 변경 할 수 없음(immutable)

c는 아스키 코드로 저장

저장

유니코드(UTF8)

#### 문자열 뒤집기

읽어서 타겟에 쓰는 방법

swap

#### 문자열 비교

`==`, `is`

- `==`, `__eq__()`

parse

int, float, str, repr

## 패턴 매칭

Brute Force 완전 탐색

- 처음부터 끝까지 차례대로 순회, 일일이 비교하는 방식

```python
ptrn = "is"
text = "This is a book~!"  # 전체 텍스트
len_ptrn = len(ptrn)  # 찾을 패턴의 길이
len_text = len(text)  # 전체 텍스트의 길이

def brute_force(ptrn, text):
    idx_text = 0  # text의 인덱스
    idx_ptrn = 0  # pattern의 인덱스
    while idx_ptrn < len_ptrn and idx_text < len_text:
        if text[idx_text] != ptrn[idx_ptrn]:
            idx_text -= idx_ptrn
            idx_ptrn = -1
        idx_text += 1
        idx_ptrn += 1
    if idx_ptrn == len_ptrn:
        return idx_text - len_ptrn  # 검색 성공
    else:
        return -1  # 검색 실패
```

```python
pattern = "is"
text = "This is a book~!"


def brute_force(pattern, text):
    M = len(pattern)  # 패턴의 길이
    N = len(text)  # 텍스트의 길이

    for idx in range(N - M + 1):  # 텍스트 순회
        for jdx in range(M):
            if pattern[jdx] != text[idx]:
                break
            else:  # 패턴이 매칭된 상태
                return idx
        else:
            return -1
```

시간 복잡도

- 최악의 경우, 텍스트, 패턴, `O(MN)`

### Knuth–Morris–Pratt 알고리즘

앞 부분에 어떤 문자가, 앞 부분, 매칭을 수행

전처리, `next[M]`, 잘못된 시작을 최소화

`O(M+N)`

패턴

### 보이어-무어 알고리즘

## 문자열 암호화

## 문자열 압축
