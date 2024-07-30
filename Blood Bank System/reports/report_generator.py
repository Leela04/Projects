from database.db_handler import get_all_donors

def generate_donor_report():
    donors = get_all_donors()
    report = "Donor Report\n"
    report += "============\n"
    for donor in donors:
        report += f"ID: {donor[0]}, Name: {donor[1]}, Blood Type: {donor[2]}, Contact: {donor[3]}\n"
    return report

if __name__ == "__main__":
    print(generate_donor_report())
