# CPLEX and/or Gurobi 
from src.optimizers.optimizer import PortfolioOptimizer

class ClassicalOptimizer(PortfolioOptimizer):
    def __init__(self):
        super().__init__()
    
    def __call__(self, model, weights, unique_identifier=None, log_best_feasible=False):
        pass