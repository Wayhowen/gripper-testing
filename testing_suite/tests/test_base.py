from abc import abstractmethod


class Test:
    def __init__(self):
        pass

    @abstractmethod
    def pre_test(self):
        raise NotImplementedError

    @abstractmethod
    def perform_test(self):
        raise NotImplementedError

    @abstractmethod
    def post_test(self):
        raise NotImplementedError

    @abstractmethod
    def finish_testing(self):
        raise NotImplementedError
