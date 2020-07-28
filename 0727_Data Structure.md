#  데이터 구조(Data Structure)

> string
>
> list

input을 하면 return이 되는지, output이 되는지

immutabel/ordered=literable 여부



## 문자열

### 조회/탐색

####  .find(x)

x의 **첫 번째 위치**를 반환합니다. 없으면, `-1`을 반환합니다.

```
'apple'.find('f')
>>> -1
```



#### .index(x)

x의 **첫번째 위치**를 반환합니다. 없으면, 오류가 발생합니다.

```
'apple'.index('k')
>>>Value Error
```



### 값 변경

#### .replace(old, new[, count])

#### .strip([chars])

#### .split()

#### `'separator'.join(iterable)`



## 리스트

변경 가능하고(mutable), 순서가 있고(ordered), 순회 가능한(iterable)

원본변경하는지 return값이 none

 안하는지 return값이 변경된 데이터

#### `.append(x)`

`.extend(iterable)`

#### `.insert(i, x)`

그 밑 개별학습(원본변경유무, 리턴되는지유무)



### 리스트 복사

복사를 해도  [3, 2]를 가리킨다는 개념이므로 [3,2]를 수정하면 원본과 복사본 둘 다 바껴진다.

![image-20200727112640023](C:\Users\kimyeunjung\AppData\Roaming\Typora\typora-user-images\image-20200727112640023.png)



## List Comprehension

표현식과 제어문을 통해 리스트를 생성합니다.

여러 줄의 코드를 한 줄로 줄일 수 있습니다.

```
[식 for 변수 in iterable]

list(식 for 변수 in iterable)
```



## 데이터구조에 적용가능한 Built-in Function

순회가능한(iterable) 데이터 구조에 적용가능한 Built-in Function

> iterable 타입 - `list`, `dict`, `set`, `str`, `bytes`, `tuple`, `range`

- `map()`
- `filter()`
- `zip()`
- ~~`reduce()`~~ ([참고](https://docs.python.org/ko/3/library/functools.html#functools.reduce))



#### `map(function, iterable)`

- 순회가능한 데이터 구조(iterable)의 모든 요소에 function을 적용한 후 그 결과를 돌려준다.

- return은 `map_object` 형태이다.



## 세트

순서가 없다

