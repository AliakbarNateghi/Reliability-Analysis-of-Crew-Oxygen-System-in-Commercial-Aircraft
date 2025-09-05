# Sensitivity analysis for Upgrade A and B costs
import numpy as np

deltaP_A, deltaP_B = 0.131846, 0.019887
cost_A, cost_B = 80000, 30000

def utility(deltaP, cost):
    return (deltaP * 1e6) / (cost + 50000)

# vary costs by ±20%
for cA in [0.8*cost_A, cost_A, 1.2*cost_A]:
    for cB in [0.8*cost_B, cost_B, 1.2*cost_B]:
        print(f"A cost {cA}, U_A={utility(deltaP_A,cA):.3f} | "
              f"B cost {cB}, U_B={utility(deltaP_B,cB):.3f}")
