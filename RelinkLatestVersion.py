import os
import subprocess
dirList = next(os.walk(".\\", topdown=True, followlinks=False))[1]
try:
    dirList.remove('latest')
except ValueError:
    pass
print('Select a directory to link: ')
print('--------------')
numTemp = 0
for numDisp in dirList:
    numTemp += 1
    print(numTemp + ": " + numDisp)
print('--------------')
while True:
    verIndex = int(input('Input the number: '))
    if ValueError:
        print('\033[0;33m[Warning]\033[0m Please enter a number.')
    elif verIndex > len(dirList):
        print('\033[0;33m[Warning]\033[0m The number is too big.')
    elif verIndex < 0:
        print('\033[0;33m[Warning]\033[0m The number should be a positive number.')
    else:
        break
subprocess.call('rd latest>nul', shell=True)
subprocess.call(['mklink', '/J', 'latest', dirList[int(verIndex)-1], '>nul'], shell=True)
print('Done!')
print('Press any key to quit.')
os.system('pause>nul')
