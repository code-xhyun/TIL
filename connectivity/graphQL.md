# GraphQL

GraphQL은 Query Language 중에서도 Server API 를 통해 정보를 주고받기 위해 사용하는 Query Language 이다.
웹 클라이언트가 데이터를 서버로 부터 효율적으로 가져오는 것이 목적

RestApi의 단점이라 생각하는 아래 두가지를 효율적으로 해결

- 오버페칭
- 언더페칭

### GraphQL Subscription

구독을 통해 클라이언트는 서버의 실시간 메시지를 수신 가능

[참조](https://dgraph.io/docs/graphql/subscriptions/)

### Schema-First-Develoment

스키마 우선주의는 디자인 방법론의 일종입니다. 말 그대로 개발 시에 스키마를 우선적으로 개발하는 것입니다. 여기사 스키마(Schema)란 데이터 타입의 집합 입니다. 이를 미리 정의해 두면, 스키마 정의는 API 문서 같은 역할을 하며, 프론트엔드 개발자와 백엔드 개발자가 많은 의사소토에 대한 비용을 줄이고, 빠른 개발을 할 수 있다는 장점이 있습니다.

백엔드 개발자는 어떤 데이터를 전달해야 하는지, 프론트엔드 개발자는 인터페이스 작업을 할 때 필요한 데이터를 정의할 수 있는 것입니다.

[참조](https://velog.io/@sms8377/Server-GraphQL-API-Apollo-Client)

[REF](https://deview.kr/data/deview/session/attach/1100_T1_%E1%84%87%E1%85%A1%E1%86%A8%E1%84%89%E1%85%A5%E1%86%BC%E1%84%92%E1%85%A7%E1%86%AB_GraphQL%20API%20%E1%84%81%E1%85%A1%E1%84%8C%E1%85%B5%E1%86%BA%E1%84%80%E1%85%A5%20%E1%84%8B%E1%85%AE%E1%86%AB%E1%84%8B%E1%85%A7%E1%86%BC%E1%84%92%E1%85%A2%E1%84%87%E1%85%A9%E1%84%8C%E1%85%B5%20%E1%84%86%E1%85%AF.pdf)
