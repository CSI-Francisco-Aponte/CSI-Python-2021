import random

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



LettersSub = []
EligibleLetters = ["A" , "B", "C","D","E","F","G","H","I", "J","K", "L", "M", "N", "O", "P", "Q", "R","S","T","U", "V", "W", "X", "Y", "Z"]

def random_pueblo():
   pueblos = ["Adjuntas", "Aguada", "Aguadilla", "Aguas Buenas", "Aibonito", "Arecibo", "Arroyo", "Anasco", "Barceloneta",  "Barranquitas",  "Bayamon",  "Cabo Rojo" , "Caguas",  "Camuy",  "Canovanas",  "Carolina",  "Catano",  "Cayey",  "Ceiba",  "Ciales",  "Cidra",  "Coamo",  "Comerio",  "Corozal",  "Culebra",  "Dorado",  "Fajardo",  "Florida",  "Guayama",  "Guayanilla",  "Guaynabo",  "Gurabo",  "Guanica",  "Hatillo",  "Hormigueros",  "Humacao",  "Isabela",  "Jayuya",  "Juana Diaz" , "Juncos",  "Lajas",  "Lares",  "Las Marias" , "Las Piedras" , "Loiza",  "Luquillo",  "Manati",  "Maricao",  "Maunabo",  "Mayaguez",  "Moca",  "Morovis",  "Naguabo",  "Naranjito",  "Orocovis",  "Patillas",  "Penuelas",  "Ponce",  "Quebradillas",  "Rincon",  "Rio Grande" , "Sabana Grande", "Salinas",  "San German" , "San Juan" , "San Lorenzo" "San Sebastiaan" , "Santa Isabel" , "Toa Alta" , "Toa Baja", "Trujillo Alto" , "Utuado",  "Vega Alta" , "Vega Baja" , "Vieques",  "Villalba",  "Yabucoa",  "Yauco"]
   answer = random.choice(pueblos).upper()
   return answer

answer = random_pueblo()
def printword():
   temp:str = ""

   for letter in answer:
      if (letter in LettersSub):
         temp = temp + letter
      else: 
         temp = temp + "_ "

   print(temp)

def getInput():

   while(True):
      letter = input("Chose letter, capitalize it, dont worry about accent marks ")

      if(len(letter)!= 1):
         print ("ERROR, Submit only 1 letter. Try again")
         continue
   
      if(letter not in EligibleLetters):
         print ("ERROR, Use a valid letter. Try again")
         continue

      if(letter in LettersSub):
         print ("ERROR, You already used this letter. Try again")
         continue

      LettersSub.append(letter)
      return letter

print(hang_man[0])
def get_hangman():


while True:
   getInput()
   printword()