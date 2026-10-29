class PersonalTrainer:
    def __init__(self):
        self.alunos = []

    def cadastrar_aluno(self):
        print("\n--- CADASTRO DE ALUNO ---")
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        meta = input("Digite a meta de treino (ex: Hipertrofia, Emagrecimento): ")
        dias = input("Digite os dias disponíveis (ex: Seg/Qua/Sex): ")

        aluno = {"nome": nome, "idade": idade, "meta": meta, "dias": dias}
        self.alunos.append(aluno)
        print(f"\n[Sucesso] Aluno '{nome}' cadastrado com sucesso!")

    def listar_alunos(self):
        if not self.alunos:
            print("\n[Aviso] Nenhum aluno cadastrado.")
            return False
        
        print("\n--- LISTA DE ALUNOS CADASTRADOS ---")
        for i, aluno in enumerate(self.alunos):
            print(f"[{i}] Nome: {aluno['nome']} | Idade: {aluno['idade']} anos | Meta: {aluno['meta']} | Dias: {aluno['dias']}")
        return True

    def atualizar_aluno(self):
        if not self.listar_alunos():
            return

        indice = int(input("\nDigite o número (índice) do aluno que deseja atualizar: "))
        
        if 0 <= indice < len(self.alunos):
            print(f"Atualizando dados de: {self.alunos[indice]['nome']}")
            self.alunos[indice]['nome'] = input("Novo nome: ")
            self.alunos[indice]['idade'] = int(input("Nova idade: "))
            self.alunos[indice]['meta'] = input("Nova meta de treino: ")
            self.alunos[indice]['dias'] = input("Novos dias disponíveis: ")
            print("\n[Sucesso] Dados atualizados com sucesso!")
        else:
            print("\n[Erro] Aluno não encontrado.")

    def deletar_aluno(self):
        if not self.listar_alunos():
            return

        indice = int(input("\nDigite o número (índice) do aluno que deseja remover: "))
        
        if 0 <= indice < len(self.alunos):
            removido = self.alunos.pop(indice)
            print(f"\n[Sucesso] Aluno '{removido['nome']}' removido com sucesso!")
        else:
            print("\n[Erro] Aluno não encontrado.")

    def gerar_ficha_treino(self):
        if not self.listar_alunos():
            return

        indice = int(input("\nDigite o número do aluno para gerar a ficha: "))

        if 0 <= indice < len(self.alunos):
            aluno = self.alunos[indice]
            idade = aluno['idade']
            print(f"\n========================================")
            print(f" FICHA DE TREINO - UEMA FIT")
            print(f" Aluno: {aluno['nome']} | Idade: {idade} anos | Meta: {aluno['meta']}")
            print(f"========================================")

            if idade <= 17:
                print("GRUPO: Adolescente (Até 17 anos)")
                print("-> Foco: Desenvolvimento motor e resistência leve (3x na semana).")
            elif 18 <= idade <= 59:
                print("GRUPO: Adulto (18 a 59 anos)")
                print(f"-> Foco: Foco principal em {aluno['meta']} com musculação e cardio.")
            else:
                print("GRUPO: Idoso (60 anos ou mais)")
                print("-> Foco: Funcionalidade, mobilidade e baixo impacto.")
            print("========================================\n")

            input("Pressione ENTER para voltar ao menu...")

            
        else:
            print("\n[Erro] Aluno não encontrado.")

    def menu(self):
        while True:
            print("\n==============================")
            print("    UEMA FIT - SISTEMA DE TREINOS   ")
            print("==============================")
            print("1. Cadastrar Aluno")
            print("2. Listar Alunos")
            print("3. Atualizar Dados")
            print("4. Remover Aluno")
            print("5. Gerar Ficha de Treino")
            print("6. Sair")
            print("==============================")

            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao == 1: self.cadastrar_aluno()
                elif opcao == 2: self.listar_alunos()
                elif opcao == 3: self.atualizar_aluno()
                elif opcao == 4: self.deletar_aluno()
                elif opcao == 5: self.gerar_ficha_treino()
                elif opcao == 6:
                    print("\nSaindo... Até logo!")
                    break
                else: print("\n[Erro] Opção inválida!")
            except ValueError:
                print("\n[Erro] Digite apenas números!")
