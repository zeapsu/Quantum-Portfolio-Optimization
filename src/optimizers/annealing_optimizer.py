# Annealing
from src.optimizers.optimizer import PortfolioOptimizer

class AnnealingOptimizer(PortfolioOptimizer):
    def __init__(self):
        super().__init__()
        
    def __call__(self, model, weights=None, unique_identifier=None, log_best_feasible=False):
        pass