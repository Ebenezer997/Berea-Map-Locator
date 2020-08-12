#Berea Locator Map : Find tourist sites  in Berea City

class Map:
    # Anglin_Falls = (36.963390, -84.795200)             # coordinates of prominent location in Berea
    # West_Pinnacle = (43.718070, -109.982070)
    # Boorne_Tavern_Hotel = (38.968500, -92.419630)
    # Owsley_fork = (32.816898, -114.838097)

    def __init__(self, latitude = "", longitude = ""):
        self.latitude = latitude
        self.longitude = longitude
        self.Anglin_Falls = (36.963390, -84.795200)         # coordinates of prominent location in Berea
        self.West_Pinnacle = (43.718070, -109.982070)
        self.Boorne_Tavern_Hotel = (38.968500, -92.419630)
        self.Owsley_fork = (32.816898, -114.838097)

    def user_input(self):                                       # Getting the latitude and longitude from user
        self.latitude = float(input("Insert your latitude: "))
        self.longitude = float(input("Insert your longitude: "))

    def calculate(self):
        from math import sin, cos, atan2, radians, sqrt

        # changing from degree to radians
        Anglin_Falls = (radians(38.921669), radians(-77.021361))
        self.latitude = radians(self.latitude)
        self.longitude = radians(self.longitude)
        clat = Anglin_Falls[0] - self.latitude
        clong = Anglin_Falls[1] - self.longitude

        # using the heversine formula
        #Calculating  distance from Anglin Falls
        a = sin(clat / 2) ** 2 + cos(Anglin_Falls[0]) * cos(self.latitude) * sin(clong / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        self.d = round(3958.8 * c, 1)
        r = (self.d + 1, self.d + 2)



        # Calculating distance from Owsley Fork
        # changing from degree to radians
        Owsley_fork = (radians(32.816898), radians(-114.838097))
        self.latitude = radians(self.latitude)
        self.longitude = radians(self.longitude)
        clat = Owsley_fork[0] - self.latitude
        clong = Owsley_fork[1] - self.longitude

        a = sin(clat / 2) ** 2 + cos(Owsley_fork[0]) * cos(self.latitude) * sin(clong / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        self.d1 = round(3958.8 * c, 1)
        r = (self.d1 + 1, self.d1 + 2)


        # calculating distance from Boorne Tavern Hotel
        Boorne_Tavern_Hotel = (radians(38.968500), radians(-92.419630))
        latitude = radians(self.latitude)
        longitude = radians(self.longitude)
        clat = Boorne_Tavern_Hotel[0] - self.latitude
        clong = Boorne_Tavern_Hotel[1] - self.longitude

        a = sin(clat / 2) ** 2 + cos(Boorne_Tavern_Hotel[0]) * cos(self.latitude) * sin(clong / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        self.d2 = round(3958.8 * c, 1)
        r = (self.d2 + 1, self.d2 + 2)


        # Calculating distance from West Pinnacle
        West_Pinnacle = (radians(43.718070), radians(-109.982070))
        self.latitude = radians(self.latitude)
        self.longitude = radians(self.longitude)
        clat = West_Pinnacle[0] - self.latitude
        clong = West_Pinnacle[1] - self.longitude

        a = sin(clat / 2) ** 2 + cos(West_Pinnacle[0]) * cos(self.latitude) * sin(clong / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        self.d3 = round(3958.8 * c, 1)
        r = (self.d3 + 1, self.d3 + 2)

    # Calculating the closest tourist site relative to user's location
    def Compare(self):

         if self.d < self.d1 and self.d <self. d2 and self.d < self.d3:
             # print("You are " + str(d) + "  miles from Anglin Falls")
             if self.latitude < self.Anglin_Falls[0] and self.longitude < self.Anglin_Falls[1]:
                 print("Your nearest position is " + str(self.d3) + " miles southwest of Anglin Falls")
             elif  self.latitude < self.Anglin_Falls[0] and  self.longitude > self.Anglin_Falls[1]:
                 print("You are nearest position is " + str( self.d3) + " miles southeast of Anglin Falls")
             if  self.latitude > self.Anglin_Falls[0] and  self.longitude > self.Anglin_Falls[1]:
                 print("You are nearest postion is  " + str( self.d3) + " miles northeast of Anglin Falls")
             elif  self.latitude > self.Anglin_Falls[1] and  self.longitude < self.Anglin_Falls[1]:
                 print("You are nearest position is " + str( self.d3) + " miles northwest of Anglin Falls")



         if  self.d1 <  self.d and  self.d1 <  self.d2 and  self.d1 <  self.d3:
             # print("You are  " + str(d1) + "  miles from Owsley Fork")
             if  self.latitude < self.Owsley_fork[0] and  self.longitude < self.Owsley_fork[1]:
                 print("Your nearest position is  " + str( self.d3) + " miles southwest of Owsley Fork")
             elif  self.latitude < self.Owsley_fork[0] and  self.longitude > self.Owsley_fork[1]:
                 print("Your  nearest position is " + str( self.d3) + " miles southeast of Owsley Fork")
             if  self.latitude > self.Owsley_fork[0] and  self.longitude > self.Owsley_fork[1]:
                 print("Your nearest position is  " + str( self.d3) + " miles northeast of Owsley Fork")
             elif  self.latitude > self.Owsley_fork[1] and  self.longitude < self.Owsley_fork[1]:
                 print("Your nearest position is  " + str( self.d3) + " miles northwest of Owsley fork")


         if  self.d2 <  self.d and  self.d2 <  self.d1 and  self.d2 <  self.d3:
             # print("You are " + str(d2) + "  miles from Boorne Tavern Hotel")
             if  self.latitude < self.Boorne_Tavern_Hotel[0] and  self.longitude < self.Boorne_Tavern_Hotel[1]:
                 print("Your nearest position is  " + str( self.d3) + " miles southwest of Boorne Tavern Hotel")
             elif  self.latitude < self.Boorne_Tavern_Hotel[0] and  self.longitude > self.Boorne_Tavern_Hotel[1]:
                 print("Your nearest position is  " + str( self.d3) + " miles southeast of Boorne Tavern Hotel")
             if  self.latitude > self.Boorne_Tavern_Hotel[0] and  self.longitude > self.Boorne_Tavern_Hotel[1]:
                 print("Your nearest position is " + str( self.d3) + " miles northeast of Boorne Tavern Hotel")
             elif  self.latitude > self.Boorne_Tavern_Hotel[1] and  self.longitude < self.Boorne_Tavern_Hotel[1]:
                 print("Your nearest   position is " + str( self.d3) + " miles northwest of Boorne Tavern Hotel")



         if  self.d3 <  self.d and  self.d3 <  self.d1 and  self.d3 <  self.d2:
             # print("You are  " + str(d3) +"  miles from West Pinnacle")
             if  self.latitude < self.West_Pinnacle[0] and  self.longitude < self.West_Pinnacle[1]:
                 print("Your nearest  position is " + str( self.d3) + " miles southwest of West Pinnacle")
             elif  self.latitude < self.West_Pinnacle[0] and  self.longitude >self. West_Pinnacle[1]:
                 print("Your nearest position is  " + str( self.d3) + " miles southeast of West Pinnacle")
             if  self.latitude > self.West_Pinnacle[0] and  self.longitude > self.West_Pinnacle[1]:
                 print("Your nearest position is  " + str( self.d3) + " miles northeast of West Pinnacle")
             elif  self.latitude > self.West_Pinnacle[1] and  self.longitude < self.West_Pinnacle[1]:
                 print("Your nearest position is " + str( self.d3) + " miles northwest of West Pinnacle")

def main():
    lad = Map()
    lad.user_input()
    lad.calculate()
    lad.Compare()





if __name__ == "__main__":

  main()



