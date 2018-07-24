# -*- coding: utf-8 -*-
import sys
import queue as queue
import pandas as pd
import random
import operator


class agent:
    '''This class is for an agent's state'''
    def __init__(self, _health_level, _finance_level, _preference):
        self.health_level = _health_level # low(0), mid(1), high(2)
        self.finance_level = _finance_level # low(0), mid(1), high(2)
        self.preference = _preference # "cost", "safety"
        self.emotion = "great" # "great", "ok", "horrible"
        self.num_think = 1
        self.rules = []

    def fire_rules(self, curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation):
        ##print('agent rules firing')
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
        self.weather = _weather # normal(0), slightly bad(1), extremely bad(2) *bad means you travel in a bad weather like rainy
        self.isRushHour = _isRushHour # No(0), Yes(1) whether now is in rush hour or not 
        self.isNight = _isNight # No(0), Yes(1) whether now is night or not 
        self.rules = []

    def fire_rules(self, curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation):
        ##print('env rules firing')
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
        ##print('journey rules firing')
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
        ##print('{} rules firing'.format(self.name))
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
    _car_eliminate, _walk_eliminate, _bus_eliminate, _uber_eliminate, _train_eliminate, _bike_eliminate, _location_to_be_fired, _human_language):
        
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
        self.human_language = _human_language
        
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
        curr_explanation.add_explanation(' - Rule {} is fired, which is {}. \n'.format(self.ID, self.human_language))
        ##print(' - rule {} is fired, which is "{}"'.format(self.ID, self.human_language))
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
            ##print('  - delete car from the list')
            eliminate_transportation("car", candidate_transportations)
            last_deleted_transportation[0] = "car"
        if self.walk_eliminate == 1:
            ##print('  - delete walk from the list')
            eliminate_transportation("walk", candidate_transportations)
            last_deleted_transportation[0] = "walk"
        if self.bus_eliminate == 1:
            ##print('  - delete bus from the list')
            eliminate_transportation("bus", candidate_transportations)
            last_deleted_transportation[0] = "bus"
        if self.uber_eliminate == 1:
            ##print('  - delete uber from the list')
            eliminate_transportation("uber", candidate_transportations)
            last_deleted_transportation[0] = "uber"
        if self.train_eliminate == 1:
            ##print('  - delete train from the list')
            eliminate_transportation("train", candidate_transportations)
            last_deleted_transportation[0] = "train"
        if self.bike_eliminate == 1:
            ##print('  - delete bike from the list')
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
        res = " - "
        if self.health_level != 2:
            res += "The agent is not sick and "
        else:
            res += "the agent is sick and "
        if self.weather != 2:
            res += 'the weather is not extremely bad and '
        else:
            res += 'the weather is extremely bad and '
        if self.isRushHour!= 1:
            res +='now is not in rush hour, '
        else:
            res +='now is in rush hour, '
        if self.isNight!= 1:
            res +='now is not at night, '
        else:
            res +='now is at night, '  
        if self.time_available != 0:
            res +='the agent has a lot of time to get a destination, '
        else:
            res +='the agent does not have a lot of time to get a destination, '
        if self.importance_level != 2:
            res +='the trip is really not really in a hurry, '
        else:
            res +='the agent is really in a hurry, '
        if self.emotion != "horrible":
            res +='the agents posttrip emotion is great, '
        else:
            res +='the agents posttrip emotion is horrible, '
        if self.result != None:
            res += 'Then the agent uses {} for the trip! \n'.format(self.result.name)
        else:
            res += '\n'
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
    
    def __eq__(self, other):
        if (self.health_level == other.health_level or (self.health_level != 2 and other.health_level != 2)) and \
        (self.weather == other.weather or (self.weather != 2 and other.weather != 2)) and \
        self.isRushHour == other.isRushHour and self.isNight == other.isNight and \
        (self.time_available == other.time_available or (self.time_available != 2 and other.time_available != 2)) and\
        (self.importance_level == other.importance_level or (self.importance_level != 2 and other.importance_level != 2)):
            return True
        return False
    
class habit:
    def __init__(self):
        self.experiences = []  
    def add_experience(self, experience):
        self.experiences.append(experience)
    def extract(self):
        curr_total = 0
        extracted_habit ={} #dictionary storing[‘habit_i’: experience obj, number of appearance]
        count_typeOfOption = {}
        for curr_exp in self.experiences:
            is_curr_exp_found = False
            for key in extracted_habit:
                if extracted_habit[key][0] == curr_exp:
                    if curr_exp.emotion == 'horrible':
                        extracted_habit[key][1] -= 999
                    if curr_exp.result.name in count_typeOfOption['habit_{}'.format(curr_total-1)]:
                        count_typeOfOption['habit_{}'.format(curr_total-1)][curr_exp.result.name] += 1
                    else:
                        count_typeOfOption['habit_{}'.format(curr_total-1)][curr_exp.result.name] = 1
                    #return the name of transportation with highest appearence among one habit
                    resultTransportation = max(count_typeOfOption['habit_{}'.format(curr_total-1)].items(), key=operator.itemgetter(1))[0]
                    curr_exp.result.name = resultTransportation
                    extracted_habit[key][0] = curr_exp
                    extracted_habit[key][1] += 1
                    is_curr_exp_found = True
            if is_curr_exp_found == False:
                extracted_habit['habit_{}'.format(curr_total)] = [curr_exp, 1]
                count_typeOfOption['habit_{}'.format(curr_total)] = {}
                count_typeOfOption['habit_{}'.format(curr_total)][curr_exp.result.name] = 1
                curr_total += 1
    
        res = 'Habits from the experiences are as follows.\n'        
        for key in extracted_habit:
            if extracted_habit[key][1] > 3:
                res += ' - {} is If '.format(key,)
                curr_habit = extracted_habit[key][0]
                if curr_habit.health_level != 2:
                    res +='the agent is not sick and, '
                else:
                    res +='the agent is sick and, '
                if curr_habit.weather != 2:
                    res +='the weather is not extremely bad and, '
                else:
                    res +='the weather is extremely bad and, '  
                if curr_habit.isRushHour!= 1:
                    res +='now is not in rush hour, '
                else:
                    res +='now is in rush hour, '
                if curr_habit.isNight!= 1:
                    res +='now is not at night, '
                else:
                    res +='now is at night, '  
                if curr_habit.time_available != 0:
                    res +='the agent has a lot of time to get a destination, '
                else:
                    res +='the agent does not have a lot of time to get a destination, '
                if curr_habit.importance_level != 2:
                    res +='the trip is really not really in a hurry, '
                else:
                    res +='the agent is really in a hurry, '
                if curr_habit.emotion != "horrible":
                    res +='the agents posttrip emotion is great, '
                else:
                    res +='the agents posttrip emotion is horrible, '
                res += 'Then the agent uses {} for the trip! \n'.format(curr_habit.result.name)

        return res
        
    def str(self):
        print_return = 'Current experiences are as folllows \n'
        for curr_exp in self.experiences:
            print_return += curr_exp.str()
        return print_return
        
    def __str__(self):
        print_return = 'Current experiences are as folllows \n'
        for curr_exp in self.experiences:
            print_return += curr_exp.str()
        return print_return
        
class explanation:
    def __init__(self):
        self.explanations = []
    def add_explanation(self, curr_explanation):
        self.explanations.append(curr_explanation)
    def __str__(self):
        print_res = "The agent decides the best transportation among car, walk, bus, uber, train, bike for the trip in the following way.\n"
        for curr_explanation in self.explanations:
            print_res += curr_explanation
        return print_res
    def write_explantion(self):
        print_res = "The agent decides the best transportation among car, walk, bus, uber, train, bike for the trip in the following way.\n"
        for curr_explanation in self.explanations:
            print_res += curr_explanation
        return print_res

def eliminate_transportation(transportation_name, candidate_transportations):
    '''This is the fuction to remove a transportation from the candidate_transportations list'''
    # transporatation_name is the name of the transportation you want to remove from the candidate list
    for curr_can in candidate_transportations:
        if curr_can == transportation_name:
            candidate_transportations.remove(curr_can)

def call_transportation_object_from_string(transportation_name, car, walk, bus, uber, train, bike):
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

def choose_best_transportation(input_data, curr_habit, curr_agent, candidate_transportations, last_deleted_transportation, car, walk, bus, uber, train, bike, curr_explanation):
    '''choose the best transportation among candidate_transportation list and store this trip as one experience into habit''' 
    transportation_name = ""
    if len(candidate_transportations) >= 2: 
        # case where there are more than one transportation objects in candidate_transportation list
        # choose one transportation from multiple based on the agent's preference
        result = call_transportation_object_from_string(candidate_transportations[0], car, walk, bus, uber, train, bike)
        if curr_agent.preference == "cost":
            ##print("As there are still more than one transportation left in candidate_transportations list, the agent chooses one transportation with lowest cost from the list since agent current preference is cost.")
            curr_explanation.add_explanation("As there are still more than one transportation left in candidate_transportations list, the agent chooses one transportation with lowest cost from the list since agent current preference is cost.\n")
            for curr_candidate_transporation in candidate_transportations:
                if call_transportation_object_from_string(curr_candidate_transporation, car, walk, bus, uber, train, bike).price < result.price:
                    result = call_transportation_object_from_string(curr_candidate_transporation, car, walk, bus, uber, train, bike)
            return result
        else:
            ##print("As there are still more than one transportation left in candidate_transportations list, the agent chooses one transportation with highest safety from the list since agent current preference is safety.")
            curr_explanation.add_explanation("As there are still more than one transportation left in candidate_transportations list, the agent chooses one transportation with highest safety from the list since agent current preference is safety.\n")
            for curr_candidate_transporation in candidate_transportations:
                if call_transportation_object_from_string(curr_candidate_transporation, car, walk, bus, uber, train, bike).safety > result.safety:
                    result = call_transportation_object_from_string(curr_candidate_transporation, car, walk, bus, uber, train, bike)
            return result
    elif len(candidate_transportations) == 0: 
        # case where there is no transportation object in candidate_transportation list
        if curr_agent.num_think == 1:
            ##print("The agent think once but still does not get best transportation. Then the agent decides to loose conditions so that the agent is more willing to pay trasnportation fee and does not consider how tired the agent is to make sure s/he can decide best transportation in the next round.") 
            curr_explanation.add_explanation("The agent think once but still does not get best transportation. Then the agent decides to loose conditions so that the agent is more willing to pay trasnportation fee and does not consider how tired the agent is to make sure s/he can decide best transportation in the next round.\n") 
            return think_twice(input_data, curr_habit, curr_explanation)
        else:
            ##print("The agent thinks twice but still does not get best transportation. So the agent chooses a transportation which was deleted last from candidate_transportation list while firing rules.")
            curr_explanation.add_explanation("The agent thinks twice but still does not get best transportation. So the agent chooses a transportation which was deleted last from candidate_transportation list while firing rules.\n")
            transportation_name = last_deleted_transportation[0]
            return call_transportation_object_from_string(transportation_name, car, walk, bus, uber, train, bike)
    else:
        # case where there is only one transportation object left in candidate_transportations list
        ##print("The agent chooses one trasportation left in candidate_transportations list.")
        curr_explanation.add_explanation("The agent chooses one trasportation left in candidate_transportations list. \n")
        return call_transportation_object_from_string(candidate_transportations[0], car, walk, bus, uber, train, bike)
    
    

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
        if (experience.health_level == curr_agent.health_level or (experience.health_level != 2 and curr_agent.health_level != 2)) and \
        (experience.weather == curr_env.weather or (experience.weather != 2 and curr_env.weather != 2)) and \
        experience.isRushHour == curr_env.isRushHour and experience.isNight == curr_env.isNight and \
        (experience.time_available == curr_journey.time_available or (experience.time_available != 2 and curr_journey.time_available != 2)) and\
        (experience.importance_level == curr_journey.importance_level or (experience.importance_level != 2 and curr_journey.importance_level != 2)):
            if experience.emotion == "horrible": # case where agent re-consider the transportation because of horrible experience
                ##print("Because of the previous bad experience, emotion state for the agent becomes horrible so that the agent cannot use habit!!! \n ")
                return False, None
            count += 1
            habituated_transportation = experience.result
    if count > 4:
        return True, habituated_transportation
    return False, None      

def run(input_data, curr_habit, text_file):
    '''create non-rule objects''' 
    # create agent object
    curr_agent = agent(input_data[1], input_data[2], input_data[3])
    # create environment object
    curr_env = env(input_data[4], input_data[5], input_data[6])
    # create journey object
    curr_journey = journey(input_data[7], input_data[8], input_data[9])

    # create transportation objects
    car = transportation('car', input_data[10], input_data[11], input_data[12], input_data[13], input_data[14])
    walk = transportation('walk', input_data[15], input_data[16], input_data[17], input_data[18],input_data[19])
    bus = transportation('bus', input_data[20], input_data[21], input_data[22], input_data[23],input_data[24])
    uber = transportation('uber', input_data[25], input_data[26], input_data[27], input_data[28],input_data[29])
    train = transportation('train', input_data[30], input_data[31], input_data[32], input_data[33],input_data[34])
    bike = transportation('bike', input_data[35], input_data[36], input_data[37], input_data[38],input_data[39])

    ''' list of candidate transportations'''
    # list to store possible transportations
    candidate_transportations = ["car", "walk", "bus", "uber", "train", "bike"]
    last_deleted_transportation = [""]
    
    '''create a set of rules based on excel'''
    # read rule data from excel files
    rule_data = pd.read_excel(r'rule_test.xlsx')
    rule_data = rule_data.where((pd.notnull(rule_data)), None)
    rule_data = rule_data.as_matrix() # matrix which has rule data 
    num_rules = 50 #NEEDS TO BE CHANGED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

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
        rule_data[i][67], rule_data[i][68], rule_data[i][69], rule_data[i][70]) 
        distribute_rules(curr_rule, curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike)
    
    #print(len(curr_agent.rules), len(curr_env.rules), len(curr_journey.rules), len(car.rules))
    
    '''summary of pre-run status'''
    curr_explanation = explanation()
    curr_explanation.add_explanation(curr_habit.extract())
    curr_experience = experience(curr_agent, curr_env, curr_journey, None)
    ##print('\n Summary of states in this upcoming trip is as follows \n{}'.format(curr_experience.str()))
    curr_explanation.add_explanation('Summary of states in this upcoming trip is as follows \n{}'.format(curr_experience.str()))
    if is_use_habit(curr_habit, curr_agent, curr_env, curr_journey)[0] == True and\
     is_use_habit(curr_habit, curr_agent, curr_env, curr_journey)[1].accessability == 1 and \
     is_use_habit(curr_habit, curr_agent, curr_env, curr_journey)[1].availability == 1:
        curr_explanation.add_explanation("Habit is being used to decide the transportation since the states in this upcoming trip match to one of the habits above.\n")
        ##print('Habit is being used to decide the transportation.\n')
    else:
        curr_explanation.add_explanation("Habit cannot be used since the current trip characteristics does not match to any habit. Thus, the agent uses the normal cognitive procedure to decide the transportation.\n")
        ##print('Habit cannot be used. Thus, the agent uses the normal cognitive procedure to decide the transportation.\n')
    
    '''use habit or fire rules in the appropriate order discussed in the report''' 
    if is_use_habit(curr_habit, curr_agent, curr_env, curr_journey)[0] == True and\
     is_use_habit(curr_habit, curr_agent, curr_env, curr_journey)[1].accessability == 1 and \
     is_use_habit(curr_habit, curr_agent, curr_env, curr_journey)[1].availability == 1: # case where the agent can reduce the cognitive load by using habit to decide
        result = is_use_habit(curr_habit, curr_agent, curr_env, curr_journey)[1]
        curr_explanation.add_explanation("Based on the habit, ")
    else: # case where habit does not work to decide the transportation so that the agent dive into the cognitive procedure
        curr_explanation.add_explanation("As found through the literature reviews and interviews, rules associated with agent schema are fired first. rules associated with journey schema, environment schema,j transporation schema follows.\n")
        curr_agent.fire_rules(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation)   #fire rules associated to agent
        curr_journey.fire_rules(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation) #fire rules associated to journey
        curr_env.fire_rules(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation)     #fire rules associated to env
        car.fire_rules(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation)          #fire rules associated to car
        walk.fire_rules(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation)         #fire rules associate to walk     
        bus.fire_rules(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation)          #fire rules associate to bus 
        uber.fire_rules(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation)         #fire rules associate to uber 
        train.fire_rules(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation)        #fire rules associate to train 
        bike.fire_rules(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation)         #fire rules associate to bike 
        #print('last_deleted_transporation = {}'.format(last_deleted_transportation))
        
        result = choose_best_transportation(input_data, curr_habit, curr_agent, candidate_transportations, last_deleted_transportation, car, walk, bus, uber, train, bike, curr_explanation) # function to choose best transporttaion from candidate_transportations list  
    
    '''output and store the experience in habit'''
    print('Best transportation for this trip = {}'.format(result.name))
    curr_explanation.add_explanation("The agent chooses {} for the transportation for the trip!".format(result.name))
    
    ''' assign post-trip emotion as output for this trip'''
    curr_agent.emotion = "great"
    if random.randint(0,10) == 0:
        curr_agent.emotion = "horrible"
    
    '''store the new experience into list of experience in habit class (object)'''
    curr_experience = experience(curr_agent, curr_env, curr_journey, result)
    curr_habit.add_experience(curr_experience)
    
    '''print explanation into .txt file'''
    #print("--------------")
    text_file.write(curr_explanation.write_explantion())
    #final_explanation += curr_explanation.write_explantion()
    #print(curr_explanation)
    
    
def think_twice(input_data, curr_habit, curr_explanation):
    '''create non-rule objects''' 
    # create agent object
    curr_agent = agent(0, 2, 2)
    # create environment object
    curr_env = env(input_data[4], input_data[5], input_data[6])
    # create journey object
    curr_journey = journey(input_data[7], input_data[8], input_data[9])

    # create transportation objects
    car = transportation('car', input_data[10], input_data[11], input_data[12], input_data[13], input_data[14])
    walk = transportation('walk', input_data[15], input_data[16], input_data[17], input_data[18],input_data[19])
    bus = transportation('bus', input_data[20], input_data[21], input_data[22], input_data[23],input_data[24])
    uber = transportation('uber', input_data[25], input_data[26], input_data[27], input_data[28],input_data[29])
    train = transportation('train', input_data[30], input_data[31], input_data[32], input_data[33],input_data[34])
    bike = transportation('bike', input_data[35], input_data[36], input_data[37], input_data[38],input_data[39])

    ''' list of candidate transportations'''
    # list to store possible transportations
    candidate_transportations = ["car", "walk", "bus", "uber", "train", "bike"]
    last_deleted_transportation = [""]
    
    '''create a set of rules based on excel'''
    # read rule data from excel files
    rule_data = pd.read_excel(r'rule_test.xlsx')
    rule_data = rule_data.where((pd.notnull(rule_data)), None)
    rule_data = rule_data.as_matrix() # matrix which has rule data 
    num_rules = 50 #NEEDS TO BE CHANGED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

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
        rule_data[i][67], rule_data[i][68], rule_data[i][69], rule_data[i][70]) 
        distribute_rules(curr_rule, curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike)
    
    #print(len(curr_agent.rules), len(curr_env.rules), len(curr_journey.rules), len(car.rules))
    
    '''summary of pre-run status'''
    curr_experience = experience(curr_agent, curr_env, curr_journey, None)
    ##print('Summary of states in this upcoming trip is as follows \n{}'.format(curr_experience.str()))
    
    if is_use_habit(curr_habit, curr_agent, curr_env, curr_journey)[0] == True and\
     is_use_habit(curr_habit, curr_agent, curr_env, curr_journey)[1].accessability == 1 and \
     is_use_habit(curr_habit, curr_agent, curr_env, curr_journey)[1].availability == 1:
        curr_explanation.add_explanation("Habit is being used to decide the transportation.\n")
        ##print('Habit is being used to decide the transportation.\n')
    else:
        curr_explanation.add_explanation("Habit cannot be used since the current trip does not match to the previous trips. Thus, the agent uses the normal cognitive procedure to decide the transportation.\n")
        ##print('Habit cannot be used. Thus, the agent uses the normal cognitive procedure to decide the transportation.\n')
    
    '''use habit or fire rules in the appropriate order discussed in the report''' 
    if is_use_habit(curr_habit, curr_agent, curr_env, curr_journey)[0] == True and\
     is_use_habit(curr_habit, curr_agent, curr_env, curr_journey)[1].accessability == 1 and \
     is_use_habit(curr_habit, curr_agent, curr_env, curr_journey)[1].availability == 1: # case where the agent can reduce the cognitive load by using habit to decide
        result = is_use_habit(curr_habit, curr_agent, curr_env, curr_journey)[1]
        curr_explanation.add_explanation("Based on the habit, ")
    else: # case where habit does not work to decide the transportation so that the agent dive into the cognitive procedure
        curr_agent.fire_rules(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation)   #fire rules associated to agent
        curr_journey.fire_rules(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation) #fire rules associated to journey
        curr_env.fire_rules(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation)     #fire rules associated to env
        car.fire_rules(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation)          #fire rules associated to car
        walk.fire_rules(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation)         #fire rules associate to walk     
        bus.fire_rules(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation)          #fire rules associate to bus 
        uber.fire_rules(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation)         #fire rules associate to uber 
        train.fire_rules(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation)        #fire rules associate to train 
        bike.fire_rules(curr_agent, curr_env, curr_journey, car, walk, bus, uber, train, bike, candidate_transportations, last_deleted_transportation, curr_explanation)         #fire rules associate to bike 
        #print('last_deleted_transporation = {}'.format(last_deleted_transportation))
        
        result = choose_best_transportation(input_data, curr_habit, curr_agent, candidate_transportations, last_deleted_transportation, car, walk, bus, uber, train, bike, curr_explanation) # function to choose best transporttaion from candidate_transportations list  
    
    '''output and store the experience in habit'''
    ##print('Best transportation for this trip = {}'.format(result.name))
    curr_explanation.add_explanation("The agent chooses {} for the transportation for the trip!".format(result.name))
    
    return result

    
    
    
def main():
    '''Main function to be run'''
    # read input data from excel files
    input_data = pd.read_excel(r'input_modified.xlsx')
    input_data = input_data.where((pd.notnull(input_data)), None)
    input_data = input_data.as_matrix() # matrix which has input data 
    num_input_data = 47 # 47 NEEDSTO BE CHANGED

    # habit
    curr_habit = habit()
    text_file = open("Output.txt", "w")
    for i in range(0, num_input_data):
        text_file.write('{}-th travel \n'.format(i+1))
        print('{}-th travel'.format(i+1))
        #print(curr_habit)
        ##print(curr_habit.extract())
        run(input_data[i], curr_habit, text_file)
        text_file.write('\n \n')
        print('\n')

    text_file.close()

if __name__ == "__main__":
    main()
