from database.db_handler import insert_donor, get_all_donors
from models.donor import Donor

def add_donor(name, blood_type, contact):
    donor = Donor(name, blood_type, contact)
    insert_donor(donor)

def list_donors():
    donors = get_all_donors()
    for donor in donors:
        print(donor)
