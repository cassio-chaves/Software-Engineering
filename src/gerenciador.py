class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar(self, titulo):
        if not titulo: return False
        self.tarefas.append({"titulo": titulo, "status": "A Fazer"})
        return True

    def listar(self):
        return self.tarefas,