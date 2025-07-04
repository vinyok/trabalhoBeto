def cadastrar_participante_em_evento(participantes, eventos):
    cpf_participante = input("Digite o CPF do participante: ")
    evento_nome = input("Digite o nome do evento: ")
    
    for p in participantes:
        if p["codigo"] == cpf_participante:
            participante_nome = p["nome"]
            break
    else:
        print("Participante não encontrado.")
        return
    for e in eventos:
        if e["nome"].lower() == evento_nome.lower():
            evento_atual = e
            break
    else:
        print("Evento não encontrado.")
        return
    if cpf_participante in evento_atual["participantes"]:
        print(f"O participante '{participante_nome}' já está inscrito no evento '{evento_atual['nome']}'.")
        return
    evento_atual["participantes"].append(cpf_participante)
    print(f"Participante '{participante_nome}' foi cadastrado no evento '{evento_atual['nome']}' com sucesso!")


def adicionar_participante(participantes):
    nome = input("Digite o primeiro e o último nome do participante: ")
    
    codigo_cpf = input("\nDigite o código único (CPF) do participante: ")
    for participante in participantes:
        if participante["codigo"] == codigo_cpf:
            print("CPF já cadastrado!")
            return
        
    email = input("Digite o e-mail do participante: ")
    for participante in participantes:
        if participante["email"] == email:
            print("E-mail já cadastrado!")
            return
        
    preferencia_tema = input("Digite a preferência temática do participante: ")

    novo_participante = {
        "codigo": codigo_cpf,
        "nome": nome,
        "email": email,
        "preferencia_tematica": preferencia_tema,
    }
    participantes.append(novo_participante)
    print(f"Participante '{nome}' adicionado com sucesso!")


def buscar_participante(participantes):
    codigo_cpf = input("Digite o código único (CPF) do participante: ")
    for participante in participantes:
        if participante["codigo"] == codigo_cpf:
            print("\nParticipante encontrado:")
            print(f"Nome: {participante['nome']}")
            print(f"Email: {participante['email']}")
            print(f"Preferência temática: {participante['preferencia_tematica']}")
            return
    print("Participante não encontrado.")


def listar_participantes(participantes):
    print("Lista de participantes:")
    if not participantes:
        print("Nenhum participante cadastrado.")
    else:
        for p in participantes:
            print(f"- Código: {p['codigo']} | Nome: {p['nome']} | Email: {p['email']} | Preferência temática: {p['preferencia_tematica']}")

def remover_participante(participantes):
    codigo = input("Digite o código (CPF) do participante a ser removido: ")
    for i, participante in enumerate(participantes):
        if participante["codigo"] == codigo:
            nome = participante["nome"]
            del participantes[i]
            print(f"Participante '{nome}' removido com sucesso!")
            return
    print("Participante não encontrado.")


def atualizar_participante(participantes):
    codigo = input("Digite o código (CPF) do participante para atualizar: ")
    for participante in participantes:
        if participante["codigo"] == codigo:
            print("\nDados atuais:")
            print(f"Nome: {participante['nome']}")
            print(f"Email: {participante['email']}")
            print(f"Preferência temática: {participante['preferencia_tematica']}")

            novo_nome = input("Novo nome (pressione Enter para manter o atual): ")
            novo_email = input("Novo e-mail (pressione Enter para manter o atual): ")
            nova_preferencia = input("Nova preferência temática (pressione Enter para manter a atual): ")

            if novo_nome.strip():
                participante["nome"] = novo_nome
            if novo_email.strip():
                participante["email"] = novo_email
            if nova_preferencia.strip():
                participante["preferencia_tematica"] = nova_preferencia

            print("Participante atualizado com sucesso!")
            return
    print("Participante não encontrado.")



def listar_eventos_que_participante_esta_cadastrado(participantes, eventos):
    codigo = input("Digite o código (CPF) do participante: ")
    nome_participante = ""
    encontrado = False

    for p in participantes:
        if p["codigo"] == codigo:
            nome_participante = p["nome"]
            encontrado = True
            break

    if not encontrado:
        print("Participante não encontrado.")
        return

    eventos_encontrados = []

    for evento in eventos:
        if codigo in evento.get("participantes", []):
            eventos_encontrados.append(evento["nome"])

    print(f"\nEventos em que '{nome_participante}' está inscrito:")
    if eventos_encontrados:
        for nome_evento in eventos_encontrados:
            print(f"- {nome_evento}")
    else:
        print("Nenhum evento encontrado para este participante.")

            