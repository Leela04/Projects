import sys
from services.donor_service import add_donor, list_donors
from reports.report_generator import generate_donor_report

def main_menu():
    while True:
        print("Blood Bank Management System")
        print("1. Add Donor")
        print("2. View Donors")
        print("3. Generate Donor Report")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter donor name: ")
            blood_type = input("Enter blood type: ")
            contact = input("Enter contact: ")
            add_donor(name, blood_type, contact)
        elif choice == '2':
            list_donors()
        elif choice == '3':
            report = generate_donor_report()
            print(report)
        elif choice == '4':
            sys.exit()
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main_menu()
