from tarefa import Tarefa
from datetime import datetime
import json

class Gestor:
    def __init__(self):
        self.tarefas = []
        self.proximo_id = 1

    def encontrar_tarefa(self,id):
        for t in self.tarefas:
            if t.id == id:
                print(t)
                return True
        return False
    def adicionar_tarefa(self, titulo, descricao, data_fim):
        tarefa = Tarefa(self.proximo_id, titulo, descricao, data_fim)
        self.tarefas.append(tarefa)
        self.proximo_id += 1
    
    def listar_tarefas(self):
        if self.tarefas:
            for tarefa in self.tarefas:
                print(tarefa)
            return True
        else:
            print("Nenhuma tarefa com cadastrada no sistema!")
            return False
                
    def atualizar_tarefa(self, id, novo_titulo, nova_descricao, concluida):
        for tarefa in self.tarefas:
            if tarefa.id == id:
                print("Tarefa encontrada")
                print(tarefa)
                tarefa.titulo = novo_titulo
                tarefa.descricao = nova_descricao
                tarefa.concluida = True if concluida == 's' else False
                print("Tarefa atualizada com sucesso!")
                return True
        print("Tarefa não encontrada.")
        return False
        
    def eliminar_tarefa(self, id):
        for tarefa in self.tarefas:
            if tarefa.id == id:
                self.tarefas.remove(tarefa)
                print("Tarefa eliminada com sucesso!!!")
                return
            print("Tarefa não encontrada.")
        
        
        

        