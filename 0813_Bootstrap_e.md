# Float

* 한 요소(element)가 정상흐름(normal flow)으로 부터 빠져서 텍스트 및 인라인 요소가 그 주위를 감사도록 컨테이너 좌, 우측을 따라 배치되어야 함을 지정함.
* clear
  * 선행 floating요소가 그 아래로 내려가야 하는지(normal flow)를 지정할 때 사용되는 속성
* flex box 및 grid layout과 같은 기술 전에 float은 열 레이아웃을 만드는데 사용됨.
* mdn에서는 더 새롭게 나온 레이아웃 기술(flex, gird)이 나와서 현재 레거시한 레이아웃 기술로 분류.
* 결국 텍스트 블록 내에서 이미지를 위한 역할로 쓰임.(but, 네이버에서는 여전히  float사용 중.)



# Flex(Flexible box module)

* flex 인터페이스 내의 아이템 간 공간배분과 정렬기능을 제공하기 위한 1차원 레이아웃모델.
* 축
  * justify: main축을 담당(default: 좌 -> 우)
  * align: cross축을 담당
  * content: 여러 줄 설정
  * items: 한 줄 설정
  * self: 개별요소 설정
* display: Flex
  * __정렬하려는 부모 요소에 선언__
  * inline-flex
* flex-direction: 쌓이는 방향결정
  * row(기본 값): 좌 -> 우
  * row-reverse: 우 -> 좌
  * column: 위 -> 아래
  * column-reverse: 아래 -> 위
* justify content: 메인 방향축 요소들을 어떻게 배치할지 설정.
  * flex-start(기본값) : 좌상부터 차례로 배치됨
  * flex-end: 끝나는 점부터 배치.(아이템 순서는 그대로, 정렬만 우측부터 시작)
  * center: 메인축 정중앙
  * space-between: 좌우 정렬(양 끝 아이템은 양 끝에 배치 후 균등하게 아이템을 위치시킴.)
  * space-around: 아이템 좌우에 동일한 공간을 부여함
  * space-evenly: 모든 공간이 균등하게 정렬.
* align-items: cross축 요소를 어떻게 배치할지 결정.
  * 기본값: stretch-공간을 아이템으로 가득 채움
  * flex start, flex end, center
  * baseline: item내부의 text밑을 기준선으로 맞춤.
* align-self: cross축 각 개별 아이템을 어떻게 배치할 지 결정.
  * 설정 값은 위와 동일(기본값: auto)
* order: 정렬
  * 모든 아이템의 기본값은 0이다.
  * 작은 숫자일수록 앞에 배치됨.
* flex-grow: 메인 축에서 남는 공간을 각 항목에 분배하는 정렬
  * 각 아이템에 값을 줘서 그 공간만큼 할당함.
  * 각 아이템의 비율을 설정하는게 아님. 즉, 음수불가능



# Bootstrap

* 트위터가 만든 오픈소스 프론트엔드 라이브러리
* 웹페이지에서 사용되는 많은 요소를 내장하고 있음.
* 장점
  * 디자인 할 시간을 줄여주고
  * 여러 브라우저를 지원하기 위한 크로스 브라우징에 골머리를 썩일 필요없음.
  * 웹 브라우저 크기에 따라 자동 정렬되는 '그리드 시스템'
* 반응형 웹 디자인
* Grid system
  * flex box를 기반으로 12개의 column시스템을 가짐.
  *  12의 약수 개수가 많아서, 사용하는 경우의 수를 많이 고려할 수 있다.
  * container> row > col
  * sm(576px) - md(768px) - lg(992px) - xl(1200px)