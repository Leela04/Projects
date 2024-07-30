class Donor:
    def __init__(self, name, blood_type, contact):
        self.name = name
        self.blood_type = blood_type
        self.contact = contact

    def __repr__(self):
        return f"Donor({self.name}, {self.blood_type}, {self.contact})"
