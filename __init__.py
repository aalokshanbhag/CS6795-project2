import sys
import queue as queue
import pandas as pd
#test
class agent:
    '''This class is for an agent's state'''
    def __init__(self, _health_level, _finance_level, _has_car, _has_bike):
        self.health_level = _health_level # low(0), mid(1), high(2)
        self.finance_level = _finance_level # low(0), mid(1), high(2)
        self.has_car = _has_car  # True, False
        self.has_bike = _has_bike  # True, False
        
    def __str__(self):
        return 'Current agent State Summary \n' \
        + 'health_level = {}\n'.format(self.health_level) \
        + 'fatigue_level = {}\n'.format(self.fatigue_level) \
        + 'has_car = {}\n'.format(self.has_car) \
        + 'has_bike = {}\n'.format(self.has_bike)
    
class env:
    '''This class is for an enviroment factors'''
    def __init__(self, _weather, _time_of_day):
        self.weather = _weather # bad(0), so so(1), good(2) *bad means you travel in a bad weather like rainy
        self.time_of_day = _time_of_day # bad(0), so so(1), good(2) *bad means you travel in a rush hour 
        
    def __str__(self):
        return 'Current journey Summary \n' \
        + 'weather = {}\n'.format(self.weather) \
        + 'time_of_day = {}\n'.format(self.time_of_day)
        
        
class journey:
    '''This class is for characteristics of a journey'''
    def __init__(self, _distance, _time_available, _urgent_level):
        self.distance =_distance              # short(0), mid(1), long(2)
        self.time_available = _time_available # short(0), mid(1), long(2)
        self.urgent_level = _urgent_level     # low(0), mid(1), high(2)
        
    def __str__(self):
        return 'Current journey Summary \n' \
        + 'distance = {}\n'.format(self.distance) \
        + 'time_available = {}\n'.format(self.time_available) \
        + 'urgent_level = {}\n'.format(self.urgent_level) 
     
class transportation:
    '''This class is for a type of transportation'''
    def __init__(self, _name, _price, _comfort_level, _availability, _accessability, _safety):
        self.name = _name                   # "car", "bus", "walk", "uber", "train", "bike"
        self.price =_price                  # low(0), mid(1), high(2)
        self.comfort_level = _comfort_level # low(0), mid(1), high(2)
        self.availability = _availability   # True False
        self.accessability = _accessability # True False
        self.safety = _safety               # low(0), mid(1), high(2)
        self.score = 0                 # integer to represent score for a type of transportation, higher score means higher probability to be chosen by agent 
    
    def __lt__(self, other):
        """intentionally reverse the inequality for the priority queue use"""
        return (self.score > other.score)

    def __str__(self):
        return 'type of transportation = {}\n'.format(self.name) \
        + 'price = {}\n'.format(self.price) \
        + 'comfort_level = {}\n'.format(self.comfort_level) \
        + 'availability = {}\n'.format(self.availability) \
        + 'accessability = {}\n'.format(self.accessability) \
        + 'safety = {}\n'.format(self.safety)
                       
class rule:
    '''This class if for a rule. Each rules has different condtions.'''
    def __init__(self, _ID, _health_level, _has_car, _has_bike, _finance_level,\
    _weather, _time_of_day,\
    _distance, _time_available, _urgent_level,\
    _car_score_change, _bus_score_change, _walk_score_change, _uber_score_change, _train_score_change, _bike_score_change):
        # conditions where the rule is fired"""
        self.ID = _ID
        self.health_level = _health_level
        self.has_car = _has_car
        self.has_bike = _has_bike
        self.finance_level = _finance_level
        self.weather = _weather
        self.time_of_day = _time_of_day
        self.distance = _distance
        self.time_available = _time_available
        self.urgent_level = _urgent_level
        self.num_condi = 0
        self.score = 0
        
        # changes by the rule fired
        self.car_score_change = _car_score_change
        self.bus_score_change = _bus_score_change
        self.walk_score_change = _walk_score_change
        self.uber_score_change = _uber_score_change
        self.train_score_change = _train_score_change
        self.bike_score_change = _bike_score_change
    
        # compute number of conditions
        if _health_level != None:
            self.num_condi = self.num_condi + 1
        if _has_car != None:
            self.num_condi = self.num_condi + 1
        if _has_bike != None:
            self.num_condi = self.num_condi + 1
        if _finance_level != None:
            self.num_condi = self.num_condi + 1
        if _weather != None:
            self.num_condi = self.num_condi + 1
        if _time_of_day != None:
            self.num_condi = self.num_condi + 1
        if _distance != None:
            self.num_condi = self.num_condi + 1
        if _time_available != None:
            self.num_condi = self.num_condi + 1
        if _urgent_level != None:
            self.num_condi = self.num_condi + 1
        
    def computeScore(self, _curr_agent, _curr_env, _curr_journey):
        '''Compute how many conditions are statisfied based on "state" and "environment"'''
        score = 0
        # conditions related to agent
        if self.health_level != None and self.health_level == _curr_agent.health_level:
            score += 1
        if self.has_car != None and self.has_car == _curr_agent.has_car:
            score += 1
        if self.has_bike != None and self.has_bike == _curr_agent.has_bike:
            score += 1
        if self.finance_level != None and self.finance_level == _curr_agent.finance_level:
            score += 1
        
        # conditions related to environment
        if self.weather != None and self.weather == _curr_env.weather:
            score += 1
        if self.time_of_day != None and self.time_of_day == _curr_env.time_of_day:
            score += 1
            
        # conditions related to journey
        if self.distance != None and self.distance == _curr_journey.distance:
            score += 1
        if self.time_available != None and self.time_available == _curr_journey.time_available:
            score += 1
        if self.urgent_level != None and self.urgent_level == _curr_journey.urgent_level:
            score += 1
        
        # update the score which is the number of conditions satisfied
        self.score = score
    
    def __lt__(self, other):
        """intentionally reverse the inequality for the priority queue use"""
        return (self.score > other.score)
           
    def __str__(self):
        return 'Rule {} Summary \n'.format(self.ID) \
        + 'This rule is fired if \n' \
        + 'health_level = {}\n'.format(self.health_level) \
        + 'has_car = {}\n'.format(self.has_car) \
        + 'has_bike = {}\n'.format(self.has_bike) \
        + 'finance_level = {}\n'.format(self.finance_level) \
        + 'weather = {}\n'.format(self.weather) \
        + 'time_of_day = {}\n'.format(self.time_of_day) \
        + 'distance = {}\n'.format(self.distance) \
        + 'time_available = {}\n'.format(self.time_available) \
        + 'urgetnt_level = {}\n'.format(self.urgetnt_level) \
        + 'score = {}\n'.format(self.score)
    
def update_score(rule, bus, car):
    if rule.car_score_change != None:
        car.score = car.score + rule.car_score_change
    if rule.bus_score_change != None:
        bus.score = bus.score + rule.bus_score_change
    #walk.score = walk.score + rule.walk_score_change
    #uber.score = uber.score + rule.uber_score_change
    #train.score = train.score + rule.train_score_change
    #bike.score = bike.score + rule.bike_score_change

def best_transportation(bus, car):
    transportations = queue.PriorityQueue()
    transportations.put(bus)
    transportations.put(car)
    return transportations.get().name
    
def main():
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
    agent_q1 = input('How is your health condition? (0 for low, 1 for mid, 2 for high) : ')
    agent_q2 = input('How is your financial condition? (0 for low, 1 for mid, 2 for high) : ')
    agent_q3 = input('Do you have a car? (0 for No, 1 for Yes) : ')
    agent_q4 = input('Do you have a bike? (0 for No, 1 for Yes) : ')
    curr_agent = agent(int(agent_q1), int(agent_q2), int(agent_q3), int(agent_q4))
    
    # create environment object
    env_q1 = input('How is the weather now? (0 for bad, 1 for so so, 2 for good) : ')
    env_q2 = input('How bad is the traffic? (0 for bad, 1 for so so, 2 for good) : ')
    curr_env = env(int(env_q1), int(env_q2))
    
    # create journey object
    journey_q1 = input('How far is your distination? (0 for close, 1 for midium, 2 for far away) : ')
    journey_q2 = input('How much time is available for you? (0 for short, 1 for mid, 2 for long) : ')
    journey_q3 = input('How urgent is this journey for you? (0 for No, 1 for just so so, 2 for yes) : ')
    curr_journey = journey(int(journey_q1), int(journey_q2), int(journey_q3))
    
    '''create a set of rules based on excel (TO DO)'''
    num_rules = 8
    rule_data = pd.read_excel(r'rules.xlsx', sheet_name='Final')
    rule_data = rule_data.where((pd.notnull(rule_data)), None)
    rule_data = rule_data.as_matrix() # matrix which has rule data 
    
    rules = queue.PriorityQueue()
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

