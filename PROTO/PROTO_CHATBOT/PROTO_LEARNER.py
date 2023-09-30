while True:
      s1=(input('Speaker 1 : '))
      s2=(input('Speaker 2 : '))

      with open('prototxt.txt', 'a+') as f:
          f.write(s2.lower()+',')
          
      with open('spkr.txt', 'a+') as f:
          f.write(s1.lower()+',')

