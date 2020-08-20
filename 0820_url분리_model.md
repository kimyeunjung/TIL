## URL분리

1. 앱생성(articles)-settings.py에 등록

2. urls.py

   * include를 임포트해주고 path적기

   ```python
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('articles/', include('articles.urls')),
   ]
   ```

3.  앱에 urls.py 생성해주기

4. 앱의 urls.py에 입력

   ```python
   from django.urls import path
   
   app_name = "articles"
   urlpatterns = [
       
   ]
   ```

   



 ## 모델정의

1. models.py에 정의하기(class)

   ```python
   class Article(model.Model):#클래스명은 앱의 단수형으로. 
       title = models.CharField(max_length=100)#charfield는 항상 max_length인자를 써야함)
       content = models.TextField()#글자수는 따로 없고 입력하는데로 다 저장함
       created_at = models.DateTimeField(auto_now_add=True)
       #시간과 날짜를 모두 저장. autonowadd는 입력당시.
   ```

2. ```
   터미널창에 설계도 작성하기
   python manage.py makemigrations
   그러면 migrations에 0001_initial.py가 생성됨.
   ```

3.

```
python manage.py makemigrate
```



#### models.py 수정

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)#charfield는 항상 max_length인자를 써야함)
    content = models.TextField()#글자수는 따로 없고 입력하는데로 다 저장함
    created_at = models.DateTimeField(auto_now_add=True)
    #수정부분
    abc = models.CharField(max_length=50, default='1')
```

터미널창에 1,2번 중에 하나 선택하라고 함.

1번은 자동으로 현재시간이 디폴트값인 0002_py파일이 생성됨

2번은 내가 직접 디폴트값을 지정.



sqlite 설치

$ pip install django-extensions후에 settings.py에 등록

```python
INSTALLED_APPS = [
    'articles',
    'django_extensions', 	#언더바 주의
```

터미널에

```python
$ python manage.py shell_plus
```



------



## Field lookups

* 구글링 키워드: `django queryset`
* `필드명__필드룩업`
* exact: 대소문자 전부 일치해야함
* iexact: 대소문자 상관없이 일치하면 됨
* contains: 해당 글자가 어느 위치던 포함되어 있으면 됨
* startswith: 해당글자로 시작하는 것만
* endswith: 해당글자로 끝나는 것만
* gt/ gte/ lt/ lte : 비교연산자



### 실습

* 제목이 first이고 한개만 가져오기. (여러 개의 데이터가 있는데 하나만 가져오고 싶을 때)

```python
Article.objects.filter(title="second").first()
```

* * 해당 모델의 클래스로 값이 리턴됨.

    

* 정렬을 하고 싶을 때(오름차순 & 내림차순)

  ```python
  #오름차순
  Article.objects.order_by('title')
  
  #내림차순
  Article.objects.order_by('-title')
  ```



* QuerySet으로 리턴받았을 때

  * QuerySet은 List와 유사함

  * Indexing & Slicing

    ```python
    #indexing
    Article.objects.all()[2]
    
    Article.objects.all()[-2] # 음수는 지원안함
    
    #slicing
    Article.objects.all()[:2]
    ```

    