import webview
import os
import sys

def get_html_path():
    if getattr(sys, 'frozen', False):
        base_dir = sys._MEIPASS
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, 'MiniDisc_Label_Generator.html')

if __name__ == '__main__':
    html_file = get_html_path()
    window = webview.create_window('MiniDisc 标签设计器 (竖向双列排版版)', html_file, width=1100, height=800, resizable=True)
    webview.start()
