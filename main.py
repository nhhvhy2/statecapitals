import random
import os

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',                      
   'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus',      
   'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',                              
   'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
  'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

def Generate():
  try:                                # Create Directories for Quizzes and Keys
    os.makedirs("Answer Keys")
    os.makedirs("Quizzes")
  except:                             # Ignore if directories already exist 
    pass
  
  for formNum in range(35):
   form = open("Quizzes/QuizForm"+str(formNum + 1)+".txt", mode="w")
   key = open("Answer Keys/AnswerKey"+str(formNum + 1)+".txt", mode ="w")
   randStates = list(capitals.keys())
   random.shuffle(randStates)

   form.write("Name:\n\nDate:\n\nPeriod:\n\n\n")
    
   for question in range(50):
     state = randStates[question]
     answers = []
     correct = capitals[randStates[question]]
     correctpos = random.randint(0,3)

     while len(answers) < 3:
       answers.append(capitals[randStates[random.randint(0,49)]])
     answers.insert(correctpos, correct)
     
     form.write(str((question+1))+". What is the capital of "+state+"?\nA: "+str(answers[0])+"\nB: "+str(answers[1])+"\nC: "+str(answers[2])+"\nD: "+str(answers[3])+"\n\n")

     key.write(str((question+1))+": "+str('ABCD'[answers.index(correct)])+"\n")

Generate()

#35 ITERATIONS:
#1. Create quiz and answer key files
#2. Write Header to quiz and answer key files
#3. Create randomized capital order using random.shuffle()
#4.  50 ITERATIONS:
#       Write "What is the capital of _____?"
#       Write correct answer to A, B, C, or D at random
#       Write correct answer to answer key
#       Fill remaining answers with incorrect solutions