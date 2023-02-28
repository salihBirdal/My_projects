from rent import CarRent,BikeRent,Customer


bike=BikeRent(100)
car=CarRent(10)
customer=Customer()


main_menu=True
while True:
    if main_menu:
        print("""*******  Vehicle Rental Shop  *******
        
        A. )Bike Menu
        B. )CarMenu
        Q. )Exit    
        """)
    main_menu=False
    choice=input("Enter choice:")
    if choice.upper()=="A":
        print("""*****Bike Menu*****
        1.Display avaible bikes
        2.Request a bike on hourly basis $ 5
        3.Request a bike on daily basis $ 50
        4. return a bike
        5.Main Menu 
        6.Exit   
        
        """)
        choice_1=input("Enter choice:")
        try:
            choice_1=int(choice_1)
        except ValueError:
            print("Please enter a integer value")
            continue
        if choice_1==1:
            bike.displaystock()
            choice="A"
        elif choice_1==2:
           customer.rentalTime_b= bike.renthourly(customer.requestVehicle("bike"))
           customer.rentalBasis_b=1
           main_menu=True
           print("-------------")
        elif choice_1==3:
            customer.rentalTime_b=bike.renthourly(customer.requestVehicle("bike"))
            customer.rentalBasis_b=2
            main_menu=True
            print("-------------")
        elif choice_1==4:
            customer.bill=bike.returnVehicle(customer.returnVehicle("bike"),"bike")
            customer.rentalBasis_b,customer.rentalTime_b,customer.bikes=0
            main_menu=True
        elif choice_1==5:
            main_menu=True
        elif choice_1==6:
            break
        else:
            print("İnvalid İnput.Please try again")
            main_menu=True



    elif choice.upper()=="B":
        print("""*****Car Menu*****
        1.Display avaible car
        2.Request a car on hourly basis $ 10
        3.Request a car on daily basis $ 192
        4. return a car
        5.Main Menu 
        6.Exit   
        
        """)
        choice_1=input("Enter choice:")
        try:
            choice_1=int(choice_1)
        except ValueError:
            print("Please enter a integer value")
            continue
        
        if choice_1==1:
            car.displaystock()
            choice="B"
        elif choice_1==2:
           customer.rentalTime_c= car.renthourly(customer.requestVehicle("car"))
           customer.rentalBasis_c=1
           main_menu=True
           print("-------------")
        elif choice_1==3:
            customer.bill=customer.rentalTime_c=car.renthourly(customer.requestVehicle("car"))
            customer.rentalBasis_c=2
            main_menu=True
            print("-------------")
        elif choice_1==4:
            car.returnVehicle(customer.returnVehicle("car"),"car")
            customer.rentalBasis_c,customer.rentalTime_c,customer.cars=0,0,0
            main_menu=True
        elif choice_1==5:
            main_menu=True
        elif choice_1==6:
            break
        else:
            print("İnvalid İnput.Please try again")
            main_menu=True

    elif choice.upper()=="Q":
        break
    else:
        print("Invalid input.Please enter a-b-q")
    print("Thank you for using a vehicle rental shop")







