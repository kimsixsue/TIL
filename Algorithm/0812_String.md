# String

## 문자의 표현

- **컴퓨터에서의 문자표현**
  
  - 메모리는 **숫자**만을 저장할 수 있기 때문에, 글자의 모양 그대로 **비트맵**으로 저장하는 방법을 사용하지 않는 한(이 방법은 **메모리 낭비가 심하다**) 각 문자에 대해서 **대응**되는 **숫자를 정해 놓고** 이것을 메모리에 저장하는 방법이 사용될 것이다.
  
  - 영어가 대소문자 합쳐서 **52** 이므로, **6**(64가지)비트면 모두 표현할 수 있다. 이를 **코드체계**라고 한다.

- 그런데 **네트워크**가 발전되기 전 미국의 각 지역 별로 코드체계를 정해 놓고 사용했지만

- 네트워크(인터넷: 미국에서 발전했다)이 발전하면서 서로간에 정보를 주고 받을 때 정보를 **달리 해석**한다는 **문제**가 생겼다.

- 그래서 혼동을 피하기 위해 **표준안**을 **만들기**로 했다.

- 바로 이러한 목적으로 1967년, 미국에서 **A**merican **S**tandard **C**ode for **I**nformation **I**nterchange라는 **문자 인코딩 표준**이 제정되었다.

- ASCII는 **7bit** 인코딩으로 **128문자**를 **표현**하며 **33**개의 출력 불가능한 **제어 문자**들과 공백을 비롯한 **95개의 출력 가능한 문자**들로 이루어져있다.
  
  - ASCII 32 `공백`
  
  - ASCII 65 `A`
  
  - ASCII 97 `a`

- 확장 아스키는 표준 문자 이외의 **악센트 문자, 도형 문자**, 특수 문자, 특수 기호 등 부가적인 문자를 128개 추가할 수 있게 하는 부호이다.
  
  - 표준 아스키는 7bit를 사용하여 문자를 표현하는 데 비해 확장 아스키는 **1Byte** 내의 **8bit**를 **모두 사용**함으로써 추가적은 문자를 **표현**할 수 있다.
  
  - 컴퓨터 생산자와 소프트웨어 개발자가 여러 가지 다양한 문자에 할당할 수 있도록 하고 있다. 이렇게 할당된 확장 부호는 표준 아스키와 같이 서로 다른 프로그램이나 컴퓨터 사이에 교환되지 못한다.
  
  - 그러므로 표준 아스키는 마이크로컴퓨터 하드웨어 및 소프트웨어 사이에서 세계적으로 통용되는 데 비해, 확장 아스키는 프로그램이나 컴퓨터 또는 프린터가 그것을 해독할 수 있도록 설계되어 있어야만 올바로 해독될 수 있다. 

- 오늘날 대부분의 컴퓨터는 문자를 읽고 쓰는데 ASCII형식을 사용한다.

- 그런데 컴퓨터가 발전하면서 미국 뿐 아니라 각 나라에서도 컴퓨터가 발전했으며 각 국가들은 자국의 문자를 표현하기 위하여 **코드체계**를 만들어서 사용하게 되었다.
  
  - 우리나라도 아주 오래된 이야기지만 한글 코드체계를 만들어서 사용했고 **조합형, 완성형 두 종류**를 가지고 있었다.

- 인터넷이 전 세계로 발전하면서 **ASCII**를 만들었을 때의 문제와 같은 문제가 **국가간에 정보를 주고 받을 때 발생**했다.

- **자국**의 코드체계를 **타 국가가 가지고 있지 않으면 정보를 잘못 해석 할 수 밖에 없었다.**

- 그래서 **다국어 처리**를 위해 **표준**을 마련했다 이를 **유니코드**라고 한다.

- 유니코드도 다시 Character Set으로 분류된다.
  
  - Universal Character Set-2
  
  - Universal Character Set-4
  
  - 유니코드를 저장하는 **변수의 크기를 정의**
  
  - 그러나, **바이트 순서**에 대해서 **표준화**하지 못했음.
  
  - 다시 말해 파일을 인식 시 이 파일이 **UCS-2, UCS-4**인지 **인식하고** 각 경우를 구분해서 모두 **다르게 구현**해야 하는 문제 발생
    
    - 그래서 **유니 코드의 적당한 외부 인코딩이 필요**하게 되었다.

- big-endian, little-endian

- 유니코드 인코딩 (Unicode Transformation Format)
  
  - **UTF-8 in web**
    
    - MIN: 8bit, MAX: 32bit(**1 Byte** * 4)
  
  - UTF-**16** (in **windows, java**)
    
    - MIN: 16bit, MAX: 32bit(**2 Byte** * 2)
  
  - UTF-**32** (in unix)
    
    - MIN: 32bit, MAX: 32bit(**4 Byte** * 1)

- Python 인코딩
  
  - **2.x 버전** - ASCII -> `#-*- coding: utf-8 -*-` (첫 줄에 **명시**)
  
  - **3.x** 버전, **유니코드 UTF-8** -> **생략 가능**
  
  - 다른 인코딩 방식으로 처리 시 첫 줄에 작성하는 위 항목에 원하는 인코딩 방식을 지정해주면 됨

## 문자열

문자열의 분류

- **fixed length**

- **variable length**
  
  - **length controlled**
    
    - **java** 언어에서의 문자열
  
  - delimited
    
    - **c언어**에서의 문자열

java에서 String **클래스**에 대한 메모리 배치

C와 Java의 String 처리의 기본적인 차이점

- **c는 아스키 코드로 저장**한다.
  
  - 문자배열에 문자열을 저장할 때는 항상 마지막에 끝을 표시하는 널문자 (**`\0`**)를 넣어줘야 한다.

- java는 유니코드(UTF16, 2byte)로 **저장**한다.

- 파이썬은 **유니코드(UTF8)**로 저장
  
  - char 타입 없음
  
  - **텍스트 데이터의 취급방법이 통일**되어 있음
  
  - 문자열 기호
    
    - `'`(**홑따옴표**', `"`(**쌍따옴표**), `'''`(**홑따옴표 3개**), `"""`(**쌍따옴표 3개**)
    
    - `+` 연결 Concatenation
      
      - **문자열 + 문자열** : **이어 붙여주는** 역할
    
    - `*` 반복
      
      - **문자열 `*` 수** : 수만큼 문자열이 **반복**
  
  - **문자열**은 **시퀀스 자료형으로 분류**되고, 시퀀스 자료형에서 사용할 수 있는 **인덱싱, 슬라이싱** 연산들을 사용할 수 **있음**
  
  - **문자열**은 튜플과 같이 **요소값을 변경 할 수 없음(immutable)**

#### 문자열 뒤집기

자기 문자열에서 뒤집는 방법이 있고 새로운 빈 문자열을 만들어 소스의 뒤에서부터 **읽어서 타겟에 쓰는 방법**이 있겠다.

자기 문자열을 이용할 경우는 **swap**을 위한 임시 변수가 필요하며 반복 수행을 문자열 길이의 반만을 수행해야 한다.

```python
s = 'Reverse this String'
rev_str = ''
for idx in range(len(s) - 1, -1, -1):
    rev_str += s[idx]
print(rev_str)

list_s = list(s)
for idx in range(len(s) // 2):
    list_s[idx], list_s[-1 - idx] = list_s[-1 - idx], list_s[idx]
print(''.join(list_s))
```

#### 문자열 비교

파이에서는 `==`연산자와 `is`연산자를 제공한다.

- `==`연산자는 내부적으로 특수 메서드 `__eq__()`를 호출 

```python
s1 = 'abc'
s2 = 'abc'
s3 = 'def'
s4 = s1
s5 = s1[:2] + 'c'

print(s1 == s2)  # True
print(s1 == s3)  # False
print(s1 == s4)  # True
print(s1 == s5)  # True

print(s1 is s2)  # True
print(s1 is s3)  # False
print(s1 is s4)  # True
print(s1 is s5)  # False
```

#### 문자열 숫자를 정수로 변환하기

c 언어에서는 atoi()함수를 제공한다. 역 함수로는 itoa()가 있다.

java에서는 숫자 클래스의 **parse** 메소드를 제공한다.

파이썬에서는 문자와 문자변환 함수를 제공한다.

- **`int`, `float`, `str`, `repr`**

```python
# integer to alphabet [in python]
def itoa(num):
    # 음수 여부 판단
    neg = False  # flag : 음수라면 True, 양수라면 False
    if num < 0:
        neg = True
        num = -num
    result = ''
    while num:
        num, remain = num // 10, num % 10
        result = chr(ord('0') + remain) + result
    if neg:
        return '-' + result

    return result


res = itoa(1234)
print(type(res), res)
res = itoa(-1234)
print(type(res), res)
```

## 패턴 매칭

> [Visualizing String Matching Algorithms](http://whocouldthat.be/visualizing-string-matching/)

패턴 매칭에 사용되는 알고리즘들

- **고지식한 패턴 검색 알고리즘**

- 카프-라빈 알고리즘

- **KMP 알고리즘**

- **보이어-무어 알고리즘**

### 고지식한 알고리즘 **Brute Force** 완전 탐색

본문 문자열을 **처음부터 끝까지 차례대로 순회**하면서 패턴 내의 문자들을 **일일이 비교하는 방식**으로 동작

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

고지식한 패턴 검색 알고리즘의 **시간 복잡도**

- **최악의 경우** 시간 복잡도는 **텍스트**의 모든 위치에서 **패턴**을 비교해야 하므로 `O(MN)`이 됨

### Knuth–Morris–Pratt 알고리즘

불일치가 발생한 텍스트 스트링의 **앞 부분에 어떤 문자가** 있는지를 미리 알고 있으므로, 불일치가 발생한 **앞 부분**에 대하여 다시 비교하지 않고 **매칭을 수행**

패턴을 **전처리**하여 배열 `next[M]`을 구해서 **잘못된 시작을 최소화**함

- `next[M]`: 불일치가 발생했을 경우 이동할 다음 위치

시간 복잡도: `O(M+N)`

**패턴**의 각 위치에 대해 매칭에 실패했을 때 돌아갈 곳을 준비해 둔다.

```python
def pre_process(pattern):
    # 전처리를 위한 테이블을 작성 (Longest Prefix Suffix)
    lps = [0] * len(pattern)
    j = 0  # lps 를 만들기 위한 prefix_index
    for i in range(1, len(pattern)):
    # 0 번째 자리는 패턴 확인할 필요없음

        # prefix index 위치에 있는 문자와 비교
        if pattern[i] == pattern[j]:
            lps[i] = j + 1  # i 의 앞에 중복되는 패턴이 존재한다
            j += 1          # j 는 중복된 글자의 자리수
        else:
            j = 0

            # 여기서 0으로 이동한 다음 prefix idx 비교를 한 번 더 해야함
            if pattern[i] == pattern[j]:
                lps[i] = j + 1
                j += 1

    return lps  # -1은 의미없음. 시작이라는 의미. 0으로 표시해도 괜찮음


def KMP(text, pattern):
    lps = pre_process(pattern)  # 전처리로 lps 테이블 생성

    i = 0  # text index
    j = 0  # pattern index
    while i < len(text):
        if pattern[j] == text[i]:  # 같은 문자라면
            # 다음 문자 비교
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

        if j == len(pattern):  # pattern 이 전부 일치할 때
            return i - j       # text 의 위치

    return -1  # 일치하는 문장이 없는 경우


text = 'ABC ABCDAB ABCDABCDABDE'
pattern = 'ABCDABD'
print(KMP(text, pattern))
```

### 보이어-무어 알고리즘

오른쪽에서 왼쪽으로 비교

대부분의 상용 소프트웨어에서 채택하고 있는 알고리즘

보이어-무어 알고리즘은 패턴에 **오른쪽 끝에 있는 문자가 불일치** 하고 이 문자가 패턴 내에 존재하지 않는 경우, 이동 거리는 무려 패턴의 길이만큼이 된다.

문자열 매칭 알고리즘 비교

- 찾고자 하는 **문자열 패턴의 길이 m, 총 문자열 길이 n**

- **고지식한 패턴 검색 알고리즘**: 수행시간 `O(mn)`

- **카프-라빈 알고리즘**: 수행시간 `O(n)`

- **KMP 알고리즘**: 수행시간 `O(n)`

- 보이어-무어 알고리즘
  
  - 앞의 두 매칭 알고리즘들의 공통점 텍스트 문자열의 문자를 적어도 한번씩 훑는다는 것이다. 따라서 **최선의 경우에도 O(n)**
  
  - 보이어-무어 알고리즘은 텍스트 문자를 다 보지 않아도 된다
  
  - 발상의 전환 : 패턴의 오른쪽부터 비교한다
  
  - 최악의 경우 수행시간 : `O(mn)`
  
  - **입력에 따라 다르지만 일반적으로 `O(n)`보다 시간이 덜 든다.**

```python
def pre_process(pattern):
    M = len(pattern)  # 패턴의 길이
    skip_table = dict()
    for i in range(M - 1):
        skip_table[pattern[i]] = M - i - 1
    return skip_table


def boyer_moore(text, pattern):
    skip_table = pre_process(pattern)
    M = len(pattern)
    i = 0  # text index
    while i <= len(text) - M:
        j = M - 1  # 뒤에서 비교해야 되기 때문 j를 끝에 index
        k = i + M - 1  # 비교를 시작할 위치 (현재위치 + M번째 인덱스)

        # 비교할 j가 남아있고, text 와 pattern 이 일치하면
        # 그 다음 앞에 글자를 비교하기 위해 인덱스 감소
        while j >= 0 and pattern[j] == text[k]:
            j -= 1
            k -= 1
        if j == -1:  # 일치 함
            return i
        # 일치하지 않는다면
        else:
            # i를 비교할 시작 위치를 skip table 에서 가져온다.
            i += skip_table.get(text[i + M - 1], M)
    return -1  # 일치되는 패턴이 없음


text = 'ABC ABCDAB ABCDABCDABDE'
pattern = 'ABCDABD'
print(boyer_moore(text, pattern))
```

## [참고] 문자열 암호화

**Caesar cipher 시저 암호**

- 시저 암호에서는 평문에서 사용되고 있는 **알파벳을 일정한 문자수만큼 [평행이동] 시킴으로써 암호화**를 행한다.

- 1만큼 **평행**했을 때 1을 **키값**이라 한다.

- 시저 암호문에 대한 전사공격

문자 변환표를 이용한 암호화(단일 치환 암호)

- 단순한 카이사르 암호화보다 훨씬 강력한 암호화 기법

    단일 치환 암호의 복호화

- 복호화 하기 위해서는 모든 키의 조합(key space)가 필요하다.

bit열의 암호화

- **eXclusive-OR** 배타적 논리합 연산 사용

## [참고] 문자열 압축

**Run-length encoding 알고리즘**

- 같은 값이 **몇 번 반복**되는가를 **나타냄으로써 압축**

- 이 방법은 **이미지** 파일포맷 중 **BMP 파일포맷의 압축 방법**이다.
