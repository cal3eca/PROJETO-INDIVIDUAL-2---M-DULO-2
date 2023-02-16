# PROJETO-INDIVIDUAL-2---M-DULO-2
Projeto individual do módulo 2 - SENAC - RESILIA

Esse repositório contem os arquivos que foram utilizados para a realização do projeto indivual 1, do módulo 2.
No curso de Analise de dados do Senac - Botafogo.

Criado por: Matheus Barbosa Furtado.
Data de criação : 07.02.2023

>####PROBLEMA DO PROJETO:
>Uma empresa de recrutamento recebeu muitos currículos
para determinadas vagas e agora precisa classificar
quantos candidatos tem o perfil necessário e quantos
candidatos estão concorrendo a cada vaga específica.
>> 

>####RESOLUÇÃO:
>
>>Um programa que tentei fazer de maneira mais simples possível, utilizando poucas linhas para que ficasse bem clean.

>>O funcionamento do código, se dá no sentido de que: O usuário vai cadastrar os possíveis candidatos, a partir de um conjunto de perguntas feitas a esse usuário, digitando o (nome) do candidato e as 4 palavras chaves principais do seu currículo/minibio (p1,p2,p3,p4).
De início eu separei em defs as duas operações principais, contendo dentro da def as funções que dão funcionalidade ao código.

        def listas():
          print("Bem vindo ao programa, cadastre seu candidato e coloque 5 palavras chave sobre seu currículo.")
        vaga1 = []
        vaga2 = []
        n_aprovado1 = []
        n_aprovado2 = []

>>Explicando o funciomaneto dessa estrutura: 
>>Aqui eu decidi guardar as listas que utilizo durante o programa, além de uma mensagem dizendo que a execução do
código começou!



>> Na segunda parte do projeto: Criei um menu de buscas para o avaliador.
Utilizando uma funçao def, para guardar todo esse processo que começa a partir de um looping (WHILE)
seguido de um dícionário para guardar o nome dos candidatos, e as palavras chaves, de seu currículo/minibio.


       def aprovado():
          sair = 's'
          while sair == 's':
             tipo_vaga = int(input('DIGITE (1)PARA A VAGA 1:\nDIGITE (2)PARA A VAGA 2: \n'))
             if tipo_vaga == 1:
                  print('A VAGA BUSCADA É 1')
                  cand1 = {'nome': input('Digite o nome: '), 'p1': input('Digite a Primeira palavra chave: '),
                         'p2': input('Digite a segunda palavra chave: '), 'p3': input('Digite a terceira palavra chave: '),
                         'p4': input('Digite a quarta palavra chave: ')
                         }
>>REFERENTE AO PRIMEIRO MENU ACIMA, E REFERENTE AO SEGUNDO MENU, QUE LEVA PARA A SEGUNDA VAGA.

            if tipo_vaga == 2:
                print('A VAGA BUSCADA É 2')
                cand1 = {'nome': input('Digite o nome: '), 'p1': input('Digite a Primeira palavra chave: '),
                     'p2': input('Digite a segunda palavra chave: '), 'p3': input('Digite a terceira palavra chave: '),
                     'p4': input('Digite a quarta palavra chave: ')
                     }

>>Depois desse processo, utilizando o looping (WHILE)
Em seguida, utilizando condicionais (if), são feitos testes, que comparam as palavras chaves dentro do dicionário, com as
requisitadas como profeciência para a vaga 1 ou vaga 2.

           if 'Python' in cand1.values() and 'Programação' in cand1.values() and 'Desenvolvimento' in and1.values():
                 print("*" * 50)
                 vaga1.append(cand1['nome'])
           else:
                 print('*' * 50)
                 n_aprovado1.append(cand1['nome'])
                   
>>REFERENTE AO SEGUNDO MENU DE CONDICIONAIS:

            if 'Analise de dados' in cand1.values() and 'DADOS' in cand1.values() and 'SQL' in cand1.values():
                  print("*" * 50)
                  vaga2.append(cand1['nome'])
            else:
                  print('*' * 50)
                  n_aprovado2.append(cand1['nome'])

