# Account 간단요약

* 앱을 새롭게 생성
* __Article__이 이미 존재하지만 게시글을 관리하는 역할을 하는 앱
* 회원관리 역할을 하는 기능이 필요한데 __Account__



### 회원가입 기능추가

* 회원가입 == DB유저정보를 새롭게 추가하는 행위(create)
* __UserCreationForm__: django에서 기본적으로 제공해주는 폼
  * 유저정보를 DB에 저장해야함 => ModelForm
  * `from django.contrib.auth.forms import UserCreationForm`
  * 나머지 로직은 이전 CRUD의 Create동일.
* 회원가입을 하면 따로 로그인을 해야한다
  * 근데 우리는 이미 로그인하는 방법 알고있따
  * 회원가입을 한다는 것은 



### 로그인

* 쿠키

  * 브라우저에 저장
  * 키-밸류 작은 데이터 파일
  * 만료일자
  * 종류
    * 세션쿠키: 사용자가 사이트를 탐색할 때, 설정과 선호사항을 저장하는 임시쿠키. 브라우저를 닫으면 삭제됨
    * 지속쿠키: 사용자가 주기적으로 방문하는 사이트에 대한 설정정보나 로그인이름을 유지하기 위해 주로 사용함. 브라우저를 닫거나 컴퓨터를 재시작해도 남아있다.

* 세션

  * 서버DB 혹은 메모리
  * 정말 중요한 정보저장
  * 사용자가 많아지면 서버 느려질 수 있다

* 로그인 == 세션을 새롭게 생성(create)

* __AuthenticationForm__: Django에서 기본적으로 제공해주는 Form

  * 로그인을 위해서 입력창을 제공해줌
  * 로그인 유효성검사
  * DB유저정보와 비교해서 접속인증을 해주는 칭구~
  * DB를 직접 수정하는 폼이 아니기 때문에 Form
    * 첫 인자로 request정보를 보내야 함

* __login함수__: Django에서 기본적으로 제공해주는 함수

  * 세션에 인증정보를 생성해주는 함수

  

### 로그아웃

* 로그아웃 == 세션을 삭제(delete)
* logout함수: Django에서 기본적으로 제공해주는 함수
  * 현재 request에서 session에 관한 data를 삭제.



### 접근제한

* `is_authenticated`

  * User클래스와 AnonymousUser의 속성값
    * User 해당 값이 항상 True, AnonymousUser는 항상 False
  * 유저가 인증된 유저인지 아닌지를 확인

* `is_anonymous`:유저가 인증되지않은 사용자인지 확인

* `is_superuser`: 유저가 최고 관리자인지 확인

* `is_staff`: 유저가 관리자계정에 접근가능한지 확인

* `login_required`데코레이터

  * 로그인 된 유저만 해당 함수를 실행가능하게 하는 데코레이터

  * 만약 로그인이 되지않은 유저라면

    * `/accounts/login/`으로 리다이렉트 해줌

    * next라는 쿼리문자열에 이전에 접근하려한 주소를 keep해줌

      * 킵된 주소를 사용하려면 request.GET.get('next')해서 리다이렉트

    * `@login_required(login_url='/accounts/test/')`

    * settings.py에 LOGIN_URL을 설정해주면 해당 주소로 갈 수 있음

      * LOGIN_URL기본값이 '/accounts/login/'

        

* login_required와 require_POST를 같이 사용할 수 없는 이유

  ```python
  @require_POST
  @login_required
  def logout(request):
      #if request.user.is_authenticated:
      auth_logout(request)
      return redirect('accounts:index')
  ```

  * 비로그인상태로 POST로 logout을 시도했을 때
    1. login_required에서 로그인페이로 리다이렉트(POST데이터 손실)
       * 리다이렉트는 GET
    2. 로그인완료 후 next를 이용해서 다시 logout으로 접근
       * 리다이렉트로 logout을 접근하게 됨
    3. 결국 403 http method 에러발생



### 회원탈퇴

* 회원탈퇴 == DB에서 유저정보를 삭제

* 이전에 데이터베이스로 정보를 삭제하는 방법

  ```python
  def delete(request, id):
      data = Article.objects.get(pk=id) #article 정보를 가져와서 
      data.delete()#article정보에서 delete를 실행.
      
  ```

* 유저 정보는 request.user에 담겨져 있다.

  * request.user.delete()를 하면 유저정보가 삭제
  * DB정보를 삭제하는 것이기 때문에 POST요청



### 회원정보수정

* 회원정보를 Update
* `UserChangeForm`: Django에서 기본적으로 제공해주는 폼
  * DB를 수정해야하는 폼
  * ModelForm
  * 문제점
    * 일반유저가 권한설정을 할 수 있게 됨
    * 그대로 사용하면 절대 안됨.
* `CustomUserChangeForm`:`UserChangeForm`을 상속받아서 커스텀한 폼
  * 원하는 필드만 수정할 수 있게 해야함
  * 유저의 정보를 채워서 입력창을 보여줘야하므로 `instance`설정을 해야함

* 디버깅순서(TIP)
  * 개발순서(요청->url->view->template->응답)
  * 개발순서 역순으로 생각하면서 오류를 트래킹
    * 응답(오류메세지)->template->view->url->요청(주소줄확인 or 장고 log에 찍힌 요청을 확인)



### 비밀번호 변경

* DB를 수정하는데
  * 비밀번호는 텍스트그대로 저장되면 안됨
  * Django는 비번을 그냥 저장하지않고 암호화함
* __PasswordChangeForm__
  * Form을 상속받아서 정의되어 있음
  * 첫번째 인자로 `request.user`가 반드시 필요함
  * data=request.POST를 넣어서 사용한다
* 비번변경을 성공한다면 로그인이 풀림,
  * 로그인되면 유저정보를 세션에 저장을 하는데, 비번이 변경되면 유저정보가 업데이트되어서 세션에 저장된 유저정보와 데이터가 일치하지 않음
  * `update_session_auth_hash`함수를 사용해서 세션의 유저정보를 업데이트해줘야함

-----------

##### url resolver

* resolver는 웹브라우저에서 요청을 서버로 전달하고 서버에서 주소를 받아 브라우저에 제공하는 기능을 수행함
* Django에서 url resolver는 `urls.py`에서 정의한 `path`
* reverse()함수가 존재하는데 이 함수는 url resolver모듈 안에 있는 메서드
  * redirect("articles:index", articles.pk)로 사용하는 redirect도 reverse함수사용
  * app_name과 path의 name에 일치하는 실제 주소창에 입력되는 /article/1/을 찾아줌
  * 찾지못하면 NoReverseMatch오류발생
* 결과적으로 resolver라는건 실제 주소창에 입력되는 주소와 장고내부에서 사용하는 url을 서로 번역해주는 역할을 함



#### Password 암호화

* 보안시스템이 강한지 약한지 확인하는 방법은 가장 약한 부분이 얼만큼 강한지에 따라서 결정됨.

* PBKDF2

  * NIST(미국표준기술연구소)에 의해 인증된 암호화방식
  * 미국 정부 시스템에서도 패스워드 관리 시에 사용

* 패스워드를 저장하는 방식

  * 있는 그대로 저장

  * 암호화시킨다

    * 단방향해쉬함수를 이용하여 암호화시킨다
      * 단방향이란? 메시지를 암호화하기는 쉬우나 그 반대는 불가능.

  * 단방향 해쉬함수의 문제점

    * 동일한 메세지는 동일한 hash값을 가지게 됨
    * 속도가 빨라서 문제
      * MD5라는 알고리즘. 1초 56억번 대입연산할 수 있음
      * 해커는 개이득. 서버측에서는 난감

  * 단방향 해쉬함수 보완

    * Salt + 메세지 암호화

      * salt는 랜덤한 문자열
      * 동일한 hash값이 아닌 다른 hash값을 가지게 됨

    * 속도가 빠른 문제를 해결하기 위해 iteration

      * 반복hash데이터를 생성

      * 반복숫자만 가지고 있으면 암호화가능

      * 연산이 많아져서 속도를 늦출 수 있음

        

* 장고에서는 어떻게 비번을 비교?
  * 기존 비번은 이미 솔트와 반복횟수로 암호화되어있음
  * DB에 암호화된 다이제스트와 해당 유저의 솔트값과 횟수를 저장
  * 입력되는 password를 해당 값들로 암호화 해서 다이제스트를 만들고 그 다이제스트끼리 비교함



