# Redis

Redis(REmoteDIctionaryServer)는 NoSQL 중 `Key`, `Value` 형식의 데이터베이스로

메모리에 데이터를 저장(인메모리)하기 때문에 데이터 접근이 매우 빠른 데이터베이스입니다.

NoSQL의 특징과 종류에 대해 간단히 알아보고,

인메모리 방식 스토어들의 특징과 Redis만의 특징(Redis를 사용하는 이유), 기본 개념에 대해 알아보겠습니다.

## 1\. NoSQL

### 1.1 NoSQL이란?

RDBMS를 보통 관계형 데이터베이스라고 부른다면 NoSQL은 비관계형 데이터베이스로 부를 수 있습니다.

미리 정해진 스키마에 따라 엄격하게 데이터를 테이블에 저장하는 관계형 데이터베이스와는 달리

NoSQL은 사전 정의된 스키마없이 동적인 스키마를 통해서 데이터 형식에 제한을 받지 않고 자유롭게 데이터를 저장할 수 있습니다.

> 스키마 : 개체(Entity), 속성(Attribute), 관계(Relationship), 제약조건 등을 정의해둔 것

NoSQL은 Read/Write에 매우 최적화된 데이터베이스입니다.

주로 아주 많은 양의 데이터(빅데이터)를 처리할 때 효율적이고, 분산처리, 빠른 Read/Write 작업이 필요할 때 사용합니다.

### 1.2 NoSQL 종류

`Document Database` : MongoDB, CouchDB ..

`Wide Column Database` : Cassandra, HBase ..

`Key Value Database` : **Redis**, Memcached

`Graph Database` : Neo4j

## 2\. In Memory Database

In Memory Database란 데이터를 메모리에 저장하는 데이터베이스를 말합니다.

기존 디스크 방식의 스토어는 디스크에 저장된 데이터를 대상으로 쿼리를 수행하여 디스크에 접근을 했지만

인메모리 방식의 스토어들은 데이터를 메모리에 두기 때문에 데이터 접근에 있어 훨씬 빠릅니다.

이러한 특징을 이용해 캐시 적용과 같이 빠른 데이터 접근이 필요한 작업에 많이 사용됩니다.

대표적인 인메모리 데이터베이스는 `Redis`, `Memcached` 등이 있습니다.

## 3\. Redis만의 특징

### 3.1 다양한 데이터 구조

Redis에서는 다양한 데이터 구조를 지원합니다. 덕분에 개발자는 비즈니스로직에 집중할 수 있는 환경을 제공받습니다.

#### 3.1.1 String

가장 일반적인 형태로 `key`,`value`의 형태의 데이터를 저장합니다.

-   `set <key> <value>` : key에 value를 저장합니다.
-   `get <key>` : key에 해당하는 value를 조회합니다.
-   `del <key> <key> ...` : 해당 key들을 삭제합니다.

#### 3.1.2 Set

여러 개의 값(member)들을 하나의 `value`에 넣을 수 있습니다. 집합을 생각하면 됩니다.

-   `sadd <key> <member> <member> ...` : key가 존재하지 않으면 새로 만들고, 존재하면 새로운 key에 member들을 추가합니다.
-   `smembers <key>` : key에 해당하는 member들을 조회합니다.
-   `srem <key> <member> <member> ...` : key에 있는 member들을 삭제합니다. 존재하지 않는 member를 입력하면 무시됩니다.

#### 3.1.3 Sorted Set

Set에 score(가중치) 필드가 추가된 데이터 형태로 유저 랭킹 같은 서비스를 구현하는데 사용할 수 있습니다.

#### 3.1.4 Hash

value내에 `field`, `value`의 형태로 값들을 저장합니다. value에 또 key, value를 저장한다고 생각하면 됩니다.

-   `hset <key> <field> <value> <field> <value>` : key에 field, value를 저장합니다.
-   `hget <key> <field>` : key에 해당하는 Hash 데이터 중 field에 해당하는 value를 조회합니다.
-   `hdel <key> <field> <field>` : key에 해당하는 Hash 데이터 중 field에 해당하는 value들을 삭제합니다.
-   `hlen <key>` : key에 해당하는 Hash 데이터가 가지고 있는 field의 수를 반환합니다.
-   `hkeys <key>` : key에 해당하는 Hash 데이터가 가지고 있는 모든 field를 조회합니다.
-   `hvals <key>` : key에 해당하는 Hash 데이터가 가지고 있는 모든 value를 조회합니다.
-   `hgetall <key>` : key에 해당하는 Hash 데이터가 가지고 있는 모든 field, value를 조회합니다.

### 3.2 Persistence Data Storage

Redis는 기본적으로 인메모리 방식의 데이터베이스이지만 디스크에도 데이터를 저장할 수 있습니다.

-   AOF (Append Only File)
    -   AOF 방식은 명령을 실행할 때마다 명령어들을 기록합니다. (조회 명령 제외)
    -   서버가 재시작될 때 (데이터 복구가 이뤄질 때) 기록된 명령어들을 순차적으로 실행함으로써 데이터들을 복구합니다.
    -   장점 : 명령을 실행할 때마다 기록하기 때문에 데이터 유실이 거의 없습니다.
    -   단점 : 기록한 모든 명령어들을 다시 실행하켜 데이터들을 복구하기 때문에 재시작 속도가 느립니다.
-   RDB (Snapshot)
    -   RDB 방식은 특정 시점의 메모리에 있는 데이터들을 그대로 저장하는 방식입니다.
    -   장점 : 해당 snapshot(특정 시점의 메모리에 있는 데이터들)만 불러오면 되기때문에 재시작 속도가 빠릅니다.
    -   단점 : 데이터 유실이 발생할 수 있습니다.
-   결론
    -   AOF 방식과 RDB 방식을 적절히 혼용해서 사용해야 합니다.
    -   특정 시점마다 RDB 방식을 통해 snapshot을 저장하고, 그 사이(현 snapshot과 다음 snapshot까지)에 발생한 명령어들에 대해서 AOF방식을 수행합니다.
    -   서버가 재시작될 때 (데이터 복구가 이뤄질 때) snapshot을 복구하고, 나머지 데이터들에 대해서는 AOF 방식으로 소량의 명령어들을 순차적으로 실행시켜 복구합니다.

### 3.3 Single Thread

Redis는 싱글 쓰레드이기 때문에 한 번에 하나의 명령어에 대해서만 실행할 수 있습니다.

그래서 `O(N)`의 시간복잡도를 가지는 `keys *`, `flushall` 등과 같은 명령에 대해서는 주의해야 합니다.

## 4\. maxmemory와 maxmemory-policy 설정

`redis.conf`를 통해 메모리 최대치(maxmemory)와 최대치에 도달했을 때 메모리에 있는 데이터들을 어떻게 처리할 것인지(maxmemory-policy)에 대해 설정을 할 수 있습니다.

redis-cli에서 `config set`을 통해서도 설정할 수 있으나 서버가 재시작되면 `redis.conf` 파일에 있는 설정값들로 유지됩니다.

### 4.1 maxmemory

32비트와 64비트 환경에서 maxmemory의 초기값이 다릅니다.

32비트의 경우 초기값이 3GB로 설정되어 있지만, 64비트의 경우 0으로 설정되어 있어 메모리 사용량 제한이 없습니다.

메모리 사용량 제한이 없으면 좋은거 아닌가?

메모리 사용량 제한이 없으면 운영체제의 가상메모리(스왑)까지 사용하게 되는데 속도에 엄청난 영향을 주게 됩니다.

또한 더 많은 메모리를 쓰면, 메모리 문제로 장애가 발생할 수 있기 때문에 maxmemory를 설정해줘야합니다.

### 4.2 maxmemory-policy

메모리 최대치를 정해뒀으면 최대치에 도달했을 때 메모리에 있는 데이터들을 어떻게 처리할지에 대해서도 명시를 해야합니다.

-   `noeviction` : default로 메모리 최대치 이상을 사용하게 되면 캐시 데이터를 삭제하지 않고 에러를 발생시킵니다.
-   `allkeys-lru` : 모든 key에 대해서 LRU 알고리즘 기반으로 캐시 데이터를 삭제합니다.
-   `volatile-lru` : EXPIRE SET에 있는 key에 대해서 LRU 알고리즘 기반으로 캐시 데이터를 삭제합니다.
-   `allkeys-lfu` : 모든 key에 대해서 LFU 알고리즘 기반으로 캐시 데이터를 삭제합니다.
-   `volatile-lfu` : EXPIRE SET에 있는 key에 대해서 LFU 알고리즘 기반으로 캐시 데이터를 삭제합니다.
-   `allkeys-random` : 모든 key에 대해서 랜덤으로 캐시 데이터를 삭제합니다.
-   `volatile-random` : EXPIRE SET에 있는 key에 대해서 랜덤으로 캐시 데이터를 삭제합니다.
-   `volatile-ttl` : EXPIRE SET에 있는 key에 대해서 TTL이 짧은 순으로 삭제합니다.

`EXPIRE SET`은 유효시간이 설정된 데이터들의 집합을 말합니다.

## 5\. 다른 인메모리 스토어보다 Redis를 사용해야하는 경우

인메모리 스토어는 데이터 접근이 빠르다는 특징때문에 캐시 적용에 많이 사용되고 있습니다.

캐시의 다른 방안으로는 Memcached, Ehcache 등이 있는데 다음과 같은 상황에서는 Redis를 많이 사용하고 있습니다.

-   데이터를 저장하는데 있어 다양한 데이터 구조가 필요하다.
-   로드밸런싱을 하고 있어 Global Cache 방식이 필요하다.
-   데이터 복구가 가능해야 한다.
