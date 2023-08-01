
# The Function ---Import Libery Data Time.
def get_today_date():
  import datetime  #https://www.w3schools.com/python/python_datetime.asp
  return datetime.date.today().strftime(
      '%Y%m%d'
  )  #https://www.programiz.com/python-programming/datetime/strftime


#Write Or Save in The File All Data About Tickets.
def save_data(tickets):
  with open(
      "tickets.txt", "w"
  ) as file:  #Open the File,Take Two Parameter Name Of File and Write inside that.
    for ticket in tickets:  #Loop all List .
      file.write(",".join(ticket) + "\n")  #Write In The File.


#Read Data From File *tickets.txt* and convert this file to List in List.
def read_file():
  tickets = []  # Define a list is Empty.
  file = open(
      "tickets.txt", "r"
  )  #Open File.----https://www.w3schools.com/python/python_file_open.asp
  data = file.read()  #Data into File.
  list_one = data.split("\n")  #Split use|n.
  for line in list_one:
    if line:
      ticket_data = line.split(",")
      tickets.append(ticket_data)  #Add To List.
  return tickets


#display the main menu for admin.
def admin_menu():
  print("Admin Menu Options:")
  print("1. Display Statistics")
  print("2. Book a Ticket")
  print("3. Display all Tickets")
  print("4. Change Ticketâ€™s Priority")
  print("5. Disable Ticket")
  print("6. Run Events")
  print("7. Exit")


#display the main menu for normal.
def user_menu():
  print("User Menu Options:")
  print("1. Book a Ticket")
  print("2. Exit")


#find the event ID with the highest number of tickets.
def highest_number_of_tickets(tickets):
  event_ids = []
  for line in tickets:
    if line:
      event_id = str(line).split(",")[1]
      event_ids.append(event_id)

  highest_event_id = max(event_ids)
  print("The highest event ID is: ", highest_event_id)


# Add a new ticket.
def book_ticket(tickets):
  ticket_id = 'tick' + str(len(tickets) + 101)
  event_id = input("Please Enter the event ID: ")
  username = input("Please Enter your username: ")
  event_date = input("Please Enter the event date (YYYYMMDD): ")
  priority = input("Please Enter the ticket priority: ")
  tickets.append([ticket_id, event_id, username, event_date, priority])
  print("Ticket is successfully!")


#display all tickets.
def display_all_tickets(tickets):
  today_date = get_today_date()
  today_tickets = []
  for ticket in tickets:
    if ticket[3] >= today_date:
      today_tickets.append(ticket)

  sorted_tickets = sorted(today_tickets, key=lambda x: (x[3], x[1]))
  for ticket in sorted_tickets:
    print("Ticket ID:", ticket[0])
    print("Event ID:", ticket[1])
    print("Username:", ticket[2])
    print("Event Date:", ticket[3])
    print("Priority:", ticket[4])
    print()


#change the ticket's priority
def change_priority(tickets):
  ticket_id = input("Please Enter the ticket ID: ")
  priority = input("Please Enter the new priority: ")
  for ticket in tickets:
    if ticket[0] == ticket_id:
      ticket[4] = priority
      print("Ticket priority is Change.")
      break
  else:
    print("Ticket not found.")


# Remove or Disable a ticket From File.
def disable_ticket(tickets):
  ticket_id = input("Please Enter the ticket ID: ")
  for ticket in tickets:
    if ticket[0] == ticket_id:
      tickets.remove(ticket)  #Remove From List.
      print("Ticket disabled and removed from the system.")
      break
  else:
    print("Ticket not found.")


#remove from the list and File.
def run_events(tickets):
  for ticket in tickets:
    print("Running event with ticket ID:", ticket[0])
    tickets.remove(ticket)


tickets = read_file(
)  # Call the Function read_file to return the tickets ----> List
print(
    "Welcome To Our Project:Corrupted Ticketing System.")  #Print this Message.
user_type = input(
    "Please Select Type Of User,Admin or Normal User!(admin or normal) : "
).lower()
if user_type == 'admin':  # Check the type if Admin or Normal User.
  attempts = 0
  while attempts < 5:  #admin Attempts only 5 Time.
    username = input("Username: ")  #Define Uasename Input.
    password = input("Password: ")  #Define Password Input.
    if username == "admin" and password == "admin123123":  #Chech if Username Equal *admin* and Password Equal *admin123123*.
      while True:  #Use While Loop TO Repeate Admin_Choice---Enter Value.
        admin_menu()  #Call Function To Display admin menu.
        admin_choice = input("Enter your choice (1 TO 7): ")
        if admin_choice == '1':  #If Admin Enter a number 1,Go to Call The Function To Display Higher number of tickets.
          highest_number_of_tickets(tickets)
          print(tickets)
          continue
        elif admin_choice == '2':
          book_ticket(tickets)
          continue
        elif admin_choice == '3':
          display_all_tickets(tickets)
        elif admin_choice == '4':
          change_priority(tickets)
        elif admin_choice == '5':
          disable_ticket(tickets)
        elif admin_choice == '6':
          run_events(tickets)
        elif admin_choice == '7':
          print("Exiting the program.")
          save_data(tickets)  # Call the Function To Save Data Into File.
          break
        else:
          print(
              "Try again."
          )  #In This Case The Admin If Enter Other Value From 1 To 7,Display This Message.

    else:
      print("Username Or Password Is Incorrect,Please Try again, have only",
            4 - attempts, "Time.")
      attempts += 1  #Increase attemtpts if Password and Username is Incorrect.

elif user_type == 'normal':  #If Select Normal User Complet the code.
  while True:
    user_menu()  #Call The Function To Display Menu Options.
    user_choice = input("Enter your choice (1 TO 2): ")
    if user_choice == '1':  #If The User  Enter 1,Call The Function To Add a new Tickets.
      book_ticket(tickets)
    elif user_choice == '2':  #If The User Enter 2, Call The Function To Save Any New Tickets.
      print("All The New Tickets Save.")
      save_data(tickets)  #Call The Function To Save All Data into the File.
      break  #Break The Loop.

    else:
      print(
          "Invalid choice. Please try again."
      )  #In This Case Print *Invalid* If The User Enter Other Normal User.

else:
  print("Invalid user type. Please enter 'admin' or 'normal'.")  #Print *Invalid* If Enter Other Normal User Or Admin.
