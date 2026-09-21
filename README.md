# Gerador de Currículo em Python

Programa em Python desenvolvido como Atividade Prática Supervisionada (APS), 
que permite criar, editar e exportar currículos em formato HTML, utilizando 
manipulação de arquivos como forma de persistência de dados.

## Funcionalidades

- Criação de currículo com Informações Pessoais, Experiência Profissional e Idiomas
- Edição de currículos já existentes, seção por seção
- Suporte a múltiplos currículos, cada um salvo com seu próprio conjunto de arquivos
- Lista de tamanho variável (experiências e idiomas), implementada com estrutura de repetição `while`
- Geração automática de um arquivo `.html` estilizado com CSS, a partir dos dados salvos
- Verificação de existência de arquivo antes da edição (`os.path.exists`)

## Tecnologias utilizadas

- Python 3
- Manipulação de arquivos (leitura e escrita em `.txt`)
- HTML e CSS (gerados dinamicamente pelo programa)

## Estrutura do projeto

O programa salva os dados de cada currículo em arquivos `.txt` separados 
por seção (informações pessoais, profissional, idiomas), identificados pelo 
nome escolhido pelo usuário. Ao final, uma função integradora lê esses arquivos 
e gera um currículo em HTML pronto para visualização no navegador.
