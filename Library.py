import os
import datetime


category = ['physics','maths','computers','science','english']
#To mentain library data
library_data = {}
#TO mantain membership data 
members_data = {}
#To mentain borrowers data 
borrow_list = []
#Names Validation 
def validate(temp_str,user_data):
    if(user_data == ''):
        os.system('cls')
        print("%s is Mandatory:"%temp_str)
        return input()
    elif(user_data.isnumeric()):
        print("%s Should be a name:"%temp_str)
        return input()
    else:
        return user_data
    
#Date Validation 
def date_validation(user_data):
    date_fields = user_data.split('/')
    if(int(date_fields[0])>31):
        return input("Enter correct date format:")
    elif(int(date_fields[1])>12):
        return input("Enter correct date format:")
    else:
        return user_data
#New and Old Book Registration process 
def book_register():
        while(True):
            user_choice = int(input("To Enter Book Details press 1 or press 9 to go main menu: "))
            if(user_choice == 1):            
                book_data = []
                book_name = input("Enter Book Name: ")
                book_name = validate('Book Name',book_name)

                publisher_name = input("Enter Publisher Name: ")
                publisher_name = validate('Publisher Name',publisher_name)
                book_data.append(publisher_name)

                publication_date = input("Enter Publication Date(dd/mm/yyyy):")
                publication_date = date_validation(publication_date)
                book_data.append(publication_date)
                
                edition = input("Enter Edition: ")
                edition = validate('Edition',edition)
                book_data.append(edition)
                
                category_name = input("Enter Category name:")
                if(category_name not in category):
                    category_name = input("Enter Correct Category name:")
                book_data.append(category_name)
                
                try:
                    purchase_value =float(input("Enter Purchase Value: "))
                except Exception as inst:
                    purchase_value = float(input("Value should be a number and greater than 0:"))
                book_data.append(purchase_value)
                
                rack_row_number = input("Enter Rack-Row number(####-##):")
                book_data.append(rack_row_number)    
                
                snapshot = input("Enter snapshot:")
                snapshot = validate('snapshot',snapshot)
                book_data.append(snapshot)
                
                objected = input("Enter Objected(yes or no): ").lower()
                if(objected not in ['yes','no']):
                    objected = input("Enter Objected(yes or no): ")
                book_data.append(objected)
                library_data[book_name] = book_data
                #print(library_data)
            elif(user_choice == 9):
                main_menu()
            else:
                choice= int(input("Enter correct choice:"))
#This method for membership 
def membership():
    while(True):
        
        print("\t1.New Membershhip\n\t2.Cancel Membership\n\t9.Go to Main Menu")
        membership_choice = int(input("Enter your choice: "))
        if(membership_choice == 1):
            member_data = []
            try:
                membership_id = int(input("Enter membership ID: "))
            except Exception as inst:
                membership_id = int(input("Enter membership ID(Numbers only): "))


            member_name = input("Enter member name: ")
            member_name = validate("MemberName",member_name)
            member_data.append(member_name)

            date_birth = input("Enter date of birth(dd/mm/yyyy): ")
            date_birth = date_validation(date_birth)
            member_data.append(date_birth)

            address = input("Enter address: ")
            address = validate('Address',address)
            member_data.append(address)

            city = input("Enter city name: ")
            city = validate("City Name",city)
            member_data.append(city)

            active_status = 'active'
            member_data.append(active_status)

            members_data[membership_id] = member_data
            print(members_data)
        elif(membership_choice == 2):
            print("Conformation to cancel(Enter Y to cancel):")
            cancel = input().lower()
            if(cancel =='y'):
                mem_id = int(input("Enter Membership ID:"))
                members_data[mem_id][4] = 'Cancelled'
                print("Member Details:\nmembership ID:",mem_id,"\nMemberName:%s\nDate of Birth: %s\nAddress; %s\n City: %s \nActive Status; %s"%(members_data[mem_id][0],members_data[mem_id][1],members_data[mem_id][2],members_data[mem_id][3],members_data[mem_id][4]))
        elif(membership_choice == 9):
            main_menu()
        else:
            membership_choice = int(input("Enter correct choice: "))

            
borrow_books_list = {}
# To mentain number of books borrowed
#Borrowers Module
books_list = []
def borrow_books():
    flag_id = False
    flag_book = False
    while(True):
        if(flag_id == False):
            mem_id = int(input("Enter membership ID: "))
            if(mem_id not in members_data.keys()):
                print("Invalid membership id")
            elif(members_data[mem_id][4] == 'Cancelled'):
                print("Your Membership is cancelled")
            else:
                flag_id = True
        if(flag_book == False):
            book_name = input("Enter Book Name: ")
            if(book_name in borrow_list):
                print("Book is already Borrowed")
            elif(library_data[book_name][7] == 'yes'):
                print("Book is objected")
            else:
                flag_book = True
        if(flag_id and flag_book):
            break
        userinp = int(input("Press 9 to Go main menu"))
        if(userinp == 9):
            main_menu()
    tday_date = datetime.date.today()
    next_due_date= tday_date + datetime.timedelta(days=15)
    borrow_books_list[mem_id] = {}
    borrow_books_list[mem_id][book_name] = [tday_date,next_due_date]
    books_list.append(book_name)
    print("Book is Successfully Borrowed")
    print(borrow_books_list)    

    
#Books Return History    
return_history = {}        
def return_books():
    flag_book = True
    flag_id = True
    while(flag_book):
        book_name = input("Enter Book Name: ")
        if(book_name not in books_list):
            print("Wrong book details")
            flag_book = True
        else:
            flag_book = False
    while(flag_id):
        mem_id = int(input("Enter membership ID(Press 9 to go main menu): "))
        if(mem_id not in members_data.keys()):
            print("Invalid membership ID")
            flag_id = True
        elif(mem_id == 9):
            main_menu()
        else:
            flag_id = False
    
    print("Book Details: \n")
    print("Book Name:",book_name,"\nIssue Date: %s\n Due Date %s"%(borrow_books_list[mem_id][book_name][0],borrow_books_list[mem_id][book_name][1]))
    date_of_issue = borrow_books_list[mem_id][book_name][0]
    due_date = borrow_books_list[mem_id][book_name][1]
    if(not due_date < datetime.date.today()):
        days = int(str(datetime.date.today() - due_date).split()[0])
        late_fee = days * 1
    loss_penalty = int(input("Enter Loss Penalty fee: "))
    
    spoiled_penalty = int(input("Enter Spoiled Penalty fee: "))
    
    total_fee = late_fee + loss_penalty + spoiled_penalty
    print("Total fee: ",total_fee)
    
    return_history[book_name] = [mem_id,date_of_issue,due_date,late_fee,loss_penalty,spoiled_penalty,total_fee]
    user_input_return = int(input("Enter 1 to more entries press 9 to main menu"))
    if(user_input_return == 1):
        return_books()
    if(user_input_return == 9):
        main_menu()
        
        
#Requisition of Books Module        
requisition_books = {}    
def requisition():
    counter = 0
    book_name = input("Enter Book Name: ")
    if(book_name not in books_list):
        mem_id = int(input("Enter membership ID: "))
        requisition_books[1] = [book_name,mem_id,datetime.date.today()]
    elif(book_name in library_data.keys()):
        print("Issue the book from Menu 3 ")
            

#Book Enquiry


            
            
#main menu 
def main_menu():
    print("******MENU******")
    print("1.New or Old Books Entry\n2.Memberships\n3.Borrow Books \n4.Return of Book\n5.Requisition of Books\n6.Book Enquiry\n7.Borrowers list\n8.Total Money Collected\n9.Objected Books\n10.Total Library")
    user_menu_input = int(input("Enter Your option: "))
    if(user_menu_input == 1):
        book_register()
    elif(user_menu_input ==2):
        membership()
    elif(user_menu_input == 3):
        borrow_books()
    elif(user_menu_input == 4):
        return_books()
    elif(user_menu_input == 5):
        requisition()
    #elif(user_menu_input == 6):
        
main_menu()
    
    
    
    