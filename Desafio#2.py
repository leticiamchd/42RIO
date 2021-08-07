modo = input('Você tem dólar ou real ? ')
modo2 = modo.lower()
if modo2 == 'dolar':
    dolar = float(input('Quantos dólares você tem ? '))
else:
    real = float(input('Quantos reais você tem ? '))
if modo2 == 'dolar':
    print('Na cotação de hoje seus {} dólares equivalem a {:.2f} reais.'.format(dolar,dolar*5.48))
else:
    print('Na cotação de hoje seus {} reais equivalem a {:.2f} dólares.'.format(real,real/5.48))