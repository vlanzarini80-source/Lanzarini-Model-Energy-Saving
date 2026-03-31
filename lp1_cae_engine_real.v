// ==========================================
// LP-1 CAE Engine: Real Entropy Gating (v0.4)
// Author: Valentino Lanzarini | 31 Marzo 2026
// License: Open for Planet (OFP-L) v1.0
// Logic: Real-Time Hamming Distance Entropy Analysis
// ==========================================

module lp1_cae_engine_real #(
    parameter THRESHOLD = 5 // Soglia attivazione gating (Bit-Toggle)
)(
    input  wire        clk,
    input  wire        rst_n,
    input  wire [31:0] grad_in,
    output reg  [31:0] adjusted_grad,
    output wire        gate_active
);

    reg [31:0] last_grad;
    integer diff_count;
    integer i;
    reg entropy_high;

    // --- Analisi Entropia (Distanza di Hamming) ---
    always @(*) begin
        diff_count = 0;
        for (i = 0; i < 32; i = i + 1) begin
            if (grad_in[i] != last_grad[i])
                diff_count = diff_count + 1;
        end
        // Se la variazione bit-to-bit supera la soglia -> Entropia Alta
        entropy_high = (diff_count > THRESHOLD);
    end

    // --- Gating Intelligente (Data-Hold Mode) ---
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            adjusted_grad <= 32'b0;
            last_grad     <= 32'b0;
        end else begin
            last_grad <= grad_in; // Memorizza lo stato precedente
            if (entropy_high) begin
                // Stato di HOLD: Nessuna commutazione per risparmio energetico
                adjusted_grad <= adjusted_grad; 
            end else begin
                // Stato ATTIVO: Passa il gradiente con maschera LSB
                adjusted_grad <= grad_in & 32'hFFFFFFFC;
            end
        end
    end

    assign gate_active = entropy_high;

endmodule
