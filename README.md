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

<img src="/Users/jogyutae/Desktop/스크린샷 2021-01-13 오후 5.17.17.png" alt="oh" style="zoom:50%;" />

![문어고양이](data:image/jpeg;base64,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)

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

 

