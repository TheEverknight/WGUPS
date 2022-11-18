

from Package import Package
from ReadFiles import *
# Truck class


class Truck:
    def __init__(self, truck_id):
        self.package_list = HashTable()
        self.truck_id = truck_id
        self.truck_departure_time = 0
        self.travel = 0
        self.total_cost = 0

    # Function to retrieve the package for each truck. Set the package departure time based on the departure time of
    # the truck who delivers the package.

    # 0(N^2)
    def GetPackage(self, id):
        with open(PackageData) as package_file:
            package_file_read = csv.reader(package_file, delimiter=',')
            for row in package_file_read:
                package = Package(int(row[0]),row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                if id == package.package_id:
                    self.package_list.put(package)


            for i in self.package_list.table:
                for j in i:
                    if self.truck_id == 1:
                        j.package_departure_time = self.truck_departure_time
                    elif self.truck_id == 2:
                        j.package_departure_time = self.truck_departure_time
                    elif self.truck_id == 3:
                        j.package_departure_time = self.truck_departure_time

            return self.package_list

    # set the travel time for the truck
    def SetTime(self, distance):
        self.travel = round(3.33 * distance) + self.truck_departure_time



truck1 = Truck(1)

truck2 = Truck(2)

truck3 = Truck(3)