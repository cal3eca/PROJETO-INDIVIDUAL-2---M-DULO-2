'''
ALUNO: MATHEUS BARBOSA FURTADO
PROJETO INDIVIDUAL 2 - MÓDULO 2
SENAC BOTAFOGO - RESILIA

Uma empresa de recrutamento recebeu muitos currículos
para determinadas vagas e agora precisa classificar
quantos candidatos tem o perfil necessário e quantos
candidatos estão concorrendo a cada vaga específica.

Desenvolver um projeto (usando dicionários) que vai gravar
a quantidade de currículos para aquela vaga e quantas
pessoas têm as palavras-chave necessárias no currículo.

Para isso, nosso código Python vai checar para qual vaga a
pessoa se inscreveu e o resumo que a pessoa enviou em
busca dessas informações.
'''
import os
import pandas as pd


def listas():
    print("Bem vindo ao programa, cadastre seu candidato e coloque 5 palavras chave sobre seu currículo.")
vaga1 = []
vaga2 = []
n_aprovado1 = []
n_aprovado2 = []


def aprovado():
    sair = 's'
    while sair == 's':
        tipo_vaga = int(input('DIGITE (1)PARA A VAGA 1:\nDIGITE (2)PARA A VAGA 2: \n'))
        if tipo_vaga == 1:
            print('A VAGA BUSCADA É 1')
            cand1 = {'nome': input('Digite o nome: ').title(), 'p1': input('Digite a Primeira palavra chave: ').lower(),
                     'p2': input('Digite a segunda palavra chave: ').lower(), 'p3': input('Digite a terceira palavra chave: ').lower(),
                     }
            os.system('cls')
            if 'python' in cand1.values() and 'programação' in cand1.values() and 'desenvolvimento' in cand1.values():
                print("*" * 50)
                vaga1.append(cand1['nome'])
            else:
                print('*' * 50)
                n_aprovado1.append(cand1['nome'])
        if tipo_vaga == 2:
            print('A VAGA BUSCADA É 2')
            cand1 = {'nome': input('Digite o nome: ').title(), 'p1': input('Digite a Primeira palavra chave: ').lower(),
                     'p2': input('Digite a segunda palavra chave: ').lower(), 'p3': input('Digite a terceira palavra chave: ').lower(),
                     }
            os.system('cls')
            if 'analise de dados' in cand1.values() and 'dados' in cand1.values() and 'sql' in cand1.values():
                print("*" * 50)
                vaga2.append(cand1['nome'])
            else:
                print('*' * 50)
                print('*' * 50)
                n_aprovado2.append(cand1['nome'])
        a = input('DIGITE (S) PARA CONTINUAR E (N) PARA SAIR: ')
        sair = a.lower()
        aprovados = []
        aprovados += (vaga1 + vaga2)
        if sair == 'n':
            print('')
            contagem1 = len(vaga1 + n_aprovado1)
            contagem2 = len(vaga2 + n_aprovado2)
            print('O número de candidatos, inscritos para a primeira vaga é: ', contagem1)
            print('CANDIDATOS APROVADOS NA PRIMEIRA VAGA: ', '\nNOMES: ', vaga1, '\nQuantidade: ', len(vaga1))
            print('TOTAL: ', contagem1)
            print('*' * 50)
            print('O número de candidatos, inscritos para a segunda vaga é: ', contagem2)
            print('CANDIDATOS APROVADOS NA SEGUNDA VAGA: ', '\nNOMES: ', vaga2, '\nQuantidade: ', len(vaga2))
            print('TOTAL: ', contagem2)


listas()
aprovado()
list(zip(vaga1,vaga2))
tabela = pd.DataFrame(data=zip(vaga1,vaga2), columns=['APROVADOS VAGA (1)','APROVADOS VAGA(2)'])
print(tabela)
