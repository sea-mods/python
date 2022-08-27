#PP calculator test 最終的な目標:関数にする
import math
#入力されたmodから合うものを探す
while True:

    mods = input("使用modを入力してください。")
    HR = 'HR' in mods
    HD = 'HD' in mods
    DT = 'DT' in mods
    FL = "FL" in mods
    HT = 'HT' in mods
    EZ = 'EZ' in mods
    NF = 'NF' in mods
    if DT and HT == True:
        print("DTとHTは同時に使えません。")
        continue
    elif HR and EZ == True:
        print("HRとEZは同時に使えません。")
        continue
    else:
        break
    


ms = 0
note = input('総ノーツ数を入力してください。')
greet = input('良の数を入力してください。')
good = input('可の数を入力してください。')
bad = input('不可の数を入力してください。')
SR = input('SRを入力してください(DT,HTを付けた場合はそのSRを入力してください。)')
seido = input('accを入力してください。')
if HD == True:
    HD = 1.025
    HD2 =1.1
else:
    HD = 1
    HD2 = 1    
if FL == True:
    FL = 1.05
else:
    FL = 1

if NF == True:
    NF = 0.9
else:
    NF = 1    

#int変換

note = int(note)    
SR = int(SR)
bad = int(bad)
good = int(good)
greet = int(greet)
seido = int(seido)

#EZ,HRをつけたときのOD計算
OD = input('ODを入力してください。')
OD = float(OD)


if HR == True:
   OD = (OD) * 1.4 // 1.0

elif EZ == True:
    OD = OD * 0.5
OD = float(OD)    
OD = math.floor(OD) / 10
#良判定範囲計算
teiri = float(OD * 3 // 1)
if DT == True:
    ms = (49.5 - teiri) / 1.5
elif HT == True:
    ms = 49.5 - teiri / 0.75
else:
    ms = (49.5 - teiri)  
     

miss = 0.0
miss = 0.985 ** int(bad) 
resr = SR / 0.0075
hanni = note / 1500 
if int(resr) <= 1:
    resr = 1
if hanni <= 1:
    hanni = 1    
promise = (note / 1500) ** 0.5 
if promise <= 1.15:
    promise = 1.15   
siki1 = miss * (resr * 5 - 4) ** 2 / 100000  * seido * (1 + 0.1 * hanni) * (HD * FL) ** 1.1
siki2 = (150 / ms) ** 1.1 * (seido / 100) ** 15 * 22 * (promise ** 1.1) ** (1 / 1.1) * HD * NF * 1.1
pp = siki1 + siki2
print(pp)


     
 
