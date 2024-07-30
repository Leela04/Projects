from database.db_handler import create_tables
from ui.cli import main_menu

def main():
    # Initialize the database and create tables if they don't exist
    create_tables()
    
    # Start the main menu
    main_menu()

if __name__ == "__main__":
    main()
