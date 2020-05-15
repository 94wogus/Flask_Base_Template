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
배포는 방식에 따라 다르니 차우 따로 정리해 놓겠습니다.
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
MONGODB_URI=mongodb://potato:potato123@127.0.0.1:27017/potato
```

### DB
```shell script
sudo docker-compose -f ./docker-compose.yml up --build -d db
```