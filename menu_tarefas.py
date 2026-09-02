tarefas = []

while True:
    print("\n=== Menu de Tarefas ===")
    print("1 - Cadastrar tarefa")
    print("2 - Listar tarefas")
    print("3 - Atualizar situação")
    print("4 - Encerrar sistema")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Título da tarefa: ").strip()
        prioridade = input("Prioridade (baixa, média ou alta): ").lower()

        if titulo == "":
            print("O título não pode estar vazio.")
        elif prioridade != "baixa" and prioridade != "média" and prioridade != "alta":
            print("Prioridade inválida. Escolha baixa, média ou alta.")
        else:
            tarefa = {
                "titulo": titulo,
                "prioridade": prioridade,
                "situacao": "pendente"
            }

            tarefas.append(tarefa)
            print("Tarefa cadastrada com sucesso.")

    elif opcao == "2":
        if len(tarefas) == 0:
            print("Não há tarefas cadastradas.")
        else:
            print("\n=== Tarefas cadastradas ===")

            for numero, tarefa in enumerate(tarefas, start=1):
                print(
                    f"{numero} - {tarefa['titulo']} | "
                    f"prioridade: {tarefa['prioridade']} | "
                    f"situação: {tarefa['situacao']}"
                )

    elif opcao == "3":
        numero_tarefa = input("Digite o número da tarefa que deseja concluir: ")

        if numero_tarefa.isdigit():
            indice = int(numero_tarefa) - 1

            if indice >= 0 and indice < len(tarefas):
                tarefas[indice]["situacao"] = "concluída"
                print("Tarefa atualizada com sucesso.")
            else:
                print("Tarefa inexistente.")
        else:
            print("Número inválido.")

    elif opcao == "4":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida. Escolha um número de 1 a 4.")