# ⛰️

## Week1. Computing Service: Hello, World!

EC2: http://15.168.62.119:8080 <br>
ECS: http://13.208.172.38:8080

#### EC2

1. EC2 컨테이너 생성 및 pem 키 발급
2. EC2 접속
   ```
   chmod 400 {filename}.pem
   ssh -i {filename}.pem {username}@{server-ip}
   ```
3. Security groups -> inbound rules 에서 사용하고자 하는 포트 열기
4. 도커 설치 ([Docs](https://docs.docker.com/engine/install/ubuntu/))
5. git clone
6. sudo docker-compose up

#### ECR

1. aws cli 로그인
2. ECR 접속
   ```
   aws ecr get-login-password --region {region} | docker login --username AWS --password-stdin {account-id}.dkr.ecr.{region}.amazonaws.com
   ```
3. 이미지 태깅
   ```
   docker tag {name}:{tag} {ecr-repo-uri}:{tag}
   ```
4. 이미지 푸시
   ```
   docker push {name}:{tag} {ecr-repo-uri}:{tag}
   ```

#### ECS

1. ECS 클러스터 생성
2. ECS task definition 생성
   1. 실행할 이미지 uri 설정
   2. 도커 이미지가 빌드 된 아키텍쳐와 같은 환경으로(x86, ARM64) 설정
3. 태스크 실행
   1. 태스크 실행 시 EC2와 마찬가지로 보안그룹 설정
