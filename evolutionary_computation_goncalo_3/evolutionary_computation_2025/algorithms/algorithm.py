from abc import ABC, abstractmethod


class Algorithm(ABC):
    def __init__(self, isDebug=False):
        self.isDebug = isDebug

    @abstractmethod
    def execute(self, problem, maxFes):
        pass
