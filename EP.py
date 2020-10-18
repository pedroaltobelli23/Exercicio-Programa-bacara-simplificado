# EP - Design de Software
# Equipe: Pedro Altobelli
# Data: 18/10/2020

import random
jogo = True

fichas_totais = int(input('quantas fichas voce tem no total?: '))
#perguntar em quem o jogador quer apostar

em_quem_apostou = input('Deseja apostar em quem?(banco,jogador ou empate): ')

#quanto vai apostar

quanto_vai_apostar = int(input('Quanto deseja apostar?: '))


while jogo :
    # definicao das cartas do banco e do jogador e depois suas somas
    bacara = True
    proximas_rodadas = True
    lista_com_valores = [1,2,3,4,5,6,7,8,9,0,0,0,0]
    lista_de_cartas = lista_com_valores*4
    a = random.choice(lista_de_cartas)
    b = random.choice(lista_de_cartas)
    lista_jogador = [a,b]
    c = random.choice(lista_de_cartas)
    d = random.choice(lista_de_cartas)
    e = random.choice(lista_de_cartas)
    f = random.choice(lista_de_cartas)
    lista_banco = [c,d]
    soma_jogador = (lista_jogador[0] + lista_jogador[1])%10
    soma_banco = (lista_banco[0] + lista_banco[1])%10

    if soma_jogador < 5 :
        lista_jogador.append(e)
        soma_jogador = (lista_jogador[0] + lista_jogador[1] + lista_jogador[2])%10

    if soma_banco < 5 :
        lista_banco.append(f)
        soma_banco = (lista_banco[0] + lista_banco[1] + lista_banco[2])%10

    #loop para definir quantas fichas o jogador vai ter apos a rodada e para definir se ele ganhou ou perdeu a rodada
    while soma_jogador > soma_banco and bacara :
        if em_quem_apostou == 'jogador' :
            fichas_totais += quanto_vai_apostar
            print('voce venceu e agora tem um montante de {0}'.format(fichas_totais))
            bacara = False
        else :
            fichas_totais -= quanto_vai_apostar
            print('voce perdeu porque a soma de suas cartas foi maior que soma das cartas do banco.agora tem um montante de {0}'.format(fichas_totais))
            bacara = False

    while soma_jogador < soma_banco and bacara :
        if em_quem_apostou == 'banco' :
            fichas_totais += 0.95*quanto_vai_apostar
            print('voce venceu e agora tem um montante de {0}'.format(fichas_totais))
            bacara = False
        else :
            fichas_totais -= quanto_vai_apostar
            print('voce perdeu porque a soma de suas cartas foi menor que a soma das cartas do banco.agora tem um montante de {0}'.format(fichas_totais))
            bacara = False

    while soma_banco == soma_jogador and bacara :
        if em_quem_apostou == 'empate' :
            fichas_totais += 7*quanto_vai_apostar
            print('voce venceu e agora tem um montante de {0}'.format(fichas_totais))
            bacara = False
        else :
            fichas_totais -= quanto_vai_apostar
            print('voce perdeu porque as somas das cartas suas e do banco deram empate.agora tem um montante de {0}'.format(fichas_totais))
            bacara = False

    #condicao caso ele queira continuar ate que acabe suas fichas
    if fichas_totais > 0 :
        quer_continuar = input('Deseja continuar?(sim/nao): ')
        if quer_continuar == 'sim' :
            em_quem_apostou = input('Deseja apostar em quem?(banco,jogador ou empate): ')
            quanto_vai_apostar = int(input('Quanto deseja apostar?(maximo possivel e de {0}): '.format(fichas_totais)))
        else :
            jogo = False
    else :
        jogo = False










































































