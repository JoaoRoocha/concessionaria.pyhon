idade = int(input('Digite a sua idade: '))

if idade < 0 or idade > 120:
    print('ERRO: Idade inválida.')
else:
    if idade >= 18:
        print('Venha dar uma conferida em nossos veículos. Será um prazer te atender!')
    else:
        print('Deseja dar uma olhada em nosso espaço kids? Garanto que por lá a diversão é garantida!')
