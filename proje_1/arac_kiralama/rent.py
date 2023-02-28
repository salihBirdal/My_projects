import datetime

#parent class
class VehicleRent():
    def __init__(self,stock):
        self.stock=stock
        self.now=0 #now parametresi bill kullanırken aktif edecez

    def displaystock(self):

        print(f"{self.stock} vehicle avaible to rent")
        return self.stock

        
    def renthourly(self,n):
        if n<=0:
            print("number should be positive")
            return None
        elif n>self.stock:
            print(f"sorry {self.stock} vehicle not avaible to rent")
            return None
        else:
            self.now=datetime.datetime.now()
            print(f"rented a {n} vehicle for hourly at {self.now.hour} hours")
            self.stock-=n

            return self.now

        
    def dailyrent(self,n):
        if n<=0:
            print("Number should be positive")
        elif n>self.stock:
            print(f"sorry {self.stock} vehicle not avaible to rent")
        else:
            self.now=datetime.datetime.now()
            print(f"rented a {n} vehicle for daily at {self.now.hour} hours")
            self.stock-=n

        
    def returnVehicle(self,request,brand):
        car_h_price=20
        car_d_price=car_h_price*8/10*24
        bike_h_price=8
        bike_d_price=bike_h_price*7/10*24

        rentalTime,rentalBasis,numofVehicle=request
        bill=0
        if brand=="CAR":
            if rentalTime and rentalBasis and numofVehicle:
                self.stock+=numofVehicle
                now=datetime.datetime.now
                rentalPeriod=now-rentalTime

                if rentalBasis==1:
                    bill=rentalPeriod.second/3600*car_h_price*numofVehicle
                
                elif rentalBasis==2:
                    bill=rentalPeriod.second/3600*24*car_d_price*numofVehicle
                
                
                print("Thank you for returning you car")
                print(f"Price: $ {bill}")
                return bill
        
        elif brand=="BİKE":
            if rentalTime and rentalBasis and numofVehicle:
                self.stock+=numofVehicle
                now=datetime.datetime.now
                rentalPeriod=now-rentalTime

                if rentalBasis==1:
                    bill==rentalPeriod.seconds/3600*bike_h_price*numofVehicle
                elif rentalBasis==2:
                    bill==rentalBasis.seconds/(3600*24)*bike_d_price*numofVehicle
                elif (4<=numofVehicle):
                    print("You have a extra 20% discount")
                    bill=bill*0.8
                print("Thank you for returning your bike")
                print(f"price: $ {bill}")
                return bill
        else:
            print("You do not rent a vehicle")



#child class
class CarRent(VehicleRent):
    global discount_rate
    discount_rate=15
    def __init__(self,stock):
        super().__init__(stock)

    def discount(self,b):
        bill=b-(b*discount_rate)/100
        return bill

class BikeRent(VehicleRent):
    def __init__(self,stock):
        super().__init__(stock)
        
class Customer():
    def __init__(self):
        self.bikes=0
        self.rentalBasis_b=0
        self.rentalTime_b=0

        self.cars=0
        self.rentalBasis_c=0
        self.rentalTime_c=0

    def requestVehicle(self,brand):
        if brand=="BİKE":
            bikes=input("How many bikes would you like to rent:")
            try:
                int(bikes)
            except ValueError:
                print("Number should be positive number")
                return -1
            if bikes<1:
                print("Number of Bikes should be greater than zero")
                return -1
            

            else:
                self.bikes=bikes
            return self.bikes
            



        elif brand=="CAR":
            car=input("How many car would you like to rent")
            try:
                int(car)
            except ValueError:
                print("Number should be positive number")
                return -1

            if car<1:
                print("Number of bikes should be greater than zero")

            else:
                self.car=car
            
            return self.car
            
        else:
            print("Something is wrong.Please try again")
        
    def returnVehicle(self,brand):
        if  brand=="bike":
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b,self.rentalBasis_b,self.bikes
            else:
                return 0,0,0
        elif brand=="car":
            if self.rentalTime_c and self.rentalBasis_c and self.car:
                return self.rentalTime_c,self.rentalBasis_c,self.car
            else:
                return 0,0,0


            
        else:
            pass

        

        

















































