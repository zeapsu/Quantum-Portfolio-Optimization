# 1) Use to_qubo to turn to unconstrained problem, solve using QAOA class, return optimized decisions (asset weights)
from src.optimizers.optimizer import PortfolioOptimizer

class QAOAOptimizer(PortfolioOptimizer):
    def __init__(self):
        super().__init__()

    def __call__(self, model, weights=None, unique_identifier=None, log_best_feasible=False):
        pass