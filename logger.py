import logging

# Configure logging
logging.basicConfig(
    filename="expense_tracker.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)

def log_warning(message):
    logging.warning(message)

def view_logs():
    try:
        with open("expense_tracker.log", "r") as log_file:
            print("\n--- Log Viewer ---")
            for line in log_file:
                print(line.strip())
    except FileNotFoundError:
        print("No logs found yet.")
