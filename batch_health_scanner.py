import os


os.system("sfc /scannow")
os.system("DISM.exe /Online /Cleanup-image /Scanhealth")
os.system("DISM.exe /Online /Cleanup-image /Restorehealth")

