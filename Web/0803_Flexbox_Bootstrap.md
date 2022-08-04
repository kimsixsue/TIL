# Flexbox / Bootstrap

## CSS Layout

- CSS layout techniques
  
  - Display, Position, **Float, Flexbox, Grid**, **Responsive Web Design, Media Queries**

### Float

- CSS 원칙
  
  - Normal Flow: 모든 요소는 **네모**(**박스모델**)이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 **쌓인다**. (**좌측 상단에 배치**)
  
  - 어떤 요소를 감싸는 형태로 배치는? 혹은 좌/우측에 배치는?

- Float
  
  - 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 **인라인요소들이 주변을 wrapping 하도록 함**
  
  - **요소가 Normal flow를 벗어나도록 함**

- Float 속성
  
  - none: 기본값
  
  - left: 요소를 왼쪽으로 띄움
  
  - right: 요소를 오른쪽으로 띄움

--- 

### Flexbox

- CSS Flexible Box Layout
  
  - 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
  
  - **축**
    
    - **main axis (메인 축)**
    
    - **cross axis (교차 축)**
  
  - Flexbox 구성 요소
    
    - **Flex** Container (**부모 요소**)
      
      - flexbox 레이아웃을 형성하는 가장 기본적인 모델
      - Flex Item들이 놓여있는 영역
      - **display** 속성을 **flex** 또는 **inline-flex**로 지정
    
    - Flex Item (**자식 요소**)
      
      - 컨테이너에 속해 있는 컨텐츠(박스)
  
  - Flexbox 축
    
    - flex-direction: row
  
  - 왜 Flexbox를 사용해야 할까?
    
    - 이전까지 Normal Flow를 벗어나는 수단은 Float 혹은 Position
    
    - 하기 어려웠던 것?
      
      - (수동 값 부여 없이)
        
        1. 수직 정렬
        
        2. 아이템의 너비와 높이 혹은 간격을 동일하게 배치

- Flexbox 시작
  
  - 부모 요소에 **display**: **flex** 혹은 **inline-flex**

- Flex 속성
  
  - 배치 설정
    
    - **flex-direction**
      
      - Main axis 기준 방향을 설정
      
      - 역방향의 경우 **HTML 태그 선언 순서와 시각적으로 다르니 유의** (웹 접근성에 영향)
      
      - row, row-reverse, column, column-reverse
    
    - flex-wrap
      
      - 요소들이 강제로 한 줄에 배치 되게 할 것인지 여부 설정
      
      - 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정
      
      - 즉, **기본적**으로 컨테이너 영역을 벗어나지 않도록 함
        
        - nowrap(기본 값): 한 줄에 배치
        
        - **wrap**: 넘치면 그 다음 줄로 배치
    
    - flex-flow
      
      - flex-direction과 flex-wrap의 shorthand
      
      - flex-direction과 flex-wrap에 대한 설정 값을 차례로 작성
      
      - 예시) flex-flow: row nowrap;
  
  - 공간 나누기
    
    - **justify-content** (**main axis**)
      
      - **Main axis**를 기준으로 공간 배분
    
    - **align-content** (**cross axis**)
      
      - **Cross** axis를 기준으로 공간 배분(아이템이 한 줄로 배치되는 경우 확인할 수 없음)
    
    - 공간 배분
      
      - flex-start(기본 값): 아이템들을 axis 시작점으로
      
      - flex-end: 아이템들을 axis 끝 쪽으로
      
      - **center**: 아이템들을 axis 중앙으로
      
      - **space-between**: 아이템 사이의 간격을 균일하게 분배
      
      - space-**around**: 아이템을 둘러싼 영역을 균일하게 분배 (가질 수 있는 영역을 반으로 나눠서 양쪽에)
      
      - space-**evenly**: 전체 영역에서 아이템 간 간격을 균일하게 분배
  
  - 정렬
    
    - **align-items**
      
      - 모든 아이템을 **Cross axis**를 기준으로 정렬
      
      - baseline: 텍스트 baseline에 기준선을 맞춤
    
    - align-self
      
      - 개별 아이템을 Cross axis 기준으로 정렬
        
        - 주의! 해당 속성은 컨테이너에 적용하는 것이 아니라 개별 아이템에 적용
    
    - Cross axis를 중심으로
      
      - stretch (기본 값): 컨테이너를 가득 채움
      - flex-start: 위
      - flex-end: 아래
      - center: 가운데
  
  - 기타 속성
    
    - flex-grow: **남은 영역을 아이템에 분배**
    
    - order: 배치 순서 

## [Bootstrap v5.2](https://getbootstrap.com/docs/5.2/getting-started/introduction/)

- Quickly, responsive, the world's most popular, responsive grid system, prebuilt components

- The world most popular front-end open source

- CDN
  
  - Content Delivery(distribution) Network
  
  - 컨텐츠(CSS, JS Image, Text 등)을 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템.
  
  - 개별 end-user의 가까운 서버를 통해 빠르게 전달 가능(지리적 이점)
  
  - 외부 서버를 활용함으로써 본인 서버의 부하가 적어짐

### Bootstrap 기본 원리

#### [Spacing](https://getbootstrap.com/docs/5.2/utilities/spacing/)

- spacing (Margin and padding)

- {property}{sides}-{size}
  
  ```html
    <div class="mt-3 ms-5">bootstrap-spacing</div>
  ```

- where *property* is one of:
  
  - m - for classes that set margin
  
  - p - for classes that set padding

- where *sides* is one of:
  
  - t - for classes that set margin-top or padding-top
  
  - b - for classes that set margin-bottom or padding-bottom
  
  - s - (start) for classes that set margin-left or padding-left in LTR, margin-right or padding-right in RTL
  
  - e - (end) for classes that set margin-right or padding-right in LTR, margin-left or padding-left in RTL
  
  - x - for classes that set both `*-left` and `*-right`
  
  - y - for classes that set both `*-top` and `*-bottom`
  
  - blank - for classes that set a margin or padding on all 4 sides of the element

- where *size* is one of:
  
  - 0 - for classes that eliminate the margin or pading by setting it to 0
  
  - 1 - (by default) for classes that set the margin or padding to `$spacer * .25`
  
  - 2 - (by default) for classes that set the margin or padding to `$spacer * .5`
  
  - 3 - (by default) for classes that set the margin or padding to `$spacer`
  
  - 4 - (by default) for classes that set the margin or padding to `$spacer * 1.5`
  
  - 5 - (by default) for classes that set the margin or padding to `$spacer * 3`
  
  - auto - for classes that set the margin to auto

- 브라우저 <html>의 root 글꼴 크기는 16px
  
  | class name | rem  | px  |
  |:----------:|:---- |:---:|
  | m-1        | 0.25 | 4   |
  | m-2        | 0.5  | 8   |
  | m-3        | 1    | 16  |
  | m-4        | 1.5  | 24  |
  | m-5        | 3    | 48  |

#### 기타

- [Color](https://getbootstrap.com/docs/5.2/customize/color/), [Text](https://getbootstrap.com/docs/5.2/utilities/text/), [Display](https://getbootstrap.com/docs/5.2/utilities/display/), [Position](https://getbootstrap.com/docs/5.2/utilities/position/)

### Boostrap 컴포넌트

- Components
  
  - Bootstrap의 다양한 UI 요소를 활용할 수 있음
  
  - 아래 Components 탭 및 검색으로 원하는 UI 요소를 찾을 수 있음
  
  - 기본 제공된 Components를 변환해서 활용
  
  - [Form controls](https://getbootstrap.com/docs/5.2/forms/form-control/)
    
    - form-control 클래스를 사용해 \<input> 및 \<form> 태그를 스타일링할 수 있습니다.
  
  - [Buttons](https://getbootstrap.com/docs/5.2/components/buttons/)
    
    - 클릭 했을 때 어떤 동작이 일어나도록 하는 요소
  
  - [Cards](https://getbootstrap.com/docs/5.2/components/card/#grid-cards)
    
    - 화면이 작아지면 1줄에 표시되는 카드의 개수가 줄어듬
  
  - [Carousel](https://getbootstrap.com/docs/5.2/components/carousel/)
    
    - 콘텐츠(사진)을 순환시키기 위한 슬라이드쇼
  
  - [Dropdowns](https://getbootstrap.com/docs/5.2/components/dropdowns/)
    
    - dropdown, dropdown-menu, dropdown-item 클래스를 활용해 옵션 메뉴를 만들 수 있습니다.
  
  - [Modal](https://getbootstrap.com/docs/5.2/components/modal/)
    
    - 사용자와 상호작용 하기 위해서 사용하며, 긴급 상황을 알리는 데 주로 사용
    
    - 현재 열려 있는 페이지 위에 또 다른 레이어를 띄움
    
    - 페이지를 이동하면 자연스럽게 사라짐(제거를 하지 않고도 배경 클릭시 사라짐)
  
  - [Navbar](https://getbootstrap.com/docs/5.2/components/navbar/)
    
    - navbar 클래스르 활용하면 네비게이션 바를 제작할 수 있습니다.

- Flexbox in Bootstrap

- **Responsive Web Design**
  
  - 다양한 화면 크기를 가진 디바이스들이 등장함에 따라 responsive web 개념이 등장
  
  - 반응형 웹은 별도의 기술 이름이 아닌 웹 디자인에 대한 접근 방식, 반응형 레이아웃 작성에 도움이 되는 사례들의 모음 등을 기술하는데 사용되는 용어
  
  - 예시
    
    - Media Queries, Flexbox, Bootstrap Grid System, The viewport meta tag

### Bootstrap Grid System

- **Grid system (web design)**
  
  - 요소들의 디자인과 배치에 도움을 주는 시스템
  
  - 기본 요소
    
    - Column: 실제 컨텐츠를 포함하는 부분
    
    - Gutter: 칼럼과 칼럼 사이의 공간 (사이 간격)
    
    - Container: Column들을 담고 있는 공간
  
  - [Grid system](https://getbootstrap.com/docs/5.2/layout/grid/)
    
    - Bootstrap Grid system은 flexbox로 제작됨
    
    - container, **rows, column**으로 컨텐츠를 배치하고 정렬
    
    - 반드시 기억해야 할 2가지 !
      
      - **12개의 column**
      
      - **6개의 grid system breakpoints**
        
        - sm, md, lg, xl, xxl
