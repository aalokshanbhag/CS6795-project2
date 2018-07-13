# CS6795-project2
Stimulation of human cognitive process to choose type of transportation in daily life

This file has 
 - __init__.py which is the first version of the source code
 - Rules.xlsx which contains the rules in excel sheet

Procedure\
1, install pandas package if not installed yet

2, run with the following command 
   python __init__.py

3, In the command, you can see the following questions.\
   Q1: Is bus available for you now? \
   -> input 1 for Yes and 0 for No.\
   Q2: Is bus accessible for you now?\
   -> input 1 for Yes and 0 for No.\
   Q3: How safe is using a bus for you? \
   -> input 0 for low, 1 for mid, 2 for high\
   Q4: Is car available for you now? \
   -> input 1 for Yes and 0 for No.\
   Q5: Is car accessible for you now?\
   -> input 1 for Yes and 0 for No.\
   Q6: How safe is using a car for you? \
   -> input 0 for low, 1 for mid, 2 for high\
   Q7: Is walk available for you now? \
   -> input 1 for Yes and 0 for No.\
   Q8: Is walk accessible for you now?\
   -> input 1 for Yes and 0 for No.\
   Q9: How safe is walking for you? \
   -> input 0 for low, 1 for mid, 2 for high\
   Q10: Is uber available for you now? \
   -> input 1 for Yes and 0 for No.\
   Q11: Is uber accessible for you now?\
   -> input 1 for Yes and 0 for No.\
   Q12: How safe is using a uber for you?\ 
   -> input 0 for low, 1 for mid, 2 for high\
   Q13: Is train available for you now? \
   -> input 1 for Yes and 0 for No.\
   Q14: Is train accessible for you now?\
   -> input 1 for Yes and 0 for No.\
   Q15: How safe is using a train for you?\ 
   -> input 0 for low, 1 for mid, 2 for high\
   Q16: Is bike available for you now? \
   -> input 1 for Yes and 0 for No.\
   Q17: Is bike accessible for you now?\
   -> input 1 for Yes and 0 for No.\
   Q18: How safe is using bike for you? 
   -> input 0 for low, 1 for mid, 2 for high\
   Q19: How is your health condition?\
   -> input 0 for low, 1 for mid, 2 for high\
   Q20: How is your financial condition? \
   -> input 0 for low, 1 for mid, 2 for high \
   Q21: Do you have a car?\
   -> input 0 for No, 1 for Yes\
   Q22: Do you have a bike? \
   -> input 0 for No, 1 for Yes\
   Q23: How is the weather now? \
   -> input 0 for bad, 1 for so so, 2 for good \
   Q24: How bad is the traffic?\
   -> input 0 for bad, 1 for so so, 2 for good\
   Q25: How far is your distination?\
   -> input 0 for close, 1 for midium, 2 for far away\
   Q26: How much time is available for you?\
   -> input 0 for short, 1 for mid, 2 for long\
   Q27: How urgent is this journey for you? \
   ->input 0 for No, 1 for just so so, 2 for yes\
  
   The example command line looks like \
   Is bus available for you now? (True, False) : 1\
   Is bus accessible for you now? (True, False) : 1\
   How safe is using a bus for you? (0 for low, 1 for mid, 2 for high) : 1\
   Is car available for you now? (True, False) : 1\
   Is car accessible for you now? (True, False) : 1\
   How safe is using a car for you? (0 for low, 1 for mid, 2 for high) : 1\
   Is walking available for you now? (True, False) : 1\
   Is walking accessible for you now? (True, False) : 1\
   How safe is walking for you? (0 for low, 1 for mid, 2 for high) : 1\
   Is uber available for you now? (True, False) : 1\
   Is uber accessible for you now? (True, False) : 1\
   How safe is uber for you? (0 for low, 1 for mid, 2 for high) : 1\
   Is train available for you now? (True, False) : 1\
   Is train accessible for you now? (True, False) : 1\
   How safe is train for you? (0 for low, 1 for mid, 2 for high) : 1\
   Is bike available for you now? (True, False) : 1\
   Is bike accessible for you now? (True, False) : 1\
   How safe is bike for you? (0 for low, 1 for mid, 2 for high) : 1\
   How is your health condition? (0 for low, 1 for mid, 2 for high) : 2\
   How is your financial condition? (0 for low, 1 for mid, 2 for high) : 0\
   Do you have a car? (0 for No, 1 for Yes) : 0\
   Do you have a bike? (0 for No, 1 for Yes) : 1\
   How is the weather now? (0 for bad, 1 for so so, 2 for good) : 2\
   How bad is the traffic? (0 for bad, 1 for so so, 2 for good) : 2\
   How far is your distination? (0 for close, 1 for midium, 2 for far away) : 0\
   How much time is available for you? (0 for short, 1 for mid, 2 for long) : 2\
   How urgent is this journey for you? (0 for No, 1 for just so so, 2 for yes) : 0\

4, Your command shows which rules are fired.\

   The example command line with the example input above is as follows.\
   Rule 4 fired now in priority queue\
   Rule 2 fired now in priority queue\
   Rule 8 fired now in priority queue\
   
5, Then your command shows the result which type of transportation you may choose which is either "car", "bus", "walk", "uber", "train", or "bike".

Note
Python3.4.2 is used for this project.
Git hub repository is "https://github.com/kameturtle/CS6795-project2"
