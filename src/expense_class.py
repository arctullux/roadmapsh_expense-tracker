import json
from pathlib import Path
import chardet
import time
from colorutil import textRed, textYellow, textGreen
from datetime import date
from datetime import datetime
class Expenses:
    # =====[DATA HANDLING]=====

    targetFile = Path(__file__).resolve()
    jsonPath = targetFile.parent.parent / "assets" / "json" / "expense_list.json"
    error = False

    if jsonPath.exists():
        pass
    else:
        print(textRed(f"ERR !> Path not found. Looking for: {jsonPath}."))

    @classmethod
    def _json_helper_method(cls, permission, classMethodData):
        """
            A "helper method" that keeps code cleaner.

            Args:
                permission: "r" or "w" for read/write ("w" will overwrite whole file. Use this while reading previous file data to protect it.)

            Returns:
                The result of the operation, or none if an error occured.

        """
        try:
            with open(cls.jsonPath, permission, encoding="utf-8") as file:
                if permission == "r":
                    data = json.load(file)
                    return classMethodData(data, file)
                else: # permission == "w"
                    return classMethodData(file)
        except FileNotFoundError:
            print(textRed("ERR !> File not found."))
            return None
        except json.JSONDecodeError:
            print(textRed("ERR !> File is not valid JSON format."))
            return None
        except UnicodeDecodeError:
            print(textRed("ERR !> File is not correct encoding or data requested does not exist."))
            return None



    """
    try:
        with open(jsonPath, 'r') as file:
            expensePool = json.load(file) # JSON Data carrying expenses
            print(expensePool["00"]["name"])

    except FileNotFoundError:
        print("ERR !> File not found.")
    except json.JSONDecodeError:
        print("The file is not a valid JSON format.")
    except json.UnicodeDecodeError:
        print("The file does not contain UTF8, UTF16, or UTF32 encoded data.")"""


    # ============[Helper Methods]===============
    def checkDate(dateString):
        try:
            format = datetime.strpdate(dateString, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    # ===========================================
    def clearExpenses():
        pass
    @classmethod
    def addExpense(cls):

        # Data collection segment

        print(textGreen("Starting function."))
        # ==
        print("Enter your expense data.\n")

        name = input("Expense label(name): ")
        if name == "exit":
            return

        price = input("How much did this cost?: ")
        if price == "exit":
            return

        description = input("What is this expense for?: ")
        if description == "exit":
            return

        summary = input("Summarize your description in simpler words: ")
        if summary == "exit":
            return

        date = input("The date of this expense (mm/dd/yyyy): ")
        if date == "exit":
            return

        print(textGreen('Checkpoint 1'))

        # =========
        # Add user input data while reading original file data (contained in data variable)

        """def readFile(data, file):
            data[expenseID] = {
                "name": name,
                "price": price,
                "description": description,
                "summary": summary,
                "date": date
            }
            return data
        expensePool = cls._json_helper_method("r",readFile)"""

        try:
            with open(cls.jsonPath, "r", encoding="UTF-8") as file:
                expensePool = json.load(file)
        except FileNotFoundError:
            print(textRed("ERR !> File not found."))
            return None
        except json.JSONDecodeError:
            print(textRed("ERR !> File is not valid JSON format."))
            return None
        except UnicodeDecodeError:
            print(textRed("ERR !> File is not correct encoding or data requested does not exist."))
        else:
            print(textGreen("File loaded successfully."))

        # =========

        print(textGreen("Checkpoint 2"))
        # ==

        # Calculate new expense ID.

        expenseIDList = [int(key) for key in expensePool.keys()]
        expenseIDMax = max(expenseIDList, default=0)
        expenseID = expenseIDMax + 1
        print(f"Your new expenseID is: {expenseID}.")

        # ---------------------------------
        #
        expensePool[str(expenseID)] = {
                "name": name,
                "price": price,
                "description": description,
                "summary": summary,
                "date": date
            }

        # Write current data + new data to file.

        print(textGreen("Checkpoint 3"))
        # ==
        print(textGreen("Checkpoint 4"))
        # ==
        def writeData(file):
            json.dump(expensePool, file, indent=2)
        cls._json_helper_method("w", writeData)
        print(textGreen("Posted."))

        # ================

    def updateExpense(expenseID):
        pass
    @classmethod
    def viewAllExpenses(cls):

        # Read and print all expense data in a specified format.

        def readFile(data, file):
            return data
        expensePool = cls._json_helper_method("r", readFile)
        for expenseID, expense in expensePool.items():
            if expenseID != "00":
                print(f"""\t{expenseID}:
                        Name: {expense["name"]}
                        Price: {expense["price"]}
                        Description: {expense["description"]}
                        Summary: {expense["summary"]}
                        Date: {expense["date"]}""")




    def viewAllSummaris():
        pass
    def viewSummary(month):
        pass
    @classmethod
    def removeExpense(cls, expenseID):
        if expenseID == "cont":
            print("Continued.")
            return

        def readFile(data, file):
            return data

        expensePool = cls._json_helper_method("r", readFile)

        if expenseID in expensePool:
            choice = input(f"Are you sure you want to delete item # {expenseID}? > ")
            if choice.upper() == "Y":
                if expenseID not in expensePool:
                    print(textYellow("WAR #> Key not found."))
                    return
                else:

                    with open(cls.jsonPath, 'w') as file:
                        del expensePool[expenseID]
                        json.dump(expensePool, file, indent=2)
                print(f"{expenseID} has been deleted.")
            elif choice.upper() == "N":
                print(f"{expenseID} has NOT been deleted.")
            else:
                print(textYellow(f"{choice} is not a valid choice. Please choose 'Y' or 'N'."))

    @classmethod
    def searchExpense(cls, expenseID):
        def readFile(data, file):
            return data
        expensePool = cls._json_helper_method('r', readFile)
        if expensePool == None or expenseID == None:
            warMSG = textYellow("WAR #> Stored data does not exist or expenseID does not exist.")
            return warMSG

    @classmethod
    def debug(cls):
        def readFile(data, file):
            return data

        expensePool = cls._json_helper_method("r", readFile)



def jsonTest():
    e1 = Expenses()
    count = 0
    menu = """
            1. Add an expense
            2. Clear a specific expense
            3. Clear all expenses
            4. View all expenses
            5. Search expense using expenseID.
            6. View all summaries
            7. View specific summary
            !q to quit program.\n
            """
    print(menu)
    while True:
        if count == 5:
            print(menu)
            count = 0
        count += 1
        choice = input("Choose an option from the menu. > ")
        match choice:
            case "1": # Finished
                print("Add expense.\n")
                e1.addExpense()
                choice = None
            case "2": # Finished
                expenseID = input("Enter expense ID you want to delete. If you do not know, enter 'cont' then select option #4. > ")
                e1.removeExpense(expenseID)
                choice = None
            case "3":
                print("Clear all expenses.\n")
                choice = None
            case "4": # Finished
                print("View all expenses.\n")
                e1.viewAllExpenses()
                choice = None
            case "5":
                expenseID = input("Enter the expenseID you would like to look up. > ")
                print(e1.searchExpense(expenseID))
                choice = None
            case "6":
                print("View all summaries.\n")
                choice = None
            case "7":
                print("View a specific summary.\n")
                choice = None
            case "8":
                e1.debug()
                choice = None
            case "!q":
                print("Exit program.\n")
                choice = None
                break
            case _:
                print("Not a valid option.\n")


# Function to run ================
if __name__ == "__main__":
    jsonTest()
