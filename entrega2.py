class Torneio():
    torneios = []
    lutadores = []
    def __init__(self): 
        print('Bem vindo')
        print('Este é o Menu. Caso deseje criar um torneio digite 1')
        print('Caso queira inscrever um lutador digite 2')
        print('Para ver os torneios existentes digite 3')
        print('Se deseja ver o ranking de torneio digite 4')
        print('Para saber os lutadores inscritos digite 5')
        print('Por fim, para realizar uma luta digite 6')
        self.fazer = input('O que deseja fazer?')
        if self.fazer == '1':
            setCriar_torneio()
        if self.fazer == '2':
            setInscrever_lutador()
        if self.fazer == '3':
            setVer_torneio()
        if self.fazer == '4':
            nome_torneio = input('De qual torneio que deseja ver?')
            setVer_ranking(nome_torneio)
        if self.fazer == '5':
            nome_torneio = input('De qual torneio que deseja ver?')
            setVer_lutadores(nome_torneio)
        if self.fazer == '6':
            nome_torneio = input('Qual torneio que deseja ver?')
            lutador1, lutador2 = input('Qual é o nome de um dos lutadores?')\
            , input('Qual o nome do outro lutador?')
            setRealizar_luta(nome_torneio, lutador1, lutador2)
        else:
            print('Opção inválida')    

    def setCriar_torneio(self):
        torneio = {}
        nome = input('Qual o nome do torneio?')
        nome.lower()
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
        torneios = setVer_torneio()
        if  torneio in torneios:
            lutador['Torneio'] = torneio
            faixa = input('qual é a faixa do lutador?(escrever "sem" caso não tenha)')
            faixa.lower()
            lutador['Faixa'] = faixa
            faixas = setFaixas(torneio)
            if faixas != None and faixa in faixas:
                nome = input('Qual o nome do lutador?')
                nome.lower()
                lutador['Nome'] = nome
                idade = input('Qual é a idade do lutador?')
                idade = int(idade)
                lutador['Idade'] = idade
                peso = input('Qual é o peso do lutador?')
                peso = float(peso)
                lutador['Peso'] = peso
                forca = input('Qual é a força deste lutador?')
                forca = int(forca)
                lutador['Força'] = forca

                luta = input('Qual é a arte marcial do lutador?')
                luta.lower()
                lutador['Arte marcial'] = luta
                self.lutadores.append(lutador)
            else:
                print('Faixa não aceita pelo torneio')
        else:
            print('Torneio inexistente')

    def setVer_torneio(self):
        for torneio in self.torneios:
            print torneio['Nome']

    def setVer_ranking(self,torneio):
        pass

    def setVer_lutadores(self, torneio):
    torneio.lower()
    pessoas = 0
    for lutador in self.lutadores:
        if lutador['Torneio'] == torneio:
            print lutador['Nome']
            pessoas+=1
    if pessoas<=0:
        print('Não há lutadores inscritos neste torneio')

    def setRealizar_luta(self,torneio,lutador1,lutador2):
        torneio.lower()
        if torneio not in self.torneio:
            print('torneio inexistente')
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
                    print(f'O lutador {lutador1['Nome']} venceu')
                if lutador1['Força']<lutador2['Força']:
                    print(f'O lutador {lutador2['Nome']} venceu')
                else:
                    #Empate, deixar aleatoriedade decidir usando random
                    pass


    def setFaixas(self,torneio):
        faixas = None
        for t in self.torneios:
            if t['Nome'] == torneio:
                faixas = t['Faixas']
        return faixas



objeto = Torneio()