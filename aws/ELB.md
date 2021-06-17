# ELB

- CLB (Classic Load Balancer)

```
가장 오래된 로드밸런서
L7,L4 둘다 지원
EC2-Classic 대상으로 지원
```

- ALB (Application Load Balancer)

```
L7 부하분산 지원(IP+PORT)
HTTP,HTTPS 트래픽을 로드밸런싱해서 내부 인스턴스에 전달
클라이언트가 웹화면을 요청하는 상황
```

- NLB (Network Load Balancer)

```
L4 부하분산 지원(IP+PORT+packet)
TCP/UDP 트래픽을 로드밸런싱해서 내부 인스턴스에 전달
내부로 들어온 트래픽 처리, 내부의 인스턴스로 트래픽전송
```
