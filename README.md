# CS6795-project2
Stimulation of human cognitive process to choose type of transportation in daily life

This file has 
 - __init__.py which is the first version of the source code
 - Rules.xlsx which contains the rules in excel sheet

Procedure
1, install pandas package if not installed yet

2, run with the following command 
   python __init__.py

3, In the command, you can see the following questions.
   Is bus available for you now? 
   -> input 1 for Yes and 0 for No.
   
    bus_q2 = input('Is bus accessible for you now? (True, False) : ')
    bus_q3 = input('How safe is using a bus for you? (0 for low, 1 for mid, 2 for high) : ')
    bus = transportation("bus", 1, 1, int(bus_q1), int(bus_q2), int(bus_q3))
    
    # create bus object
    car_q1 = input('Is car available for you now? (True, False) : ')
    car_q2 = input('Is car accessible for you now? (True, False) : ')
    car_q3 = input('How safe is using a car for you? (0 for low, 1 for mid, 2 for high) : ')
    car = transportation('car', 2, 2, int(car_q1), int(car_q2), int(car_q3))
    
    # create walk object
    walk_q1 = input('Is walking available for you now? (True, False) : ')
    walk_q2 = input('Is walking accessible for you now? (True, False) : ')
    walk_q3 = input('How safe is walking for you? (0 for low, 1 for mid, 2 for high) : ')
    walk = transportation('walk', 2, 2, int(walk_q1), int(walk_q2), int(walk_q3))
    
    # create uber object
    uber_q1 = input('Is uber available for you now? (True, False) : ')
    uber_q2 = input('Is uber accessible for you now? (True, False) : ')
    uber_q3 = input('How safe is uber for you? (0 for low, 1 for mid, 2 for high) : ')
    uber = transportation('uber', 2, 2, int(uber_q1), int(uber_q2), int(uber_q3))
    
    # create train object
    train_q1 = input('Is train available for you now? (True, False) : ')
    train_q2 = input('Is train accessible for you now? (True, False) : ')
    train_q3 = input('How safe is train for you? (0 for low, 1 for mid, 2 for high) : ')
    train = transportation('train', 2, 2, int(train_q1), int(train_q2), int(train_q3))
    
    # create bike object
    bike_q1 = input('Is bike available for you now? (True, False) : ')
    bike_q2 = input('Is bike accessible for you now? (True, False) : ')
    bike_q3 = input('How safe is bike for you? (0 for low, 1 for mid, 2 for high) : ')
    bike = transportation('bike', 2, 2, int(bike_q1), int(bike_q2), int(bike_q3))
    
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
   q1. Does the article have a bias? (yes, no, cantSay) :
     -> answer either yes, no, cantSay (no need to put " ")
   q2. Which comments did you read? (all, sortedByLikes, sampledBothSidesOfArgument, unsorted, never) :
     -> answer either all, sortedByLikes, sampledBothSidesOfArgument, unsorted, never (no need to put " ")
   q3. Are the comments offensive? (notAtAll, little, neutral, quite, very) :
     -> answer either notAtAll, little, neutral, quite, very (no need to put " ")
   q4. Which way is the comment section leaning (stronglyAgainstYou, againstYou, neutral, withYou, stronglyWithYou) :
     -> answer either stronglyAgainstYou, againstYou, neutral, withYou, stronglyWithYou (no need to put " ")
   q5. Are the comments well reasoned ? (notAtAll, little, neutral, quite, very) :
     -> answer either notAtAll, little, neutral, quite, very (no need to put " ")
   opinion :
     -> answer -2 if totallyDisagree, -1 if disagree, 0 if neutral(0), 1 if agree, 2 if  totallyAgree
   input confidence_level :
     -> answer 0 if low, 1 if mid, 2 if high
   input attention_level :
     -> answer 0 if low, 1 if mid, 2 if high
   input interest_level :
     -> answer 0 if low, 1 if mid, 2 if high

   The example command line looks like 
    q1. Does the article have a bias? (yes, no, cantSay) : no
    q2. Which comments did you read? (all, sortedByLikes, sampledBothSidesOfArgument, unsorted, never) : all
    q3. Are the comments offensive? (notAtAll, little, neutral, quite, very) : notAtAll
    q4. Which way is the comment section leaning (stronglyAgainstYou, againstYou, neutral, withYou, stronglyWithYou) : stronglyAgainstYou
    q5. Are the comments well reasoned ? (notAtAll, little, neutral, quite, very) : very
    q6. input opinion : 2
    q7. input confidence_level : 1
    q8. input attention_level : 2
    q9. input interest_level : 2

4, Your command shows the result which is either "Opinion Changed!" or "Stick to the original opinion..." along with detail information about rules fired.

Note
Python3.4.2 is used for this project.
Git hub repository is "https://github.com/kameturtle/CS6795-project1.git"
As a first step, we develop a decision tree. But until the 2nd version submission, we change the code in such a way that it execute rules as actual human brain does.
