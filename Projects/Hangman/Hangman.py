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
12
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

print(hang_man[0])

LettersSub = []
EligibleLetters = ["A" , "B", "C","D","E","F","G","H","I", "J","K", "L", "M", "N", "O", "P", "Q", "R","S","T","U", "V", "W", "X", "Y", "Z", "Ñ"]

def answer(pueblos):
   pueblos = ["Adjuntas", "Aguada", "Aguadilla", "Aguas Buenas", "Aibonito", "Arecibo", "Arroyo", "Añasco", "Barceloneta",  "Barranquitas",  "Bayamon",  "Cabo Rojo" , "Caguas",  "Camuy",  "Canovanas",  "Carolina",  "Cataño",  "Cayey",  "Ceiba",  "Ciales",  "Cidra",  "Coamo",  "Comerio",  "Corozal",  "Culebra",  "Dorado",  "Fajardo",  "Florida",  "Guayama",  "Guayanilla",  "Guaynabo",  "Gurabo",  "Guanica",  "Hatillo",  "Hormigueros",  "Humacao",  "Isabela",  "Jayuya",  "Juana Diaz" , "Juncos",  "Lajas",  "Lares",  "Las Marias" , "Las Piedras" , "Loiza",  "Luquillo",  "Manati",  "Maricao",  "Maunabo",  "Mayaguez",  "Moca",  "Morovis",  "Naguabo",  "Naranjito",  "Orocovis",  "Patillas",  "Peñuelas",  "Ponce",  "Quebradillas",  "Rincon",  "Rio Grande" , "Sabana Grande", "Salinas",  "San German" , "San Juan" , "San Lorenzo" "San Sebastiaan" , "Santa Isabel" , "Toa Alta" , "Toa Baja", "Trujillo Alto" , "Utuado",  "Vega Alta" , "Vega Baja" , "Vieques",  "Villalba",  "Yabucoa",  "Yauco"]
   return random.choice(pueblos)


def getInput():

   while(True):
      letter = input("Chose letter, dont worry about accent marks")

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
      return LettersSub

while True:
   print(hang_man[0])
   getInput()
   printword()