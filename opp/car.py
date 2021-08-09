from vehicle import Vehicle

class Car(Vehicle): #() inheritance

    def brag(self):
        print('Look')

car1 = Car()
car1.drive()

#Car.top_speed = 200
car1.add_warning('Nothing')
#car1.__warnings.append([])
#print(car1.__dict__)
print(car1)

#Car.top_speed = 200

car2 = Car(200)
car2.drive()
print(car2.get_warnings())

car3 = Car(250)
car3.drive()
print(car3.get_warnings())