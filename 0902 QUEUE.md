# 0902 QUEUE

#### 우선순위 큐

* 우선순위를 가진 항목들을 저장하는 큐
* FIFO순서가 아니라 우선순위가 높은 순대로 먼저 나간다
* 시뮬레이션시스템, 네트워크트래픽제어, 운영체제의 테스크 스케줄링에 적용됨



#### ★★★BFS★★★

```
그래프: 비선형구조
-표현방법: 인접행렬, 인접리스트
-순회: DFS, BFS
```

* 그래프 너비우선탐색
* 탐색 시작점의 인접정점들을 먼저 모두 차례로 방문하고, 방문했던 정점을 시작으로 하여 다시 인접정점들을 차례로 방문하는 방식
* 인접정점들에 대해 탐색 한 후, 차례로 다시 너비우선탐색을 진행해야하므로, 선입선출 형태의 자료구조인 큐를 활용함.



__ 같은 그래프를 다른 방법으로 탐색_

	##### DFS

![image-20200902142750493](C:\Users\kimyeunjung\AppData\Roaming\Typora\typora-user-images\image-20200902142750493.png)

##### BFS

ABCDEFGHI순서로 탐색



* BFS알고리즘

  ![image-20200902142950840](C:\Users\kimyeunjung\AppData\Roaming\Typora\typora-user-images\image-20200902142950840.png)

  

![image-20200902155440030](C:\Users\kimyeunjung\AppData\Roaming\Typora\typora-user-images\image-20200902155440030.png)