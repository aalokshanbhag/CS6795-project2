import sys
import queue as queue
import pandas as pd
import random

'''ToDO
1, explanation
   1-1. define class
   1-2. rules
2, >2 case
'''

class agent:
    '''This class is for an agent's state'''
    def __init__(self, _health_level, _finance_level):
        self.health_level = _health_level # low(0), mid(1), high(2)
        self.finance_level = _finance_level # low(0), mid(1), high(2)
        self.emotion = "great" # "great", "ok", "horrible"
        self.rules = []

    def fire_rules(self, curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation):
        print('agent rules firing')
        curr_explanation.add_explanation('Rules associated with agent schema is going to be fired as follows.\n')
        for rule in self.rules:
            if rule.isMatch(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike) == True:
                rule.fire_rule(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation)
        
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

    def fire_rules(self, curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation):
        print('env rules firing')
        curr_explanation.add_explanation('Rules associated with environment schema is going to be fired as follows.\n')
        for rule in self.rules:
            if rule.isMatch(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike):
                rule.fire_rule(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation)

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

    def fire_rules(self, curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation):
        print('journey rules firing')
        curr_explanation.add_explanation('Rules associated with journey schema is going to be fired as follows.\n')
        for rule in self.rules:
            if rule.isMatch(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike):
                rule.fire_rule(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation)

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
    
    def fire_rules(self, curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation):
        print('{} rules firing'.format(self.name))
        curr_explanation.add_explanation('Rules associated with {} schema is going to be fired as follows.\n'.format(self.name))
        for rule in self.rules:
            if rule.isMatch(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike):
                rule.fire_rule(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation)
    
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
    _bus_price, _bus_comfort_level, _bus_availability, _bus_accessability, _bus_safety,\
    _uber_price, _uber_comfort_level, _uber_availability, _uber_accessability, _uber_safety,\
    _train_price, _train_comfort_level, _train_availability, _train_accessability, _train_safety,\
    _bike_price, _bike_comfort_level, _bike_availability, _bike_accessability, _bike_safety,\
    _rate_car_comfort_level, _rate_car_availability, _rate_car_accessability, _rate_car_safety,\
    _rate_walk_comfort_level, _rate_walk_availability, _rate_walk_accessability, _rate_walk_safety,\
    _rate_bus_comfort_level, _rate_bus_availability, _rate_bus_accessability, _rate_bus_safety,\
    _rate_uber_comfort_level, _rate_uber_availability, _rate_uber_accessability, _rate_uber_safety,\
    _rate_train_comfort_level, _rate_train_availability, _rate_train_accessability, _rate_train_safety,\
    _rate_bike_comfort_level, _rate_bike_availability, _rate_bike_accessability, _rate_bike_safety,\
    _car_eliminate, _walk_eliminate, _bus_eliminate, _uber_eliminate, _train_eliminate, _bike_eliminate, _location_to_be_fired):
        
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
        
        self.bus_price = _bus_price
        self.bus_comfort_level = _bus_comfort_level
        self.bus_availability = _bus_availability
        self.bus_accessability = _bus_accessability
        self.bus_safety	= _bus_safety
        
        self.uber_price = _uber_price
        self.uber_comfort_level = _uber_comfort_level
        self.uber_availability = _uber_availability
        self.uber_accessability = _uber_accessability
        self.uber_safety = _uber_safety
        
        self.train_price = _train_price
        self.train_comfort_level = _train_comfort_level
        self.train_availability = _train_availability
        self.train_accessability = _train_accessability
        self.train_safety	= _train_safety
        
        self.bike_price = _bike_price
        self.bike_comfort_level = _bike_comfort_level
        self.bike_availability = _bike_availability
        self.bike_accessability = _bike_accessability
        self.bike_safety = _bike_safety
        
        self.rate_car_comfort_level = _rate_car_comfort_level
        self.rate_car_availability = _rate_car_availability
        self.rate_car_accessability = _rate_car_accessability
        self.rate_car_safety	= _rate_car_safety
        
        self.rate_walk_comfort_level = _rate_walk_comfort_level
        self.rate_walk_availability = _rate_walk_availability
        self.rate_walk_accessability = _rate_walk_accessability
        self.rate_walk_safety = _rate_walk_safety
        
        self.rate_bus_comfort_level = _rate_bus_comfort_level
        self.rate_bus_availability = _rate_bus_availability
        self.rate_bus_accessability = _rate_bus_accessability
        self.rate_bus_safety	= _rate_bus_safety
        
        self.rate_uber_comfort_level = _rate_uber_comfort_level
        self.rate_uber_availability = _rate_uber_availability
        self.rate_uber_accessability = _rate_uber_accessability
        self.rate_uber_safety = _rate_uber_safety
        
        self.rate_train_comfort_level = _rate_train_comfort_level
        self.rate_train_availability = _rate_train_availability
        self.rate_train_accessability = _rate_train_accessability
        self.rate_train_safety	= _rate_train_safety
        
        self.rate_bike_comfort_level = _rate_bike_comfort_level
        self.rate_bike_availability = _rate_bike_availability
        self.rate_bike_accessability = _rate_bike_accessability
        self.rate_bike_safety = _rate_bike_safety
        
        self.car_eliminate = _car_eliminate
        self.walk_eliminate = _walk_eliminate
        self.bus_eliminate = _bus_eliminate
        self.uber_eliminate = _uber_eliminate
        self.train_eliminate = _train_eliminate
        self.bike_eliminate = _bike_eliminate
        
        self.location_to_be_fired = _location_to_be_fired

    def isMatch(self, curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike):
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
            
        if self.bus_price != None and self.bus_price != bus.price:
            return False
        if self.bus_comfort_level != None and self.bus_comfort_level != bus.comfort_level:
            return False
        if self.bus_availability != None and self.bus_availability != bus.availability:
            return False
        if self.bus_accessability != None and self.bus_accessability != bus.accessability:
            return False
        if self.bus_safety != None and self.bus_safety != bus.safety:
            return False
            
        if self.uber_price != None and self.uber_price != uber.price:
            return False            
        if self.uber_comfort_level != None and self.uber_comfort_level != uber.comfort_level:
            return False
        if self.uber_availability != None and self.uber_availability != uber.availability:
            return False
        if self.uber_accessability != None and self.uber_accessability != uber.accessability:
            return False
        if self.uber_safety != None and self.uber_safety != uber.safety:
            return False
        
        if self.train_price != None and self.train_price != train.price:
            return False
        if self.train_comfort_level != None and self.train_comfort_level != train.comfort_level:
            return False
        if self.train_availability != None and self.train_availability != train.availability:
            return False
        if self.train_accessability != None and self.train_accessability != train.accessability:
            return False
        if self.train_safety != None and self.train_safety != train.safety:
            return False
            
        if self.bike_price != None and self.bike_price != bike.price:
            return False            
        if self.bike_comfort_level != None and self.bike_comfort_level != bike.comfort_level:
            return False
        if self.bike_availability != None and self.bike_availability != bike.availability:
            return False
        if self.bike_accessability != None and self.bike_accessability != bike.accessability:
            return False
        if self.bike_safety != None and self.bike_safety != bike.safety:
            return False
        return True

    def fire_rule(self, curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation):
        curr_explanation.add_explanation(' - Rule {} is fired. \n'.format(self.ID))
        print(' - rule {} is fired'.format(self.ID))
        #Do not exceed 2 !!!!!!!!! -> future work
        if self.rate_car_comfort_level != None:
            car.comfort_level += self.rate_car_comfort_level
            if 0 > car.comfort_level: car.comfort_level = 0 
            if 2 < car.comfort_level: car.comfort_level = 2 
        if self.rate_car_availability != None:
            car.availability += self.rate_car_availability
            if 0 > car.availability: car.availability = 0 
            if 1 < car.availability: car.availability = 1 
            
        if self.rate_walk_comfort_level != None:
            walk.comfort_level += self.rate_walk_comfort_level
            if 0 > walk.comfort_level: walk.comfort_level = 0 
            if 2 < walk.comfort_level: walk.comfort_level = 2 
        if self.rate_walk_availability != None:
            walk.availability += self.rate_walk_availability
            if 0 > walk.availability: walk.availability = 0 
            if 1 < walk.availability: walk.availability = 1 
            
        if self.rate_bus_comfort_level != None:
            bus.comfort_level += self.rate_bus_comfort_level
            if 0 > bus.comfort_level: bus.comfort_level = 0 
            if 2 < bus.comfort_level: bus.comfort_level = 2 
        if self.rate_bus_availability != None:
            bus.availability += self.rate_bus_availability
            if 0 > bus.availability: bus.availability = 0 
            if 1 < bus.availability: bus.availability = 1 
            
        if self.rate_uber_comfort_level != None:
            uber.comfort_level += self.rate_uber_comfort_level
            if 0 > uber.comfort_level: uber.comfort_level = 0 
            if 2 < uber.comfort_level: uber.comfort_level = 2 
        if self.rate_uber_availability != None:
            uber.availability += self.rate_uber_availability
            if 0 > uber.availability: uber.availability = 0 
            if 1 < uber.availability: uber.availability = 1 
            
        if self.rate_train_comfort_level != None:
            train.comfort_level += self.rate_train_comfort_level
            if 0 > train.comfort_level: train.comfort_level = 0 
            if 2 < train.comfort_level: train.comfort_level = 2 
        if self.rate_train_availability != None:
            train.availability += self.rate_train_availability
            if 0 > train.availability: train.availability = 0 
            if 1 < train.availability: train.availability = 1 
            
        if self.rate_bike_comfort_level != None:
            bike.comfort_level += self.rate_bike_comfort_level
            if 0 > bike.comfort_level: bike.comfort_level = 0 
            if 2 < bike.comfort_level: bike.comfort_level = 2 
        if self.rate_bike_availability != None:
            bike.availability += self.rate_bike_availability
            if 0 > bike.availability: bike.availability = 0 
            if 1 < bike.availability: bike.availability = 1 
            
        if self.car_eliminate == 1:
            print('  - delete car')
            eliminate_transportation("car", candidate_transportations)
            last_deleted_transportation[0] = "car"
        if self.walk_eliminate == 1:
            print('  - delete walk')
            eliminate_transportation("walk", candidate_transportations)
            last_deleted_transportation[0] = "walk"
        if self.bus_eliminate == 1:
            print('  - delete bus')
            eliminate_transportation("bus", candidate_transportations)
            last_deleted_transportation[0] = "bus"
        if self.uber_eliminate == 1:
            print('  - delete uber')
            eliminate_transportation("uber", candidate_transportations)
            last_deleted_transportation[0] = "uber"
        if self.train_eliminate == 1:
            print('  - delete train')
            eliminate_transportation("train", candidate_transportations)
            last_deleted_transportation[0] = "train"
        if self.bike_eliminate == 1:
            print('  - delete bike')
            eliminate_transportation("bike", candidate_transportations)
            last_deleted_transportation[0] = "bike"
            
    def __str__(self):
        return 'Rule {} Summary \n'.format(self.ID) \
        + 'This rule is fired if \n' \
        + 'health_level = {}\n'.format(self.health_level) \
        + 'finance_level = {}\n'.format(self.finance_level) \
        + 'weather = {}\n'.format(self.weather) \
        + 'distance = {}\n'.format(self.distance) \
        + 'time_available = {}\n'.format(self.time_available) \
        + 'importance_level = {}\n'.format(self.importance_level) \
    
class experience:
    def __init__(self, curr_agent, curr_env, curr_journey, result):
        self.health_level = curr_agent.health_level
        self.weather = curr_env.weather
        self.isRushHour = curr_env.isRushHour
        self.isNight = curr_env.isNight
        self.time_available = curr_journey.time_available
        self.importance_level = curr_journey.importance_level
        self.emotion = curr_agent.emotion
        self.result = result
    def str(self):
        res =  'health_level = {}, '.format(self.health_level) \
        + 'weather = {}, '.format(self.weather) \
        + 'isRushHour = {}, '.format(self.isRushHour) \
        + 'isNight = {}, '.format(self.isNight) \
        + 'time_available = {}, '.format(self.time_available) \
        + 'importance_level = {}, '.format(self.importance_level)\
        + 'emotion = {}, '.format(self.emotion)
        if self.result != None:
            res += 'result = {} \n'.format(self.result.name)
        #print(res)
        return res
        
    def __str__(self):
        return 'Experience Summary \n'\
        + 'health_level = {}\n'.format(self.health_level) \
        + 'weather = {}\n'.format(self.weather) \
        + 'isRushHour = {}\n'.format(self.isRushHour) \
        + 'isNight = {}\n'.format(self.isNight) \
        + 'time_available = {}\n'.format(self.time_available) \
        + 'importance_level = {}\n'.format(self.importance_level)\
        + 'emotion = {}\n'.format(self.emotion)\
        + 'result = {}\n'.format(self.result.name)
    
class habit:
    def __init__(self):
        self.experiences = []
        
    def add_experience(self, experience):
        self.experiences.append(experience)
        
    def __str__(self):
        print_return = 'current habit is as folllows \n'
        for curr_exp in self.experiences:
            print_return += curr_exp.str()
        return print_return
        
class explanation:
    def __init__(self):
        self.explanations = []
    def add_explanation(self, curr_explanation):
        self.explanations.append(curr_explanation)
    def __str__(self):
        print_res = "The agent decides the transportation for the trip in the following way.\n"
        for curr_explanation in self.explanations:
            print_res += curr_explanation
        return print_res
    def write_explantion(self):
        return "TODO"

def eliminate_transportation(transportation_name, candidate_transportations):
    '''This is the fuction to remove a transportation from the candidate_transportations list'''
    # transporatation_name is the name of the transportation you want to remove from the candidate list
    for curr_can in candidate_transportations:
        if curr_can == transportation_name:
            candidate_transportations.remove(curr_can)

def choose_best_transportation(candidate_transportations, last_deleted_transportation, car, walk, bus, uber, train, bike, curr_explanation):
    '''choose the best transportation among candidate_transportation list and store this trip as one experience into habit''' 
    transportation_name = ""
    if len(candidate_transportations) >= 2: # case where there are more than one transportation object in list
        print("choose transportation randomly from candidate_transportations")
        curr_explanation.add_explanation("Since there are more than two transportations from which the agent cannot decide based on the reasoning, the agent choose transportation randomly from them to save time.\n")
        transportation_name = candidate_transportations[random.randint(0,len(candidate_transportations)-1)]
    elif len(candidate_transportations) == 0: # case where there is no transportation object in list
        transportation_name = last_deleted_transportation[0]
        curr_explanation.add_explanation("Since there is no transportation the agent can choose based on the reasoning, the agent chooses a transportation which the agent declined last.\n")
    else:
        transportation_name = candidate_transportations[0] # otherwise
        curr_explanation.add_explanation("Based on the reasoning, the agent succeeds in chooses one transportation! \n")
    
    if transportation_name == "car":
        return car
    elif transportation_name == "walk":
        return walk
    elif transportation_name == "bus":
        return bus
    elif transportation_name == "uber":
        return uber
    elif transportation_name == "train":
        return train
    elif transportation_name == "bike":
        return bike

def distribute_rules(curr_rule, curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike) :
    if curr_rule.location_to_be_fired == "agent":
        curr_agent.rules.append(curr_rule)
    if curr_rule.location_to_be_fired == "env":
        curr_env.rules.append(curr_rule)
    if curr_rule.location_to_be_fired == "journey":
        curr_journey.rules.append(curr_rule)
    if curr_rule.location_to_be_fired == "car":
        car.rules.append(curr_rule)
    if curr_rule.location_to_be_fired == "walk":
        walk.rules.append(curr_rule)
    if curr_rule.location_to_be_fired == "bus":
        bus.rules.append(curr_rule)
    if curr_rule.location_to_be_fired == "uber":
        uber.rules.append(curr_rule)
    if curr_rule.location_to_be_fired == "train":
        train.rules.append(curr_rule)
    if curr_rule.location_to_be_fired == "bike":
        bike.rules.append(curr_rule)

def is_use_habit(curr_habit, curr_agent, curr_env, curr_journey):
    #[health_level, weather, isRushHour, isNight, time_available, urgetnt_level, emotion, result]
    habituated_transportation = None
    count  = 0
    for experience in curr_habit.experiences:
        if abs(experience.health_level - curr_agent.health_level) != 2 and abs(experience.weather- curr_env.weather) != 2 and \
        abs(experience.isRushHour - curr_env.isRushHour) != 2 and abs(experience.isNight - curr_env.isNight) != 2 and \
        abs(experience.time_available - curr_journey.time_available) != 2 and abs(experience.importance_level - curr_journey.importance_level) != 2:
            if experience.emotion == "horrible": # case where agent re-consider the transportation because of horrible experience
                return False, None
            count += 1
            habituated_transportation = experience.result
    if count > 2:
        return True, habituated_transportation
    return False, None      

def run(input_data, curr_habit):
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
    bus = transportation('bus', input_data[19], input_data[20], input_data[21], input_data[22],input_data[23])
    uber = transportation('uber', input_data[24], input_data[25], input_data[26], input_data[27],input_data[28])
    train = transportation('train', input_data[29], input_data[30], input_data[31], input_data[32],input_data[33])
    bike = transportation('bike', input_data[34], input_data[35], input_data[36], input_data[37],input_data[38])

    ''' list of candidate transportations'''
    # list to store possible transportations
    candidate_transportations = ["car", "walk", "bus", "uber", "train", "bike"]
    last_deleted_transportation = [""]
    
    '''create a set of rules based on excel'''
    # read rule data from excel files
    rule_data = pd.read_excel(r'rule_test.xlsx')
    rule_data = rule_data.where((pd.notnull(rule_data)), None)
    rule_data = rule_data.as_matrix() # matrix which has rule data 
    num_rules = 56 #NEEDS TO BE CHANGED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # create rule objects and distribute them accordingly 
    for i in range(0,num_rules):
        curr_rule = rule(rule_data[i][0], rule_data[i][1], rule_data[i][2], \
        rule_data[i][3], rule_data[i][4], rule_data[i][5], rule_data[i][6], \
        rule_data[i][7], rule_data[i][8], rule_data[i][9], rule_data[i][10], \
        rule_data[i][11], rule_data[i][12], rule_data[i][13], rule_data[i][14], \
        rule_data[i][15], rule_data[i][16], rule_data[i][17], rule_data[i][18], \
        rule_data[i][19], rule_data[i][20], rule_data[i][21], rule_data[i][22], \
        rule_data[i][23], rule_data[i][24], rule_data[i][25], rule_data[i][26], \
        rule_data[i][27], rule_data[i][28], rule_data[i][29], rule_data[i][30],\
        rule_data[i][31], rule_data[i][32], rule_data[i][33], rule_data[i][34], \
        rule_data[i][35], rule_data[i][36], rule_data[i][37], rule_data[i][38], rule_data[i][39], rule_data[i][40], \
        rule_data[i][41], rule_data[i][42], rule_data[i][43], rule_data[i][44], \
        rule_data[i][45], rule_data[i][46], rule_data[i][47], rule_data[i][48], \
        rule_data[i][49], rule_data[i][50], rule_data[i][51], rule_data[i][52], \
        rule_data[i][53], rule_data[i][54], rule_data[i][55], rule_data[i][56], \
        rule_data[i][57], rule_data[i][58], rule_data[i][59], rule_data[i][60], \
        rule_data[i][61], rule_data[i][62], rule_data[i][63], rule_data[i][64], rule_data[i][65], rule_data[i][66], \
        rule_data[i][67], rule_data[i][68], rule_data[i][69]) 
        distribute_rules(curr_rule, curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike)
    
    #print(len(curr_agent.rules), len(curr_env.rules), len(curr_journey.rules), len(car.rules))
    
    '''summary of pre-run status'''
    curr_explanation = explanation()
    curr_experience = experience(curr_agent, curr_env, curr_journey, None)
    print('current status is as follows \n{}'.format(curr_experience.str()))
    
    if is_use_habit(curr_habit, curr_agent, curr_env, curr_journey)[0] == True and\
     is_use_habit(curr_habit, curr_agent, curr_env, curr_journey)[1].accessability == 1 and \
     is_use_habit(curr_habit, curr_agent, curr_env, curr_journey)[1].availability == 1:
        curr_explanation.add_explanation("Habit is being used to decide the transportation.\n")
        print('habit is being used to decide the transportation')
    else:
        curr_explanation.add_explanation("Habit cannot be used since the current trip does not match to the previous trips. Thus, use the normal cognitive procedure to decide the transportation.\n")
        print('habit cannot be used, go to the normal cognitive procedure')
    
    '''use habit or fire rules in the appropriate order discussed in the report''' 
    if is_use_habit(curr_habit, curr_agent, curr_env, curr_journey)[0] == True and\
     is_use_habit(curr_habit, curr_agent, curr_env, curr_journey)[1].accessability == 1 and \
     is_use_habit(curr_habit, curr_agent, curr_env, curr_journey)[1].availability == 1: # case where the agent can reduce the cognitive load by using habit to decide
        result = is_use_habit(curr_habit, curr_agent, curr_env, curr_journey)[1]
        curr_explanation.add_explanation("Based on the habit, ")
    else: # case where habit does not work to decide the transportation so that the agent dive into the cognitive procedure
        curr_agent.fire_rules(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation)   #fire rules associated to agent
        #print('last_deleted_transporation = {}'.format(last_deleted_transportation))
        curr_journey.fire_rules(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation) #fire rules associated to journey
        #print('last_deleted_transporation = {}'.format(last_deleted_transportation))
        curr_env.fire_rules(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation)     #fire rules associated to env
        #print('last_deleted_transporation = {}'.format(last_deleted_transportation))
        car.fire_rules(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation)          #fire rules associated to car
        #print('last_deleted_transporation = {}'.format(last_deleted_transportation))
        walk.fire_rules(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation)         #fire rules associate to walk     
        #print('last_deleted_transporation = {}'.format(last_deleted_transportation))
        result = choose_best_transportation(candidate_transportations, last_deleted_transportation, car, walk, bus, uber, train, bike, curr_explanation) # function to choose best transporttaion from candidate_transportations list  
    
    '''output and store the experience in habit'''
    print('best transportation for this trip = {}'.format(result.name))
    curr_explanation.add_explanation("The agent chooses {} for the transportation for the trip!".format(result.name))
    curr_agent.emotion = "great"
    curr_experience = experience(curr_agent, curr_env, curr_journey, result)
    curr_habit.add_experience(curr_experience)
    
    #print(curr_explanation)
    
def main():
    '''Main function to be run'''
    # read input data from excel files
    input_data = pd.read_excel(r'input_test.xlsx')
    input_data = input_data.where((pd.notnull(input_data)), None)
    input_data = input_data.as_matrix() # matrix which has input data 
    num_input_data = 9 # NEEDSTO BE CHANGED

    # habit
    curr_habit = habit()
    for i in range(0, num_input_data):
        print('{}-th travel'.format(i+1))
        print(curr_habit)
        run(input_data[i], curr_habit)
        print('\n')

if __name__ == "__main__":
    main()
