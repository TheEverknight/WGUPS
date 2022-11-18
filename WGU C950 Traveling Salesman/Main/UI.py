from WGUPS import *
from Truck import *

class UI:
    # Function that runs the delivery simulation. Starts truck 1 and 2 at certain times based on the constrains of the project.
    # Truck 3 departure time is based on the complete travel time of truck 1.

    # 0(1)
    def run(self, time):
        truck2.truck_departure_time = 545
        truck1.truck_departure_time = 480
        WGU.delivery(truck1, time)
        truck3.truck_departure_time = truck1.travel
        WGU.delivery(truck2, time)
        WGU.delivery(truck3, time)


    # Allows to view the packages between at user input times.
    # 0(N)
    def PackageStatus(self,time):

        print('-------------------PRINTING PACKAGE STATUSES AT', time,'-------------------------\n')
        for i in WGU.delivered:
                i.Find(time)

    # Function to view the delivery.
    # 0(N)
    def FindAll(self):
        for i in WGU.delivered:
            print(i.package_id, i.address, i.deadline,i.city, i.zipcode, i.state, i.weight, i.status_update)
        print('\n---------------------TOTAL DISTANCE OF ', round(WGU.total_distance),'---------------------')

    # Function to view each package after a simulation.
    # 0(N)
    def FindPackage(self,option, id, time):
        for i in WGU.delivered:
            if option == '1' and i.package_id == int(id):
                print(i.address, '')
            if option == '2' and i.package_id == int(id):
                print(i.city)
            if option == '3' and i.package_id == int(id):
                print(i.zipcode)
            if option == '4' and i.package_id == int(id):
                print(i.state)
            if option == '5' and i.package_id == int(id):
                print(i.deadline)
            if option == '6' and i.package_id == int(id):
                print(i.weight)
            if option == '7' and i.package_id == int(id):
                i.Find(time)

ui = UI()