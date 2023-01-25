email=input()
if '@gmail.com' == email[-10:]:
    first= email[0].lower()
    if first in 'abcdefghijklmnopqrstuvwxyz':
        print('valid')
else:
    print('invalid')
        
    
    
