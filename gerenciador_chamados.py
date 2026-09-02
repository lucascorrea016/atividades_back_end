chamados = [
    {
        "id": 1,
        "titulo": "Sem acesso ao sistema interno",
        "prioridade": "alta",
        "situacao": "aberto",
        "categoria": "acesso"
    },
    {
        "id": 2,
        "titulo": "Impressora sem conexão",
        "prioridade": "média",
        "situacao": "em atendimento",
        "categoria": "hardware"
    },
    {
        "id": 3,
        "titulo": "Erro no sistema financeiro",
        "prioridade": "alta",
        "situacao": "aberto",
        "categoria": "software"
    },
    {
        "id": 4,
        "titulo": "Solicitação de novo usuário",
        "prioridade": "baixa",
        "situacao": "concluído",
        "categoria": "acesso"
    },
    {
        "id": 5,
        "titulo": "Teclado com defeito",
        "prioridade": "média",
        "situacao": "em atendimento",
        "categoria": "hardware"
    }
]


print("=== Lista de Chamados ===")

for chamado in chamados:
    print(f"ID: {chamado['id']}")
    print(f"Título: {chamado['titulo']}")
    print(f"Prioridade: {chamado['prioridade']}")
    print(f"Situação: {chamado['situacao']}")
    print(f"Categoria: {chamado['categoria']}")
    print("------------------------------")


print("\n=== Filtro por Situação ===")

situacao_desejada = "aberto"
encontrou_chamado = False

for chamado in chamados:
    if chamado["situacao"] == situacao_desejada:
        print(f"ID: {chamado['id']} - {chamado['titulo']}")
        print(f"Prioridade: {chamado['prioridade']}")
        print(f"Categoria: {chamado['categoria']}")
        print("------------------------------")
        encontrou_chamado = True

if encontrou_chamado == False:
    print("Nenhum chamado encontrado para essa situação.")


print("\n=== Filtro sem Resultado ===")

situacao_desejada = "cancelado"
encontrou_chamado = False

for chamado in chamados:
    if chamado["situacao"] == situacao_desejada:
        print(f"ID: {chamado['id']} - {chamado['titulo']}")
        encontrou_chamado = True

if encontrou_chamado == False:
    print("Nenhum chamado encontrado para essa situação.")


print("\n=== Atualização de Chamado ===")

id_atualizar = 2
nova_situacao = "concluído"
chamado_encontrado = False

for chamado in chamados:
    if chamado["id"] == id_atualizar:
        chamado["situacao"] = nova_situacao
        chamado_encontrado = True
        print(f"Chamado {id_atualizar} atualizado com sucesso.")
        break

if chamado_encontrado == False:
    print("Chamado não encontrado.")


print("\n=== Atualização de Chamado Inexistente ===")

id_atualizar = 10
nova_situacao = "concluído"
chamado_encontrado = False

for chamado in chamados:
    if chamado["id"] == id_atualizar:
        chamado["situacao"] = nova_situacao
        chamado_encontrado = True
        print(f"Chamado {id_atualizar} atualizado com sucesso.")
        break

if chamado_encontrado == False:
    print("Chamado não encontrado.")


print("\n=== Categorias dos Chamados ===")

categorias = set()

for chamado in chamados:
    categorias.add(chamado["categoria"])

print("Categorias encontradas:")

for categoria in categorias:
    print(f"- {categoria}")