# Base Optimizer (we could substitute explicit timing for approximate hybrid benchmarking)
from abc import ABC, abstractmethod
import numpy as np 


class PortfolioOptimizer(ABC):
    """
    Abstract class of optimizer component
    Must overwrite and match the call function signature
    """

    def __init__(self):
        self.name = self.__class__.__name__

    @abstractmethod
    def __call__(
        self,
        model,
        weights,
        unique_identifier=None,
        log_best_feasible=False,
    ):
        """
        Example signature and return overwriting methods needs to follow
        :param model: docplex model
        :param weights: docplex variable
        :param unique_identifier: hex id of the optimization
        :param log_best_feasible: log best feasible solutions
        :return:
        """
        optimal_weights = np.zeros(10)
        execution_time = 1
        processing_time = 1
        return optimal_weights, execution_time, processing_time

