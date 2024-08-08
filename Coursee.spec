# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main_gui.py', 'excute.py'],
    pathex=[],
    binaries=[('chromedriver', '.')],
    datas=[('login.txt', '.'), ('HYU_pic.png', '.'), ('style.kv', '.'), ('msyhl.ttc', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Coursee',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['Hello World.icns'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Coursee',
)
app = BUNDLE(
    coll,
    name='Coursee.app',
    icon='Hello World.icns',
    bundle_identifier=None,
)
