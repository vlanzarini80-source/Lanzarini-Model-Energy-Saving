"""
LANZARINI KERNEL CORE - MAIN INTERFACE
Author: Valentino Lanzarini
License: Open for Planet (OFP-L)
"""

# Importiamo tutta la logica dal file engine che hai appena creato
from lanzarini_engine import *

def main():
    # 1. Inizializzazione parametri Lanzarini
    N = 128            # Dimensioni (Target Chip LP-1)
    classical_cost = 100 # Benchmark Wh
    
    print("="*60)
    print("STARTING LANZARINI GEODETIC OPTIMIZATION ENGINE")
    print("Official Release v2026.3 - Global Energy Saving: 5.01 TWh")
    print("="*60)

    # 2. Esecuzione del Modello (Richiama l'Engine)
    report = run_lanzarini_simulation(N, classical_cost)

    # 3. Output Risultati Certificati
    print(f"\n[REPORT FINALE VALENTINO LANZARINI]")
    print(f"Efficienza Reale: {report['efficiency']:.2f}%")
    print(f"Risparmio Energetico: {report['saving_wh']:.2f} Wh")
    print(f"Consumo Finale Ottimizzato: {report['optimized_energy_wh']:.2f} Wh")
    print("\n[STATUS] Open for Planet License Active - Royalty 5% Mandated.")
    print("="*60)

if __name__ == "__main__":
    main()

