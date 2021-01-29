import random
class Torneio():
    torneios = []
    lutadores = []
    def __init__(self): 
        print('Bem vindo')
        while True:
            print('Este é o Menu. Caso deseje criar um torneio digite 1')
            print('Caso queira inscrever um lutador digite 2')
            print('Para ver os torneios existentes digite 3')
            print('Se deseja ver o ranking de torneio digite 4')
            print('Para saber os lutadores inscritos digite 5')
            print('Por fim, para realizar uma luta digite 6')
            print('Caso deseje sair digite "sair" ou s')
            self.fazer = input('O que deseja fazer?')
            if self.fazer == '1':
                self.setCriar_torneio()
                continuar = input('Deseja voltar ao menu?(s/n)')
                if continuar == 's':
                    continue
                elif continuar == 'n':
                    break
            elif self.fazer == '2':
                self.setInscrever_lutador()
                continuar = input('Deseja voltar ao menu?(s/n)')
                if continuar == 's':
                    continue
                elif continuar == 'n':
                    break
            elif self.fazer == '3':
                self.setVer_torneio()
                continuar = input('Deseja voltar ao menu?(s/n)')
                if continuar == 's':
                    continue
                elif continuar == 'n':
                    break
            elif self.fazer == '4':
                nome_torneio = input('De qual torneio que deseja ver?')
                self.setVer_ranking(nome_torneio)
                continuar = input('Deseja voltar ao menu?(s/n)')
                if continuar == 's':
                    continue
                elif continuar == 'n':
                    break
            elif self.fazer == '5':
                nome_torneio = input('De qual torneio que deseja ver?')
                self.setVer_lutadores(nome_torneio)
                continuar = input('Deseja voltar ao menu?(s/n)')
                if continuar == 's':
                    continue
                elif continuar == 'n':
                    break
            elif self.fazer == '6':
                nome_torneio = input('Qual torneio que deseja ver?')
                lutador1, lutador2 = input('Qual é o nome de um dos lutadores?')\
                , input('Qual o nome do outro lutador?')
                self.setRealizar_luta(nome_torneio, lutador1, lutador2)
                continuar = input('Deseja voltar ao menu?(s/n)')
                if continuar == 's':
                    continue
                elif continuar == 'n':
                    break
            elif self.fazer == 'sair' or self.fazer == 's':
                break
            else:
                print('Opção inválida')    

    def setCriar_torneio(self):
        torneio = {}
        tem = 0
        while tem>=0 and tem <=1:
            tem = 0
            nome = input('Qual o nome do torneio?')
            nome.lower()
            torneio['Nome'] = nome
            for l in self.torneios:
                if l['Nome'] == nome:
                    print(f'Já existe um torneio com o nome {nome}')
                    deseja = input('Deseja inserir outro nome? (s/n) ')
                    if deseja == 'n':
                        return None
                    tem = 1
                    break
            if tem==0:
                tem = 2
            
        torneio['Nome'] = nome
        luta = input('Qual arte marcial?')
        luta.lower()
        torneio['Arte marcial'] = luta
        faixas = []
        quer = 'sim'
        while quer == 'sim' or quer == 's':
            faixa = input('Adicione o a cor de uma faixa:(caso haja a \n \
                opção faixa livre favor escrever "sem" como uma das faixas) ')
            faixa.lower()
            faixas.append(faixa)
            quer = input('Há outra faixa?(s/n) ')
            quer.lower()
        torneio['Faixas'] = faixas
        pesos = []
        quer = 'sim'
        while quer == 'sim' or quer == 's':
            peso = []
            pesom = input('Adicione o menor peso de uma categoria de peso: ')
            try:
                pesom = float(pesom)
            except:
                print('peso inválido')
            else:
                peso.append(pesom)
                pesoM = input('Adicione o maior peso de uma categoria de peso: ')
            try:
                pesoM = float(pesoM)
            except:
                print('peso inválido')
            else:
                peso.append(pesoM)
                pesos.append(peso)
            quer = input('Há outra categoria de peso?(s/n) ')
            quer.lower()
        torneio['Pesos'] = pesos
        self.torneios.append(torneio)
        
    def setInscrever_lutador(self):
        lutador = {}
        torneio = input('De qual torneio o lutador deseja participar?')
        torneio.lower()
        e=0
        for t in self.torneios:
            if t['Nome'] == torneio:
                e +=1
        if  e!=0:
            lutador['Torneio'] = torneio
            faixa = input('qual é a faixa do lutador?(escrever "sem" caso não tenha)')
            faixa.lower()
            lutador['Faixa'] = faixa
            faixas = setFaixas(torneio)
            if faixa in faixas:
                tem = 0
                while tem == 0:
                    nome = input('Qual o nome do lutador?')
                    nome.lower()
                    lutador['Nome'] = nome
                    for l in self.lutadores:
                        if l['Nome'] == nome:
                            print(f'No torneio já existe um lutador com o nome {nome}')
                            deseja = input('Deseja inserir outro nome? (s/n) ')
                            if deseja == 'n':
                                tem = 1
                                return None
                            break
                while True:
                    idade = input('Qual é a idade do lutador?')
                    try:
                        idade = int(idade)
                    except KeyboardInterrupt:
                        break
                    except:
                        print('Idade inválida. Idade deve ser um numero inteiro')
                    else:
                        lutador['Idade'] = idade
                        break
                while True:
                    peso = input('Qual é o peso do lutador?')
                    try:
                        peso = float(peso)
                    except KeyboardInterrupt:
                        break
                    except:
                        print('Peso inválido. Peso deve ser um número')
                    else:
                        lutador['Peso'] = peso
                        break
                while True:
                    forca = input('Qual é a força deste lutador?')
                    try:
                    forca = int(forca)
                    except KeyboardInterrupt:
                        break
                    except:
                        print('Força inválida. Força deve ser um numero inteiro')
                    else:
                    lutador['Força'] = forca
                    break

                luta = input('Qual é a arte marcial do lutador?')
                luta.lower()
                lutador['Arte marcial'] = luta
                lutador['Pontos'] = 0
                self.lutadores.append(lutador)
            else:
                print('Faixa não aceita pelo torneio')
        else:
            print('Torneio inexistente')

    def setVer_torneio(self):
        if bool(self.torneios) == False:
            print('Não há torneios')
        else:
            for torneio in self.torneios:
                print (torneio['Nome'])

    def setVer_ranking(self,torneio):
        torneio.lower()
        e=0
        for t in self.torneios:
            if t['Nome'] == torneio:
                e +=1
        if  e!=0:
            participantes=[]
            for lutador in self.lutadores:
                if lutador['Torneio'] == torneio:
                    participante = [lutador['Nome'],lutador['Pontos']]
                    participantes.append(participante)
            if bool(participantes)==False:
                print('Não há participantes neste torneio ou o torneio não existe')
            else:
                pos = 0
                while pos<(range(participantes)-1):
                    if participantes[pos][1]<participantes[pos+1][1]:
                        menor = participantes[pos]
                        maior = participantes[pos+1]
                        participantes[pos] = maior
                        participantes[pos+1] = menor
                p = 1
                while p<=range(participantes):
                    print(f'O participante {participantes[p-1][0]} ficou na {p} colocação com {participantes[p-1][1]} pontos')
        else:
            print('Torneio inexistente')

    def setVer_lutadores(self, torneio):
        torneio.lower()
        s = 0
        for t in self.torneios:
            if t['Nome'] == torneio:
                s+=1
        if s==0:
            print('Torneio inexistente')
        else:
            pessoas = 0
            for lutador in self.lutadores:
                if lutador['Torneio'] == torneio:
                    print (lutador['Nome'])
                    pessoas+=1
            if pessoas<=0:
                print('Não há lutadores inscritos neste torneio')

    def setRealizar_luta(self,torneio,lutador1,lutador2):
        torneio.lower()
        e = 0
        for t in self.torneios:
            if t['Nome'] == torneio:
                e +=1
        if  e == 0:
            print('Torneio inexistente')
        else:
            tem1=0
            tem2=0
            for lutador in self.lutadores:
                if lutador['Nome'] == lutador1:
                    lutador1 = lutador
                    tem1 = 1
                elif lutador['Nome'] == lutador2:
                    lutador2 = lutador
                    tem2 = 1
            if tem1==0:
                print('O primeiro lutador não está inscrito neste torneio')
            if tem2==0:
                print('O segundo lutador não está inscrito neste torneio')
            else:
                if lutador1['Força']>lutador2['Força']:
                    print(f"O lutador {lutador1['Nome']} venceu")
                    lutador1['Pontos'] += 1
                if lutador1['Força']<lutador2['Força']:
                    print(f"O lutador {lutador2['Nome']} venceu")
                    lutador2['Pontos'] += 1
                else:
                    sorte = random.randint(1,2)
                    if sorte == 1:
                        print(f"O lutador {lutador1['Nome']} venceu")
                        lutador1['Pontos'] += 1
                    if sorte == 2:
                        print(f"O lutador {lutador2['Nome']} venceu")
                        lutador2['Pontos'] += 1


    def setFaixas(self,torneio):
        faixas = None
        for t in self.torneios:
            if t['Nome'] == torneio:
                faixas = t['Faixas']
        return faixas



objeto = Torneio()