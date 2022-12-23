import csv
from airport import Airport
from flight import Flight


class FlightMap :
    def import_airports(csv_file):
        airports =[]
        with open(csv_file) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            for row in csv_reader:
                airports.append(row)
            return(airports)
        

    def import_flights(csv_file):
        flights =[]
        with open(csv_file) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            for row in csv_reader:
                flights.append(row)
            return(flights)

    def airports():
        AirportList =FlightMap.import_airports('aeroports.csv')
        print(AirportList)
        obj =[]
        for i in AirportList:
            obj.append(Airport(i[0], i[1], i[2], i[3]))

    def flights():
        FlightList =FlightMap.import_airports('flights.csv')
        print(FlightList)
        obj =[]
        for i in FlightList:
            obj.append(Flight(i[0], i[1], i[2]))
FlightMap.airports()
FlightMap.flights()




