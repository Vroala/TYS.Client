# -*- mode: python -*-

block_cipher = None


a = Analysis(['background_Start.py'],
             pathex=['C:\\Users\\st-company-pc\\Desktop\\SVN\\TYS.Client\\TEST\\멀티채팅프로그램'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='background_Start',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='chat.ico')
