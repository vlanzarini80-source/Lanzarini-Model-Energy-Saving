// ==========================================
// LP-1 CAE Engine: Real Entropy Gating (v0.4.1)
// Author: Valentino Lanzarini | 31 Marzo 2026
// Status: RTL Gold Master - Fixed Timing
// ==========================================

module lp1_cae_engine_real #(
    parameter THRESHOLD = 5 // Soglia di bit che cambiano (Entropia)
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

    // --- Calcolo dell'Entropia (Hamming Distance) ---
    // Logica combinatoria istantanea
    always @(*) begin
        diff_count = 0;
        for (i = 0; i < 32; i = i + 1) begin
            if (grad_in[i] != last_grad[i])
                diff_count = diff_count + 1;
        end
        // Se cambiano troppi bit, l'entropia è alta -> ATTIVA GATING
        entropy_high = (diff_count > THRESHOLD);
    end

    // --- Logica di Gating Data-Driven ---
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            adjusted_grad <= 32'b0;
            last_grad     <= 32'b0;
        end else begin
            last_grad <= grad_in; // Memorizza per il prossimo ciclo
            if (entropy_high) begin
                // Entropia alta: Mantieni il dato precedente (HOLD) 
                // per azzerare lo switching energetico
                adjusted_grad <= adjusted_grad; 
            end else begin
                // Entropia bassa: Passa il gradiente (con maschera LSB)
                adjusted_grad <= grad_in & 32'hFFFFFFFC;
            end
        end
    end

    // Segnale di controllo esterno
    assign gate_active = entropy_high;

endmodule

