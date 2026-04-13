# Simulador de Tempo de Viagem Espacial
# Autor: Gabriel Prata Sinfães Rossi
# Objetivo: Calcular o tempo de deslocamento entre astros

def calcular_viagem():
    print("--- SIMULADOR DE MISSÃO ESPACIAL ---")
    
    # 1. Coleta de dados
    nome_astronauta = input("Digite o nome completo do astronauta: ").strip()
    
    try:
        distancia_km = float(input("Digite a distância da viagem (km): "))
        velocidade_kmh = float(input("Digite a velocidade média da nave (km/h): "))
        
        # Validação simples: velocidade não pode ser zero
        if velocidade_kmh <= 0:
            print("Erro: A velocidade deve ser maior que zero para sair da órbita!")
            return

        # 2. Cálculos (Processamento)
        # Fórmulas aplicadas:
        tempo_horas = distancia_km / velocidade_kmh
        tempo_dias = tempo_horas / 24

        # 3. Exibição dos resultados (Saída)
        print(f"\nAstronauta {nome_astronauta}, bem-vindo à simulação!")
        print(f"A viagem terá uma distância de {distancia_km:.0f} km.")
        print(f"Com velocidade média de {velocidade_kmh:.0f} km/h, o tempo estimado é:")
        print(f"{tempo_horas:.2f} horas ({tempo_dias:.2f} dias).")
        print("Boa sorte na missão!")

    except ValueError:
        print("Erro: Por favor, insira apenas números para distância e velocidade.")

# Executa o programa
if __name__ == "__main__":
    calcular_viagem()
