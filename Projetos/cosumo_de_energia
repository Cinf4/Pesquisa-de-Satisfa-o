# --- CALCULADORA DE CONSUMO RESIDENCIAL ---

total_kwh_casa = 0
total_custo_casa = 0

print("=== Mentor de Energia: Simulador de Consumo Total ===")

# 1. Definição da Bandeira (Feita uma única vez para a casa toda)
print("\n--- Configuração da Tarifa ---")
while True:
    try:
        print("Bandeiras: 1-Verde | 2-Amarela | 3-Vermelha P1 | 4-Vermelha P2")
        opcao_bandeira = input("Selecione a bandeira atual: ")
        
        # Dicionário de acréscimos por kWh (Lógica limpa)
        tarifas = {"1": 0.0, "2": 0.018, "3": 0.044, "4": 0.078}
        
        if opcao_bandeira in tarifas:
            adicional = tarifas[opcao_bandeira]
            break
        else:
            print("❌ Erro: Escolha uma opção de 1 a 4.")
    except ValueError:
        print("❌ Entrada inválida. Digite apenas o número da opção.")

preco_base = 0.75
preco_final_kwh = preco_base + adicional

# 2. Laço para Adicionar Vários Aparelhos
while True:
    print("\n--- Novo Aparelho ---")
    nome = input("Nome do aparelho (ou digite 'sair' para finalizar): ").strip().capitalize()
    
    if nome.lower() == 'sair':
        break

    # Loop de validação para garantir que os números sejam digitados corretamente
    while True:
        try:
            potencia = float(input(f"Potência de {nome} (Watts): "))
            horas = float(input(f"Uso diário (Horas): "))
            break # Sai do loop de validação se os inputs forem números
        except ValueError:
            print("❌ Erro: Por favor, use números. Para decimais, utilize ponto (ex: 1.5).")

    # Cálculos Individuais
    consumo_mensal = (potencia * horas * 30) / 1000
    custo_mensal = consumo_mensal * preco_final_kwh
    
    # Acumuladores (Soma o aparelho atual ao total da casa)
    total_kwh_casa += consumo_mensal
    total_custo_casa += custo_mensal

    print(f"✅ {nome} adicionado: {consumo_mensal:.2f} kWh | R$ {custo_mensal:.2f}")

# 3. Relatório Final
print("\n" + "="*40)
print("📊 RESUMO DO CONSUMO MENSAL DA RESIDÊNCIA")
print(f"Consumo Total: {total_kwh_casa:.2f} kWh")
print(f"Custo Total Estimado: R$ {total_custo_casa:.2f}")
print(f"Tarifa aplicada (kWh): R$ {preco_final_kwh:.3f}")
print("="*40)
print("Dica: Reduzir 10% do consumo total economizaria R$ {:.2f}!".format(total_custo_casa * 0.1))