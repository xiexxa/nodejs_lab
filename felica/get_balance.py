# -*- coding: utf-8 -*-

from __future__ import print_function
from ctypes import *

# libpafe.hの77行目で定義
FELICA_POLLING_ANY = 0xffff

# 構造体の代わりとなるクラスの定義
class felica_block_info(Structure):
    _fields_ = [
        ("service", c_uint16),
        ("mode", c_uint8),
        ("block", c_uint16)
    ]

if __name__ == '__main__':

    libpafe = cdll.LoadLibrary("/usr/local/lib/libpafe.so")

    libpafe.pasori_open.restype = c_void_p
    pasori = libpafe.pasori_open()

    libpafe.pasori_init(pasori)

    libpafe.felica_polling.restype = c_void_p
    felica = libpafe.felica_polling(pasori, FELICA_POLLING_ANY, 0, 0)

    # Cのint型配列の定義(長さ16)
    int_array16 = c_uint8 * 16

    # 応答データ
    data = int_array16()
    # サービスコードのリスト
    info = felica_block_info(c_uint16(0x090f), c_uint8(0), c_uint16(0))
    for i in range(0, 32):
        c_i = c_int(i)
        libpafe.felica_read(felica, byref(c_i), byref(info), byref(data))
        if (data[1] > 0) or (data[2] > 0):
            print("残高:", data[11] * 256 + data[10], "円")
            break

    libpafe.free(felica)

    libpafe.pasori_close(pasori)
