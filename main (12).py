import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPressione ENTER para voltar ao menu...")

def escrever_lento(texto):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(0.015)
    print()

# ==============================
# EVENTOS HISTÓRICOS DETALHADOS
# ==============================

def povos_indigenas():
    limpar_tela()
    escrever_lento("📜 Povos Indígenas (Antes de 1500)\n")
    escrever_lento("A região era habitada pelos povos Carijós, do tronco Tupi-Guarani.")
    escrever_lento("Viviam da pesca, coleta, caça e agricultura.")
    escrever_lento("A mandioca era base da alimentação.")
    escrever_lento("Mantinham forte relação espiritual com a natureza.")
    pausar()

def chegada_europeus():
    limpar_tela()
    escrever_lento("⚓ 1542 – Primeiras Expedições Europeias\n")
    escrever_lento("O navegador espanhol Álvar Núñez Cabeza de Vaca passou pela região.")
    escrever_lento("A ilha era estratégica para navegação no Atlântico Sul.")
    pausar()

def fundacao_vila():
    limpar_tela()
    escrever_lento("🏘️ 1673 – Fundação da Vila\n")
    escrever_lento("Francisco Dias Velho fundou o povoado.")
    escrever_lento("Foi construída a Capela de Nossa Senhora do Desterro.")
    escrever_lento("A vila tornou-se ponto estratégico contra invasões.")
    pausar()

def fortificacoes():
    limpar_tela()
    escrever_lento("🏰 Século XVIII – Sistema de Fortificações\n")
    escrever_lento("Foram construídas fortalezas para defender a ilha.")
    escrever_lento("Destaques:")
    escrever_lento("- Fortaleza de São José da Ponta Grossa")
    escrever_lento("- Fortaleza de Santo Antônio de Ratones")
    escrever_lento("- Fortaleza de Santa Cruz de Anhatomirim")
    escrever_lento("Essas estruturas protegiam contra invasões espanholas.")
    pausar()

def chegada_acorianos():
    limpar_tela()
    escrever_lento("🌊 1748–1756 – Chegada dos Açorianos\n")
    escrever_lento("Milhares de imigrantes vieram dos Açores (Portugal).")
    escrever_lento("Influenciaram arquitetura, culinária e tradições.")
    escrever_lento("A pesca artesanal tornou-se atividade central.")
    pausar()

def invasao_espanhola():
    limpar_tela()
    escrever_lento("⚔️ 1777 – Invasão Espanhola\n")
    escrever_lento("A ilha foi ocupada pela Espanha temporariamente.")
    escrever_lento("Posteriormente, voltou ao domínio português.")
    pausar()

def mudanca_nome():
    limpar_tela()
    escrever_lento("🏛️ 1894 – Mudança para Florianópolis\n")
    escrever_lento("Durante a Revolução Federalista, a cidade foi palco de conflitos.")
    escrever_lento("Após o conflito, o nome foi alterado para homenagear Floriano Peixoto.")
    pausar()

def ponte_hercilio_luz():
    limpar_tela()
    escrever_lento("🌉 1926 – Inauguração da Ponte Hercílio Luz\n")
    escrever_lento("A ponte ligou a ilha ao continente.")
    escrever_lento("Tornou-se símbolo da cidade.")
    escrever_lento("Foi reaberta após restauração em 2019.")
    pausar()

def desenvolvimento_turismo():
    limpar_tela()
    escrever_lento("🏖️ Décadas de 1970–1990 – Crescimento do Turismo\n")
    escrever_lento("Florianópolis tornou-se destino turístico nacional.")
    escrever_lento("Praias como Jurerê, Campeche e Canasvieiras ganharam destaque.")
    pausar()

def polo_tecnologico():
    limpar_tela()
    escrever_lento("💻 Século XXI – Polo Tecnológico\n")
    escrever_lento("A cidade passou a ser conhecida como 'Ilha do Silício'.")
    escrever_lento("Destaca-se na área de tecnologia e startups.")
    escrever_lento("Hoje é um dos principais polos tecnológicos do Brasil.")
    pausar()

# ==============================
# MENU
# ==============================

def menu():
    while True:
        limpar_tela()
        print("=" * 60)
        print("🏝️ LINHA DO TEMPO COMPLETA – FLORIANÓPOLIS")
        print("=" * 60)
        print("1 - Povos Indígenas")
        print("2 - Primeiras Expedições Europeias")
        print("3 - Fundação da Vila")
        print("4 - Sistema de Fortificações")
        print("5 - Chegada dos Açorianos")
        print("6 - Invasão Espanhola")
        print("7 - Mudança de Nome")
        print("8 - Ponte Hercílio Luz")
        print("9 - Crescimento do Turismo")
        print("10 - Polo Tecnológico")
        print("0 - Sair")
        print("=" * 60)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            povos_indigenas()
        elif opcao == "2":
            chegada_europeus()
        elif opcao == "3":
            fundacao_vila()
        elif opcao == "4":
            fortificacoes()
        elif opcao == "5":
            chegada_acorianos()
        elif opcao == "6":
            invasao_espanhola()
        elif opcao == "7":
            mudanca_nome()
        elif opcao == "8":
            ponte_hercilio_luz()
        elif opcao == "9":
            desenvolvimento_turismo()
        elif opcao == "10":
            polo_tecnologico()
        elif opcao == "0":
            limpar_tela()
            print("Obrigado por explorar a história de Florianópolis! 🏝️")
            break
        else:
            print("Opção inválida!")
            time.sleep(1)

if __name__ == "__main__":
    menu()