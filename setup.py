'''
Created on Mar 11, 2018

@author: Jason
'''
import cx_Freeze
from cx_Freeze import setup, Executable
setup(
    version = '0.1',
    name = 'Pokemon RPG : ALPHA',
    description = 'A Pokemon Parody Game created by JASON HUANG'
    options = {'build_exe' :{'packages': ['api', 'Trainer']} },
    executables = [Executable("driver.py",)]
    )

