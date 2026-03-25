# Lanzarini Model: Scientific Validation Protocol

This folder contains the official scripts to verify the **Geodetic Efficiency** of the Lanzarini Model compared to standard dissipative AI training methods.

## Objective
To demonstrate that the **Lanzarini Geodetic Gradient** ($\alpha \nabla S_{ent}$) achieves a lower error state (Loss) with fewer computational iterations, leading to a theoretical energy saving of up to **58%** in large-scale neural networks.

## How to run the test
1. Install dependencies:
   `pip install -r requirements.txt`
2. Execute the validation script:
   `python lanzarini_validation.py`

## Interpreting Results
- **Red Line (Standard):** Represents the current "Brute Force" statistical approach.
- **Green Line (Lanzarini):** Represents the Geodetic Optimization. 
- **The Gap:** The vertical distance between the lines (on a log scale) represents the reduction in computational entropy. 

## Paternity & Ethics
This validation is part of the **Lanzarini Project** (Discovery Date: March 15, 2026) and is released under the **Open for Planet (OFP-L)** License to ensure AI remains a sustainable common good.
