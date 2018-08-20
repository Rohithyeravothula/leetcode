from collections import defaultdict
class StatisticsCalculator:
    def __init__(self):
        self.user = defaultdict(int)
        self.city = defaultdict(int)
        self.total_dist = 0
    # You may enter code here

    def get_keys(self, d, v):
        l = []
        for key, val in d.items():
            if v == val:
                l.append(key)
        l.sort()
        return l[0]

    
    def process(self, line: str) -> str:
        user_id, scity, ecity, dist = line.split(":")
        self.user[user_id] += int(dist)
        self.city[scity] += 1
        self.city[ecity] += 1
        self.total_dist += int(dist)
        max_dist = self.user[max(self.user, key=self.user.get)]
        busy_city = self.city[max(self.city, key=self.city.get)]
        max_user_id = self.get_keys(self.user, max_dist)
        max_city = self.get_keys(self.city, busy_city)
        response = "{}:{}:{}".format(self.total_dist, max_user_id, max_city)
        print(response)
        return response

s = StatisticsCalculator()
s.process("C0FFEE1C:CHI:NYC:714")
s.process("0FF1CE18:LA:SEATTLE:961")
s.process("C0FFEE1C:NYC:LA:2448")




class StatisticsCalculator:

    def __init__(self):
        self.total_distance = 0
        self.users = {}
        self.cities = {}

    def add_user(self, user_id, distance):
        if user_id in self.users:
            self.users[user_id] += distance
        else:
            self.users[user_id] = distance

    def increment_city(self, city_name):
        if city_name in self.cities:
            self.cities[city_name] += 1
        else:
            self.cities[city_name] = 1
    
    
    def process(self, line: str) -> str:
        
        # You must enter code here
        user_id, start_city, end_city, distance = line.split(":")
        distance = int(distance)
        self.total_distance += distance
        self.add_user(user_id, distance)
        self.increment_city(start_city)
        self.increment_city(end_city)


        max_distance = self.users[max(self.users, key=self.users.get)]
        busy_city_count = self.cities[max(self.cities, key=self.cities.get)]
        busy_cities = [city for city, count in self.cities.items() if count == busy_city_count]
        max_user_ids = [user for user, dist in self.users.items() if dist == max_distance]
        busy_cities.sort()
        max_user_ids.sort()
        busy_city = busy_cities[0]
        max_user_id = max_user_ids[0]
        return "{}:{}:{}".format(self.total_distance, max_user_id, busy_city)
        


s = StatisticsCalculator()
s.process("C0FFEE1C:CHI:NYC:714")
s.process("0FF1CE18:LA:SEATTLE:961")
s.process("C0FFEE1C:NYC:LA:2448")