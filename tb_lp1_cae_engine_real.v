==========================================
// Testbench: Validazione Dinamica LP-1 (v0.4)
// Genera log di confronto In/Out/Gating per prova tecnica
// ==========================================
`timescale 1ns/1ps

module tb_lp1_cae_engine_real;
    reg clk;
    reg rst_n;
    reg [31:0] grad_in;
    wire [31:0] adjusted_grad;
    wire gate_active;

    // Istanza Modulo con Soglia 5
    lp1_cae_engine_real #(.THRESHOLD(5)) uut (
        .clk(clk), .rst_n(rst_n), .grad_in(grad_in),
        .adjusted_grad(adjusted_grad), .gate_active(gate_active)
    );

    // Clock 100MHz
    initial clk = 0;
    always #5 clk = ~clk;

    // Dataset di Test
    reg [31:0] dataset [0:5];
    initial begin
        dataset[0] = 32'h00000000;
        dataset[1] = 32'h00000001; // Stabile
        dataset[2] = 32'h00000003; // Stabile
        dataset[3] = 32'h00000FFF; // RUMORE (Cambio > 5 bit) -> GATING ON
        dataset[4] = 32'hFFFFFFFF; // RUMORE (Cambio > 5 bit) -> GATING ON
        dataset[5] = 32'hFFFFFFF0; // Ritorno alla stabilità -> GATING OFF
    end

    integer i;
    initial begin
        $display("--- START VALIDATION LP-1 v0.4 ---");
        rst_n = 0; #20 rst_n = 1;
        for (i = 0; i < 6; i = i + 1) begin
            grad_in = dataset[i];
            #10 $display("Time: %t | In: %h | Out: %h | Gating: %b", $time, grad_in, adjusted_grad, gate_active);
        end
        $display("--- END VALIDATION ---");
        $finish;
    end
endmodule
