from math import sin, cos, acos, radians
class DestinationCalculator:
    def __init__(self):
        # You may enter code here.
        self.places = {}

    def process(self, line: str) -> str:
        res = line.split(":")
        phi = 0
        delta = 0
        if res[0] == "LOC":
            self.places[res[1]] = [res[2], res[3]]
            return res[1]
        elif res[0] == "TRIP":
            phi = abs(float(self.places[res[2]][1]) - float(self.places[res[3]][1]))
            phi1 = radians(float(self.places[res[2]][0]))
            phi2 = radians(float(self.places[res[3]][0]))
            phi12 = radians(float(self.places[res[2]][0]))
            phi22 = radians(float(self.places[res[3]][0]))
            delta = acos((sin(phi1) * sin(phi2) + (cos(phi12) * cos(phi22) * cos(phi))))
            distance = 3963 * delta
            response = res[1] + ":" + res[2] + ":" + res[3] + ":" + str(distance)
            print(response)
            return response


d = DestinationCalculator()
d.process("LOC:CHI:41.836944:-87.684722")
d.process("LOC:NYC:40.7127:-74.0059")
d.process("TRIP:C0FFEE1C:CHI:NYC")