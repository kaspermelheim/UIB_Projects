msg = "cnbcrwp xdc juu yxbbrkun tnhb dwcru rw cqrb fjh rb anonaanm cx jb j kadcn-oxaln bnjalq, xa ngqjdbcren bnjalq, jwm ljw rw yarwlryun kn jyyurnm jpjrwbc jwh lryqna. Rc bdllnnmb fqnw cqn wdvkna xo tnhb rb cxx bvjuu, r.n. fqnw cqn tnh byjln xo cqn lryqna rb bdoorlrnwcuh bvjuu" 
apb = "abcdefghijklmnopqrstuvwxyz"

for key in range(len(apb)):

    translated = ''
    
    for symbol in msg:
        if symbol in apb:
            num = apb.find(symbol)
            num = num - key
            
            if num < 0:
                num = num + len(apb)
            
            translated = translated + apb[num]
            
        else:
            translated = translated + symbol

    print('Key #%s: %s' % (key, translated))