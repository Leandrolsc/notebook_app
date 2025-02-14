# Bloco de Notas com Streamlit

Este projeto é uma aplicação de bloco de notas construída com Streamlit, seguindo a arquitetura limpa (Clean Architecture).
Acesso: https://lsc-notebook-app.streamlit.app/ 


## Estrutura do Projeto

```plaintext
notebook_app/
│
├── auth/
│   └── user_auth.py
│
│── data/
│
├── entities/
│   └── note.py
│
├── frameworks/
│   └── streamlit_app.py
│
├── interface_adapters/
│   └── repositories.py
│
├── use_cases/
│   ├── add_note.py
│   ├── delete_note.py
│   ├── load_notes.py
│   └── update_note.py
│
└── .gitignore
```

## Descrição dos Arquivos

- **entities/note.py**: Define a entidade Note que representa uma nota com título e conteúdo.
- **frameworks/streamlit_app.py**: Implementa a interface do usuário utilizando Streamlit.
- **interface_adapters/repositories.py**: Implementa o repositório NoteRepository que gerencia as notas, incluindo operações de carregar, salvar, adicionar, deletar e atualizar notas.
- **use_cases/add_note.py**: Implementa o caso de uso para adicionar uma nova nota.
- **use_cases/delete_note.py**: Implementa o caso de uso para deletar uma nota existente.
- **use_cases/load_notes.py**: Implementa o caso de uso para carregar todas as notas.
- **use_cases/update_note.py**: Implementa o caso de uso para atualizar uma nota existente.
- **notes.json**: Arquivo JSON que armazena as notas.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale as dependências necessárias:
    ```sh
    pip install -r requirements.txt
    ```
3. Execute a aplicação Streamlit:
    ```sh
    streamlit run frameworks/streamlit_app.py
    ```

## Funcionalidades

- **Adicionar Nota**: Adicione uma nova nota fornecendo um título e conteúdo.
- **Excluir Nota**: Exclua uma nota existente selecionando-a na lista e clicando no botão "Excluir Nota".
- **Editar Nota**: Edite o conteúdo de uma nota existente.
- **Listar Notas**: Veja todas as notas listadas na interface principal.

## Arquitetura

Este projeto segue a arquitetura limpa (Clean Architecture), que separa a lógica de negócios da lógica de interface e infraestrutura. Isso facilita a manutenção e a escalabilidade do código.

- **Entities**: Contém as entidades de negócios.
- **Use Cases**: Contém a lógica de negócios.
- **Interface Adapters**: Contém os adaptadores que conectam a lógica de negócios com a infraestrutura.
- **Frameworks**: Contém a implementação da interface do usuário e outras dependências de infraestrutura.


