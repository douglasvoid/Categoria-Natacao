from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = atual - nasc

if idade <= 9:
    print('A idade do atleta é: {} anos.\nA categoria é: MIRIM'.format(idade))
elif idade <= 14:
    print('A idade do atleta é: {} anos.\nA categoria é: INFANTIL'.format(idade))
elif idade <= 19:
    print('A idade do atleta é: {} anos.\nA categoria é: JUNIOR'.format(idade))
elif idade <= 25:
    print('A idade do atleta é: {} anos.\nA categoria é: SÊNIOR'.format(idade))
else:
    print('A idade do atleta é: {} anos.\nA categoria é: MASTER'.format(idade))
