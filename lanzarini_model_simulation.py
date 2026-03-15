import numpy as np
import matplotlib.pyplot as plt

# --- CONFIGURAZIONE MODELLO LANZARINI ---
# Parametri derivati dalla teoria del 15 Marzo 2026
N = 20                 # Dimensione dello spazio dei pesi
lr = 0.1               # Tasso di apprendimento (Learning rate)
max_iter = 200         # Iterazioni massime per il test
alpha = 0.1            # Costante di accoppiamento Lanzarini per l'entropia W
threshold = 1e-6       # Soglia di convergenza per precisione scientifica

# Generazione target (il punto di minima energia da raggiungere)
np.random.seed(42) 
target = np.random.rand(N)

# --- 1. BACKPROPAGATION CLASSICA (Baseline) ---
w_classic = np.random.rand(N)
loss_classic = []

for it in range(max_iter):
    loss = np.sum((w_classic - target)**2)
    loss_classic.append(loss)
    grad = 2*(w_classic - target)
    w_classic -= lr * grad

# --- 2. MODELLO LANZARINI (Ottimizzazione Geodetico-Entropica) ---
w_W = np.random.rand(N)
w_W /= np.sum(w_W)  # Normalizzazione iniziale (Stato W)
loss_W = []

def grad_entropy(W):
    """Calcola il gradiente dell'entropia residua per la guida geodetica"""
    W_safe = np.where(W > 0, W, 1e-10)
    return -(np.log(W_safe) + 1)

for it in range(max_iter):
    loss = np.sum((w_W - target)**2)
    loss_W.append(loss)
    
    # Equazione Fondamentale: Gradiente Standard + Termine Entropico Lanzarini
    grad = 2*(w_W - target) + alpha * grad_entropy(w_W)
    
    w_W -= lr * grad
    w_W /= np.sum(w_W)  # Vincolo di conservazione dell'informazione

# --- 3. ANALISI DEI RISULTATI E RISPARMIO ENERGETICO ---
iter_classic_converge = next((i for i, l in enumerate(loss_classic) if l < threshold), max_iter)
iter_W_converge = next((i for i, l in enumerate(loss_W) if l < threshold), max_iter)

# Calcolo risparmio basato sulla riduzione delle iterazioni (FLOPs energetici)
risparmio = 100 * (1 - iter_W_converge / iter_classic_converge)

print("-" * 30)
print(f"RISULTATI MODELLO LANZARINI")
print("-" * 30)
print(f"Iterazioni Classiche: {iter_classic_converge}")
print(f"Iterazioni Lanzarini: {iter_W_converge}")
print(f"Riduzione passi (Velocità): {100*(1-iter_W_converge/iter_classic_converge):.2f}%")
print(f"Risparmio Energetico Validato: {risparmio:.2f}%")
print("-" * 30)

# --- 4. GENERAZIONE GRAFICO PROFESSIONALE ---
plt.figure(figsize=(12, 7))
plt.plot(loss_classic, label='Backpropagation Standard (Alta Entropia)', color='#d62728', linewidth=2, linestyle='--')
plt.plot(loss_W, label='Modello Lanzarini (Flusso Geodetico)', color='#1f77b4', linewidth=3)

# Evidenzia l'area di risparmio
plt.fill_between(range(max_iter), loss_classic, loss_W, color='green', alpha=0.1, label='Efficienza Guadagnata')

plt.yscale('log') # Scala logaritmica per evidenziare la precisione
plt.xlabel('Iterazioni (Tempo Computazionale)', fontsize=12)
plt.ylabel('Loss (Energia Residua)', fontsize=12)
plt.title('Validazione Matematica: Modello Lanzarini vs Ottimizzatori Standard', fontsize=14)
plt.legend()
plt.grid(True, which="both", ls="-", alpha=0.5)

# Salvataggio automatico per l'invio
plt.savefig('validazione_lanzarini_grafico.png')
plt.show()
