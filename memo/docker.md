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