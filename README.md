# ⛰️

## Week1. Computing Service: Hello, World!

> - fastAPI로 root에 접속 시 `Hello, World!` 를 반환하는 초간단 서버
> - 도커로 컨테이너화하기
> - EC2(t2.micro)에서 외부접속 가능하도록 도커 띄우기
> - ECS fargate로 외부접속 가능하도록 띄우기

EC2: http://15.168.62.119:8080 <br>
ECS: http://13.208.172.38:8080

#### EC2

1. EC2 컨테이너 생성 및 pem 키 발급
2. EC2 접속
   ```
   chmod 400 {filename}.pem
   ssh -i {filename}.pem {username}@{server-ip}
   ```
3. 보안그룹 -> inbound rules 에서 사용하고자 하는 포트 열기
4. 도커 설치 ([Docs](https://docs.docker.com/engine/install/ubuntu/))
5. 도커 띄우기
   ```
   git clone https://github.com/treblenalto/infra-study.git
   sudo docker-compose up
   ```

#### ECR

1. AWS CLI 로그인
   ```
   aws configure sso
   aws sso login --sso-session {session-name}
   ```
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

## Week2. Storage Service: Store & Load

#### Lambda

> S3 에 파일 업로드 시 슬랙 채널에 메세지가 오도록 하는 Lambda 구현

1. AWS Lambda > Functions > Create Function
2. 함수 이름과 런타임 설정
3. Lambda 트리거 설정 (ex. S3 버켓, 이벤트 등)
4. 슬랙으로 알람 보내주는 코드 작성
   1. 이벤트로부터 메타데이터 받아와 원하는 정보 파싱
   2. 민감한 정보들은 환경변수로 설정
5. 💡 디버깅할 때 S3를 통해 계속 트리거하기보다는 목표하는 이벤트 로그로부터 테스트를 설정해 돌리는 것이 편하다

#### [EBS, EFS, S3](https://www.notion.so/corcaai/week2-809a95fb8fd24016817db477f9f4adca?pvs=4)

> EC2에서 EBS, EFS, S3에 각각 파일을 100번씩 store, load 하는 시간 측정 및 비교

| Storage Service | Avg. Store Time | Avg. Load Time |
| :-------------: | :-------------: | :------------: |
|       EBS       |    0.062 sec    |   0.072 sec    |
|       EFS       |    0.079 sec    |   0.071 sec    |
|       S3        |    0.097 sec    |   0.076 sec    |

- Store: S3 > EBS = EFS
- Load: S3 > EFS > EBS
- EBS, EFS 가 EC2에 마운트해서 사용 가능한 만큼 store/load 모두 S3 보다 빠른 결과를 보임
- S3 의 write 연산이 특히 오래 걸림
- EFS 의 경우 파일시스템이 복잡해지면 검색 시간이 늘어난다고 하는데 이번에 진행한 태스크에서는 간단한 구조라 EBS 와 큰 차이를 보이지는 않았음
- 빠른 데이터 접근에는 EBS가 가장 좋지만 여러 개의 EC2 인스턴스에서 동시접근해야 하는 데이터일 경우 EFS가 적합해보임

#### EBS

1. EC2 인스턴스 스토리지로 EBS 를 지정해서 인스턴스 생성 or EBS 볼륨 추가
2. EBS 볼륨 연결 확인 - 디바이스 명이 /dev/sdf or /dev/sda 일 시 최신 Linux 커널이 내부적으로 xvdf으로 변경
   ```
   ls -asl /dev/xvd*
   ```
3. EBS 볼륨 파일시스템 포맷
   1. `/dev/xvdf: data` -> 파일시스템 존재 X
   2. Linux 파일시스템: ext, ext2, ext3, ext4, xfs
   ```
   file -s /dev/xvdf # 파일시스템 존재여부 확인
   df -hT # root 파일시스템 확인
   mkfs -t {volume type} /dev/xvdf
   ```
4. EBS 볼륨 마운트

   ```
   blkid # 파일시스템 UUID, TYPE 확인

   sudo vi /etc/fstab # 마운트 할 파일시스템의 UUID 추가
   sudo mount -a
   ```

#### EFS

1. EFS 전용 보안그룹 생성
2. EFS 파일시스템 생성 밎 보안그룹 설정
3. EC2 보안그룹에 EFS 보안그룹 추가
4. EFS 마운트

   ```
   sudo apt-get install nfs-common
   sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport {file-system-id}.efs.{region}.amazonaws.com:/ {mount-point}
   ```

#### S3

1. EC2에 AWS CLI 설치 및 SSO 로그인
2. Boto3 활용해 파일 업로드/다운로드
