import cx_Freeze
import sys

base= None

if sys.platform == 'win32':
    base = "Win32GUI"
    
executables = [cx_Freeze.Executable("combustion.py", base=base)]

cx_Freeze.setup(
        name="SeaofBTC-Client",
        options={"build_exe": {"packages":["tkinter", "numpy", "pandas", "sympy", "tkinter.messagebox", "os"],
                               "include_files": ["thermo_Data.xlsm", "algo.png", "layout_feed.gif",
                                                 "thermo_Data_display.xlsm"]}},
        version="0.01",
        description="Combustion Analyzer",
        executables=executables
        )

