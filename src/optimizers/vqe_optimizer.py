# 1) Use to_qubo to turn to unconstrained problem, solve using VQE class, return optimized decisions (asset weights)
from src.optimizers.optimizer import PortfolioOptimizer

class VQEOptimizer(PortfolioOptimizer):
    def __init__(self):
        super().__init__()

    def __call__(self, model, weights=None, unique_identifier=None, log_best_feasible=False):
        pass