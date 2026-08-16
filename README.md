# Sistema de Gerenciamento de Tarefas - TechFlow Solutions

## 1. Sobre o Projeto
Este repositório contém, o desenvolvimento de um sistema de gerenciamento de tarefas básico baseado em metodologias ágeis[cite: 1], desenvolvido para atender às necessidades da **TechFlow Solutions** e de uma startup de logística parceira[cite: 1]. O objetivo principal é permitir o acompanhamento do fluxo de trabalho em tempo real, priorizar tarefas críticas e monitorar o desempenho da equipe[cite: 1].

## 2. Metodologia Adotada
O projeto foi gerido utilizando a metodologia **Kanban**, estruturada através da aba *Projects* do GitHub[cite: 1]. O quadro divide-se nas seguintes colunas:
* **A Fazer (To Do):** Backlog inicial de tarefas mapeadas para o sistema.
* **Em Progresso (In Progress):** Funcionalidades e tarefas em desenvolvimento ativo.
* **Concluído (Done):** Tarefas finalizadas, testadas e integradas.

## 3. Estrutura do Repositório
* `/src`: Contém o código fonte principal do sistema (`gerenciador.py`)[cite: 1].
* `/tests`: Contém os testes, unitários automatizados (`test_gerenciador.py`)[cite: 1].
* `/.github/workflows`: Contém a pipeline de Integração Contínua (CI) do GitHub Actions (`pipeline.yml`)[cite: 1].

## 4. Instruções para Executar o Sistema e Testes
### Pré-requisitos
* Python 3.x instalado.
* Biblioteca PyTest instalada (`pip install pytest`).

### Como rodar os testes automatizados
No terminal, na raiz do projeto, execute o comando:
```bash
pytest