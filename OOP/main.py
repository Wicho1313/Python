from car import Car
from account import Account
from UberX import UberX
from Driver import Driver
from User import User

if __name__ =="__main__":
    car = Car("sdas12", Account("Andres Herrera","xv3341"))

    print(vars(car))
    print(vars(car.driver))
    
    uberX = UberX("ffkhk13", "Carlos", "Chevy", "Aveo")
    print (vars(uberX))

    driver = Driver("fads", "asda", "asda", "Asdas")
    print(vars(driver))

    user = User("Luis", "fjld")
    print(vars(user))