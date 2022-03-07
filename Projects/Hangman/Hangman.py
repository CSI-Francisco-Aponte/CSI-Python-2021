#This allows the program to pick something at random. In this program, it is to hoose a random municipality.
import random

# Every step in the hangman, in the program, every time the user guesses an incorrect letter, the steps replace eachother +1, until reaching the last one which is when the user loses.
hang_man = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''

   +---+
   O   |
   |   |
       |
      ===''', '''

   +---+
   O   |
  /|   |
       |
      ===''', '''

   +---+
   O   |
  /|\  |
       |
      ===''', '''

   +---+
   O   |
  /|\  |
  /    |
      ===''', '''

   +---+
   O   |
  /|\  |
  / \  |
      ===''']


#Here there is a list of all the letter that the user can use to guess the municipality, and a place for the programs to print all the letters the user has already submitted.
LettersSubmitted = []
EligibleLetters = ["A" , "B", "C","D","E","F","G","H","I", "J","K", "L", "M", "N", "O", "P", "Q", "R","S","T","U", "V", "W", "X", "Y", "Z"]

# Here a random municipality is chosen using the import mentioned before
def random_pueblo():
   pueblos = ["Adjuntas", "Aguada", "Aguadilla", "Aguas Buenas", "Aibonito", "Arecibo", "Arroyo", "Anasco", "Barceloneta",  "Barranquitas",  "Bayamon",  "Cabo Rojo" , "Caguas",  "Camuy",  "Canovanas",  "Carolina",  "Catano",  "Cayey",  "Ceiba",  "Ciales",  "Cidra",  "Coamo",  "Comerio",  "Corozal",  "Culebra",  "Dorado",  "Fajardo",  "Florida",  "Guayama",  "Guayanilla",  "Guaynabo",  "Gurabo",  "Guanica",  "Hatillo",  "Hormigueros",  "Humacao",  "Isabela",  "Jayuya",  "Juana Diaz" , "Juncos",  "Lajas",  "Lares",  "Las Marias" , "Las Piedras" , "Loiza",  "Luquillo",  "Manati",  "Maricao",  "Maunabo",  "Mayaguez",  "Moca",  "Morovis",  "Naguabo",  "Naranjito",  "Orocovis",  "Patillas",  "Penuelas",  "Ponce",  "Quebradillas",  "Rincon",  "Rio Grande" , "Sabana Grande", "Salinas",  "San German" , "San Juan" , "San Lorenzo" "San Sebastiaan" , "Santa Isabel" , "Toa Alta" , "Toa Baja", "Trujillo Alto" , "Utuado",  "Vega Alta" , "Vega Baja" , "Vieques",  "Villalba",  "Yabucoa",  "Yauco"]
   answer = random.choice(pueblos).upper()
   return answer

# Here the function that receives the input is defined. This function serves to check if the letter submitted by the user is in the word, or is ineligble.
def getInput():

#Here the program allows the user to submit a letter to guess the word
   while(True):
      letter = input("Chose letter, capitalize it, dont worry about accent marks ")

# Here the program checks if the character submitted by the user is more than just 1 letter, if it is it tells the user to resubmit only 1 letter
      if(len(letter)!= 1):
         print ("ERROR, Submit only 1 letter. Try again")
         continue
   
# Here the program checks if the charater submitted by the user is not a capitalized letter or not a letter at all. If so, the program tells the user to submit a valid letter
      if(letter not in EligibleLetters):
         print ("ERROR, Use a valid letter. Try again")
         continue

# Here the program checks if the letter submitted by the user was already submitted once before. If so, the program tells the user to use another letter
      if(letter in LettersSubmitted):
         print ("ERROR, You already used this letter. Try again")
         continue

# Here the program takes in the letter submitted from the user and adds it to a list of letters already submitted so the user cant reuse the same letter.
      LettersSubmitted.append(letter)
      return letter


#Here the function that prints each body part of the hangman for every wrong guess by the user is defined
def get_hangman():
#Here i defined a variable named bodypart to represent each step in the hangman figure. For every guess that the user gets incorrect, the steps increase + 1
   bodypart = 0
   for letter in LettersSubmitted:
      if letter not in answer:
         bodypart = bodypart + 1

   print(hang_man[bodypart])

#Here the program ends the game when the entire hangman puppet is drawn.
   if bodypart == 6:
         print("YOU LOST! :(")
         return False


 # Here the function that shows the word in blanks and how much of the word the user has guessed is defined.
answer = random_pueblo()
def printword():
#
   temp:str = ""
#
   for letter in answer:
      if (letter in LettersSubmitted):
         temp = temp + letter
      else: 
         temp = temp + "_ "

   print(temp)



#Falta: hacer el loop que vuelva a empezar el juego cuando pierde Y cuando gana, you win!, documentar printword
while True:
   getInput()
   printword()
   get_hangman()