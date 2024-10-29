from task_manager import TaskManager

def mostrar_menu():
    print("\n--- Gerenciador de Tarefas ---")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Deletar Tarefa")
    print("5. Sair")
   

def main():
    task_manager = TaskManager()
    
    while True:
        mostrar_menu()
        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            titulo = input("\nTítulo da tarefa: ")
            descricao = input("\nDescrição da tarefa: ")
            prioridade = input("\nPrioridade (Alta, Média, Baixa): ")
            task_manager.add_task(titulo, descricao, prioridade)
        
        elif escolha == "2":
            tasks = task_manager.list_tasks()
            if not tasks:
                print("\nYou don't have any task in your list.")
            else:
                for task in tasks:
                    print(task)

        elif escolha == "3":
            task_manager.list_tasks()
            index = int(input("Número da tarefa a ser concluída: ")) - 1
            task_manager.complete_task(index)
        
        elif escolha == "4":
            task_manager.list_tasks()
            indice = int(input("Número da tarefa a ser deletada: ")) - 1
            task_manager.delete_task(indice)
        
        elif escolha == "5":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()