# 마크다운(Markdown)

> 일반 텍스트 형식 구문을 사용하는 마크업 언어의 일종으로 사용법이 쉽고 간결하여 빠르게 문서정리를 할 수 있습니다. 단, 모든 HTML 마크업을 대체하지는 않습니다.



## 1. 문법

### 1.1 Header

> 헤더는 제목을 표현할 때 사용합니다. 단순히 글자의 크기를 표현하는 것이 아닌 의미론적인 중요도를 나타냅니다.

- `<h1>` 부터 `<h6>` 까지 표현이 가능합니다.
- `#` 의 개수를 표현하거나 `<h1></h1>` 의 형태로 표현 가능합니다.

# h1 태그입니다.

## h2 태그입니다.

### h3 태그입니다.

#### h4 태그입니다.

##### h5 태그입니다.

###### h6 태그입니다.



### 1.2 List

>목록을 나열할 때 사용합니다. 순서가 필요한 항목과 그렇지 않은 항목으로 구분할 수 있습니다. 순서가 있는 항목 아래 순서가 없는 항목을 지정할 수 있으며 그 반대도 가능합니다.

- 순서가 있는 항목
  - `1.` 을 누르고 스페이스바를 누르면 생성할 수 있습니다.
  - `tab` 키를 눌러서 하위 항목을 생성할 수 있고 `shift + tab` 키를 눌러서 상위 항목으로 이동할 수 있습니다.
- 순서가 없는 항목
  - `-` (하이픈)을 쓰고 스페이스바를 누르면 생성할 수 있습니다.
  - `tab` 키를 눌러서 하위 항목을 생성할 수 있고 `shift + tab` 키를 눌러서 상위 항목으로 이동할 수 있습니다.

1. 순서가 있는 항목
2. 순서가 있는 항목
   1. 순서가 있는 하위 항목
   2. 순서가 있는 하위 항목

- 순서가 없는 항목
  - 순서가 없는 하위 항목
  - 순서가 없는 하위 항목



### 1.3 Code Block

> 코드 블럭은 작성한 코드를 정리하거나 강조하고 싶은 부분을 나타낼 때 사용합니다. 인라인과 블럭 단위로 구분할 수 있습니다.

- Inline
  - 인라인 블럭으로 처리하고 싶은 부분을 `(백틱)으로 감싸줍니다.
- Block
  - `(백틱)을 3번 입력하고 Enter를 눌러 생성합니다

`add` 한 요소를 remote 저장소에 올리려면 `git push origin master` 를 터미널에 입력합니다.

```python
$ git add .
$ git commit -m "first commit"
$ git push origin master
```



### 1.4 Image

> 로컬에 있는 이미지를 삽입하거나 이미지 링크를 활용하여 이미지를 나타낼 때 사용합니다.

- `![]()` 을 작성하고 `()` 안에 이미지 주소를 입력합니다. `[]` 안에는 이미지 파일의 이름을 작성합니다.
- 로컬에 이미 파일을 저장한 경우 절대 경로가 아닌 상대 경로를 사용하여 이미지를 저장합니다.

<img src="/Users/jogyutae/Desktop/스크린샷 2021-01-13 오후 9.42.30.png" alt="스크린샷" style="zoom:50%;" />

![문어고양이](data:image/png;base64,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)





### 1.5 Link

> 특정 주소로 링크를 걸 때 사용합니다.
>
> - `[]()` 을 작성하고 `()` 안에 주소를 작성하고 `[]` 안에 어떤 주소인지 작성합니다.

[git 공식 문서](https://git-scm.com/book/ko/v2)



### 1.6 Table

> 표를 작성하여 요소를 구분할 수 있습니다.

- `|` (파이브)사이에 컬럼을 작성하고 `enter` 를 입력합니다.
- 마지막 컬럼을 작성하고 뒤에 `|` 를 붙여줍니다.

| working directory | staging area | remote repo |
| ----------------- | ------------ | ----------- |
| Working tree      | Index        | History     |
| Working copy      | cache        | tree        |



### 1.7 기타

인용문(참조문)

- `>` 을 입력하고 `enter` 키를 누릅니다.

> Git은 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율하기위한 분산 버전관리 시스텝이다.

- 인용문 안에 인용문을 작성하면 중첩해서 사용할 수 있습니다.

>$ git add .
>
>> $ git commit -m "first commit"
>>
>> > $ git push origin master



수평선

- `---` , `***` , ` ___` 을 입력하여 작성합니다.

Working Directory

---

Staging Area

***

Remote Repository

___



강조

- 이텔릭체는 해당 부분을 `*` 혹은 `_` (언더바)로 감싸줍니다.
- 볼드체는 해당 부분을 `**` 혹은 `__` (언더바 2개)로 감싸줍니다.
- 취소선은 해당 부분을 `~~` 로 감싸줍니다. 

 

