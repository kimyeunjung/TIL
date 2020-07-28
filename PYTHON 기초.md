# PYTHON 기초 

###### 2020-07-20



## 1. 기초 문법

프로그래밍은 저장과 제어로 이뤄짐

저장 - 데이터를 저장하는 방법과 무엇을 저장하는지
제어 - 단순한 명령을 복잡하게 제어하기위해 어떻게 조건을 주고 반복할지.

무엇을 - data type(자료형)

어떻게 - =( =는 저장, ==는 같다는 의미)

어디에 - variable, container(여러개의 변수를 담을 수 있다.)



### 공백

들여쓰기는 네칸!

탭과 스페이스 둘 중 하나 정해서 쓰자

```
foo = long_function_name(var_one, var_two,
                         var_three, var_four)
```

연산기호는 앞에 쓴다! 뒤에 붙이면 안돼요!

```
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

트레일링 콤마는 공백주면 안된다.

```
foo = (0,)
```

우선순위가 낮은 연산자만 띄워준다

```
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
```



### 주석

* #을 쓰면 한 줄 주석을 표현함.
* 여러 줄의 주석은
  - 한 줄 씩 #을 이용하거나
  - """ 나 '''으로 표현할 수 있다.

```
"""
이건 주석이다.
"""
```



### 코드라인

* 파이썬은 한 줄에 한 문장이 원칙.
* 여러 줄을 작성할 때는
  -  역슬래시`\`을 이용하거나
  - '''나 """을 이용한다.
* [] {} () 는  `\` 없이도 가능하다. (list이므로)

```
a = [

    1, 2, 3, 4

    5, 6, 7, 8

]
```



## 2. 변수

### 변수

* 변수는 =을 통해 할당됨.

* type()으로 데이터 타입을 확인할 수 있다.

* id()로 메모리 주소를 확인할 수 있다.

  ```
  x = 'ssafy'
  type(x)
  
  >> str
  
  id(x)
  
  >>1402097328
  ```

* 같은 값을 동시에 할당할 수 있다.

  ```
  x = y = 'ssafy'
  print(x)
  print(y)
  
  >>ssafy
    ssafy
  ```

* 다른 값을 동시에 할당할 수 있다.

  ```
  a, b = 2020, 4
  print(a)
  print(b)
  
  >>2020
    4
  ```

* 변수와 값은 개수가 같아야 한다.

* 서로 값을 바꿀 수 있다.

  ```
  a, b = 1, 2
  print(a)
  print(b)
  >>1
    2
  a, b = b, a
  print(a)
  print(b)
  >>2
    1
  
  예외
  (a, b) = (b, a)
  print(a)
  print(b)
  >>1
    2
  ```

  

### 식별자

변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름.

* 첫 글자에 숫자가 올 수 없다.

* 대소문자 구별한다.

* 예약어는 사용할 수 없다. (어떤 단어를 적었을 때, 초록색으로 바뀌면 그냥 쓰지마라!)
  확인하는 방법은 
  
  ```
  import keyword
  print(keyword.kwlist)
  ```
  
* 내장함수는 모듈 등의 이름으로도 만들면 안된다.

  ```
  print = 'a'
  print(print)
  >>심각한 오류!!! 이를 없애기 위해서는
  
  del print
  >>위에 생성했던 print를 삭제해준다.
  ```



## 3. 데이터 타입

### 숫자

* 모든 정수는 int로 표현됨.
* 실수는 float로 표현됨.
  - 실수의 연산은 주의해야 할 점이 있다.

```
3.5 + 3.2
>> 6.7

3.5 - 3.2
>> 0.2999999999    덧셈과 다르게 근사값으로 출력된다.

a = 3.5 - 3.2
b = 0.3
a == b
>> false

이를 해결하기 위한 방법은 epsilon사용(부동소수점 연산에서 반올림함으로써 발생하는 오차상환)
import sys
print(sys.float_info.epsilon)

abs(a - b) <= sys.float_info.epsilon

또는 math모듈을 사용한다.
import math
math.isclose(a, b)
```

* 복소수는 complex로 표현됨.

  

### 문자

* 문자열은 기본적으로  str로 입력된다.

  ```
  number = input('숫자를 입력해주세요: ')
  print(int(number) * 3)
  #글자를 숫자로 바꾸고 싶을 때는 int로 형변환을 해주면 됨. 반대도 마찬가지
  ```

* 문자열 안에 문장부호(`'`, `"`)가 사용될 경우 이스케이프 문자(`\`)를 활용한다.

  ```
  "he's cool"
  "그의 이름은 \"김영철\"이다"
  
  >> '그의 이름은 "김영철"이다'
  ```

* 여러줄에 걸쳐있는 문장은 """을 사용한다

  ```
  print("""
  이건
   여러줄에 걸친
   문자열이다
   """)
   >>>이건
   여러줄에 걸친
   문자열이다
  ```

* 문자열은 +로 이어붙이고, *로 반복시킬 수 있다.

  ```
  'go' + 'swim'
  >> 'goswim'
  
  'go' * 3
  >> 'gogogo'
  ```

* 변수화해서 사용할 수 있다.

  ```
  name = 'john'
  'my name is ' + name
  >> 'my name is john'
  ```

* 이스케이프 시퀀

| <center>예약문자</center> |    내용(의미)     |
| :-----------------------: | :---------------: |
|            \n             |      줄 바꿈      |
|            \t             |        탭         |
|            \r             |    캐리지리턴     |
|            \0             |     널(Null)      |
|           \\\\            |        `\`        |
|            \\'            | 단일인용부호(`'`) |
|            \\"            | 이중인용부호(`"`) |

* String Interpolation

  - str.format()

    ```
    name = john
    print("내 이름은 {}입니다.".format(name))
    >>내 이름은 john입니다.
    ```

  - f-strings

    ```
    print(f'내 이름은 {name}입니다')
    >>내 이름은 john입니다.
    ```

    ```
    다양한 형식을 지정할 수 있다.
    import datetime
    now = datetime.datetime.now()
    print(now)
    
    f'오늘은 {now:%Y}년 {now:%m}월 {now:%d}일'
    >>오늘을 2020년 07월 20일
    ```

    