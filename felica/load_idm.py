# -*- coding: utf-8 -*-

from __future__ import print_function
from ctypes import *

# libpafe.hの77行目で定義
FELICA_POLLING_ANY = 0xffff

if __name__ == '__main__':

    libpafe = cdll.LoadLibrary("/usr/local/lib/libpafe.so")

    libpafe.pasori_open.restype = c_void_p
    pasori = libpafe.pasori_open() # デバイスファイルのオープン

    libpafe.pasori_init(pasori) # パソリの初期化

    while True:
        libpafe.felica_polling.restype = c_void_p
        felica = libpafe.felica_polling(pasori, FELICA_POLLING_ANY, 0, 0) # リクエストコマンドを送信し､以降の通信で必要なデータを取得する

        idm = c_ulonglong() #←16桁受けとるために変更
        libpafe.felica_get_idm.restype = c_void_p

        libpafe.felica_get_idm(felica, byref(idm)) # 製造識別子の取得｡第2引数にIDmが格納される｡

        # IDmは16進表記
        print("%016X" % idm.value) #←16桁表示させるために変更
        """
        if idm.value == int('IDm', 16):
            print('Suica')
        elif idm.value == int('IDm', 16):
            print('三井住友iD')
        else:
            print('else')
        """

    # READMEより、felica_polling()使用後はfree()を使う
    # なお、freeは自動的にライブラリに入っているもよう
    libpafe.free(felica)

    libpafe.pasori_close(pasori) # デバイスファイルをクローズ
