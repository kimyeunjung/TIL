# 데이터 구조 1



## 예외처리

* 문법 에러: 문법적 오류가 있을 때

* exception

  * NameError
  * TypeError: 문법오류 (iterable)
  * ValueError: 값이 적절하지 않을 때 ex)int('3.5')=>float을 형변환시키려고 함. 실수로 형변환 후 int해야함
  * ZeroDivisionError:0으로나누려고 할때
  * IndexError
  * KeyError
  * ModuleError- 외장모듈이름을 잘못쓰거나, 설치필요한 모듈일 때
  * ImportError- 모듈을 불러오는 것을 실패했을 때(보통 오타)

* 예외처리

  * try & except

    ```python
    try:
    	코드블럭1(오류가 난 코드)
    except 예외1:
    	코드블럭2
    except 예외2, 예외3:(두개동시에 묶어서 해도 가능)
    	코드블럭3
    except 예외4 as err:
    	print(f'{err}로 에러메시지를 프린트할 수 있다)
    else: #코드블럭1에서 에러가 발생하지 않았을 때만 실행가능
    	코드블럭4
    finally: #반드시 실행해야하는 코드를 선언.
    	코드블럭5
    ```

* 예외발생

  * raise: 예외를 강제로 발생 ex) raise ValueError('숫자를 입력하시오')

  * assert: 예외를 강제로 발생

    * 상태를 주로 검증하기 위해 `assert Boolean expression, error message`

      `assert type(x) == int`, '숫자항이 아닙니다.'

      

## 데이터 구조

> * 데이터구조란?
>
>   데이터에 편리하게 접근하고 그 값을 편리하게 변경하기 위해 데이터를 저장하거나 조작하는 방법
>
> * 순서가 있는 구조(ordered)
>
>   * 문자열, 리스트
>
> * 순서가 없는 구조(inordered)
>
>   * set, dictionary

	#### 문자열

* 변경할 수 없다(`immutable`)

* 순서가 있다, 순회가능(`ordered, iterable`)

* String Method

  * 값을 변경하는 method

    * repalce(바꿀 문자열) old, 바꾸려는 문자열(new)count)

      ``` python
      'yay!'.replace('a', '-') #'y-y!'
      'wooooo'.replace('o', '!', 3) #'w!!!oo'
      ```

    * strip([char])

      * 특정문자를 지정하면 해당 문자를 양쪽에서 찾아서 제거한다.
      * strip 해당문자를 왼쪽에서 찾아서 제거/ rstrip

    * split([char])★★★많이 사용

      * 문자열을 특정 단위로 나누어서 리스트로 반환

        ```python
        input = '1 2 3 4 5'
        li_input = input.split() #=>{'1', '2', '3', '4', '5'}
        
        a = 'a_b_c'
        print(a.split('_')) #=>['a', 'b', 'c']
        print(a.split('b')) #=>['a_', 'c_']
        ```

    * join(iterable)★★★많이사용

      * 특정문자열로 만들어서 반환

        ```python
        word = '배고파'
        a = '!'.join(word) #=>'배!고!파'
        words = ['a', 'b', 'c']
        b = '_'.join(words) #=>'a_b_c'
        ```

  * 문자변경

    * capitalize()
    * title()
    * upper()
    * lower()
    * swapcase()대소문자 서로 바꿔줌

  * 문자열 관련 검증

    * istitle()
    * isalpha() 해당 문자열이 알파벳으로 이뤄져있는지
    * isupper()
    * islower()
    * isdecimal() 순수int로 형변환이 가능한 문자열인지
    * isdigit() 윗 첨자도 순자로 인식(제곱같은거)
    * isnumeric() 분수의 특수기호, 특수 로마자도 숫자로 인식
      * 주의: 해당 decimal, digit, numeric은 float형태의 문자열은 false로 반환

  * 기타 문자열 관련 메소드

    `dir('string')`

#### 리스트

* 변경가능(`mutable`)

* 순서있고 순회가능(`ordered, iterable`)

* List Method

  * 값을 추가 및 삭제

    * append(x) 있는 그대로 값을 붙임
    * extend(iterable한 객체) literable한 요소를 분리해서 값을 붙임
    * insert(i, x) 정해진 위치에 x를 추가가능. i값이 리스트를 넘을 만큼 숫자가 크면, 리스트의 끝에 x가 붙음
    * remove(x) 리스트안의 처음x만 삭제. 지우려는 값이 없다면 IndexError발생
    * pop(i) 해당 위치(i)에 있는 값을 삭제하고 그 값을 반환.
    * clear()

  * 탐색 및 정렬

    * index(x) 가장 처음 위치에 있는 x를 찾아서 반환. 그 값이 없으면 Error발생.

    * count(x) 리스트에서 x의 개수를 세고 반환.

    * sort():None을 반환. 그리고 원본을 변경(사용시 주의!!!)`sort(reverse=False)`. ★★★★★★

      * sorted(iterable[, reverse=True]): 정렬된 값을 반환.원본유지★★★★★★

    * reverse(): 정렬없이 앞뒤를 뒤집어준다.

      ```python
      s = 'abcde'
      s_list = list(s)
      s_list.reverse()
      
      print(''.join(s_list))
      ```

      

      * reversed(): 앞뒤를 뒤집어 주지만, `list_reverseiterator object` 반환

        ```python
        s = 'abcde'
        print(''.join(reversed(s)))
        >>> edcba
        ```

        

  * 리스트복사

    ```python
    a = [1, 2, 3]
    b = a
    b[0] = 10
    print(a) #=> [10, 2, 3]
    ```

    * slicing활용하여 복사

      ```python
      a = [[1, 2], [3, 4]]
      b = a[:]
      
      a[0] = [4, 5]
      print(b)
      ```

    * list() 메서드를 활용해서 복사

      ```python
      a = [1, 2, 3]
      b = list(a)
      
      b[1] = 200
      print(a)
      ```

    * copy 모듈을 활용

      ```python
      import copy
      
      a = [1, 2, 3]
      b = copy.copy(a)
      ```

      * deepcopy

    ```python
    a = [1, 2, [1, 2]]
    b = copy.deepcopy(a)
    ```

  * 데이터 분류

    * immutable

      * number, string bool, range, tuple, frozenset

    * mutable

      * list, set, dictionary

      ```python
      def pos_num(num):
      	if num > 0:
      		return num
      	else:
      		return false
      		
      numbers = list(range(-10, 10))
      pos = list(filter(pos_num, numbers)) #=> [1, 2, ,,,9] 
      ```

* Built-in Function

  * map(function, iterable)

    * iterable한 데이터를 인자로 받아 모든 요소에 function을 적용한 후 결과를 map object로 반환

      ```python
      def square(num):
          return num ** 2
      numbers = [1, 2, 3, 4, 5]
      double_li = list(map(square, numbers))
      print(double_li)
      input = '1 2 3 4 5'
      list(map(int, input().split()))
      ```

  * filter(function, iterable)

    * function의 return값이 True인 값만 추출

      ```python
      def pos_num(num):
          if num > 0:
              return num #음수일 경우 Nonetype반환 ->암시적 형변환 False
      numbers = list(range(-10, 10))
      pos = filter(pos_num, numbers) #[1, 2, 3,,,9]
      ```

  * zip(*iterable)

    * 복수의 iterable한 객체를 모아준다. tuple 모음으로 구성된 zip object를 반환.

      ```python
      girls = ['jane', 'iu', 'mary']
      boys = ['justin', 'david', 'kim']
      ranking = [1, 2, 3]
      couples = list(zip(girls, boys)) 
      #=> [('jane', 'justin', 1),('iu', 'david', 2) ('mary, 'kim', 3)]
      ```

    * 되도록이면 길이가 같은 객체를 사용하는 것이 좋다

    * 길이가 다르다면 짧은 객체를 기준으로 합쳐주고 나머지는 무시된다.

    * `itertools` 내장모듈안에 `zip_longest`함수를 사용하면 긴 것을 기준으로 합쳐준다

      ```python
      from itertools import zip_longest
      num1 = [1, 2]
      num2 = [4, 5, 6]
      zip(num1, num2) #=> [(1, 4), (2, 5)]
      list(zip_longest(num1, num2, fillvalue=0)) #=>[(1, 4), (2, 5), (0, 6)]
      ```

      

# 데이터 구조2

### 세트(set)

* 변경가능하고 순서없고 순회가능
* 집합요소는 유니크하다. 중복불가능
* 집합요소는  immutable한 값만 가능. mutable객체를 넣으면 TypeError발생
* Set Methods
  * 추가 및 삭제
    * add(elem) : 값을 하나 추가시킬 때 사용.
    * update(*others): 여러 개의 값을 넣을 때 사용.
    * remove(elem): 값을 삭제하고, 만약 값이 없으면 KeyError발생.
    * discard(elem): 값을 삭제하고, 만약 값이 없으면 에러발생하지않음.
    * pop(): 임의의 요소를 제거하고 그 값을 반환.



### 딕셔너리

* 변경가능 순서없고 순회가능

* dictionary Methods

  * get(key[, default]) 디폴트값 설정안하면 None을 반환

    * key를 통해서 해당 value를 가져온다.

      ```
      dic['key']: 키값을 직접 넣어서 값을 가져올 때, 키가 없으면 KeyError발생
      ```

    * key가 없어도 에러를 발생하지않음.

  * pop(key[, default])

    * key가 있으면 dictionary에서 제거하고, 키가 없으면 default값을 반환.
    * default가 없으면 keyerror발생.

  * update()

    * 1개 이상으 ㅣ값을 `key='value'`의 형식으로 값을 추가할 수 있다.
    * key가 존재하면 그 값을 수정.
    * key가 존재하지않으면 새롭게 추가.

  * keys()

    * 해당 dictionary의 키를 리스트로 반환.`(dict_key object`)

  * values()

    * 해당 dictionary의 value를 리스트로 반환.`(dict_value object`)

  * items()

    * 해당 dictionary의 key와 value를 tuple형태로 반환`(dict_items object)`

* Dictionary 순회

  ```python
  # 1. dictionary를 for로 순회할 때
  for dic in dicts:
  	print(dic) # dicts의 키값이 들어있다.
  	
  # 2. keys로 순회했을 때.
  for dic in dicts.keys():
  	print(dic) # dicts의 키값이 들어있다.
  
  #3. value로 순회했을 때
  for val in dicts.values():
  	print(val) #dict의 value만 들어있다.
  
  #4. items로 순회했을 때
  for dic in dicts.items():
  	print(dic) #dic에는 (key, value)형태의 tuple값이 들어있다.
  	
  for key, value in dicts.items():
  	print(key)
  	print(value)
  ```



#### List Comprehension

* 간결함

* python만의 특징을 갖고있다. pythonic한 코드

* 속도 빠른 편

* 무분별하게 사용하면 가독성이 떨어진다.

  * 기본형태

  ```python
  li_comp = [식 for 임시변수 in iterable]
  li_comp2 = list(식 for 임시변수 in iterable)
  ```

  * 기본형태 + 조건식

  ```python
  li_comp3 = [식 for 임시변수 in iterable if 조건식]
  li_comp4 = [식1 if 조건식 else 식2 for 임시변수 in iterable]
  li_comp5 = [식1 if 조건식 else 식2 if 조건식2 else 식3 for 임시변수 in iterable]
  
  ```

  

