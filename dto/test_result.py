from typing import List


class TestResult:
    def __init__(self, test_name, runs_data: List[dict]):
        self.test_name = test_name

        self.runs_data = runs_data

    @property
    def column_names(self):
        return list(self.runs_data[0].keys())

    def run_values(self, run: int):
        return list(self.runs_data[run].values())
