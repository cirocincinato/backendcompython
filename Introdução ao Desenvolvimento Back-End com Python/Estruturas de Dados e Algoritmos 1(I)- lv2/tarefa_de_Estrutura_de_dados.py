

def adicionar_tarefa(tarefa):
    global tarefas
    #Solicita o nome da tarefa via input().

    #Verifica se já existe no dicionário.
    try:
        if tarefas[tarefa]==True or tarefas[tarefa]==False:
            #Se existir: Exibe "Essa tarefa já existe."
            return("Essa tarefa já existe.")
    except:
        #Se não existir: Adiciona com status False e exibe "Tarefa '{nome}' adicionada com sucesso!".
            tarefas[tarefa]=False
            return(f"Tarefa '{tarefa}' adicionada com sucesso!")

def listar_tarefas(tarefa):
    global tarefas
    if not tarefas:
        return("não a tarefa")
    else:
    
        resultado = ""
        for nome, status in sorted(tarefas.items()):
            if status:
                resultado += f"{nome} ✅ Concluída\n"
            else:
                resultado += f"{nome} ❌ Não concluída\n"
        return resultado.strip()
    
def remover_tarefa(tarefa):
    global tarefas
    try:
      del tarefas[tarefa]
      return(f"Tarefa '{tarefa}' removida com sucesso!") 
    except KeyError:        
            return("Erro: Tarefa não encontrada.")

def marcar_concluida(tarefa):
    global tarefas
    try:
        #if tarefas[tarefa]==False or tarefas[tarefa]==True:
        if tarefa in tarefas:
                tarefas[tarefa]=True
                return (f"Tarefa '{tarefa}' marcada como concluída!")
    except:
            return("Erro: Tarefa não encontrada.")

def exibir_menu(tarefas):
     while True:
        print("Menu:\n"
              "1 - Adicionar tarefa\n"
              "2 - Listar tarefas\n"
              "3 - Remover tarefa\n"
              "4 - Marcar tarefa como concluída\n"
              "5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tarefa=input()
            print(adicionar_tarefa(tarefa))
        elif opcao == "2":
            tarefa= input("De enter para listar as tarefas: ")
            print(listar_tarefas(tarefa))
        elif opcao == "3":
            
            tarefa=input()
            print(remover_tarefa(tarefa))
        elif opcao == "4":
            tarefa=input()
            print(marcar_concluida(tarefa))
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
def main():
    #criar o dicinaris para armazenas as tarefas que serão solicitadas 
    #tarefas={"correr":False,"caminhar":True}
    global tarefas
    tarefas={}
    
    exibir_menu(tarefas)

if __name__ == "__main__":
    main()
