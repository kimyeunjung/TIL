# Error_Exception



syntax error

EOL(end of line) - 따옴표오류

EOF(end of file) - 괄호 오류 



exception error

NameError

TypeError - 동일한 타입이 아닐 경우

ValueError - 자료형

​	함수의 값

```
int('3.5')#=>float값을 int()에 넣어서 오류남.
```



​	존재하지않는 값을 찾고자 할 경우

```
numbers = [1, 2]
numbers.index(3)
```

IndexError

존재하지 않는 인덱스로 조회할 경우

```
empty_list = []
empty_list[-1]
```



KeyError

딕셔너리에서 key가 없는 경우

```
songs = {'sia': 'candy cane lane'}
songs['queen']
```



ModuleNotFoundError

존재하지 않는 모듈 찾는 경우

```
import reque
```



ImportError

```
from random import sampl
```



KeyboardInterrupt

```

```



예외처리

문법

try:

​	코드블럭

except:

​	코드블럭



![image-20200727100904677](C:\Users\kimyeunjung\AppData\Roaming\Typora\typora-user-images\image-20200727100904677.png)



### as

![image-20200727101447631](C:\Users\kimyeunjung\AppData\Roaming\Typora\typora-user-images\image-20200727101447631.png)



### 복수에러

```
try:
	코드블럭
except (예외1, 예외2):
	코드블럭
	
try:
	코드블럭
except 예외1:
	코드블럭
except 예외2:
	코드블럭
```

단, 에러가 순차적으로 진행되므로, 가장 작은 범주부터 시작해야함

![image-20200727102312899](C:\Users\kimyeunjung\AppData\Roaming\Typora\typora-user-images\image-20200727102312899.png)

### else

에러가 발생하지 않는 경우 실행 시킬 문장은 `else`를 활용한다.

```
try:
    numbers = [1, 2, 3]
    number = numbers[2]
except IndexError:
    print('오류 발생')
else:
    print(number)
   
>>>3
```



### finally

어떤 경우에든 반드시 실행해야하는 코드에는 `finally`를 활용한다.

```
try:
    languages = {'python': 'good'}
    languages['java']
except KeyError as err:
    print(f'{err}는 딕셔너리에 없는 키입니다.')
finally:
    print('감사')
    
>>>>
'java'는 딕셔너리에 없는 키입니다.
감사
```



## 예외 발생시키기(의도적으로 발생시킴)

### raise

```
raise
>>>RuntimeError
```

```
raise NameError('이름없다')
>>>NameError:이름없다
```

