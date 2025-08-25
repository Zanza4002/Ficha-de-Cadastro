from datetime import datetime
import os

def criar_ficha(nome, idade, salario, funcao, cidade, estado, bairro, data_nascimento):
    return { 
        "nome": nome,
        "idade": idade,
        "salario": salario,
        "funcao": funcao,
        "data_nascimento": data_nascimento, #formato 'dd/mm/aaaa'
        "endereco": {
            "cidade": cidade,
            "estado": estado,
            "bairro": bairro,
            }
    }

def mostrar_ficha(ficha):
    print("\n---FICHA---")
    print(f"Nome: {ficha['nome']}")
    print(f"Idade: {ficha['idade']}")
    print(f"Salário: {ficha['salario']}")
    print(f"Função: {ficha['funcao']}")
    print(f"Nascimento: {ficha['data_nascimento']}")
    print(f"Cidade/UF: {ficha['endereco']['cidade']} - {ficha['endereco']['estado']} - {ficha['endereco']['bairro']}")

# ---------------------------
# Funções auxiliares de leitura
# ---------------------------

def ler_nome():
    while True:
        nome = input("Nome: ").strip()
        if len(nome) >= 2:
            return nome
        print("⚠️ Nome muito curto. Tente Novamente")

def ler_idade():
    while True:
        valor = input("Idade (anos):  ").strip()
        if valor.isdigit():
            idade = int(valor)
            if idade >= 0:
                return idade
        print ("⚠️ Idade inválida. Digite um número inteiro > 0.")

def parse_float_br(txt):
    # aceita "3500", "3.500,75", "3500.75", "3,500.75" etc.
    normalizado = txt.replace(".", "").replace(",", ".")
    return float(normalizado)

def formatar_moeda_br(valor):
    # formata 1234567.8 -> '1.234.567,80'
    s = f"{valor:,.2f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")

def ler_salario():
    while True:
        txt = input("Salário (ex: 3500,00): ").strip()
        try:
            valor = parse_float_br(txt)
            if valor >= 0:
                return valor
        except ValueError:
            pass
        print("⚠️  Salário inválido. Tente algo como 3500,00.")

def ler_funcao():
    while True:
        funcao = input("Função/Cargo: ").strip()
        if funcao:
            return funcao.title()
        print("⚠️ Função não pode ficar vazia.")

def ler_data_nascimento():
    while True:
        txt = input("Data de Nascimento (dd/mm/aaaa): ").strip()
        try:
            dt = datetime.strptime(txt, "%d/%m/%Y")
            return dt.strftime("%d/%m/%Y")
        except ValueError:
            print("⚠️ Data inválida. Use dd/mm/aaaa.")

def ler_cidade():
    while True:
       cidade = input("Cidade: ").strip()
       if cidade:
           return cidade
       print("⚠️ Cidade não pode ficar vazia.")

def ler_estado():
    while True:
        uf = input("Estado (UF, ex: SP:) ").strip().upper()
        if len(uf) == 2 and uf.isalpha():
            return uf
        print("⚠️  Informe a UF com 2 caractéres (ex: SP, RJ, BA).")

def ler_bairro():
    while True:
        bairro = input("Bairro: ").strip()
        if bairro:
            return bairro
        print("⚠️ Bairro não pode ficar vazio.")

# ---------------------------
# Programa principal
# ---------------------------

if __name__ == "__main__":
    # 1 - Mostrar Ficha de Ana
    pessoa = criar_ficha(
        nome= "Ana", #nome
        idade= 25, #idade
        salario= 3500.00, #salário
        funcao= "Analista", #função
        cidade= "São Bernardo do Campo", #cidade
        estado= "SP", #estado
        bairro= "Riacho Grande", #bairro
        data_nascimento= "10/02/2000" #data_nascimento
    )
pessoa['salario'] = formatar_moeda_br(pessoa['salario'])
mostrar_ficha(pessoa)

# Pausa até usuário apertar Enter
input("\nPressione Enter para preencher sua ficha.")

#Limpa tela (Windows/Linux)
os.system("cls" if os.name == "nt" else "clear")

# 2 - Pedir os dados do usuário
print("Preencha a Ficha:")
ficha = criar_ficha(
        ler_nome(),
        ler_idade(),
        ler_salario(),
        ler_funcao(),
        ler_cidade(),
        ler_estado(),
        ler_bairro(),
        ler_data_nascimento(),  
    )
ficha['salario'] = formatar_moeda_br(ficha['salario'])

# Limpa a tela de novo antes de exibir a ficha preenchida
os.system("cls" if os.name == "nt" else "clear")

# Mostrar somente a ficha final
mostrar_ficha(ficha)
print("\n✅ Ficha Preenchida com Sucesso!")