from gestor import Gestor
import os
import time

def limpar_tela():
    print("Voltando ao menu...")
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    gestor = Gestor()
    
    while True:
        print("\n \t=========== BEM VINDO AO GESTOR DE TAREFAS ===========\n")
        print("1. Adicionar Tarefa\t2. Listar Tarefas\t3. Atualizar Tarefa\n4. Eliminar Tarefa\t 5. Sair")
        opcao = input("Escolha a opção que deseja: ")
        
        if opcao == '1':
            titulo = input("Título da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            data_fim = input("Data de término da tarefa: ")
            gestor.adicionar_tarefa(titulo, descricao, data_fim)
            limpar_tela()
            
        elif opcao == '2':
            gestor.listar_tarefas()
            limpa = input("Prima qualquer tecla para voltar ao menu...")
            limpar_tela()
            
        elif opcao == '3':
            try:
                if gestor.listar_tarefas() == True:
                    id = int(input("ID da tarefa a atualizar: "))
                if gestor.encontrar_tarefa(id) == True:
                    novo_titulo = input("Novo titulo: ")
                    nova_descricao = input("Nova descrição: ")
                    concluida = input("Está concluída? (s/n): ").lower()
                    gestor.atualizar_tarefa(id, novo_titulo, nova_descricao, concluida)
                else:
                    print("Tarefa não encontrada")
            except Exception as e:
                print("Erro", e)
            finally:
                limpar_tela()
            
        elif opcao == '4':
            try:
                if gestor.listar_tarefas() == True:
                    id = int(input("ID da tarefa a eliminar: "))
                    gestor.eliminar_tarefa(id)
            except Exception as e:
                print("Erro",e)
            finally:
                limpar_tela()
            
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tentar novamente.")
            limpar_tela()

# Executa o menu
if __name__ == "__main__":
    menu()