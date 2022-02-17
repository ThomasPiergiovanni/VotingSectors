"""
"""
from controller.client.csv_manager import CsvManager
from config.settings.settings import (
    INPUT_DIR, INPUT_FILE, INPUT_DELIMITER, INPUT_QUOTECHAR,
    INPUT_REF_DIR, REF_FILE, REF_DELIMITER, REF_QUOTECHAR
)


class VotingSectorSetter:
    """
    """
    def __init__(self):
        self.sector = []
        self.address = []
        self.csv_manager = CsvManager()
    
    def get_voting_sector(self):
        self.sector = self.csv_manager.import_data(
            INPUT_DIR, INPUT_FILE, INPUT_DELIMITER, INPUT_QUOTECHAR
        )
        self.address = self.csv_manager.import_data(
            INPUT_REF_DIR, REF_FILE, REF_DELIMITER, REF_QUOTECHAR
        )
    
    def list_checker(self, lists):
        for item in lists:
            print(item)
        

