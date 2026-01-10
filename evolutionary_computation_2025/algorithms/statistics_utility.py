import numpy as np

class StatisticsUtility:

    @staticmethod
    def get_min(values):
        return np.min(values)

    @staticmethod
    def get_average(values):
        return np.mean(values)

    @staticmethod
    def get_std(values):
        return np.std(values)
