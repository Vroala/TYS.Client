# -*- mode: python -*-

block_cipher = None


a = Analysis(['2.0ver_Client.py'],
             pathex=['C:\\Users\\st-company-pc\\Desktop\\SVN\\TYS.Client\\채팅프로그램 완성작'],
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
          name='2.0ver_Client',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='chat.ico')
