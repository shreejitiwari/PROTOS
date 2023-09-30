print('type something !!!')

while True:
    with open('spkr.txt', 'r+') as f:
        spkr=f.read().split(',')
    with open('prototxt.txt', 'r+') as f:
        proto=f.read().split(',')
        

    user=input('YOU : ')    
    for sen in spkr[0:len(spkr)]:
        if sen==user.lower():
            n=spkr.index(sen)
            print('PROTO : ',proto[n])
            break
    else:
        print('PROTO : Sorry, I don\'t have anything to say about it.\nmere paas abhi iss baare me kuchh kahne ko nhi hai...maaf kijiye.')
            
        
    
