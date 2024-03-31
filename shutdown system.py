import os

print('Operating System :',os.name)#find OS name


def shutdown():
    if (os.name == 'nt'):  # For Windows
        os.system('shutdown /s /t 1')

    elif (os.name == 'posix'):  # For Linux/Unix/MacOS
        os.system('sudo shutdown now')

    else:
        print("Unsupported operating system.")


shutdown() #call to Shutdown function    
