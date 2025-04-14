from tarefa import Tarefa
from datetime import datetime

class Gestor:
    def __init__(self):
        self.tarefas = []
        self.proximo_id = 1

    def adicionar_tarefa(self, titulo, descricao, data_fim):
        tarefa = Tarefa(self.proximo_id, titulo, descricao, data_fim)
        if tarefa == Tarefa:
            self.tarefas.append(tarefa)
            self.proximo_id += 1

    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa com cadastrada no sistema!")
        else:
            for tarefa in self.tarefas:
                print(tarefa)

    def atualizar_tarefa(self, id):
        for tarefa in self.tarefas:
            if tarefa.id == id:
                print("Tarefa encontrada:")
                print(tarefa)
                novo_titulo = input("Novo título: ")
                nova_descricao = input("Nova descrição: ")
                tarefa.titulo = novo_titulo
                tarefa.descricao = nova_descricao
                concluida = input("Está concluída? (s/n): ").lower()
                tarefa.concluida = True if concluida == 's' else False
                print("Tarefa atualizada com sucesso!")
                return
        print("Tarefa não encontrada.")
        
    def eliminar_tarefa(self, id):
            for tarefa in self.tarefas:
                if tarefa.id == id:
                    self.tarefas.remove(tarefa)
                    print("Tarefa eliminada com sucesso!!!")
                    return
            print("Tarefa não encontrada.")
        
        
        

        