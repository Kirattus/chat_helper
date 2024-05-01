# 📝 Descrição

> O Chat_Helper é uma ferramenta projetada para otimizar a comunicação de usuários e profissionais que frequentemente interagem através de chats. Seu propósito principal é simplificar o processo de inserção de textos predefinidos durante atendimentos, garantindo consistência e precisão nas mensagens. Ao pressionar uma *HOTKEY* predefinida, o programa exibe um menu visual intuitivo, permitindo ao usuário selecionar rapidamente a opção desejada. Uma vez selecionado, o texto correspondente é inserido automaticamente na posição inicial do chat, proporcionando uma experiência de uso fluida e eficiente. Com o Chat_Helper, os usuários podem evitar erros de digitação, economizar tempo e manter um padrão profissional em suas comunicações por chat.

# 🧰 Instalação

## Pré-requisitos

> Chat_Helper pode funcionar em versões antigas, porem não foi testado.
- [`Python`](https://www.python.org/downloads/release/python-3913) 3.11.3
- [`Poetry`](https://python-poetry.org/docs/#installation) >=1.7.1

Antes de continuar, crie um ambiente virtual, executando:
```bash
poetry shell
```
Para instalar as dependencias do projeto, execute:
```bash
poetry install
```
## 🎯 Funcionamento

O Chat_Helper tentará identificar a janela ativa com base no nome da janela definida no arquivo 'chat', exibindo as opções correspondentes para esse ambiente. Caso não seja encontrada nenhuma correspondência, serão exibidas as opções padrão configurada em "default".


![TrayApp](/src/app.ico) Esse icone aparecerá na bandeja onde será o controle da aplicação, ao selecionar "Ativar", o *json* de configuração será carregado para criação do menu tendo a oções *hotkey* configurada para mostrar o menu.
Não é necessario reiniciar a aplicação para modificar o json, basta Desativar e Ativar novamente o App pela bandeja.

> Esse é um modelo basico da estrutura do arquivo de configuração para a criação dos menus (config.json).
```
{
    "name": "SEU_NOME_AQUI",
    "hotkey": "ctrl+shift+a",
    "chat": {
        "default":{
            "Opção 1":{
                "SubOption1": ["paste", "SubOption1 > Olá sou o $name$, tudo bem?$newLine$Como posso ajudar?"],
                "SubOption2": ["paste", "SubOption2 > Option 1"],
                "SubOption3":{
                    "SubSubOption1": ["SubSubOption1 > SubOption3 > Option 1"],
                    "SubSubOption2": ["SubSubOption2 > SubOption3 > Option 1"]
                }
            },
            "Opção 2":{
                "SubOption1": ["paste", "SubOption1 > Option 2"],
                "SubOption2": ["paste", "SubOption2 > Option 2"],
            }
        },
        "whatsapp":{
            "Opção 1":["paste", "Option 1"],
            "Opção 2":["paste", "Option 2"]
        }
    }
}
```


> Podemos usar as seguintes opções para a formatação do texto dentro do arquivo json:
- \$name$" - Adiciona o valor de "name" dentro da frase nas opções.
- \$newLine$ - Faz o pressionamento das teclas "Shift+ENTER" para pular uma linha.
- \\n - Pressiona ENTER.


# ⌨ Desenvolvimento

## ⚙ Executando a aplicação

```bash
poetry run python main.py
```

## 📝 Licença

Copyright © 2024 [**Kirattus**](https://github.com/kirattus)  
Este projeto contém a licença [MIT](https://opensource.org/licenses/MIT).