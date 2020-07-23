# 함수

#### 1. 함수를 사용하는 이유

* 한 번 정의하면 이후에는 재활용해서 사용가능.
* 코드의 짜임새가 좋아지고, 간결하게 표현가능.



#### 2. 함수의 기본특징

* return

  input을 가공한 결과로 함수 밖에서 활용하기 위해 내보내는 역할

  return시 함수는 즉시 종료됨.

* parameter(매개변수) 

  함수에 들어올 값을 받는 변수

* argument(인자)

  함수의 input으로 들어오는 값



#### 3. 함수 호출

* 정의한 함수의 이름과 함수에 필요한 input값을 같이 넣어주는 형태로 호출
* 내장함수: dir(____builtins__)



#### 4. 일급객체(first class object)

* 3가지 조건

  * 변수에 담을 수 있다
  * 인자로 전달가능
  * 반환값으로 전달가능

  ```
  def first():
  	return 3
  	
  def second():
  	return first()
  	
  def third(func):
  	return func()
  	
  sample = second()
  third(sample)
  ```



#### 5. 위치인자

​	매개변수가 선언된 순서대로 인자의 값이 대입되는 형태

```
def func(a, b):
	return a + b

func(3, 5)
```



#### 6. 키워드 인자

​	해당 매개변수에 직접 인자를 전달하는 형태	

```
def func(a, b):
	return a + b
	
func(a=6, b=7)
#위치인자와 같이 사용가능
func(4, b=10) #사용가능. 반대순서는 사용불가
func(a=9, 10) #사용불가. 위치인자 다음에 키워드인자적는거만 가능	
func(8, a=10) #사용불가. 이미 a가 위치인자로 전달되었는데 키워드로 다시 전달되므로 에러뜸
```



#### 7. 기본값 인자

​	매개변수에 초기값을 설정한 형태

```
def func(a, b=5):
	return a + b
	
func(3, 4) => 7
func(2) => 7
```



#### 8. 가변인자

* 입력되는 인자의 개수가 정해져 있지 않을 때 사용

* tuple형태로 저장됨.

* 매개변수 앞에 *를 붙여주는 형태로 가변인자를 받을 수 있음.

  ```
  def func(*args)
  	print(type(args)) #tuple
  	print(args) #(인자1, 인자2, 인자3...)
  ```



#### 9. 정의되지 않은 키워드인자

* 입력되는 키워드가 다양할 때 주로 사용.

* dict형태로 저장됨

* 매개변수 앞에 **를 붙여주는 형태로 가변인자를 받을 수 있음.

  ```
  def func(**kwargs):
  	print(type(kwargs)) #dict
      print(kwargs) #{key:value, key:value,,,}
  ```



#### 10. 이름공간(name space)★★★★★★★

* 우리집 중2 히키코모리 동생

* LEGB

  L(Local) - 정의된 함수 내부

  E(Enclosed) - 함수 내부에 다시 함수가 정의되어있을 때 내부함수(local)의 바깥쪽 함수(enclosed)

  G(global) - 함수밖의 변수

  E(built-in) - 파이썬이 제공하는 변수나 함수. 내장.



#### 11. 재귀함수

* 함수가 함수 자신을 내부에서 호출하는 형태

* 작고 반복적인 문제로 나눌 수 있는 문제를 해결하기 위해 사용

* 재귀함수는 메모리를 많이 사용하므로 신중하게 사용해야 함. (공간복잡도 상승)

  ```
  K = K(n-1) + K(n-2)
  
  def fib(n):
  	if n > 2:
  		return fib(n-1) + fib(n-2)
  	else:
  		return n
  
  fib(5)
  ```

  