# delLine.py
from tkinter import filedialog

inputFile = filedialog.askopenfilename()  # 読み込みファイル
inputwidth = input("横幅を入力してください。")
inputheight = input("縦幅を入力してください。")

with open(inputFile, encoding='shift_jis') as f:
    l = f.readlines()
    l[89] = "Height = " + inputheight + "\n"
    l[90] = "Width = " + inputwidth + "\n"
  
with open(inputFile, 'w') as f:
    for d in l:
        f.write(d)             