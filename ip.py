import socket

print(''' \033[1;30m   

███    ███ ██    ██       ██ ██████  
████  ████  ██  ██        ██ ██   ██ 
██ ████ ██   ████   █████ ██ ██████  
██  ██  ██    ██          ██ ██      
██      ██    ██          ██ ██      
               

                                    ''')
print(''' \033[1;31m 
        ==========================
        # py ==> naif-alajmi     #
        # my snapchat ==> qzmq1  #
        # my instagram ==> 3kfe_ #
        # my tiktok ==> preac_   #
        # my Github ==> qzmq1    #
        ==========================
''')
print(''' \033[1;34m   

[01] about

[02] show my ip and desktop

''')
chinput = input(' Enter the number :')
if chinput == '2':
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print("\033[1;36m", IPAddr)
    print("\033[1;36m", hostname)

if chinput == '1':
        print('''
        
        py ==> naif-alajmi
        
        instagram ==> 3kfe_
        
        my snapchat ==> qzmq1
        
        my tiktok ==> preac_
        
        my Github ==> qzmq1
        
        ''')
