# #!/usr/bin/env python
# *-# -*- coding: utf-8 -*-


#駒と局面の内部表現
OUT_OF_BOARD = 64
EMPTY = 0
FU = 1
KY = 2
KE = 3
GI = 4
KI = 5
KA = 6
HI = 7
OU = 8
PROMOTED = 8
TO = PROMOTED + FU
NY = PROMOTED + KY
NK = PROMOTED + KE
NG = PROMOTED + GI
UM = PROMOTED + KA
RY = PROMOTED + HI
ENEMY = 16
EFU = ENEMY + FU
EKY = ENEMY + KY
EKE = ENEMY + KE
EGI = ENEMY + GI
EKI = ENEMY + KI
EKA = ENEMY + KA
EHI = ENEMY + HI
EOU = ENEMY + OU
ETO = ENEMY + TO
ENY = ENEMY + NY
ENK = ENEMY + NK
ENG = ENEMY + NG
EUM = ENEMY + UM
ERY = ENEMY + RY

komastr = ["　・","△歩","△香","△桂","△銀","△金","△角","△飛","△玉",
           "△と","△杏","△圭","△全","△金","△馬","△竜",
           "　・","▼歩","▼香","▼桂","▼銀","▼金","▼角","▼飛","▼王",
           "▼と","▼杏","▼圭","▼全","▼金","▼馬","▼竜"]


def is_enemy_retn(koma):
    return koma + ENEMY
def is_self_retn(koma):
    return FU <= koma and koma <= RY

def is_enemy(sengo, koma):
    if sengo == 0:
        return is_enemy_retn(koma)
    return is_self_retn(koma)
def is_self(sengo, koma):
    if sengo == 0:
        return is_self_retn(koma)
    return is_enemy_retn(koma)

hand = [[0 for j in range(HI + 1)] for i in range(2)]

board = [[EKY,EKE,EGI,EKI,EOU,EKI,EGI,EKE,EKY],
               [EMPTY,EHI,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EKA,EMPTY],
               [EFU,EFU,EFU,EFU,EFU,EFU,EFU,EFU,EFU],
               [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
               [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
               [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
               [FU,FU,FU,FU,FU,FU,FU,FU,FU],
               [EMPTY,KA,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,HI,EMPTY],
               [KY,KE,GI,KI,OU,KI,GI,KE,KY]]


class KYOKUMEN():
    display_li_str = []

    display_li_str.append("先手　持ち駒 \n")
    for koma in range(FU, HI + 1):
        if hand[0][koma] == 1:
            display_li_str.append("%s " % komastr[koma])
        elif hand[0][koma] > 1:
            display_li_str.append("%s%d " % (komastr[koma], hand[1][koma]))
    display_li_str.append("　　　９　８　７　６　５　４　３　２　１　\n")
    display_li_str.append("　＋−−−−−−−−−−−−−−−−−−＋\n")
    for dan in range(0,9):
        display_li_str.append("%s | " % [
            "一","二","三","四","五","六","七","八","九"][dan])
        for suji in range(8, -1, -1):
            display_li_str.append("%s " % komastr[board[dan][suji]])
        display_li_str.append("｜\n")
    display_li_str.append("　＋−−−−−−−−−−−−−−−−−−＋\n")
    display_li_str.append("後手 持ち駒 \n")
    for koma in range(FU, HI + 1):
        if hand[1][koma] == 1:
            display_li_str.append("%s " % komastr[koma])
        elif hand[1][koma] > 1:
            display_li_str.append("%s%d " % (komastr[koma], hand[1][koma]))

    print("".join(display_li_str))