### Asythronous

1. 비동기: 기다리지않음
2. Single Thread: 혼자서 일함.
3. Event Loop: 일하는 방식.



### Promise

* then, catch를 개선시켜서 나온 것이 __async/await__



### Axios(엑시오스)

* Promise를 기반으로 request를 날림



### 동기와 비동기

* 동기: 기다려준다.
  * 언제 동작이 완료되는지 알 수 없는 응답을 받는 일이 있을 때 다른 작업을 수행하지 못하고 멈춘 채로 해당 응답을 받을 때까지 기다리게 된다.
* 비동기: 기다려주지않는다
  * 언제 동작이 완료되는지 알 수 없는 응답을 받을 때 응답을 기다리지 않고 다른 작업을 진행한다

----

### Like 흐름

* 시작점, 이벤트리스너 달기
  * querySelectAll
* axios요청
  * get시작해서 post로 요청완성
  * 각각의 form을 특정하기 위해서 article.pk로 dataset을 설정함
  * csrf token
* django응답을 수정
* .then으로 받아서
  * 하트변경
    * dataset으로 각각의 하트의 형태를 변경
  * 숫자도 변경

