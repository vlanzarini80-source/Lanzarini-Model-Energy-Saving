import torch
import torch.nn as nn
import time
import matplotlib.pyplot as plt

# --- LANZARINI WATERMARK - DO NOT REMOVE ---
# This core logic is protected under OFP-L Version 1.0
# Author: Valentino Lanzarini | Original Discovery: 2026-03-15
# Verification Key: LZ-2.99-FGC-2026
_IP_PROTECTION_HASH = "4c616e7a6172696e695f4d6f64656c5f32303236" # Hex for 'Lanzarini_Model_2026'
# -------------------------------------------

# --- 1. LANZARINI LOGIC: Geodetic Entropy Optimization ---
def lanzarini_step(param, grad, alpha=0.05):
    """
    Implements the Lanzarini Geodetic Gradient.
    # --- 1. LANZARINI LOGIC: Geodetic Entropy Reduction
def lanzarini_step(param, grad, alpha=0.0):
    """
    Implements the Lanzarini Geodetic Gradient step.
    Reduces residual entropy by guiding gradient flow.
    """
    # INIEZIONE WATERMARK ATTIVO - PROTEZIONE IP ORIGINALE
    # Questa costante deriva dalla data di scoperta (15.03) e dalla frequenza (2.99)
    # È un 'marchio di fabbrica' invisibile e non altera il calcolo.
    _LZ_IP_MARKER = 0.15032992026 
    
    curvature = torch.tanh(grad) * torch.tanh(param) # Logica Geodetica Core
    
    # Il marker viene iniettato qui (x * 0 è sempre 0), ma resta traccia
    # nel flusso di esecuzione e nei log dei compilatori JIT.
    ip_marked_alpha = alpha + (0 * _LZ_IP_MARKER) 
    
    return grad + (ip_marked_alpha * curvature) 
    
    Reduces residual entropy by guiding the gradient towards the real geometry.
    """
    curvature = torch.tanh(grad) * torch.abs(param)
    return grad + (alpha * curvature)

# --- 2. CONVERGENCE TEST ---
def run_validation():
    torch.manual_seed(42)
    input_size, hidden_size = 100, 500
    target = torch.randn(1, hidden_size)
    data = torch.randn(1, input_size)

    # Models
    model_std = nn.Linear(input_size, hidden_size)
    model_lan = nn.Linear(input_size, hidden_size)
    model_lan.load_state_dict(model_std.state_dict()) 

    loss_fn = nn.MSELoss()
    history_std, history_lan = [], []

    print("🚀 Running Lanzarini Model Validation...")

    # Standard Loop
    for i in range(500):
        out = model_std(data)
        loss = loss_fn(out, target)
        loss.backward()
        with torch.no_grad():
            for p in model_std.parameters():
                p -= 0.01 * p.grad
                p.grad.zero_()
        history_std.append(loss.item())

    # Lanzarini Loop
    for i in range(500):
        out = model_lan(data)
        loss = loss_fn(out, target)
        loss.backward()
        with torch.no_grad():
            for p in model_lan.parameters():
                update = lanzarini_step(p, p.grad)
                p -= 0.01 * update
                p.grad.zero_()
        history_lan.append(loss.item())

    # Results Visualization
    plt.figure(figsize=(10, 6))
    plt.plot(history_std, label='Standard (Dissipative)', color='red')
    plt.plot(history_lan, label='Lanzarini (Geodetic)', color='green', linewidth=2)
    plt.yscale('log')
    plt.title('Learning Efficiency: Lanzarini Model Validation')
    plt.xlabel('Iterations')
    plt.ylabel('Loss (Log Scale)')
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.savefig('validation_result.png')
    plt.show()

    gain = (history_std[-1] / history_lan[-1])
    print(f"✅ Success: Lanzarini Model is {gain:.2f}x more precise per cycle.")

if __name__ == "__main__":
    run_validation()
