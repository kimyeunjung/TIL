# Vue Directive

```html
<div id="app"></div>

<!--vue CDN 추가-->
<script>
	const app = new Vue({
		el: '#app',
    	data: {
            // vue에서 사용되는 변수들. 다양한 정보의 타입이 저장될 수 있다.
        },
    	methods: {
            // vue에서 사용할 함수들을 정의하는 곳. 메소드를 정의할 시 화살표함수사용하지않는다.(this)
        }
    })
</script>
    
```

* **v-html**
  * innerHTML로 할당
  * HTML을 그대로 읽기 때문에 XSS공격에 취약
* **v-text**
  * innerText로 할당
  * {{머스타치}}: 보간법(interpolation)과 동일한 역할
* **v-if, v-if-else, v-else**
  * 조건문에 따라서 해당 Tag의 렌더링여부를 결정한다.
  * 아예 코드자체가 렌더링되지않는다.
  * v-if, v-else를 사용할 때 사이에 어떠한 Tag가 있으면 제대로 동작하지 않는다.

* **v-show**

  * v-show의 값에 따라 css display속성을 조절해서 화면노출을 결정한다.

* **v-for**

  * 반복문

* **v-bind**

  * HTML표준속성에 Vue의 데이터를 연결

  * `:`(shortcut)

  * Object형태(키-밸류)로 사용하면 value가  true인 경우만 바인딩 된 값으로 할당 가능. 

    ```
    :class = "{클래스 이름:false}"
    ```

* **v-model**

  * 양방향바인딩
  * 입력되어지는 태그 (input, textarea)

* **v-on**

  * 이벤트
  * `@`(shortcut)

* **this**

  * obj.functionCall() => this === obj : 메소드 호출되었을 때

  * 그 외 => this === window

    ```html
    const myObj = {
    	myFunc: function () {
    		console.log(this) //myobj
            // 1.콜백함수에서 this를 obj로 만드는 방법 (.bind)
            axios.get(URL)
            	.then(function () {
                    console.log(this) //myObj
                }.bind(myObj))
            // 2.콜백함수에서 this를 obj로 만드는 방법
            axios.get(URL)
            	.then(() => {
                    console.log(this) //myObj
    		})
    	}
    }
    ```


--------

 ## computed & watch

#### computed

* 값을 캐싱하기 때문에 값이 변치않으면 기존에 계산된 값(캐싱된 값)을 사용함.

* 특정 데이터를 직접적으로 가공하여 다른 값으로 만들어 사용할 때 주로 활용한다.

  `반갑습니다. 00시 입니다`

#### watch

* 데이터가 변경되는지 지켜보고 변경된다면 특정 함수를 실행

* 특정 데이터의 변화에 따라서 다른 데이터 혹은 환경등을 변화시켜야 하는 경우에 주로 활용

  `00시의 날씨는 00입니다.`

    