#Trivia Quiz
print("This is a quiz that tests your knowlegde on SOF")
name= input("Enter your name :")
print("Hello", name, "Are you ready to start the quiz?")

print("I will ask you 5 questions and give you three different choices")
print("Select which choice is best for each question, A,B, or C")
print("____________________________")

#set the score of the quiz to 0
score=0
score= int(score)

#Question 1
print("Question 1: Who is the highschool principle?")

print("A. Stacy")
print("B. Fanning")
print("C. Regis")
print("")

Q1_answer="B" #the right answer to question 1
Q1_response= input("Your answer: ")

if Q1_response== "B" or Q1_response=="b":
    print("Correct answer",Q1_response)
    score= score + 1
    print("your current score is", score, "out of 5")
elif Q1_response != "B" or Q1_response != "b":
    print("sorry, incorrect")
    print("Your currect score is", score, "out of 5")
print("______________________________")
#Question 2
print("Question 2: Who is the college counselor?")
print("A. Regis")
print("B. Ms. Robinson")
print("C. Felix")
print("")

Q2_answer= "C" #the right answer to question 2
Q2_response= input("Your answer :")

if Q2_response== "C" or Q2_response== "c":
    print("Correct answer", Q2_answer)
    score= score +1
    print("Your current score is", score, "out of 5")
elif Q2_response != "C" or Q2_response != "c":
    print("sorry, incorrect")
    print("Your currect score is", score, "out of 5")
print("______________________________")
#Question 3
print("Question 3: Who gets kicked out of the elevator?")
print("A. Seniors")
print("B. teachers")
print("C. middle schoolers/freshman")
print("")

Q3_answer= "C" #the right answer to Question 3
Q3_response= input("Your answer: ")

if Q3_response== "C" or Q3_response== "c":
    print("Correct answer", Q3_answer)
    score= score +1
    print("Your current score is", score, "out of 5")
elif Q3_response != "C" or Q3_response!="c":
    print("sorry, incorrect")
    print("Your current score is", score, "out of 5")
print("______________________________")
#Question 4
print("Question 4: Whats the class motto?")
print("A. No man gets left behind")
print("B. A grade that cheats together, passes together")
print("C. hit the steps")
print("")

Q4_answer= "B"
Q4_response= input("Your answer")

if Q4_response== "B" or Q4_response== "b":
    print("Correct answer", Q4_answer)
    score= score +1
    print("Your current score is", score, "out of 5")
elif Q4_response != "B" or Q4_response != "b":
    print("Sorry, incorrect")
    print("Your current score is", score, "out of 5")
print("______________________________")
#Question 5
print("Question 5: Who's the G.O.A.T of SOF?")
print("A. Regis Enama")
print("B. Regis Enama")
print("C. Regis Enama")
print("")

Q5_answer= "Regis Enama"
Q5_response= input("Your answer")

if Q5_response== "A" or Q5_response== "a" or Q5_response== "B" or Q5_response== "b" or Q5_response== "C" or Q5_response== "c":
    print("Correct answer", Q5_answer)
    score= score +1
    print("Your current score is", score, "out of 5")

elif Q5_response !="A" or Q5_response != "a" or Q5_response != "B" or Q5_response != "b" or Q5_response != "C" or Q5_response != "c":
    print("Sorry, incorrect" )
    print("Your current score is", score, "out of 5")
print("______________________________")          
#Percent score
print("Congratulation, you finished the quiz")
final_score= (score*100)/5
print("Your final score is", final_score, "Percent")
if final_score <= 20:
    print("You are an SOF loser....Loser")
if final_score== 40:
    print("SOF Amature")
if final_score== 60:
    print("Freshman")
if final_score== 80:
    print("You were so close")
if final_score== 100:
    print("You feen") 


    


    
  

