import json
import tkinter as tk
from tkinter import messagebox

def show_Info(title, msg):
    messagebox.showinfo(title, msg+"\nPor favor, verifique as configurações.")

def createFile():
    try:
        data = {'name': 'SEU_NOME_AQUI',
                'hotkey': None,
                "chat":{
                    "default":{ }
                    }
                }
        
        with open('config.json', 'w') as arquivo:
            json.dump(data, arquivo, indent=4)
        return True
    except Exception as e:
        show_Info("Create File (JSON)", "Erro ao tentar criar arquivo: ", e)
        return False

def load():
    # TODO Verificar
    try:
        with open('config.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            name = data["name"]
            data = substituir_nome(data, name)
        return data
    except FileNotFoundError:
        show_Info("JSON", "O arquivo não foi encontrado.\nCriando novo arquivo.")
        createFile()
        return False
    except json.JSONDecodeError:
        show_Info("JSON", "Erro ao decodificar o arquivo JSON.")
        return False
    except PermissionError:
        show_Info("JSON", "Sem permissão para acessar o arquivo.")
        return False
    except IOError:
        show_Info("JSON", "Erro de entrada/saída ao acessar o arquivo.")
        return False
    except TypeError:
        show_Info("JSON", "Os dados no arquivo JSON não puderam ser decodificados em um objeto Python.")
        return False
    except ValueError:
        show_Info("JSON", "Os dados no arquivo JSON não correspondem ao esperado.")
        return False
    except UnicodeDecodeError:
        show_Info("JSON", "Erro de decodificação de caracteres Unicode.")
        return False
    except OSError:
        show_Info("JSON", "Erro do sistema operacional.")
        return False
    return False

def verify():
    ...

def substituir_nome(valor, substituto):
    if isinstance(valor, str):
        return valor.replace("$name$", substituto)
    elif isinstance(valor, dict):
        for chave, valor_interior in valor.items():
            valor[chave] = substituir_nome(valor_interior, substituto)
        return valor
    elif isinstance(valor, list):
        for i in range(len(valor)):
            valor[i] = substituir_nome(valor[i], substituto)
        return valor
    else:
        return valor