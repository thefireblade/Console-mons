'''
Created on Mar 11, 2018

@author: Jason
'''
import cx_Freeze
from cx_Freeze import setup, Executable
import sys
base = 'Win32GUI' if sys.platform=='win32' else None
buildOptions = dict(packages = [], 
	excludes = [],
    includes = ["Trainer", "api"],
    include_files = [])
setup(
    version = '0.1',
    name = 'Pokemon RPG : ALPHA',
    description = 'A Pokemon Parody Game created by JASON HUANG',
    options = dict(build_exe = buildOptions),
    executables = [Executable("driver.py", base = base)]
    )

