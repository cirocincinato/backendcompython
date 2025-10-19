from fastapi import FastAPI,HTTPException

app=FastAPI()


tarefas = []

@app.get("/tarefas")
def get_livros():
    if not tarefas:
        return {"message":"Não existe nenhuma tarefa!"}
    else:
        return {"tarefa": tarefas}

@app.post("/adicionar")
def post_tarefa(id_tarefa:int,nome_tarefa:str,descricao_tarefa:str):
    # Verificar se o ID já existe
    id_existe = any(id_tarefa in d for d in tarefas)

    # Verificar se o nome já existe
    nome_existe = any(
            dados['nome_tarefa'] == nome_tarefa
            for item in tarefas
            for dados in item.values()
        )
    if id_existe==True or nome_existe==True:
        raise HTTPException(status_code=400,detail="esse tarefa ja existe!")
    elif id_existe==False and nome_existe==False:
        tarefas.append({
                id_tarefa: {
                    'nome_tarefa': nome_tarefa,
                    'descricao': descricao_tarefa,
                    'concluida': False
                }
            })
        return{"massage":"As informações da tarefa foram adicionadas com sucesso!"}
    
@app.put("/atualiza/{nome_tarefa}")
def put_livro(nome_tarefa:str):
    for item in tarefas:
        for dados in item.values():
            if dados['nome_tarefa']==nome_tarefa:
                dados['concluida'] = True
                return {"mensagem": "As informações da tarefa foram atualizadas com sucesso!"}
    raise HTTPException(status_code=400, detail="Não existe essa tarefa!")
        
@app.delete("/deletar/{id_tarefa}")
def delete_livro(id_tarefa:int):    
    for item in tarefas:
        if id_tarefa in item:
            tarefas.remove(item)
            return{"message":"sua tarefa foi deletada"}
    raise HTTPException(status_code=404,detail="Esse livro não foi encontrado")
   
        
