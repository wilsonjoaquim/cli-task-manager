from datetime import datetime

class Tarefa:
    
    def __init__(self, id, titulo, descricao, data_fim):
        """ 
        Meu metodo construtor com os seguintes

        Argumentos:
            tema (str): tema da tarefa
            data_fim (datetime): data limite para a tarefa 
            descricao (str): descricao da tarefa
            estado (str, opcional): padrão "Pendente".
        """
        try:
            self.id = id
            self.titulo = titulo
            self.descricao = descricao
            self.data_inicio = datetime.now()
            if datetime.strptime(data_fim, "%d-%m-%Y") < datetime.now():
                print("Data de fim inválida, menor que a anterior")
                return
            self.data_fim = datetime.strptime(data_fim, "%d-%m-%Y")
        except Exception as e:
            print("Erro", e)
        else:
            print("Tarefa adicionada com sucesso")
        self.concluida = False
        
    def __str__(self):
        """
        O meu metodo toString para apresentar o objecto em string
        retorna uma representação legivel da tarefa
        """
        try:
            if not (self.concluida) and self.data_fim < datetime.now():
                estado = "Atrasada"
            elif not self.concluida:
                estado = "Pendente"
            elif self.concluida:
                estado = "Concluído"     
        except Exception as e:
            print("Erro", e)
        else:
            return f"""ID: {self.id}\nTarefa: {self.titulo}\nDescrição: {self.descricao}\nInício: {self.data_inicio}\nFim: {self.data_fim}\n{estado} 
            """
            
        
    
