
def create_student_file():
    with open("student_details.txt", "w") as f:
        f.write("Student Name, Age, GPA\n")
        f.write("John Doe    , 20 , 3.8\n")
        f.write("Jane Doe    , 19 , 3.9\n")

if __name__ == "__main__":
    create_student_file()
    



while(True):
    itemname = str(input("Enter the item Name: "))
    itemid = int(input("Enter the item id: "))
    itemQty = int(input("Enter num of items avalible: "))
    itemprice = float(input("Enter the price of the items: "))
    nextitem = input("Do you want to enter new record: Y/N")
    if(nextitem == "Y" or nextitem == "y"):
        continue
    else:
      break


    