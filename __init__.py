import sys
import queue as queue
import pandas as pd

class agent:
    '''This class is for an agent's state'''
    def __init__(self, _health_level, _finance_level, _has_car, _has_bike):
        self.health_level = _health_level # low(0), mid(1), high(2)
        self.finance_level = _finance_level # low(0), mid(1), high(2)
        self.rules = []

    def fire_rules(self, curr_agent, curr_env, curr_journey, car, walk):
        for rule in self.rules:
            if rule.isMatch(curr_agent, curr_env, curr_journey, car, walk):
                rule.fire_rule(curr_agent, curr_env, curr_journey, car, walk)
        
        
    def __str__(self):
        return 'Current agent State Summary \n' \
        + 'health_level = {}\n'.format(self.health_level) \
        + 'finance_level = {}\n'.format(self.finance_level)
    
class env:
    '''This class is for an enviroment factors'''
    def __init__(self, _weather, _isRushHour, _isNight):
        self.weather = _weather # bad(0), so so(1), good(2) *bad means you travel in a bad weather like rainy
        self.isRushHour = _isRushHour # No(0), Yes(1) whether now is in rush hour or not 
        self.isNight = _isNight # No(0), Yes(1) whether now is night or not 
        self.rules = []

    def fire_rules(self, curr_agent, curr_env, curr_journey, car, walk):
        for rule in self.rules:
            if rule.isMatch(curr_agent, curr_env, curr_journey, car, walk):
                rule.fire_rule(curr_agent, curr_env, curr_journey, car, walk)

    def __str__(self):
        return 'Current enviroment Summary \n' \
        + 'weather = {}\n'.format(self.weather) \
        + 'isRushHour = {}\n'.format(self.isRushHour) \
        + 'isNight = {}\n'.format(self.isNight) \
        
        
class journey:
    '''This class is for characteristics of a journey'''
    def __init__(self, _distance, _time_available, _importance_level):
        self.distance =_distance              # short(0), mid(1), long(2)
        self.time_available = _time_available # short(0), mid(1), long(2)
        self.importance_level = _importance_level # low(0), mid(1), high(2)
        self.rules = []

    def fire_rules(self, curr_agent, curr_env, curr_journey, car, walk):
        for rule in self.rules:
            if rule.isMatch(curr_agent, curr_env, curr_journey, car, walk):
                rule.fire_rule(curr_agent, curr_env, curr_journey, car, walk)

    def __str__(self):
        return 'Current journey Summary \n' \
        + 'distance = {}\n'.format(self.distance) \
        + 'time_available = {}\n'.format(self.time_available) \
        + 'importance_level = {}\n'.format(self.importance_level) 
     
class transportation:
    '''This class is for a type of transportation'''
    def __init__(self, _name, _price, _comfort_level, _availability, _accessability, _safety):
        self.name = _name                   # "car", "bus", "walk", "uber", "train", "bike"
        self.price =_price                  # low(0), mid(1), high(2)
        self.comfort_level = _comfort_level # low(0), mid(1), high(2)
        self.availability = _availability   # True False
        self.accessability = _accessability # True False
        self.safety = _safety               # low(0), mid(1), high(2)
        self.rules = []
    
    def fire_rules(self, curr_agent, curr_env, curr_journey, car, walk):
        for rule in self.rules:
            if rule.isMatch(curr_agent, curr_env, curr_journey, car, walk):
                rule.fire_rule(curr_agent, curr_env, curr_journey, car, walk)
    
    def __str__(self):
        return 'type of transportation = {}\n'.format(self.name) \
        + 'price = {}\n'.format(self.price) \
        + 'comfort_level = {}\n'.format(self.comfort_level) \
        + 'availability = {}\n'.format(self.availability) \
        + 'accessability = {}\n'.format(self.accessability) \
        + 'safety = {}\n'.format(self.safety)
                       
class rule:
    '''This class if for a rule. Each rules has different condtions.'''
    def __init__(self, _ID, _health_level, _finance_level,\
    _weather, _isRushHour, _isNight,\
    _distance, _time_available, _importance_level,\
    _car_price, _car_comfort_level, _car_availability, _car_accessability, _car_safety,\
    _bus_price, _bus_comfort_level, _bus_availability, _bus_accessability, _bus_safety,\
    _walk_price, _walk_comfort_level, _walk_availability, _walk_accessability, _walk_safety,\
    _uber_price, _uber_comfort_level, _uber_availability, _uber_accessability, _uber_safety,\
    _train_price, _train_comfort_level, _train_availability, _train_accessability, _train_safety,\
    _bike_price, _bike_comfort_level, _bike_availability, _bike_accessability, _bike_safety,\
    _rate_health_level, _rate_finance_level,\
    _rate_weather, _rate_isRushHour, _rate_isNight,\
    _rate_distance, _rate_time_available, _rate_importance_level,\
    _rate_car_price, _rate_car_comfort_level, _rate_car_availability, _rate_car_accessability, _rate_car_safety,\
    _rate_bus_price, _rate_bus_comfort_level, _rate_bus_availability, _rate_bus_accessability, _rate_bus_safety,\
    _rate_walk_price, _rate_walk_comfort_level, _rate_walk_availability, _rate_walk_accessability, _rate_walk_safety,\
    _rate_uber_price, _rate_uber_comfort_level, _rate_uber_availability, _rate_uber_accessability, _rate_uber_safety,\
    _rate_train_price, _rate_train_comfort_level, _rate_train_availability, _rate_train_accessability, _rate_train_safety,\
    _rate_bike_price, _rate_bike_comfort_level, _rate_bike_availability, _rate_bike_accessability, _rate_bike_safety,\
    _car_eliminate, _walk_eliminate):
        # conditions where the rule is fired"""
        self.ID = _ID
        self.health_level = _health_level
        self.finance_level = _finance_level
        self.weather = _weather
        self.isRushHour = _isRushHour
        self.isNight = _isNight
        self.distance = _distance
        self.time_available = _time_available
        self.importance_level = _importance_level
        
        self.car_price = _car_price
        self.car_comfort_level = _car_comfort_level
        self.car_availability = _car_availability
        self.car_accessability = _car_accessability
        self.car_safety	= _car_safety
        
        self.walk_price = _walk_price
        self.walk_comfort_level = _walk_comfort_level
        self.walk_availability = _walk_availability
        self.walk_accessability = _walk_accessability
        self.walk_safety = _walk_safety
        
        self.rate_car_price = _rate_car_price
        self.rate_car_comfort_level = _rate_car_comfort_level
        self.rate_car_availability = _rate_car_availability
        self.rate_car_accessability = _rate_car_accessability
        self.rate_car_safety	= _rate_car_safety
        
        self.rate_walk_price = _rate_walk_price
        self.rate_walk_comfort_level = _rate_walk_comfort_level
        self.rate_walk_availability = _rate_walk_availability
        self.rate_walk_accessability = _rate_walk_accessability
        self.rate_walk_safety = _rate_walk_safety
        
        self.car_eliminate = _car_eliminate
        self.walk_elinimate = _walk_eliminate
        
        # compute number of conditions(TODO)
        

    def isMatch(self, curr_agent, curr_env, curr_journey, car, walk):
        if self.health_level != None and self.health_level != curr_agent.health_level:
            return False
        if self.finance_level != None and self.finance_level = curr_agent.finance_level:
            return False
        if self.weather != None and self.weather != curr_env.weather:
            return False
        if self.isRushHour != None and self.isRushHour != curr_env.isRushHour:
            return False
        if self.isNight != None and self.isNight != curr_env.isNight:
            return False
        if self.distance != None and self.distance != curr_journey.distance:
            return False
        if self.time_available != None and self.time_available != curr_journey.time_available:
            return False
        if self.importance_level != None and self.importance_level != curr_journey.importance_level:
            return False
        if self.car_price != None and self.car_price != car.price:
            return False
        if self.car_comfort_level != None and self.car_comfort_level != car.comfort_level:
            return False
        if self.car_availability != None and self.car_availability != car.availability:
            return False
        if self.car_accessability != None and self.car_accessability != car.accessability:
            return False
        if self.car_safety != None and self.car_safety != car.safety:
            return False
        if self.walk_price != None and self.walk_price != walk.price:
            return False            
        if self.walk_comfort_level != None and self.walk_comfort_level != walk.comfort_level:
            return False
        if self.walk_availability != None and self.walk_availability != _walk_availability:
            return False
        if self.walk_accessability != None and self.walk_accessability != _walk_accessability:
            return False
        if self.walk_safety != None and self.walk_safety != _walk_safety:
            return False
        return True

    def fire_rule(self, curr_agent, curr_env, curr_journey, car, walk):
        #Do not exceed 2 !!!!!!!!! -> future work
        if self.rate_car_comfort_level != None:
            car.comfort_level += self.rate_car_comfort_level
        if self.rate_car_availability != None:
            liavavailability += self.rate_car_availability
        if self.rate_walk_comfort_level != None:
            walk.comfort_level += self.rate_walk_comfort_level
        if self.rate_walk_availability != None:
            walk.availability += self.rate_walk_availability

    def __str__(self):
        return 'Rule {} Summary \n'.format(self.ID) \
        + 'This rule is fired if \n' \
        + 'health_level = {}\n'.format(self.health_level) \
        + 'finance_level = {}\n'.format(self.finance_level) \
        + 'weather = {}\n'.format(self.weather) \
        + 'distance = {}\n'.format(self.distance) \
        + 'time_available = {}\n'.format(self.time_available) \
        + 'urgetnt_level = {}\n'.format(self.urgetnt_level) \
    

def best_transportation(bus, car):
    transportations = queue.PriorityQueue()
    transportations.put(bus)
    transportations.put(car)
    return transportations.get().name

def distribute_rules(rule_data, curr_agent, curr_env, curr_journey, car, walk) :
    for rule in rule_data:
        if location_to_be_fired == "agent":
            curr_agent.rules.append(rule)
        if location_to_be_fired == "env":
            curr_env.rules.append(rule)
        if location_to_be_fired == "journey":
            curr_journey.rules.append(rule)
        

def main():
    input_data = pd.read_excel(r'input_test.xlsx')
    input_data = input_data.where((pd.notnull(input_data)), None)
    input_data = input_data.as_matrix() # matrix which has input data 
    
    #car_price = input_data[0][9]
    car = transportation('car', input_data[0][9], input_data[0][10], _availability, _accessability, _safety):
    


    rule_data = pd.read_excel(r'rule_test.xlsx')
    rule_data = rule_data.where((pd.notnull(rule_data)), None)
    rule_data = rule_data.as_matrix() # matrix which has rule data 
    

    
    
    
    
    car = transportation('car, _price, _comfort_level, _availability, _accessability, _safety):
    transportations = []
    '''Main function to be run'''

    '''create transportation objects'''
    # create bus object
    bus_q1 = input('Is bus available for you now? (True, False) : ')
    bus_q2 = input('Is bus accessible for you now? (True, False) : ')
    bus_q3 = input('How safe is using a bus for you? (0 for low, 1 for mid, 2 for high) : ')
    bus = transportation("bus", 1, 1, int(bus_q1), int(bus_q2), int(bus_q3))
    
    # create bus object
    car_q1 = input('Is car available for you now? (True, False) : ')
    car_q2 = input('Is car accessible for you now? (True, False) : ')
    car_q3 = input('How safe is using a car for you? (0 for low, 1 for mid, 2 for high) : ')
    car = transportation('car', 2, 2, int(car_q1), int(car_q2), int(car_q3))
    
    # create walk object
    # create uber object
    # create train object
    # create bike object
    
    '''create other objects'''
    # create agent object
    curr_agent = agent(int(agent_q1), int(agent_q2), int(agent_q3), int(agent_q4))
    
    # create environment object
    curr_env = env(int(env_q1), int(env_q2))
    
    # create journey object
    curr_journey = journey(int(journey_q1), int(journey_q2), int(journey_q3))
    
    '''create a set of rules based on excel (TO DO)'''
    
    for i in range(0,num_rules):
        curr_rule = rule(rule_data[i][0], rule_data[i][1], rule_data[i][2], \
        rule_data[i][3], rule_data[i][4], rule_data[i][5], rule_data[i][6], \
        rule_data[i][7], rule_data[i][8], rule_data[i][9], rule_data[i][10], \
        rule_data[i][11], rule_data[i][12], rule_data[i][13], rule_data[i][14], rule_data[i][15])
        curr_rule.computeScore(curr_agent, curr_env, curr_journey)
        rules.put(curr_rule)

    '''while loop to fire rules with use of priority queue'''
    while not rules.empty():
        '''Iterate until there is no rule whose conditions are satisfied by the current agent, environment, and journey'''
        curr_rule = rules.get()
        if curr_rule.score != curr_rule.num_condi:
            break
        print('Rule {} fired now in priority queue'.format(curr_rule.ID))
        update_score(curr_rule, bus, car)
        
        # store all rules in a reverse priority queue except for ones already fired
        tmp_rules = queue.PriorityQueue()
        while not rules.empty():
            tmp_rule = rules.get()
            tmp_rule.computeScore(curr_agent, curr_env, curr_journey)
            tmp_rules.put(tmp_rule)
        rules = tmp_rules
        
    return best_transportation(car, bus)
    
if __name__ == "__main__":
    agent_transportation_pick = main()
    print(agent_transportation_pick)

