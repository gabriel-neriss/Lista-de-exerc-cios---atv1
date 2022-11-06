
dia_da_semana= input('Dia da compra?')
prazo_de_entrega = int(input('Prazo de entrega?'))

if dia_da_semana == 'domingo':
    dia_da_semana = 1
elif dia_da_semana == 'segunda':
    dia_da_semana = 2
elif dia_da_semana == 'terca':
    dia_da_semana = 3
elif dia_da_semana == 'quarta':
    dia_da_semana = 4
elif dia_da_semana == 'quinta':
    dia_da_semana = 5
elif dia_da_semana == 'sexta':
    dia_da_semana = 6
elif dia_da_semana == 'sabado':
    dia_da_semana = 7

  
if dia_da_semana + prazo_de_entrega > 7:
    dia_entrega = dia_da_semana + prazo_de_entrega - 7
    
else :
    dia_entrega = dia_da_semana + prazo_de_entrega


if dia_entrega == 1:
    dia_entrega = 'domingo'
elif dia_entrega == 2:
     dia_entrega = 'segunda'
elif dia_entrega == 3:
     dia_entrega = 'terca'
elif dia_entrega == 4:
     dia_entrega = 'quarta'
elif dia_entrega == 5:
     dia_entrega= 'quinta'
elif dia_entrega == 6:
     dia_entrega = 'sexta'
elif dia_entrega == 7:
     dia_entrega = 'sabado'


if prazo_de_entrega == 0:
   print ('chega hoje!')
else:
  print ('sera entregue' + ' ' + dia_entrega)
