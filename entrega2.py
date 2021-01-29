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
            self.nome_torneio = input('Qual torneio que deseja ver?')
            setVer_ranking(self.nome_torneio)
        if self.fazer == '5':
            self.nome_torneio = input('Qual torneio que deseja ver?')
            setVer_lutadores(self.nome_torneio)
        if self.fazer == '6':
            self.nome_torneio = input('Qual torneio que deseja ver?')
            lutador1, lutador2 = input('Qual é o nome de um dos lutadores?')\
            , input('Qual o nome do outro lutador?')
            setRealizar_luta(self.nome_torneio, lutador1, lutador2)
        else:
            print('Opção inválida')    

    def setCriar_torneio(self):
        torneio = {}
        torneio['Nome'] = input('Qual o nome do torneio?')
        torneio['Arte marcial'] = input('Qual arte marcial?')
        faixas = []
        quer = 'sim'
        while quer == 'sim' or quer == 's':
            faixa = input('Adicione o a cor de uma faixa: ')
            faixa.lower()
            faixas.append(faixa)
            quer = input('Há outra faixa?(s/n) ')
            quer.lower()
        torneio['Faixas'] = faixas
        pesos = []
        quer = 'sim'
        while quer == 'sim' or quer == 's':
            peso = input('Adicione o a cor de uma categoria de peso: ')
            peso.lower()
            pesos.append(peso)
            quer = input('Há outra categoria de peso?(s/n) ')
            quer.lower()
        torneio['Pesos'] = pesos
        
    def setInscrever_lutador(self):
        pass

    def setVer_torneio(self):
        pass

    def setVer_ranking(self,torneio):
        pass

    def setVer_lutadores(self):
        pass

    def setRealizar_luta(self,torneio,lutador1,lutador2):
        pass


objeto = Torneio()