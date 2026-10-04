import os

##*************************************************************************************************************************************
##Define o que sera executado
def criarEditar(iniciar):

    if iniciar.upper() == 'CRIAR':
        nomeArquivo = input('Digite o nome do novo curriculo:')
        pessoais(nomeArquivo)
        return nomeArquivo

    elif iniciar.upper() == 'EDITAR':
        nomeArquivo = input('Digite o nome do curriculo:')
        if os.path.exists(f'{nomeArquivo}.txt'):
            oqueEditar(nomeArquivo)
            return nomeArquivo
        else:
            print('\nARQUIVO NÃO ENCONTRADO.\nTENTE NOVAMENTE.\n')
            return criarEditar(iniciar)

    else:
        print('\n')
        print("OPIÇÃO INVALIDA. \nTENTE NOVAMNETE.\n")
        iniciar = input("O que deseja fazer? \n CRIAR-Novo curriculo. \n EDITAR-Editar curriculo.\n Resposta:")
        print('\n')
        return criarEditar(iniciar)
##************************************************************************************************************************************
##Define oq sera editado
def oqueEditar(nomeArquivo):
    editar = int(input("\nO que deseja editar no seu curriculo? \n 1-Informaçoes pessoais\n 2-Experiência\n 3-Idiomas\n Resposta:"))
    if editar == 1:
        pessoais = lerPessoais(nomeArquivo)
        editarPessoais(nomeArquivo, pessoais)

    elif editar == 2:
        experiencias = lerExperiencias(nomeArquivo)
        editarProfissional(nomeArquivo, experiencias)

    elif editar == 3:
        idiomas = lerIdioma(nomeArquivo)
        editarIdioma(nomeArquivo, idiomas)

    else:
        print("\nOPIÇÃO INVALIDA.\nTENTE NOVAMENTE.")

        oqueEditar(nomeArquivo)
##*************************************************************************************************************************************   
##Cria arquivo com informações pessoais
def pessoais(nomeArquivo):
    print("CRIAÇÃO DE NOVO CURRICULO: \n")

    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    endereco = input("Cidade e estado:")
        
    arquivo = open(f'{nomeArquivo}.txt', 'w', encoding='utf-8')
    arquivo.write(nome + "\n")
    arquivo.write(telefone + "\n")
    arquivo.write(email + "\n")
    arquivo.write(endereco + "\n")
    arquivo.close()

    proficional(nomeArquivo)
##************************************************************************************************************************************   
##Cria arquivo com informações profissionais
def proficional(nomeArquivo):
    resposta = input("\nVocê possui experiencia?")
    print("\nEXPERIENCIA:\n")
    arquivo = open(f'{nomeArquivo}Expe.txt', 'w', encoding='utf-8')
    if resposta.upper() == 'S':
        while resposta.upper() == 'S':
            empresa = input("Empresa: ")
            cargo = input("Cargo: ")
            dataIni = input("Data que iniciou: ")
            dataFim = input("Data de desligamento: ")
            resposta = input("\nDeseja cadastrar mais alguma empresa? S/N")

            arquivo.write(empresa + "\n")
            arquivo.write(cargo + "\n")
            arquivo.write(dataIni + "\n")
            arquivo.write(dataFim + "\n")
        arquivo.close()

    elif resposta.upper() == 'N':
        arquivo.close()
    else:
        print("OPÇÃO INVALIDA")
        arquivo.close()
        return proficional(nomeArquivo)
    idioma(nomeArquivo)

##************************************************************************************************************************************   
##Cria arquivo com idiomas
def idioma(nomeArquivo):
    resposta = 'S'
    print("\nIDIOMA:\n")
    arquivo = open(f'{nomeArquivo}Idioma.txt', 'w', encoding='utf-8')
    while resposta.upper() == 'S':
        idioma = input("Idioma: ") 
        resposta = input("\nVocê fala mais algum idioma? S/N") 
        arquivo.write(idioma + "\n")
    arquivo.close()

##************************************************************************************************************************************
##Le pessoais
def lerPessoais(nomeArquivo):
    arquivo = open(f'{nomeArquivo}.txt', 'r', encoding='utf-8')
    linhas = [linha.strip() for linha in arquivo.readlines()]
    arquivo.close()

    nome = linhas[0]
    telefone = linhas[1]
    email = linhas[2]
    endereco = linhas[3]

    pessoais = [nome, telefone, email, endereco]

    return pessoais 
    
##************************************************************************************************************************************
##Edita arquivo com informações pessoais
def editarPessoais(nomeArquivo, pessoais):
    
    print("\nEDIÇÃO DE INFORMAÇÕES PESSOAIS: \n")

    nomeAtual, telefoneAtual, emailAtual, enderecoAtual = pessoais

    print(f"Nome atual: {nomeAtual}")
    nome = input("Nome: ") or nomeAtual

    print(f"Telefone atual: {telefoneAtual}")
    telefone = input("Telefone: ") or telefoneAtual

    print(f"Email atual: {emailAtual}")
    email = input("Email: ") or emailAtual

    print(f"Cidade e estado atual: {enderecoAtual}")
    endereco = input("Cidade e estado: ") or enderecoAtual

    arquivo = open(f'{nomeArquivo}.txt', 'w', encoding='utf-8')
    arquivo.write(nome + "\n")
    arquivo.write(telefone + "\n")
    arquivo.write(email + "\n")
    arquivo.write(endereco + "\n")
    arquivo.close()

    print("Informações pessoais atualizadas!")
##***********************************************************************************************************************************
##Le o arquivo profissional antes de editar
def lerExperiencias(nomeArquivo):
    arquivo = open(f'{nomeArquivo}Expe.txt', 'r', encoding='utf-8')
    linhas = [linha.strip() for linha in arquivo.readlines()]
    arquivo.close()

    experiencias = []
    i = 0
    while i + 3 < len(linhas):
        empresa = linhas[i]
        cargo = linhas[i + 1]
        dataIni = linhas[i + 2]
        dataFim = linhas[i + 3]
        experiencias.append([empresa, cargo, dataIni, dataFim])
        i += 4

    return experiencias
##***************************************************************************************************************************************
##Edita arquivo com informações profissionais
def editarProfissional(nomeArquivo, experiencias):
    print(f"\nEDITAR PROFISSIONAL:\n")
    addEdit = int(input("Você deseja editar ou adicionar uma experiência?\n 1-Editar\n2-Adicionar"))
    if addEdit == 1:
        if not experiencias:
            print("Não há experiências para editar.")
            return 
           
        pergunta = 'S'
        while pergunta.upper() == 'S':
            i = 0
            for empresa in experiencias:
                print(f"{i+1}-{experiencias[i]}")
                i+=1

            resposta = int(input("Essas são as empresas salvas, qual deseja editar?"))
            resposta -= 1

            empresa, cargo, dataIni, dataFim = experiencias[resposta]

            novaEmpresa = input("Digite o novo nome:") or empresa
            novoCargo = input("Digite o novo cargo:") or cargo
            novaDataIni = input("Digite a nova data de inicio:") or dataIni
            novaDataFim = input("Digite a nova data de saida:") or dataFim

            experiencias[resposta] = [novaEmpresa, novoCargo, novaDataIni, novaDataFim]

            arquivo = open(f'{nomeArquivo}Expe.txt', 'w', encoding='utf-8')
            for bloco in experiencias:
                for campo in bloco:
                    arquivo.write(campo + "\n")
            pergunta = input("Deseja alterar mais alguma experiencia?")   
            arquivo.close()
        print("Atualizações feitas!")
    elif addEdit == 2:
        arquivo = open(f'{nomeArquivo}Expe.txt', 'a', encoding='utf-8')
        resposta = 'S'
        while resposta.upper() == 'S':
            empresa = input("Empresa: ")
            cargo = input("Cargo: ")
            dataIni = input("Data que iniciou: ")
            dataFim = input("Data de desligamento: ")
            resposta = input("Deseja cadastrar mais alguma empresa? S/N")
       
            arquivo.write(empresa + "\n")
            arquivo.write(cargo + "\n")
            arquivo.write(dataIni + "\n")
            arquivo.write(dataFim + "\n")
        arquivo.close() 
    else:
        print("Opção invalida.")
        editarProfissional(nomeArquivo, experiencias)
##*****************************************************************************************************************************
##Le idioma
def lerIdioma(nomeArquivo):
    arquivo = open(f'{nomeArquivo}Idioma.txt', 'r', encoding='utf-8')
    idiomas = [linha.strip() for linha in arquivo.readlines()]
    arquivo.close()

    return idiomas
##******************************************************************************************************************************
##Edita o arquivo idioma
def editarIdioma(nomeArquivo, idiomas):
    print("\nEDITAR IDIOMAS:\n")

    addEdit = int(input("Você deseja editar ou adicionar um idioma?\n1-Editar\n2-Adicionar\n"))

    if addEdit == 1:
        pergunta = 'S'
        while pergunta.upper() == 'S':
            i = 0
            for idioma in idiomas:
                print(f"{i+1}-{idiomas[i]}")
                i += 1

            resposta = int(input("Qual idioma deseja editar? "))
            resposta -= 1

            idiomaAtual = idiomas[resposta]

            novoIdioma = input("Novo idioma:") or idiomaAtual

            idiomas[resposta] = novoIdioma

            pergunta = input("Deseja editar mais algum idioma? S/N: ")

        arquivo = open(f'{nomeArquivo}Idioma.txt', 'w', encoding='utf-8')
        for idioma in idiomas:
            arquivo.write(idioma + "\n")
        arquivo.close()
        print("Idiomas atualizados!")

    elif addEdit == 2:
        resposta = 'S'
        arquivo = open(f'{nomeArquivo}Idioma.txt', 'a', encoding='utf-8')
        while resposta.upper() == 'S':
            novoIdioma = input("Idioma: ")
            arquivo.write(novoIdioma + "\n")
            resposta = input("Deseja adicionar outro idioma? S/N: ")
        arquivo.close()
        print("Idioma(s) adicionado(s)!")

    else:
        print("Opção invalida.")
        editarIdioma(nomeArquivo, idiomas)

##**********************************************************************************************
def criarCurriculo(curriculo ):
        nomeArquivo = curriculo
        pessoais = lerPessoais(nomeArquivo)
        experiencias = lerExperiencias(nomeArquivo)
        idiomas = lerIdioma(nomeArquivo)

        ## Monta o HTML
        html = "<html>\n<head>\n"
        html += "<meta charset='UTF-8'>\n"
        html += f"<title>Currículo - {pessoais[0]}</title>\n"
        html += "<style>\n"
        html += "body { font-family: Verdana, sans-serif; color: #333; background-color: #f4f4f4; }\n"
        html += "h1 { color: #2c3e50; }\n"
        html += "h2 { color: #2980b9; border-bottom: 2px solid #2980b9; }\n"
        html += "</style>\n"
        html += "</head>\n<body>\n"

        ## Seção pessoal
        html += f"<h1>{pessoais[0]}</h1>\n"
        html += f"<p>Telefone: {pessoais[1]}</p>\n"
        html += f"<p>Email: {pessoais[2]}</p>\n"
        html += f"<p>Endereço: {pessoais[3]}</p>\n"

        ## Seção profissional
        html += "<h2>Experiência Profissional</h2>\n"
        if experiencias == []:
            html += "<p>Sem experiência cadastrada.</p>\n"
        else:
            for bloco in experiencias:
                empresa, cargo, dataIni, dataFim = bloco
                html += f"<p><strong>{cargo}</strong> - {empresa} ({dataIni} a {dataFim})</p>\n"

        ## Seção idiomas
        html += "<h2>Idiomas</h2>\n<ul>\n"
        for idioma in idiomas:
            html += f"<li>{idioma}</li>\n"
        html += "</ul>\n"

        html += "</body>\n</html>"

        ## Salva o arquivo final
        arquivo = open(f'{nomeArquivo}Curriculo.html', 'w', encoding='utf-8')
        arquivo.write(html)
        arquivo.close()

        print(f"Currículo gerado com sucesso: {nomeArquivo}Curriculo.html")
        
       
##Inicialização do sistema
repetir = 'S'
while repetir.upper() == 'S':
    curriculo = criarEditar(iniciar = input("\nO que deseja fazer? \n CRIAR-Novo curriculo. \n EDITAR-Editar curriculo.\n Resposta:"))
    repetir = input("Deseja fazer alguma mudança?")
criarCurriculo(curriculo)