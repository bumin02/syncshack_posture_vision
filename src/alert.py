import platform
import os
import sys

def push(title, message):
    plt = platform.system()

    if plt.strip()=='Darwin':
        command = f'''
        osascript -e 'display notification "{message}" with title "{title}"'
        '''

    os.system(command)


if __name__=='__main__':
    
    push(sys.argv[1], sys.argv[2])