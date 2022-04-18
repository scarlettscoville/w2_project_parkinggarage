#Your parking garage class should have the following methods:

#- takeTicket
#- This should decrease the amount of tickets available by 1
#- This should decrease the amount of parkingSpaces available by 1

#- payForParking
#- Display an input that waits for an amount from the user and store it in a variable
#- If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
#- This should update the "currentTicket" dictionary key "paid" to True

#-leaveGarage
#- If the ticket has been paid, display a message of "Thank You, have a nice day"
#- If the ticket has not been paid, display an input prompt for payment
#- Once paid, display message "Thank you, have a nice day!"
#- Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
#- Update tickets list to increase by 1 (meaning add to the tickets list)

#You will need a few attributes as well:
#- tickets -> list
#- parkingSpaces -> list
#- currentTicket -> dictionary

# ---------------------------------------------------
# Plan:

# Classes:
    # Parking Garage
    # UI


class Parking_Garage():

    def __init__(self):
        self.spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.current_ticket = {}

    # User takes ticket and enters Garage
        # Decrease available tickets by 1
        # Decrease available spaces by 1
    def take_ticket(self):
        if self.spaces==[]:
            print("There are no spaces available in the garage.")

        else:
            ticket = self.tickets.pop(0)
            self.spaces.pop(0)
            self.current_ticket[ticket]="unpaid"
            print(f"Your ticket number is {self.current_ticket}")
            print(f"Spaces left: {self.spaces}.")
            
            
    # Prompt for payment
        # If payment == amount owed: print "Thank you! Have a nice day."
            # Increase available tickets by 1
            # Increase available spaces by 1
    def pay_for_parking(self):
        ticket = int(input("Enter your ticket number: "))
        if self.current_ticket[ticket] == 'paid':
            print("Thank you for your payment. You have 15 minutes to leave the garage.")
            
        else:
            print("Please pay the amount due.")
            pay = input("Enter the amount you would like to pay: Enter 'paid' ")
            if pay == 'paid':
                print("Thank you for your payment! You have 15 minutes to leave the garage.")
                self.current_ticket[ticket]="paid"
                self.spaces.append(ticket)
            

    # User Leaves
        # Check if ticket is paid
        # If so, allow to leave
        # If not, prompt for payment
    def leave_garage(self):
        ticket = int(input("Enter your ticket number: "))
        if self.current_ticket[ticket] == 'paid':
            print("Thank you for parking with us! Have a great day!")
        else:
            print("Please pay the amount due before leaving the garage.")
            self.pay_for_parking()



class UI():
    def __init__(self, Parking_Garage):
        self.Parking_Garage = Parking_Garage

    def run_garage(self):
        while True:
            print("----- Welcome to the Parking Garage! -----")
            response = input("What would you like to do? Park, pay, leave, or quit? ").lower()
            
            if response.lower() == 'park':
                self.Parking_Garage.take_ticket()
            
            elif response.lower() == 'pay':
                self.Parking_Garage.pay_for_parking()
            
            elif response.lower() == 'leave':
                self.Parking_Garage.leave_garage()

            elif response.lower() == 'quit':
                break

            else:
                print("Please select an option: pay, park, or leave.")
                


# Driver Code
ui = UI(Parking_Garage())
ui.run_garage()