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
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.data_inicio = datetime.now()
        if datetime.strptime(data_fim, "%Y-%m-%d") < self.data_inicio:
            raise ValueError("A nova data de fim não pode ser anterior à data de início.")
        else:
            self.data_fim = datetime.strptime(data_fim, "%Y-%m-%d")
        self.concluida = False
        
    def __str__(self):
        """
        O meu metodo toString para apresentar o objecto em string
        retorna uma representação legivel da tarefa
        """
        if not (self.concluida) and self.data_fim < datetime.now():
            estado = "Atrasada"  
        if not self.concluida and self.data_fim < datetime.now():
            estado = "Atrasada"
        elif not self.concluida:
            estado = "Pendente"
        elif self.concluida:
            estado = "Concluído"     
        return f"""
            ID: {self.id} \nTarefa: {self.titulo} \n Descrição: {self.descricao}\n
            Início: {self.data_inicio}\nFim: {self.data_fim} \n {estado} 
        """
        
    
