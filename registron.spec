# -*- mode: python -*-
a = Analysis(['registron.py'],
             pathex=['/home/bl4ckdu5t/Dev/Python/python lab/registron'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='registron',
          debug=False,
          strip=None,
          upx=True,
          console=False )
