from math import sin, cos, acos, radians
RADIUS_MILES = 3963
class DestinationCalculator:
    def __init__(self):
        self.cities = {}

    # You may enter code here.
    
    def process(self, line: str) -> str:
        if line[:3] == "LOC":
            _, city, phi, k = line.split(":")
            self.cities[city] = [float(phi), float(k)]
            return city
        else:
            _, user_id,start_city, end_city = line.split(":")
            start_phi, start_k = self.cities[start_city]
            end_phi, end_k = self.cities[end_city]
            delta_diff = radians(abs(start_k - end_k))
            inv_delta_sigma = sin(radians(start_phi))*sin(radians(end_phi)) + cos(radians(start_phi)) * cos(radians(end_phi)) * cos(delta_diff)
            distance = RADIUS_MILES * acos(inv_delta_sigma)
            return "{}:{}:{}:{}".format(user_id, start_city, end_city, distance)

        
        # You must enter code here.
d = DestinationCalculator()
d.process("LOC:CHI:41.836944:-87.684722")
d.process("LOC:NYC:40.7127:-74.0059")
d.process("TRIP:C0FFEE1C:CHI:NYC")