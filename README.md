# Flask_Base_Template
python3를 사용합니다.
## Project setup
```
python3 -m venv venv
source venv/bin/activate (linux & mac)
call venv/Script/activate (window)

pip install -U pip
pip install -U setuptools
pip install -r requirements.txt
```

### Compiles and hot-reloads for development
```
flask run
```

### deploy
```
배포는 방식에 따라 다르니 차후 따로 정리해 놓겠습니다.
```

### env
```.env
FLASK_APP=Flask_Base_Template
FLASK_ENV=development
FLASK_RUN_PORT=8000

#DB
MONGODB_DATABASE=potato
MONGODB_PORT=27027
MONGODB_USER=potato
MONGODB_PASSWORD=potato123
MONGODB_URI=mongodb://potato:potato123@127.0.0.1:27027/test
```

### DB
```shell script
sudo docker-compose -f ./docker-compose.yml up --build -d db
```

# 깃 리모트 변경 하기
## 기존 리포지토리 깔끔하게 pull / push
```git pull
git add .
git commit -m "clean push"
git push
```

## 기존 리포지토리 remote 제거
```git remote remove origin```

## 새 리포지토리 remote 추가
```git remote add origin https://github.com/계정/리포지토리```