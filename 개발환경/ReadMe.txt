*.ui파일을 .py파일로 바꾸기*
pyuic5 -x 파일이름.ui -o 파일이름.py

*.py파일을 .exe파일로 바꾸기*
pyinstaller.exe -F --noconsole 파일이름.py

disk안에 파일이 실행파일

*.qrc 리소스 파일을 _rc.py로 바꾸기*
pyrcc5 파일이름.qrc -o 파일이름_rc.py

