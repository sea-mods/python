
import PySimpleGUI as sg

sg.theme('DarkAmber')   # デザインテーマの設定

# ウィンドウに配置するコンポーネント
layout = [
            [sg.Text('      config.cfg path', size=(15, 2))],
            [sg.FileBrowse('    ファイルを選択    ', key='inputFilePath')],
            [sg.InputText(size=(19, 1))],
            [sg.Text('       縦幅 (Height)')],
            [sg.InputText(size=(19, 1))],
            [sg.Text('       横幅 (Width) ')], 
            [sg.InputText(size=(19,1))],
            [sg.Button('  change  '), sg.Button('  cancel  ')] ]

# ウィンドウの生成
window = sg.Window('osu! resolution changer', layout)

# イベントループ
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == '  cancel  ':
        break
    elif event == '  change  ':
        with open(values['inputFilePath'], encoding='shift_jis') as f:
            l = f.readlines()
            l[89] = "Height = " + values[1] + "\n"
            l[90] = "Width = " + values[2] + "\n"                                    
        with open(values['inputFilePath'], 'w') as f:
            for d in l:
                f.write(d)  
    break  


window.close()





