# 0921 Model Relationship

![image-20200921114409725](C:\Users\kimyeunjung\AppData\Roaming\Typora\typora-user-images\image-20200921114409725.png)

## 1:N 관계

* 장고모델에서 사용되는 Field

  * 1:1 - OneToOneField() 유저와 프로필
  * 1:N - ForeignKey() 글과 댓글, 제조사와 자동차
  * N:M - ManyToManyField() 좋아요

  

* ForeighKey() 사용법(1:N)

  * 언제 사용? 맛집-리뷰, 지역- 팔리는 소주 등
  * 사용방법
    * models.ForeignKey(__참조모델, 참조모델이 삭제되었을 때 어떻게 할지__)
      * models.ForeignKey(Articles, on_delete=models.__CASCADE__)
        * on_delete종류는?
          * CASCADE: 참조하는 테이블이 삭제되면 내 데이터도 삭제됨
          * PROTECT: 참조하는 테이블이 삭제되려고 하면 삭제하지 못하게 에러낸다
            * 참조(1의입장)테이블을 삭제하려면 N입장의 테이블의 관계정리필요
          * SET_NULL: 참조하는 테이블이 삭제되면 내 데이터에 해당 값을 NULL로 설정한다
            * 이 값을 사용하려면 null=True가 필요하다
          * SET_DEFALUT: 참조하는 테이블이 삭제되면 Default값으로 설정한다
            * 이 값을 사용하려면 defalut설정이 필요함
          * SET(함수명): 특정 함수를 호출해서 그 함수의 결과값으로 설정한다
          * DO_NOTHING: 아무것도 하지않음
    * 참조 모델이 DB에 저장될때는 pk값을 저장함
      * 그 컬럼명은 `필드명_id`라고 장고에서 만들어줌.(ForeignKey로 설정한 필드의 최종 DB필드명)

  

---

* ForeignKey를 사용하여 게시글의 댓글을 달아주는 코드를 완성
  * Comment모델정의
  * forms.py에 CommentForm정의
    * 여기서 article정보는 제외하기위해서 `exclude`사용.
  * 정의된 CommentForm을 가지고 detail페이지에서 커멘트받을 수 있게 form을 나타냄
  * 작성된 Comment를 저장하기 위해 views에 comment_create함수작성
    * form.save()하면 에러발생
      * article정보없어서 not null에러발생
      * article정보는 따로 저장해줘야함
      * form.save() 하면 바로 DB에 저장되지만 commit=False를 인자로 넣어주면 DB에 바로저장되지않음
      * article정보를 넣고 수동 save()함
  * 작성된 comment도 detail에서 보여줌
  * 삭제버튼도 추가
  * Update는 시간되는사람만 도전해보기



* 댓글 갯수 달아주는 방법

  * detail페이지에서 comments의 개수를 세어서 보여줌

    ```pytho
    1. 필터를 이용한 방법
    {{ comments|length }}
    
    2. QuerySet의 countmethod를 이용하는 방법
    {{ comments.count }}
    * QuerySet의 count를 실행하면 DB에 쿼리를 날려서 DB에서 count를 세어서 전달해줌
    
    3. 역참조하여 필터를 이용
    {{ article.comment_set.all|length }}
    ```

* 댓글이 없을 때는 `for...empty`사용

* get_object_or_404

  * DB에서 해당 정보가 없으면 404페이지 에러발생

  * 사용이유: 책임소재를 분명히 하기 위해서

    * http error code

      * 4XX코드는 요청이 잘못된 경우

      * 5XX코드는 서버에서 잘못 처리되는 경우

        








