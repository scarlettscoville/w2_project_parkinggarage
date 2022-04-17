#Your parking gargage class should have the following methods:

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

# Steps:
    # User takes ticket and enters Garage
        # Decrease available tickets by 1
        # Decrease available spaces by 1
    
    # User Leaves
        # Prompt for payment
        # If payment == amount owed: print "Thank you! Have a nice day."
            # Increase available tickets by 1
            # Increase available spaces by 1
        # If payment != amount owed: "Please pay XXX amount"
            # XXX amount should be Amount Due - Amount paid











class Parking_Garage():
    SPACES = 10

    def __init__(self, spaces, tickets):
        self.spaces = Parking_Garage.SPACES
        self.tickets = 0
        self.currentticket = {}

    def take_ticket():
        if self.tickets == 10:
            print("There are no spaces available in the garage.")

        else:
            print(f"Your ticket number is {self.spaces}")
            self.currentticket[self.spaces] = False
            self.spaces.pop(0)
            self.tickets += 1
        pass

    def pay_for_parking():
        pass

    def leave_garage():
        pass



class UI():
    def run_garage(self):
        while True:
            response = input("What would you like to do? Park, pay, or leave? ").lower()
            if response == 'park':
                self.Parking_Garage.take_ticket()








# Driver Code
run_garage()