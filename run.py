import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("employee_ratings")


def get_scores_data():
    """
    Get scores figures input from the user.
    Run a while loop to collect a valid string of data from
    the user via the terminal. The loop will repeatedly
    request data until it is valid
    """
    while True:
        print("Please enter your score ratings")
        print("Data should be three numbers seperated by commas")
        print("Accepted scores range is 0 for lowest, and 5 for highest)")
        print("Example: 0,3,5\n")

        data_str = input("Enter your data here: ")
        scores_data = data_str.split(",")

        if validate_data(scores_data):
            print("Data is valid")
            break

    return scores_data


def validate_data(values):
    """
    Use 'try/except statement to check if data is valid.
    Raise ValueError if strings cannot be converted into
    integers, or if there are not exactly 3 values.
    """
    try:
        if len(values) != 3:
            raise ValueError(
                f"Exactly 3 values required, you provided {len(values)}"
            )

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


data = get_scores_data()
