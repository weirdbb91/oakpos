# Oakpos

OakTOP에서 낄낄거리며 사용할 포스 시스템  
장고와 리액트를 배우면서 써 볼 예정  


# 프로젝트 구성 요소

- 백엔드: Django
- DBMS: MySQL
- 프론트엔드: React


# 개발 요구사항

- Docker 20.10.12+
- Python 3.9+
- MySQL 8.0+
- Node 17.5.0+


# 디렉토리 구성

```python
project/
├── api/        # 장고 앱
├── env/        # 환경변수
├── frontend/   # 리액트 앱
└── oakpos/     # 장고 프로젝트
```
# 개발 환경 준비

```python
# env/local.env 파일에 환경변수 저장
APP_SECRET_KEY=""           # 앱에서 사용할 시크릿 키, 입력 필수
MYSQL_ROOT_PASSWORD="pass"  # 루트_비밀번호
MYSQL_DATABASE="db"         # 데이터베이스_이름
MYSQL_USER="user"           # 사용자_이름
MYSQL_PASSWORD="pass"       # 사용자_비밀번호
MYSQL_HOST="db"             # 데이터베이스_호스트
MYSQL_PORT="3306"           # 데이터베이스_포트
```

# 개발환경 실행

```
$ docker-compose -f docker-compose.local.yml up
Starting oakpos.db-mysql ... done
Starting oakpos.backend-django ... done
Attaching to oakpos.db-mysql, oakpos.backend-django
oakpos.db-mysql | 2022-04-04 06:08:33+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.28-1.el8 started.
oakpos.backend-django | 2022/04/04 06:08:34 Waiting for: tcp://db:3306
oakpos.backend-django | 2022/04/04 06:08:34 Problem with dial: dial tcp 172.27.0.2:3306: connect: connection refused. Sleeping 1s
...
oakpos.backend-django | 2022/04/04 06:08:37 Connected to tcp://db:3306
oakpos.backend-django | database connected
...
oakpos.backend-django | Django version 4.0.3, using settings 'oakpos.settings'
oakpos.backend-django | Starting development server at http://0.0.0.0:8000/
oakpos.backend-django | Quit the server with CONTROL-C.
```

`docker-compose -f docker-compose.local.yml up` 명령어를 실행하면  
oakpos.backend-django에서 `docker-entrypoint.sh`를 엔트리 포인트로 실행하게 되고  
oakpos.db-mysql에서 정상적인 답변이 올 때 까지 60초간 확인한다  
정상적인 답변을 수신하고 나서야 [http://0.0.0.0:8000/](http://0.0.0.0:8000/) 주소로 서버를 작동시킨다