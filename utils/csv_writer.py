import csv
import os
import time
from typing import List

from dto.test_result import TestResult


class CSVWriter:
    def __init__(self):
        self._results_directory = "./testing_suite/results"
        self._testing_time = time.time()
        self._test_folder_name = f"{self._results_directory}/{self._testing_time}"

    def save_test_results(self, test_results: List[TestResult]):
        if not os.path.exists(self._test_folder_name):
            os.mkdir(self._test_folder_name)

        for test_result in test_results:
            with open(f"{self._test_folder_name}/{test_result.test_name}") as file:
                writer = csv.writer(file)
                writer.writerow(test_result.column_names)
                for run_result in test_result.runs_data:
                    writer.writerow(list(run_result.values()))
