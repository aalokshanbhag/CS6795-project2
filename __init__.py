import sys
import queue as queue
import pandas as pd

class agent:
    '''This class is for an agent's state'''
    def __init__(self, _health_level, _finance_level):
        self.health_level = _health_level # low(0), mid(1), high(2)
        self.finance_level = _finance_level # low(0), mid(1), high(2)
        self.emotion = "great" # "great", "ok", "horrible"
        self.rules = []

    def fire_rules(self, curr_agent, curr_env, curr_journey, car, walk, candidate_transportations):
        for rule in self.rules:
            if rule.isMatch(curr_agent, curr_env, curr_journey, car, walk):
                rule.fire_rule(curr_agent, curr_env, curr_journey, car, walk, candidate_transportations)
        
    def __str__(self):
        return 'Current agent State Summary \n' \
        + 'health_level = {}\n'.format(self.health_level) \
        + 'finance_level = {}\n'.format(self.finance_level) \
        + 'emotion = {}\n'.format(self.emotion) \
    
class env:
    '''This class is for an enviroment factors'''
    def __init__(self, _weather, _isRushHour, _isNight):
        self.weather = _weather # bad(0), so so(1), good(2) *bad means you travel in a bad weather like rainy
        self.isRushHour = _isRushHour # No(0), Yes(1) whether now is in rush hour or not 
        self.isNight = _isNight # No(0), Yes(1) whether now is night or not 
        self.rules = []

    def fire_rules(self, curr_agent, curr_env, curr_journey, car, walk, candidate_transportations):
        for rule in self.rules:
            if rule.isMatch(curr_agent, curr_env, curr_journey, car, walk):
                rule.fire_rule(curr_agent, curr_env, curr_journey, car, walk, candidate_transportations)

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

    def fire_rules(self, curr_agent, curr_env, curr_journey, car, walk, candidate_transportations):
        for rule in self.rules:
            if rule.isMatch(curr_agent, curr_env, curr_journey, car, walk):
                rule.fire_rule(curr_agent, curr_env, curr_journey, car, walk, candidate_transportations)

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
    
    def fire_rules(self, curr_agent, curr_env, curr_journey, car, walk, candidate_transportations):
        for rule in self.rules:
            if rule.isMatch(curr_agent, curr_env, curr_journey, car, walk):
                rule.fire_rule(curr_agent, curr_env, curr_journey, car, walk, candidate_transportations)
    
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
    _walk_price, _walk_comfort_level, _walk_availability, _walk_accessability, _walk_safety,\
     _rate_car_comfort_level, _rate_car_availability, _rate_car_accessability, _rate_car_safety,\
     _rate_walk_comfort_level, _rate_walk_availability, _rate_walk_accessability, _rate_walk_safety,\
    _car_eliminate, _walk_eliminate, _location_to_be_fired):
        ''' for later use
        _bus_price, _bus_comfort_level, _bus_availability, _bus_accessability, _bus_safety,\
        _uber_price, _uber_comfort_level, _uber_availability, _uber_accessability, _uber_safety,\
        _train_price, _train_comfort_level, _train_availability, _train_accessability, _train_safety,\
        _bike_price, _bike_comfort_level, _bike_availability, _bike_accessability, _bike_safety,\
        _rate_bus_price, _rate_bus_comfort_level, _rate_bus_availability, _rate_bus_accessability, _rate_bus_safety,\
        _rate_uber_price, _rate_uber_comfort_level, _rate_uber_availability, _rate_uber_accessability, _rate_uber_safety,\
        _rate_train_price, _rate_train_comfort_level, _rate_train_availability, _rate_train_accessability, _rate_train_safety,\
        _rate_bike_price, _rate_bike_comfort_level, _rate_bike_availability, _rate_bike_accessability, _rate_bike_safety,\
        '''
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
        
        self.rate_car_comfort_level = _rate_car_comfort_level
        self.rate_car_availability = _rate_car_availability
        self.rate_car_accessability = _rate_car_accessability
        self.rate_car_safety	= _rate_car_safety
        
        self.rate_walk_comfort_level = _rate_walk_comfort_level
        self.rate_walk_availability = _rate_walk_availability
        self.rate_walk_accessability = _rate_walk_accessability
        self.rate_walk_safety = _rate_walk_safety
        
        self.car_eliminate = _car_eliminate
        self.walk_elinimate = _walk_eliminate
        self.location_to_be_fired = _location_to_be_fired

    def isMatch(self, curr_agent, curr_env, curr_journey, car, walk):
        if self.health_level != None and self.health_level != curr_agent.health_level:
            return False
        if self.finance_level != None and self.finance_level != curr_agent.finance_level:
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
        if self.walk_availability != None and self.walk_availability != walk.availability:
            return False
        if self.walk_accessability != None and self.walk_accessability != walk.accessability:
            return False
        if self.walk_safety != None and self.walk_safety != walk.safety:
            return False
        return True

    def fire_rule(self, curr_agent, curr_env, curr_journey, car, walk, candidate_transportations):
        #Do not exceed 2 !!!!!!!!! -> future work
        if self.rate_car_comfort_level != None:
            car.comfort_level += self.rate_car_comfort_level
        if self.rate_car_availability != None:
            car.avavailability += self.rate_car_availability
        if self.rate_walk_comfort_level != None:
            walk.comfort_level += self.rate_walk_comfort_level
        if self.rate_walk_availability != None:
            walk.availability += self.rate_walk_availability
        if self.car_eliminate == 1:
            eliminate_transportation("car", candidate_transportations)
        if self.walk_elinimate == 1:
            eliminate_transportation("walk", candidate_transportations)

    def __str__(self):
        return 'Rule {} Summary \n'.format(self.ID) \
        + 'This rule is fired if \n' \
        + 'health_level = {}\n'.format(self.health_level) \
        + 'finance_level = {}\n'.format(self.finance_level) \
        + 'weather = {}\n'.format(self.weather) \
        + 'distance = {}\n'.format(self.distance) \
        + 'time_available = {}\n'.format(self.time_available) \
        + 'importance_level = {}\n'.format(self.importance_level) \
    
def eliminate_transportation(transportation_name, candidate_transportations):
    '''This is the fuction to remove a transportation from the candidate_transportations list'''
    # transporatation_name is the name of the transportation you want to remove from the candidate list
    for curr_can in candidate_transportations:
        if curr_can.name == transportation_name:
            candidate_transportations.pop(curr_can)

def choose_best_transportation(candidate_transportations):
    '''choose the best transportation among candidate_transportation list and store this trip as one experience into habit''' 
    '''code for exception (TODO)'''
    if len(candidate_transportations) == 2: # case where there are more than one transportation object in list
        return candidate_transportations[0]
    if len(candidate_transportations) == 0: # case where there is no transportation object in list
        return candidate_transportations[0]
    return candidate_transportations[0] # other wise

def distribute_rules(curr_rule, curr_agent, curr_env, curr_journey, car, walk) :
    if curr_rule.location_to_be_fired == "agent":
        curr_agent.rules.append(rule)
    if curr_rule.location_to_be_fired == "env":
        curr_env.rules.append(rule)
    if curr_rule.location_to_be_fired == "journey":
        curr_journey.rules.append(rule)

def is_use_habit(habit, curr_agent, curr_env, curr_journey):

    #[health_level, weather, isRushHour, isNight, time_available, urgetnt_level, emotion, result]
    habituated_transportation = None
    count  = 0
    for experience in habit:
        if abs(experience[0] - curr_agent.health_level) != 2 and abs(experience[1] - curr_env.weather) != 2 and abs(experience[2] - curr_env.isRushHour) != 2 and abs(experience[3] - curr_env.isNight) != 2 and abs(experience[4] - curr_journey.time_available) != 2 and abs(experience[5] - curr_journey.importance_level) != 2:
            if experience[6] == "horrible": # case where agent re-consider the transportation because of horrible experience
                return False, None
            count += 1
            habituated_transportation = experience[7]
    if count > 2:
        return True, habituated_transportation
    return False, None      

def run(input_data, habit):
    '''create non-rule objects''' 
    # create agent object
    curr_agent = agent(input_data[1], input_data[2])
    # create environment object
    curr_env = env(input_data[3], input_data[4], input_data[5])
    # create journey object
    curr_journey = journey(input_data[6], input_data[7], input_data[8])

    # create transportation objects
    car = transportation('car', input_data[9], input_data[10], input_data[11], input_data[12],input_data[13])
    walk = transportation('walk', input_data[14], input_data[15], input_data[16], input_data[17],input_data[18])

    ''' list of candidate transportations'''
    # list to store possible transportations
    candidate_transportations = [car, walk]
    
    '''create a set of rules based on excel'''
    # read rule data from excel files
    rule_data = pd.read_excel(r'rule_test.xlsx')
    rule_data = rule_data.where((pd.notnull(rule_data)), None)
    rule_data = rule_data.as_matrix() # matrix which has rule data 
    num_rules = 5 #NEEDS TO BE CHANGED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # create rule objects and distribute them accordingly 
    for i in range(0,num_rules):
        curr_rule = rule(rule_data[i][0], rule_data[i][1], rule_data[i][2], \
        rule_data[i][3], rule_data[i][4], rule_data[i][5], rule_data[i][6], \
        rule_data[i][7], rule_data[i][8], rule_data[i][9], rule_data[i][10], \
        rule_data[i][11], rule_data[i][12], rule_data[i][13], rule_data[i][14], \
        rule_data[i][15], rule_data[i][16], rule_data[i][17], rule_data[i][18], \
        rule_data[i][19], rule_data[i][20], rule_data[i][21], rule_data[i][22], \
        rule_data[i][23], rule_data[i][24], rule_data[i][25], rule_data[i][26], \
        rule_data[i][27], rule_data[i][28], rule_data[i][29]) 
        distribute_rules(curr_rule, curr_agent, curr_env, curr_journey, car, walk)
        
    '''fire rules in the appropriate order discussed in the report'''    
    if is_use_habit(habit, curr_agent, curr_env, curr_journey)[0] == True and\
     is_use_habit(habit, curr_agent, curr_env, curr_journey)[1].accessability == 1 and \
     is_use_habit(habit, curr_agent, curr_env, curr_journey)[1].availability == 1: # case where the agent can reduce the cognitive load by using habit to decide
        result = is_use_habit(habit, curr_agent, curr_env, curr_journey)[1]
    else: # case where habit does not work to decide the transportation so that the agent dive into the cognitive procedure
        curr_agent.fire_rules(curr_agent, curr_env, curr_journey, car, walk, candidate_transportations)   #fire rules associated to agent
        curr_journey.fire_rules(curr_agent, curr_env, curr_journey, car, walk, candidate_transportations) #fire rules associated to journey
        curr_env.fire_rules(curr_agent, curr_env, curr_journey, car, walk, candidate_transportations)     #fire rules associated to env
        car.fire_rules(curr_agent, curr_env, curr_journey, car, walk, candidate_transportations)          #fire rules associated to car
        walk.fire_rules(curr_agent, curr_env, curr_journey, car, walk, candidate_transportations)         #fire rules associate to walk     
        result = choose_best_transportation(candidate_transportations) # function to choose best transporttaion from candidate_transportations list  
    emotion = "great"
    exprience = [curr_agent.health_level, curr_env.weather, curr_env.isRushHour, curr_env.isNight, curr_journey.time_available, curr_journey.importance_level, emotion, result]
    habit.append(exprience)
    
def main():
    '''Main function to be run'''
    # read input data from excel files
    input_data = pd.read_excel(r'input_test.xlsx')
    input_data = input_data.where((pd.notnull(input_data)), None)
    input_data = input_data.as_matrix() # matrix which has input data 
    num_input_data = 20 # NEEDSTO BE CHANGED

    # habit
    habit = []
    for i in range(0, num_input_data):
        run(input_data[i], habit)
    

if __name__ == "__main__":
    main()
