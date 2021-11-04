## DECENTER SERVER 연결


### 관련 코드 가져오기 (현재 설정 위치 : /opt/DECENTER)
○ 현재는 /opt 에 설치하였지만 다른 경로를 원하는 경우 /opt 를 -> /{new_path} 로 바꿔서 실행해주면 된다. ex ) /opt/DECENTER -> /datadrive/DECENTER

```
$ cd /opt
$ mkdir DECENTER
$ cd DECENTER
$ git clone https://github.com/decenter-keti/ai-model-repository.git
```


### python 환경 설정

○ 아래 두가지 방법 중에 하나로 진행

```
$ cd /opt/DECENTER/ai-model-repository
$ conda env create -f environment.yml -n decenter
$ conda activate decenter
```

```
$ cd /opt/DECENTER/ai-model-repository
$ conda create --name decenter python=3.8 -y
$ conda activate decenter
$ pip3 install -r requirements.txt
```


### uwsgi 설정 파일 변경

```
$ cd ai-model-repository
$ sudo vim uwsgi_decenter.ini
```

○ 명령어를 입력 후, 아래 파일의 경로를 해당 경로에 맞게 수정
```
[uwsgi]
  (생략)
  wsgi-file = model_server.py
  (생략)
  daemonize=/opt/DECENTER/ai-model-repository/log.log
  (생략)
  chdir = /opt/DECENTER/ai-model-repository/
  virtualenv = /opt/anaconda3/envs/decenter
```


### 서버 실행

```
$ cd /opt/DECENTER/ai-model-repository
$ sudo sh server.sh
  [uWSGI] getting INI configuration from /opt/DECENTER/ai-model-repository/uwsgi_decenter.ini
  
# 확인
$ curl localhost:20002/home
  <!DOCTYPE html>
  <html lang="en">
  ... 생략
```
