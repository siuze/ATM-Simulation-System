# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=['atm.py', 'card_out.py', 'cash.py', 'cash1.py', 'cashAccount.py', 'deposit.py', 'deposit1.py', 'func.py', 'hnu_rc.py', 'inquiry.py', 'login.py', 'main.py', 'manager.py', 'pwchange.py', 'record.py', 'signup.py', 'transfer.py'],
    binaries=[],
    datas=[],
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
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='logo.ico',
)
