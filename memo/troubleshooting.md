## Node.jsでCannot find moduleでパッケージのインストールができないとき
```
$ sudo npm install -f --unsafe-perm node-gyp
$ sudo node-gyp rebuild
$ sudo npm install [インストールしたいパッケージの名前]
```
参考: https://qiita.com/nanashi-tech/items/0b429d654848fcb265e8
