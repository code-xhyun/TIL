# route 53

route 53의 `failover`기능은
route 53이 기본사이트 `ELB 상태를 감시`하게 된다.
ELB에 연결된 EC2 인스턴스와 애플리케이션이 모두 다운되었다고 판단되면 route 53은 `자동으로 백업 사이트의 ELB로 연결을 재설정`한다
