from enum import Enum


class SmellType(Enum):
    NON_REPRESENTATIVE_STATISTICS_ESTIMATION = 1
    NON_EXPANDING_FEATURE_MAP = 2


class SmelledFile:
    def __init__(self, full_name: str, file_name: str, line_no: int, smell_type: SmellType):
        self.repo_full_name = full_name
        self.smelled_file_name = file_name
        self.smell_line_no = line_no
        self.smell_type = smell_type

    def __repr__(self):
        return f"{self.repo_full_name}, {self.smelled_file_name}, {self.smell_line_no}"

    def get_row(self):
        return [self.repo_full_name, self.smelled_file_name, self.smell_line_no]