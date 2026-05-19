
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
from datetime import datetime
import calendar
import time
import shutil
import os

#===================================================================================
# Configurações e dados dos processos
#===================================================================================

# Nome que vai entrar no campo resumo e os operadores logicos que vão entrar nos campos de operadores, para cada tipo de processo, o sistema vai preencher os campos de resumo e operadores com as palavras e operadores definidos aqui, para cada tipo de processo, o sistema vai preencher os campos de resumo e operadores com as palavras e operadores definidos aqui, o sistema preenche os campos de resumo e operadores com as palavras e operadores definidos aqui, o sistema preenche os campos de resumo e operadores com as palavras e operadores definidos aqui, o sistema preenche os campos de resumo e operadores com as palavras e operadores definidos aqui, o sistema preenche os campos de resumo e operadores com as palavras e operadores definidos aqui, o sistema preenche os campos de resumo e operadores com as palavras e operadores definidos aqui, o sistema preenche os campos de resumo e operadores com as palavras e operadores definidos aqui, o sistema preenche os campo

processos = [

    {
        "nome": "Processo Tipo 1",
        "keywords": ["termo_1", "sigla_1", "termo_extra_1"],
        "logic": ["OR", "NOT"]
    },

    {
        "nome": "Processo Tipo 2",
        "keywords": ["termo_2", "sigla_2", "variacao_2"],
        "logic": ["OR", "OR"]
    },

    {
        "nome": "Processo Tipo 3",
        "keywords": ["termo_3", "variacao_3"],
        "logic": ["OR"]
    },

    {
        "nome": "Processo Tipo 4",
        "keywords": ["termo_4", "variacao_4"],
        "logic": ["OR"]
    },

    {
        "nome": "Processo Tipo 5",
        "keywords": ["termo_5", "variacao_5"],
        "logic": ["OR"]
    },

    {
        "nome": "Processo Tipo 6",
        "keywords": ["termo_6"],
        "logic": ["AND"]
    },

    {
        "nome": "Processo Tipo 7",
        "keywords": ["termo_7", "variacao_7"],
        "logic": ["OR"]
    },

    {
        "nome": "Processo Tipo 8",
        "keywords": ["termo_8"],
        "logic": ["AND"]
    },

    {
        "nome": "Processo Tipo 9",
        "keywords": ["termo_9", "variacao_9"],
        "logic": ["OR"]
    },

    {
        "nome": "Processo Tipo 10",
        "keywords": ["termo_10", "variacao_10", "variacao_extra_10"],
        "logic": ["OR", "OR", "OR"]
    },

    {
        "nome": "Processo Tipo 11",
        "keywords": ["termo_11"],
        "logic": ["AND"]
    },

    {
        "nome": "Processo Tipo 12",
        "keywords": ["termo_12"],
        "logic": ["AND"]
    }

]

#===================================================================================
#Configuração de data
#===================================================================================

while True:
    mes = int(input("Digite o número do mês de 1 a 12:"))
    
    #Não prossegue até digitar o mês valido, o mês deve ser entre 1 e 12.
    if 1 <= mes <= 12 :
        break
    else:
        print("Mês inválido. Tente novamente.")

#Função para pegar o primeiro e último dia do mês, usando a biblioteca calendar e com o horário já definido para preencher os campos de data e horário da consulta. O sistema não preenche a data sem o horário definido. O horário é definido como 00:00:00 no início e 23:59:59 para o fim, para garantir que a consulta pegue todo o período do mês selecionado.
def gerar_datas(mes):
    data_inicio = f"01/{mes:02d}/2026 00:00:00"
    ultimo_dia = calendar.monthrange(2026, mes)[1]
    data_fim = f"{ultimo_dia}/{mes:02d}/2026 23:59:59"
    return data_inicio, data_fim

DATA_INICIO, DATA_FIM = gerar_datas(mes)

#abre o navegador
driver = webdriver.Chrome()

#abre o site
driver.get("Link do site")

#AQUI O USUÁRIO DEVE FAZER O LOGIN MANUALMENTE, POIS O SISTEMA DE LOGIN POSSUI CAPTCHA QUE NÃO DEIXA O PROGRAMA FAZER TUDO SOZINHO.

#loop até logar
while True:
    input("faça login e depois aperte enter para continuar")

    try:
        #verifica se já esta na tela após o login
        WebDriverWait(driver, 5).until_not(EC.presence_of_element_located((By.ID, "Botao de logar")))
        
        #se o programa conseguir encontrar o botão de login ele ainda está na tela de login, então ele vai imprimir a mensagem de erro e continuar o loop, caso contrário, ele vai sair do loop
        print("saiu do login, continue")
        break
    except:
        print("ainda no login, tente novamente")

#começo da automação
print("Iniciando automação...")

#espera o menu "Área dos Processos" estar clicável e clica nele
try:
    menu = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "Menu da area de processos")))
    menu.click()
    print("Clicou no menu 'Área dos Processos'")
    #se o programa der erro ele vai imprimir a mensagem de erro, não vai fechar o navegador, para clicar manualmente no menu
except Exception as e:
    print("erro ao clicar no menu 'Área dos Processos':", e)

#espera o submenu consultar Processos estar clicável e clica nele indo para a consulta
try:
    opcao= WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH, "Consultar processos")))
    opcao.click()
    print("entrou em consultar processos")

    #se o programa der erro ele vai imprimir a mensagem de erro, não vai fechar o navegador, para clicar manualmente no submenu e ir para a consulta
except Exception as e:
    print("erro ao clicar em consultar processos:", e)




#===================================================================================
# Métodos principais
#===================================================================================


#método para limpar os filtros, caso haja algum filtro já preenchido, para limpar o filtro entigo e poder definir o outro
def limpar_filtros():

    try:
        btn = WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.ID,"Limpar filtros")))
        btn.click()
    except Exception as e:
        print("Erro ao limpar filtros:", e)

def preencher_datas():
    try:
        print(f" {DATA_INICIO} até {DATA_FIM}")

        # ===== DATA INICIO =====
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "campo de data inicial"))
        ).click()

        driver.find_element(By.ID, "campo de data inicial").send_keys(Keys.CONTROL + "a")
        driver.find_element(By.ID, "campo de data inicial").send_keys(DATA_INICIO)
        driver.find_element(By.ID, "campo de data inicial").send_keys(Keys.TAB)

        time.sleep(0.5)  # pequena pausa para o sistema processar

        # ===== DATA FIM =====
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "campo de data final"))
        ).click()

        driver.find_element(By.ID, "campo de data final").send_keys(Keys.CONTROL + "a")
        driver.find_element(By.ID, "campo de data final").send_keys(DATA_FIM)
        driver.find_element(By.ID, "campo de data final").send_keys(Keys.TAB)

        time.sleep(0.5)

    except Exception as e:
        print("Erro ao preencher datas:", e)

#Preenchendo os campos de resumo e operadores logicos com as palavras r condicionais definidas nas listas no topo do codigo.
def preencher_filtros(processo):
    import time
    
    #preenche cada campo de resumo individualmente, buscando o elemento cada vez para evitar stale elements
    campos_ids = ["Resumo 1", "Resumo 2", "Resumo 3"]
    
    for i, palavra in enumerate(processo["palavras"]):
        tentativas = 0
        while tentativas < 3:
            try:
                # Busca o campo com WebDriverWait para garantir que está pronto
                campo = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, campos_ids[i])))
                time.sleep(0.5)
                
                # Clica no campo para focar
                campo.click()
                time.sleep(0.3)
                
                # Seleciona tudo e limpa
                campo.send_keys(Keys.CONTROL + "a")
                time.sleep(0.2)
                campo.send_keys(Keys.DELETE)
                time.sleep(0.5)
                
                # Envia a palavra
                campo.send_keys(palavra)
                time.sleep(0.5)
                
                print(f"Campo {i+1} preenchido: {palavra}")
                break  # Sucesso, sai do loop de tentativas
            except Exception as e:
                tentativas += 1
                if tentativas >= 3:
                    print(f"Erro final ao preencher o campo de resumo {i+1}: {e}")
                time.sleep(0.5)

    time.sleep(1)  # Espera um pouco antes de preencher os operadores
    
    #preenche os operadores, buscando cada um individualmente
    operadores_ids = ["Condicional 1", "Condicional 2"]

    for i, operador in enumerate(processo["operadores"]):
        if i >= len(operadores_ids):
            break

        try:
            time.sleep(0.5)
            # Busca o operador novamente a cada iteração
            op_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, operadores_ids[i])))
            
            # Verifica se é um <select> normal
            select_element = Select(op_element)
            try:
                select_element.select_by_visible_text(operador)
                valor_selecionado = select_element.first_selected_option.text
                print(f"✓ Operador {i+1} selecionado: {valor_selecionado}")
            except Exception as e_operador:
                # Se não conseguir com o texto do operador, tenta com "OU" (padrão em português)
                try:
                    select_element.select_by_visible_text("OU")
                    valor_selecionado = select_element.first_selected_option.text
                    print(f"✓ Operador {i+1} selecionado (padrão): {valor_selecionado}")
                except Exception as e_ou:
                    pass
            
        except Exception as e:
            print(f"Erro ao acessar o dropdown {i+1}: {e}")

#Clica no pesquisar

def clicar_pesquisar():
    try:
        btn = WebDriverWait(driver,7).until(EC.element_to_be_clickable((By.ID, "Pesquisar")))
        btn.click()
    except Exception as e:
        print("Erro ao clicar em pesquisar:", e)

#Gravar o total de processos
def gravar_total():

    try:
        time.sleep(2)  # Espera um pouco para a página carregar
        
        # Pega o valor atual
        elemento = driver.find_element(By.ID, "Resultado da pesquisa")
        valor_texto = elemento.text.strip()
        
        # Tenta converter para inteiro
        if valor_texto and valor_texto.isdigit():
            valor = int(valor_texto)
            return valor
        else:
            return None
        
    except Exception as e:
        print(f"Erro ao gravar total de processos: {e}")
        return None
    
#Gravar os resultados na planilha XLSX
def atualizar_planilha(resultados):

    try:
        #Caminhos
        caminho_rede = r"Caminho da planilha na rede"
        caminho_local = r"Caminho na planilha localmente"
        
        #Copia o arquivo da rede para local
        shutil.copy(caminho_rede, caminho_local)
        
        #Abre a planilha local
        workbook = load_workbook(caminho_local)
        
        #Seleciona a aba correta
        nome_aba = "Aba da planilha"
        sheet = workbook[nome_aba]

        #Dicionário com o nome dos meses que são as colunas
        meses = {
            1: "Janeiro",
            2: "Fevereiro",
            3: "Março",
            4: "Abril",
            5: "Maio",
            6: "Junho",
            7: "Julho",
            8: "Agosto",
            9: "Setembro",
            10: "Outubro",
            11: "Novembro",
            12: "Dezembro"
        }

        #Encontra a coluna do mês selecionado
        coluna_mes = meses[mes]

        #variavel começa vazia
        coluna_encontrada = None

        # Percorre as colunas da planilha
        for col in range(1, sheet.max_column + 1):
            #pega o valor da célula
            valor = sheet.cell(row=1, column=col).value
            #verifica se o valor é igual ao mês selecionado
            if valor == coluna_mes:
                #guarda o número da coluna
                coluna_encontrada = col
                break

        #Se não achar a coluna
        if coluna_encontrada is None:
            print("Coluna do mês não encontrada na planilha.")
            return

        #Anda pelos resultados
        for resultado in resultados:
            nome_processo = resultado["processo"]
            total = resultado["total"]
            linha_processo = None

            #Procura a linha do processo
            for row in range(2, sheet.max_row + 1):
                # Pega o valor da coluna A
                valor = sheet.cell(row=row, column=1).value
                
                if valor and str(valor).strip().lower() == str(nome_processo).strip().lower():
                    linha_processo = row
                    break

            # Se o processo não existir
            if linha_processo is None:
                # pula para o próximo processo
                continue

            # Atualiza o valor do processo apenas se total não for None
            if total is not None:
                sheet.cell(row=linha_processo, column=coluna_encontrada).value = total
                print(f"✓ Atualizado {nome_processo} com total {total} na coluna {coluna_encontrada}")
            else:
                print(f"✗ Não atualizando {nome_processo} - total é None")

        #Salva a planilha local
        caminho_local = r"Caminho local da planilha"
        caminho_rede = r"Caminho da planilha na rede"
        workbook.save(caminho_local)
        
        #Copia de volta para a rede
        shutil.copy(caminho_local, caminho_rede)
        
        #Remove o arquivo temporário
        os.remove(caminho_local)
        print("Planilha atualizada e salva com sucesso na rede.")

    except Exception as e:
        print(f"Erro ao atualizar planilha: {e}")

#===================================================================================
#Loop que anda na lista de processos, preencher os filtros, clicar em pesquisar e gravar o total de processos encontrados para cada tipo de processo.
#===================================================================================

#Lista que guarda resultados
resultados = []

#Loop principal
try:
    for processo in processos:
        try:
            print(f"\nProcessando: {processo['nome']}")

            limpar_filtros()
            time.sleep(1)  # Espera um pouco para garantir que os filtros foram limpos
            preencher_datas()
            preencher_filtros(processo)
            clicar_pesquisar()
            total = gravar_total()

#Adiciona resultados na lista
            resultados.append({"processo": processo['nome'], "total": total})

            print(f"Total de processos para {processo['nome']}: {total}")
            
        except Exception as e:
            print(f"Erro ao processar {processo['nome']}: {e}")
            resultados.append({"processo": processo['nome'], "total": None})
            continue

#Atualiza a planilha com os resultados
    atualizar_planilha(resultados)
    print("\nAutomação concluída")

except KeyboardInterrupt:
    print("\nExecução interrompida pelo usuário")
except Exception as e:
    print(f"Erro geral: {e}")

# Fecha o navegador se ainda estiver aberto
try:
    driver.quit()
    print("Navegador fechado")
except:
    print("Navegador já estava fechado")

