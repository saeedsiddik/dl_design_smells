from smelled_file import SmelledFile, SmellType


class NonExpandingFeatureMapSmelledFile(SmelledFile):
    def __init__(self, full_name: str, file_name: str, line_no: int, previous_line_value: int):
        super(NonExpandingFeatureMapSmelledFile, self).__init__(full_name, file_name, line_no, SmellType.NON_EXPANDING_FEATURE_MAP)
        self.previous_filters_value = previous_line_value
