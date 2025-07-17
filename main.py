class Car:
    def __init__(self,car_id,make,model,year):
        self.care_id=car_id
        self.make=make
        self.model=model
        self.year=year
        self.available=True
    def rent(self):
        if self.available:
            self.available=False
            return True
        return False
    def return_car(self):
        self.available=True
class Customer:
    def __init__(self,customer_id,name):
        self.customer_id=customer_id
        self.name=name
        self.rented_cars=[]
    def rent_car(self,car):
        if car.rent():
            self.rented_cars.append(car)
            return True
        return False
    def return_car(self,car):
        if car in self.rented_cars:
            car.return_car()
            self.rented_cars.remove(car)
            return True
        return False
class Rental:
    def __init__(self,rental_id,customer,car,rental_fee):
        self.rental_id=rental_id
        self.customer=customer
        self.car=car
        self.rental_fee=rental_fee
#initialize cars
cars=[
    Car("Coo1","Toyota","Innova",2022),
    Car("Coo2","Honda","Accord",2022),
    Car("Coo3","Maruti","swift",2022),
    Car("Coo4","Mahindra","Roxx",2024),
    Car("Coo5","Hyundai","Creta",2020)
]
#initialize customer
customers=[
    Customer("CU001","Adarsh Wahewal"),
    Customer("CU002","Minal Lanjhewar"),
    Customer("CU003","Nikhil Tadayya"),
    Customer("CU004","Pratham Shambharkar"),
    Customer("CU005","Sonali,Warghat")
]
#rental transaction
customers[0].rent_car(cars[0])
customers[1].rent_car(cars[1])
customers[2].rent_car(cars[2])
customers[3].rent_car(cars[3])
customers[4].rent_car(cars[4])
#display rented cars
for customer in customers:
    rented_cars=[car.model for car in customer.rented_cars]
    print(f"{customer.name}'s Rented Cars: {rented_cars}")
#returning cars
customers[0].return_car(cars[0])
customers[2].return_car(cars[2])
customers[4].return_car(cars[4])

#display updated rental cars
for customer in customers:
    rented_cars=[car.make for car in customer.rented_cars]
    print(f"{customer.name}'s Updated Rented Cars:{rented_cars}")

#create rentals
rentals=[
    Rental("R001",customers[0],cars[0],5000.0),
     Rental("R002",customers[1],cars[1],4500.0),
      Rental("R003",customers[2],cars[2],3500.0),
       Rental("R004",customers[3],cars[3],6000.0),
        Rental("R005",customers[4],cars[4],8500.0)
]
#display rental information
for rental in rentals:
    print(f"Rental ID:{rental.rental_id},Customer:{rental.customer.name},Car:{rental.car.model},Rental fee: INR {rental.rental_fee}")