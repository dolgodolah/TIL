# MySQL Explain

MySQL 튜닝에서 가장 중요한 것은 쿼리와 스키마 최적화인데 스키마 설계는 한번 진행되면 그 테이블을 사용하는 모든 쿼리에 영향을 주기 때문에 변경하기 힘들다.

하지만 쿼리는 해당 쿼리만 수정하면 되므로 변경하기 쉽다. Slow Query를 없애는 것은 성능을 향상 시키기 위한 매우 중요한 수단이다.

MySQL Explain 이란 DB가 데이터를 찾아가는 일련의 과정을 알아보기 쉽게 DB 결과 셋으로 보여주는 것이다.

쿼리를 실제로 수행하기 전에 해당 쿼리의 성능 분석, 인덱스 전략 수립 등과 같이 성능 최적화에 대한 전반적인 업무를 처리할 수 있다.

## 사용 방법

```mysql
EXPLAIN [EXTENDED] SELECT ... FROM ... WHERE ...
```


## EXPLAIN 결과 컬럼별 의미

<img width="612" alt="MySQL Explain" src="https://user-images.githubusercontent.com/75430912/181867514-eca1cae9-d9ee-4a47-81bf-c9af6f6ebfa5.png">

- id : select 아이디로 SELECT를 구분하는 번호
- table : 참조하는 테이블
- select_type : select에 대한 타입
- type : 조인 혹은 조회 타입
- possible_keys : 데이터를 조회할 때 DB에서 사용할 수 있는 인덱스 리스트
- key : 실제로 사용할 인덱스
- key_len : 실제로 사용할 인덱스의 길이
- ref : Key 안의 인덱스와 비교하는 컬럼
- rows : 쿼리 실행 시 조사하는 행 수립
- extra : 추가 정보

### id

행이 어떤 SELECT 구문을 나타내는지 알려주는 것으로 구문에 서브 쿼리나 UNION이 없다면 SELECT는 하나밖에 없기 때문에 모든 행에 1이 부여되지만 이외의 경우는 순서에 따라 각 SELECT 구문들에 순차적으로 번호가 부여된다.

### table

행이 어떤 테이블에 접근하는 지를 보여준다.

### select_type

- SIMPLE : 단순 SELECT (UNION 이나 Sub Query 가 없는 SELECT 문)
- PRIMARY : Sub Query를 사용할 경우 Sub Query의 외부에 있는 쿼리, UNION을 사용할 경우 UNION의 첫번째 SELECT 쿼리
- UNION : UNION 쿼리에서 Primary를 제외한 나머지 SELECT
... 나머지는 원글 [참고](https://nomadlee.com/mysql-explain-sql/)

### type

- system : 테이블에 단 한개의 데이터만 있는 경우
- const : SELECT에서 Primary Key 혹은 Unique Key를 상수로 조회하는 경우로 많아야 한 건의 데이터만 있음
- eq_ref : 조인을 할 때 Primary Key
- ref : 조인을 할 때 Primary Key 혹은 Unique Key가 아닌 Key로 매칭하는 경우
- ref_or_null : ref 와 같지만 null 이 추가되어 검색되는 경우
- range : 특정 범위 내에서 인덱스를 사용하여 원하는 데이터를 추출하는 경우로, 데이터가 방대하지 않다면 단순 SELECT 에서는 나쁘지 않음
- index : 인덱스를 처음부터 끝까지 찾아서 검색하는 경우로, 일반적으로 인덱스 풀스캔이라고 함
- all : 테이블을 처음부터 끝까지 검색하는 경우로, 일반적으로 테이블 풀스캔이라고 함

### possible_keys

쿼리에서 접근하는 컬럼들과 사용된 비교 연산자들을 바탕으로 어떤 인덱스를 사용할 수 있는 지를 표시해준다.

### key

테이블에 접근하는 방법을 최적화 하기 위해 어떤 인덱스를 사용하기로 결정했는 지를 나타낸다.

### key_len

MySQL이 인덱스에 얼마나 많은 바이트를 사용하고 있는 지를 보여준다. MySQL에서 인덱스에 있는 컬럼들 중 일부만 사용한다면 이 값을 통해 어떤 컬럼들이 사용되는 지를 계산할 수 있다.

### ref

키 컬럼에 나와 있는 인덱스에서 값을 찾기 위해 선행 테이블의 어떤 컬럼이 사용되었는 지를 나타낸다.

### rows

원하는 행을 찾기 위해 얼마나 많은 행을 읽어야 할 지에 대한 예측값을 의미한다.

### extra
- using index : 커버링 인덱스라고 하며 인덱스 자료 구조를 이용해서 데이터를 추출
- using where : where 조건으로 데이터를 추출. type이 ALL 혹은 Indx 타입과 함께 표현되면 성능이 좋지 않다는 의미
- using filesort : 데이터 정렬이 필요한 경우로 메모리 혹은 디스크상에서의 정렬을 모두 포함. 결과 데이터가 많은 경우 성능에 직접적인 영향을 줌
- using temporary : 쿼리 처리 시 내부적으로 temporary table이 사용되는 경우를 의미함


# Reference

[https://nomadlee.com/mysql-explain-sql/](https://nomadlee.com/mysql-explain-sql/)