class Cars:
    def __init__(self,stock):
        self.stock=stock

    def display_cars(self):
        print("Total Cars Avalable: ",self.stock)

    def CarForRent(self,q):

        if(q<=0):
            print("Please Enter Positive Number")
        elif(q>self.stock):
            print("Please Enter Number lesser then stock avalable")
        else:
            print("Total price:",q, "*100=",q*100)
            print("Total Avalale Cars now:",self.stock-q)


while True:
    obj=Cars(100)

    uc=int(input('''
1 Display total Stack Avalable
2 Rent a car
3 Exit 
    '''))
    if uc==1:
        obj.display_cars()
    elif uc==2:
        n=int(input("Enter The Qty no:"))
        obj.CarForRent(n)
    else:
        break