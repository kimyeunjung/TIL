* 강의 순서

```
장고설치

장고pjt 생성

서버켜서 로켓페이지확인

장고 앱 생성-> 앱을 pjt에 등록

urls -> view.py -> templates
```



* 기타

```
views.py - MTV중 V를 담당함.

ctrl+c는 터미널에서 서버를 끄게만드는 단축키

장고에서 url을 입력할 때, url/로 적어줘야함

함수와 함수사이에는 두 줄의 공백이 있어야함.

```



* 앱

1.app 생성(터미널에 startapp으로 만들기)

2.app 등록(settings.py에 등록)

settings.py에서 

INSTALLED_APPS = [ 작성하는 순서.

  *#1. local apps*

  'articles',

  *# 2. 3rd party apps*

  *# 3. django apps*

파일이름,

]      ###마지막요소에 ,를 적어준다.





* view함수는 첫번째 인자로 반드시 request를 받아야함.

```python
def 함수(request):
    pass
```

사용자의 요청

그 요청에 대한 path를 url로 작성

어떤 뷰함수를 호출할건지 뷰함수 작성

뷰함수가 리턴할 템플릿 작성

리퀘스트랑 템플릿을 잘 해서 http응답으로 넘어감



* 코드작성순서(=데이터의 흐름)
  1. urls.py
  2. views.py
  3. templates

* django import style guide
  	1. standard library(import random 같은것)
   	2. 3rd party
   	3. django(from django.shortcuts import render 같은 것)
   	4. local django



# Django

* 장고설치

  ```
  pip install django
  
  #특정버전으로 받고싶다?
  pip install django==3.3
  ```

  pip list(설치확인)

  django-admin startproject first_project(프로젝트생성.디장고어드민은 처음 프로젝트만들때만 사용)

  cd first_project(경로들어가기)

  python manage.py runserver(서버작동시키기. 명령 후 뜨는 코드중 링크들어가서 확인)

  python manage.py startapp 앱이름(복수형으로)

  

  ## 프로젝트

  * 하이픈 사용X, 파이썬이나 장고에서 기본적으로 사용되는 이름X

  ```
  django-admin startproject first_webex
  ```

  * `first_webex`라는 이름으로 폴더가 생성

    * 이 안에는 `first_webex`폴더와 `manage.py`가 생성됨.

      * first_webex: 프로젝트설정파일들이 들어있음

      * manage.py: 장고 명령어를 실행하기 위한 파일

        `python manage.py : 장고명령어`

      * 가장 밖에 있는 프로젝트 폴더명은 수정가능하나, setting파일이 들어있는 폴더명은 건들지말기

  * 장고실행

    ```
    python manage.py runserver
    ```

## APP

* 장고프로젝트 Application의 집합체로 동작

  * 실제로 어떠한 역할을 해주는 친구가 바로 app

  * 하나의 프로젝트는 여러 개의 application을 가질 수 있음

    * 어플리케이션: 하나의 역할 및 기능 단위로 쪼개진 형태

      ex) 회원관리/ 글 작성, 수정, 삭제/  데이터 수집, 분석/...

      어플리케이션을 이렇게 나눠야한다는 기준은 없음

      작은 프로젝트라면 어플리케이션을 따로 나누지 않아도 됨

      

* 어플리케이션 생성

  ```
  python manage.py startapp 앱이름(복수형★★★★★★★)
  ```

  * 해당 앱이름으로 폴더가 생성됨.(앱 폴더)
  * 바로 할 일★★★★★★★★★★★★★
    * `settings.py`에 내가 생성한 앱을 등록하기
    * installed_app의 가장 윗줄에 등록해야함.
    * laguage_code = 'ko-kr' 왠만하면 소문자로
    * time_zone = 'Asia/Seoul' 대소문자 주의.

 urls views(컨드롤러) database(생략가능.모델) template reponse(뷰)





## MTV(MVC 패턴)

* MTV(MVC 패턴)
  * Model: 장고에서는 모델
  * View: 템플릿
  * Controller: 뷰
* 3대장: 우리가 가장 밀접하게 수정해야하는 파일명
  1. urls.py
  2. views.py
  3. templates (html들)

* urls.py 해야할 일
  * __path('url패턴/', 실행이 되어야 하는 views에 있는 함수, 해당 path의 별명)__
  * 많이 놓치는 부분: url뒤에 슬러쉬!!!!!!
* views.py에서 해야할 일
  * 함수를 정의(첫번째 인자로 request 필수	
  * return은 꼭 필요
    * render:주로 template 과 함께 respense 할 때 사용되는 함수.
* template에서 해야할 일

  * 폴더 명은 반드시 ```templates```인 것을 확인
  * 
* TemplateDoesNotExist at /index/오류 이유
  * 오타
  * templates폴더에 위치해있지않을 때.



# Django Template Language(DTL)

* Django Template System에서 사용하는 빌트인 템플릿 시스템.
* 조건 반복 치환 필터 변수등의 기능을 제공
* 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것.
* 파이썬처럼 if, for를 사용할 수 있으나, 단순히 python code로 실행되는 것은 아니다.



syntax

* variable: `{{}}`
* filter : `{{variable|filter}}`
* tags: `{% tag %}`



## 템플릿 시스템 설계 철학

* 장고는 템플릿시스템이 __표현을__ 제어하는 도구이자 표현에 관련된 로직일 뿐이라고 생각한다.
* 템플릿시스템에서는 이러한 기본 목표를 넘어서는 기능을 지원해서는 안된다.

https://search.naver.com/search.naver?query=헤이즈

https://search.naver.com/search.naver?

query=헤이즈;;;;쿼리는 키(input name), 헤이즈는 밸류(input value)







## 여기부터는 본격적인 장고 동작 정의 방법

* Template Variable

  * html과 같은 템플릿에서 views.py에서 준비한 변수를 가져다 쓰는 방법

  * render() 세번째 인자로 `{'key':value}`와 같이 딕셔너리 형태로 넘겨주면 Template에서 key를 이용하여 value를 가져올 수 있다.

    ```
    context = {'key':value}
    return render(request, 'index.html', context)
    ```

    ```
    {{key}}이렇게 value를 보여줄 수 있다.
    ```

* Variable Routing(동적 라우팅)

  * url주소일부를 변수처럼 사용해서 동적인 주소를 만드는 것.

    주소요청: `https://127.0.0.1:8000/hello/문자열`

    urls.py

    ```
    path('hello/<str(타입):name(저장되는 변수명)>/', views.hello),
    ```

    views.py

    ```
    def hello(request, name): #저장되는 변수명을 def에 넣어야함.
    	print(name)
    	context = {
    		'name':name,
    	}
    	return render(request, 'hello,html', context)
    ```

    template(hello.html)

    ```html
    <body>
        이름은:{{name}} #context의 key값을 사용하면 value를 출력한다.
    </body>
    ```

    

* DTL(tag와 filter)

  * 로직을 표현할 때: `{% for %}`

  * 값을 표현할 때 : `{{ }}`

  * 주석으로 나타내고 싶을 때 : `{# #}`or `{% comment %}`주석할 내용 `{% endcomment %}`

    ```html
    <!-- <h1>{#{ i * 2 }#}</h1> -->
    {% comment %} <h1>{{ i * 2}}</h1> {% endcomment %}
    ```

  * for 태그

    * 반복을 위한 태그

      ```
      {% for 임시변수 in iterable한 객체 %}
      {% endfor %}
      ```

    * for empty

      ```html
      {% for 임시변수 in iterable한 객체 %}
      	값이 하나라도 있으면 여기 실행
      {% empty %}
      	출력할 값이 없으면 출력
      {% endfor %}
      ```

  * if 태그

    * 조건을 구분하기 위한 태그

      ```
      {% if 조건문 %}
      {% elif 조건문 %}
      {% else %}
      {% endif %}
      ```

  * 나머지 기타 유용한 dtl문서를 참고(구글에서 키워드 django built in template 검색)

  * 

  * __form__

  * HTML form tag의 의미

  * 입력받은 데이터를 어딘가로 보낼 떄 사용

     ```html
    # action: 보내려는 목표
    # method: http method(get, post)
    <form action="" method="GET">
        input 데이터를 입력받게 적절히 코딩.
        #오락실버튼
        <input type="button">
        #미사일버튼
        <input type="submit">
        
        <button></button>
    
    </form>
     ```

  * action 에 들어가는 목표 url 설정 주의 사항

    ```
    action="/catch/"
    => 127.0.0.1:8000/catch?name=asdf
    
    현재 주소 : 127.0.0.1:8000/index
    action="catch/"
    => 
    ```

    

