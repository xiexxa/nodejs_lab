- 稼働中のコンテナ一覧  
`$ docker ps`
- コンテナ一覧  
`$ docker ps -a`
- コンテナ生成  
`$ docker run --name "namae" -d -it -p 80:80 ubuntu:20.04`
- コンテナ削除  
`$ docker rm [コンテナ名]`
- 起動中のコンテナに接続  
`$ docker attach [コンテナ名]`
- 起動中のコンテナに接続2
`$ docker exec -it [コンテナに接続] bash`
- イメージをダウンロード  
`$ docker pull [イメージ名]`
- イメージを削除  
`$ docker rmi [イメージ名]`

# Apacheを動かすには
--privilegedと/sbin/initを指定しないとエラーが出る。  
`$ docker run --name jikken_php -d -it -p 80:80 --privileged centos:8 /sbin/init`

# docker-composeで作ったコンテナにexec -itでシェルログインしたいが、エラーが出るとき
OCI runtime exec failedとエラーが出るときは、以下のようにbashではなくshでログインして対処する。
`$ docker exec -it [コンテナ名] /bin/sh`

# docker上でnode.jsを動かす
参考: https://zenn.dev/ymasaoka/articles/start-nodejs-development-with-docker  
1. プロジェクトディレクトリを作る  
`$ mkdir docker-nodejs-app`

2. docker-composeとDockerfileを作る　　
先程作ったディレクトリの中に、docker-compose.ymlを以下のように作成する。
```
version: '3'

services:
  app:
    image: node:lts
    build:
        context: .
        dockerfile: Dockerfile
    ports:
      - 3000:3000
    container_name: nodejs-vm
    tty: true
    volumes:
      - ./src:/src
    working_dir: "/src"
```
次にDockerfileを作る
```
FROM node:lts
RUN touch text.txt
RUN apt -y update
RUN apt install -y vim
```

3. コンテナを起動する  
`$ docker-compose up -d --build`  
--buildオプションを指定することでDockerfileが実行される

4. 任意のコマンドをコンテナに対して実行する  
`$ docker-compose run --rm app node -v`  
node -vを実行した結果が表示される。

5. シェルに入って操作する  
`$ docker exec -it nodejs-vm /bin/sh`

- その他
    以下のコマンドはdocker-compose.yamlのあるディレクトリで実行すると、コンテナ名やIDの指定の必要なく作用してくれる。　　
    - docker-composeで作ったコンテナを止める  
    `$ docker-compose stop`
    - docker-composeで作ったコンテナを削除する  
    `$ docker-compose rm`