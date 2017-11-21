from os import listdir
for file in listdir('/Users/smarman/Documents/repos/configuration-management/ansible/host_vars'):
    if 'ccapi' in file:
        print (file)
    
