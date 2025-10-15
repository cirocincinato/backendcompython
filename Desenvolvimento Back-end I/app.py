from fastapi import FastAPI,HTTPException

app=FastAPI()
#

tarefas = []

@app.get("/tarefas")
def get_livros():
    if not tarefas:
        return {"message":"Não existe nenhuma tarefa!"}
    else:
        return {"tarefa": tarefas}

@app.post("/adicionar")
def post_tarefa(id_tarefa:int,nome_tarefa:str,descricao_tarefa:str,concluida=False):
    #se id for menor(<)ou igual que tarefa então não existe na lista
    if id_tarefa <= len(tarefas):
        raise HTTPException(status_code=400,detail="esse tarefa ja existe!")
        
    else:
        tarefas.append({
            'nome_tarefa': nome_tarefa,
            'descricao_tarefa': descricao_tarefa,
            'concluida': concluida
        })
        return{"massage":"As informações do seu livro foram adicionadas com sucesso!"}
    
    
    