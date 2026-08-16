from src.gerenciador import GerenciadorTarefas

def test_adicionar_tarefa():
    sistema = GerenciadorTarefas()
    assert sistema.adicionar("Tarefa 1") == True
    assert len(sistema.listar()) == 1,