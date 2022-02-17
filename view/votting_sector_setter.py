"""
"""
from controller.client.csv_manager import CsvManager
from config.settings.settings import (
    INPUT_DIR, INPUT_FILE, INPUT_DELIMITER, INPUT_QUOTECHAR,
    INPUT_REF_DIR, REF_FILE, REF_DELIMITER, REF_QUOTECHAR,
    OUTPUT_DIR, OUTPUT_NAME_MATCHER
)


class VotingSectorSetter:
    """
    """
    def __init__(self):
        self.sector = []
        self.address = []
        self.initial_matcher = []
        self.csv_manager = CsvManager()
    
    def get_voting_sector(self):
        self.sector = self.csv_manager.import_data(
            INPUT_DIR, INPUT_FILE, INPUT_DELIMITER, INPUT_QUOTECHAR
        )
        self.address = self.csv_manager.import_data(
            INPUT_REF_DIR, REF_FILE, REF_DELIMITER, REF_QUOTECHAR
        )
        self.initial_name_matcher()

    def initial_name_matcher(self):
        address_list = []
        for address in self.address:
            address_list.append(address[15])
        myset = set(address_list)
        address_list_gr = []
        for item in myset:
           address_list_gr.append(item)

        for sector in self.sector:
            if sector[1] in address_list_gr:
                item = [sector[0], sector[1], sector[1], True]
                self.initial_matcher.append(item)
            else:
                item = [sector[0], sector[1], '', False]
                self.initial_matcher.append(item)
        self.csv_manager.export_data(
            OUTPUT_DIR, OUTPUT_NAME_MATCHER, self.initial_matcher
        )

    def list_checker(self, lists):
        for item in lists:
            print(item)
        

