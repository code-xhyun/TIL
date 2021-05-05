# aurora

```
표준 MySQL 데이터베이스보다 최대 5배 빠르고,
표준 PostgreSQL 데이터베이스보다 3배 빠르며. 1/10의 비용으로 상용 데이터베이스의 보안, 가용성 및 안정성을 제공한다
```

라고 aws 공식 페이지에서는 설명하고 있다

개인적인 관점으로서의 장점은 아래와 같다고 생각한다

- 기존의 RDS보다 5배 더 나은 성능
- 데이터의 실시간 S3로의 백업
- 무중단 auto scaling out
- 빠른 replica 동기화

기본적으로 따로 read 인스턴스를 추가하지 않는다면 default는 writer인스턴스로 생성이 된다

여기서 인스턴스들의 접속은 각각의 endpoint로 진행하며 해당 endpoint는 4가지 타입으로 이루어져 있다

- cluster endpoint (R&W)
- reader endpoint (R)
- custom endpoint
- instance endpoint

**_여기서 당연하게도 writer인스턴스에서는 읽기가 가능하다!_**

리소스 분산을 위해서 개인적으로는 아래와 같은 custom endpoint로 구성하는 방법이 좋다고 생각한다

- custom reader endpoint: (reader인스턴스 \* n) + writer인스턴스
- custom writer endpoint: writer인스턴스
