n_amigo = int(input ('n'))

resultado = n_amigo % 2 

# nª com entrada impar / saída de um nº impar anterior e posterior ao de entrada

def primeiro_impar ():
    if resultado == 1:
        return n_amigo - 2
def segundo_impar ():
    if resultado == 1:
        return n_amigo + 1

# nª com entrada par / saída de um nº impar anterior e posterior ao de entrada


def primeiro_par ():

    if resultado == 0:
        return n_amigo - 1
    
def segundo_par ():
    if resultado == 0:
        return n_amigo + 2
    
  
    
impar_1 = (str(primeiro_impar()))
impar_2 =(str(segundo_impar()))

par_1 = (str(primeiro_par()))
par_2 = (str(segundo_par()))


if resultado == 1:
    print (impar_1 + ' ' + impar_2)
    
elif resultado == 0:
    
        print (par_1 + ' ' + par_2)
