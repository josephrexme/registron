# -*- mode: python -*-
a = Analysis(['registron.py'],
             pathex=['C:\\Users\\Joseph Rex\\Desktop\\Python Windows\\registron\\registron'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='registron.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='registron.ico')
