import os
import sys
import json
print(os.getcwd())


despesas = [{'numero': 0, 'nome': 'Despesa', 'descricao': 'Descrição', 'categoria': 'Categoria', 'valor': 'Valor', 'mes': 'Mês'}]

categorias_disponiveis = ['Alimentação', 'Transporte', 'Moradia', 'Educação', 'Saúde', 'Lazer', 'Outros']

def opcoes_programa(despesas):
    print('1 - Registrar despesa')
    print('2 - Listar despesas')
    print('3 - Editar despesa')
    print('4 - Remover despesa')
    print('5 - Resumo despesas')
    print('6 - Sair')

def escolher_opcao(despesas):

    try:
        opcao_escolhida = int(input('Digite a opção que deseja: '))
        if opcao_escolhida == 1:
            registrar_despesa(despesas, proximo_numero=0)
        elif opcao_escolhida == 2:
            listar_despesas(despesas)
        elif opcao_escolhida == 3:
            editar_despesa(despesas)
        elif opcao_escolhida == 4:
            remover_despesa(despesas)
        elif opcao_escolhida == 5:
            resumo_despesas(despesas)
        elif opcao_escolhida == 6:
            sair()
        else:
            opcao_invalida()
    except ValueError:
        print('Digite um valor válido: ')
        opcao_invalida()
    finally:
        salvar_despesas()

def listar_despesas(despesas):
    clear_screen()
    exibir_titulo('Lista de Despesas')
    cabecalhos(f'{'Número da despesa'.ljust(20)} | {'Nome da Despesa'.ljust(20)} | {'Categoria'.ljust(20)} | {'Valor'.ljust(20)}\n')

    for despesa in despesas:
        numero_despesa = despesa.get('numero', 'N/A')
        nome_despesa = despesa.get('nome', 'N/A')
        categoria_despesa = despesa.get('categoria', 'N/A')
        valor_despesa = despesa.get('valor', 'N/A')


        print(f'{str(numero_despesa).ljust(20)} | {nome_despesa.ljust(20)} | {categoria_despesa.ljust(20)} | {str(valor_despesa).ljust(20)}')

    voltar_ao_menu_principal()

def registrar_despesa(despesas, proximo_numero=0):
    clear_screen()
    proximo_numero += 1
    exibir_titulo('Registrar Despesas')
    print('Categorias Disponíveis: ')
    informativos('Alimentação, ''Transporte, ' 'Moradia, ' 'Educação, ' 'Saúde, ' 'Lazer, ' 'Outros\n')

    while True:
        nome_da_despesa = input('Digite o nome da Despesa: ')
        if nome_da_despesa.strip():
            break
        else:
            print('Por gentileza, digite um nome válido para a despesa.')

    while True:
        descricao_despesa = input('Digite a descrição da Despesa: ')
        if descricao_despesa.strip():
            break
        else:
            print('Por gentileza, digite um texto válido para a descricao.')

    while True:
        categoria_despesa = input('Digite a categoria da Despesa: ')
        if categoria_despesa.strip() and categoria_despesa.capitalize() in categorias_disponiveis:
            break
        else:
            print('Por gentileza, escolha uma categoria válida.')

    while True:
            mes_da_despesa = input('Digite o mês da Despesa no formato *mmm* (Ex. jan): ')
            if mes_da_despesa.strip() and validar_mes(mes_da_despesa):
                break
            else:
                print('Por gentileza, digite um mês válido para a despesa.')

    while True:
        try:
            valor_despesa = float(input('Digite o valor da despesa: R$ ').replace(',', '.'))
            break
        except ValueError:
            print('Por gentileza, digite um valor numérico válido!')

    cadastro_despesas = {'numero': proximo_numero, 'nome' :nome_da_despesa, 'descricao' :descricao_despesa, 'categoria' :categoria_despesa, 'mes' :mes_da_despesa, 'valor' :valor_despesa}
    despesas.append(cadastro_despesas)
    print('\nVocê cadastrou a sua despesa.')
    salvar_despesas()
    voltar_ao_menu_principal()
    
    return proximo_numero

def resumo_despesas(despesas):
    clear_screen()
    exibir_titulo('Resumo de Despesas')

    despesas_por_categoria_mes = {}

    mes_desejado = input('Digite o Mês desejado: ')

    for despesa in despesas:
        if despesa.get('mes', '') == mes_desejado:
            categoria = despesa['categoria']
            valor_despesa = despesa['valor']

            if categoria in despesas_por_categoria_mes:
                despesas_por_categoria_mes[categoria] += valor_despesa
            else:
                despesas_por_categoria_mes[categoria] = valor_despesa
    
    for categoria, total_categoria in despesas_por_categoria_mes.items():
        print(f'Categoria: {categoria} | Total: {total_categoria}')

    total_geral = sum(despesas_por_categoria_mes.values())
    print(f'\nO valor total de despesas é de: R${total_geral}')
    voltar_ao_menu_principal()

def editar_despesa(despesas):
    clear_screen()
    exibir_titulo('Editar Despesas')

    print('Despesas listadas: \n')


    for despesa in despesas:
        titulo_despesa = despesa['nome']
        print(f'Despesa: {titulo_despesa}')

    titulo_despesa = input('\nDigite o nome da despesa que deseja alterar: ')

    for despesa in despesas:
        if 'nome' in despesa and despesa['nome'] == titulo_despesa:
            print('\nInformações atuais da despesa:')
            print(f'Nome da despesa: {despesa['nome']}')
            print(f'Descrição da despesa: {despesa['descricao']}')
            print(f'Categoria da despesa: {despesa['categoria']}')
            print(f'Mês da despesa: {despesa['mes']}')
            print(f'Valor da despesa: {despesa['valor']}')

            novo_nome = input('\nNovo título da despesa (Pressione o Enter para manter o atual): ')
            nova_descricao = input('Nova descrição da despesa (Pressione o Enter para manter a atual): ')

            while True:
                nova_categoria = input('Nova categoria da despesa (Pressione o Enter para manter a atual): ')
                if not nova_categoria.strip():
                    break
                elif nova_categoria.capitalize() in categorias_disponiveis:
                    despesa['categoria'] = nova_categoria.capitalize()
                    break
                else:
                    print('Por gentileza, escolha uma categoria válida.')

            novo_mes = input('Novo mês da despesa (Pressione o Enter para manter o atual): ')
            novo_valor = input('Novo valor da despesa (Pressione o Enter para manter o atual): ')

            despesa['nome'] = novo_nome if novo_nome else despesa['nome']
            despesa['descricao'] = nova_descricao if nova_descricao else despesa['descricao']
            despesa['categoria'] = nova_categoria if nova_categoria else despesa['categoria']
            despesa['mes'] = novo_mes if novo_mes else despesa['mes']
            despesa['valor'] = novo_valor if novo_valor else despesa['valor']

            print(f'\nA tarefa {despesa['nome']} foi atualizada com sucesso')
            salvar_despesas()
            voltar_ao_menu_principal()
            return
    print (f'\nA despesa {titulo_despesa} não foi encontrada.')
    salvar_despesas()
    voltar_ao_menu_principal()

def total_despesas(despesas):
    clear_screen()
    exibir_titulo('Total de Despesas')
    total = 0

    despesas_por_categoria_mes = {}
    mes_desejado = input('Digite o mês desejado: ')

    for despesa in despesas:
        if despesa.get('mes', '') == mes_desejado:
            categoria = despesa['categoria']
            valor_despesa = despesa['valor']

            if categoria in despesas_por_categoria_mes:
                despesas_por_categoria_mes[categoria] += valor_despesa
            else:
                despesas_por_categoria_mes[categoria] = valor_despesa

        for categoria, total_categoria in despesas_por_categoria_mes.items():
            print(f'Categoria: {categoria} | Total: {total_categoria}')

        total_geral = sum(despesas_por_categoria_mes.values())
        print(f'\nO valor total de despesas para o mês {mes_desejado} é de {total_geral}\n')
        voltar_ao_menu_principal()

def remover_despesa(despesas):
    clear_screen()
    exibir_titulo('Remover Despesa')

    print('Despesas listadas: \n')

    for despesa in despesas:
        numero_despesa = despesa.get('numero', 'N/A')
        print(f'Número: {numero_despesa} | Despesa: {despesa.get('nome', 'N/A')}')

    numero_despesa = input('\nDigite o número da despesa que deseja remover: ')

    for despesa in despesas:
        if 'numero' in despesa and str(despesa['numero']) == numero_despesa:
            print('\nInformações atuais da despesa:')
            print(f'Nome da despesa: {despesa['nome']}')
            print(f'Descrição da despesa: {despesa['descricao']}')
            print(f'Categoria da despesa: {despesa['categoria']}')
            print(f'Valor da despesa: {despesa['valor']}')

            confirmacao = input(f'Tem certeza que deseja excluir a despesa {despesa['nome']}? (S/N): ').lower()
            
            if confirmacao == 's':
                despesas.remove(despesa)
                print(f'A despesa {despesa['nome']} foi excluída com sucesso')
            else:
                print(f'A exclusão da despesa {despesa['nome']} foi cancelada pelo usuário.')
            salvar_despesas()
            voltar_ao_menu_principal()
            return
        
    print(f'\nA despesa com o número {numero_despesa} não foi encontrada.')
    salvar_despesas()
    voltar_ao_menu_principal()

def validar_mes(mes):
    meses_validos = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    if mes.lower() in meses_validos:
        return True
    else:
        return False

def sair():
    clear_screen()
    sys.exit()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_titulo(texto):
    clear_screen()
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)

def voltar_ao_menu_principal():
    input('\nPressione uma tecla para voltar ao menu principal: ')
    main()

def exibir_nome_programa():
    print(''' ℂ𝕠𝕟𝕥𝕣𝕠𝕝𝕖 𝕕𝕖 𝔻𝕖𝕤𝕡𝕖𝕤𝕒𝕤
      ''')

def main():
    try:
        clear_screen()
        exibir_nome_programa()
        global despesas
        despesas = carregar_despesas()
        opcoes_programa(despesas)
        escolher_opcao(despesas)
        salvar_despesas()
    except ValueError as ve:
        print(f'Erro ao salvar despesas: {ve}')

def opcao_invalida():
    while True: 
        entrada = escolher_opcao(despesas)
        if entrada.isdigit():
            break
        else:
            print('Por favor escolha um número válido entre as opções listadas: ')

def salvar_despesas():
    try:
        with open('despesas.json', 'w') as arquivo:
            json.dump(despesas, arquivo)
    except ValueError as ve:
            print(f'Erro ao salvar despesas: {ve}')

def carregar_despesas():
    try:
        with open('despesas.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return[]

def informativos(texto):
    codigo_ansi = '\033[0;31m'  # 1;31m representa a cor vermelha
    reset_ansi = '\033[0m'      # 0m para resetar o estilo
    print(f'{codigo_ansi}{texto}{reset_ansi}')

def cabecalhos(texto):
    codigo_ansi = '\033[1;36m'  # 1;36m representa a cor azul
    reset_ansi = '\033[0m'      # 0m para resetar o estilo
    print(f'{codigo_ansi}{texto}{reset_ansi}')

if __name__ == '__main__':
    main()
