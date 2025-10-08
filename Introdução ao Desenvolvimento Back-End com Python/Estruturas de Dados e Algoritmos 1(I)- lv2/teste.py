
#versão q eu fiz fa tarefa e funciona, mas devo melhorar e refazela no futuro. 
def adicionar_tarefa(tarefas):
    #Solicita o nome da tarefa via input().
    tarefa=input()

    #Verifica se já existe no dicionário.
    try:
        if tarefas[tarefa]==True or tarefas[tarefa]==False:
            #Se existir: Exibe "Essa tarefa já existe."
            print("Essa tarefa já existe.")
    except:
        #Se não existir: Adiciona com status False e exibe "Tarefa '{nome}' adicionada com sucesso!".
            tarefas[tarefa]=False
            print(tarefas)

def listar_tarefas(tarefas):
    if not tarefas:
        print("não a tarefa")
    else:
        itens_do_dicionario = tarefas.items()

            # Ordena a lista de tuplas pela chave (primeiro elemento de cada tupla)
        itens_ordenados = sorted(itens_do_dicionario, key=lambda item: item[0])

            # Converte a lista ordenada de volta para um dicionário
        dicionario_ordenado = dict(itens_ordenados)

        for chave in dicionario_ordenado: 
                if dicionario_ordenado[chave]==True:   
                        print(chave, "✅ Concluída") 
                else:
                        print(chave, "❌ Não concluída") 
def remover_tarefa(tarefas):
    tarefa=input()
    try:
      del tarefas[tarefa]
      print(f"Tarefa '{tarefa}' removida com sucesso!") 
    except KeyError:        
            print("Erro: Tarefa não encontrada.")

def marcar_concluida(tarefas):
    tarefa=input()
    try:
        if tarefas[tarefa]==False or tarefas[tarefa]==True:
                tarefas[tarefa]=True
                print(f"Tarefa '{tarefa}' marcada como concluída!")
    except:
            print("Erro: Tarefa não encontrada.")

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
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            remover_tarefa(tarefas)
        elif opcao == "4":
            marcar_concluida(tarefas)
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
def main():
    #criar o dicinaris para armazenas as tarefas que serão solicitadas 
    #tarefas={"correr":False,"caminhar":True}
    tarefas={}
    exibir_menu(tarefas)

if __name__ == "__main__":
    main()
