# CS6795-project2
Stimulation of human cognitive process to choose type of transportation in daily life

This file has 
 - prev_ver_scr which contains previous versions of sourse codes
 - __init__.py which is the final version of the source code
 - Rules.xlsx which contains the rules in excel sheet

Procedure
1, install pandas package if not installed yet

2, run with the following command 
   python __init__.py

3, In the command, you can see the following 9 questions.
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
