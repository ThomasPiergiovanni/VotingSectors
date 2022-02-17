from view.votting_sector_setter import VotingSectorSetter 


if __name__ == "__main__":
    votting_sector_setter = VotingSectorSetter()
    votting_sector_setter.get_voting_sector()
    votting_sector_setter.list_checker(votting_sector_setter.sector)
    votting_sector_setter.list_checker(votting_sector_setter.address)