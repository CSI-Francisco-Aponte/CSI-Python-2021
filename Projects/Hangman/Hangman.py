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

print(hang_man[3])

def answer(pueblos):
   pueblos = ["Adjuntas", "Aguada", "Aguadilla", "Aguas Buenas", "Aibonito", "Arecibo", "Arroyo", "Añasco", "Barceloneta",  "Barranquitas",  "Bayamón",  "Cabo Rojo" , "Caguas",  "Camuy",  "Canóvanas",  "Carolina",  "Cataño",  "Cayey",  "Ceiba",  "Ciales",  "Cidra",  "Coamo",  "Comerío",  "Corozal",  "Culebra",  "Dorado",  "Fajardo",  "Florida",  "Guayama",  "Guayanilla",  "Guaynabo",  "Gurabo",  "Guánica",  "Hatillo",  "Hormigueros",  "Humacao",  "Isabela",  "Jayuya",  "Juana Díaz" , "Juncos",  "Lajas",  "Lares",  "Las Marías" , "Las Piedras" , "Loiza",  "Luquillo",  "Manatí",  "Maricao",  "Maunabo",  "Mayagüez",  "Moca",  "Morovis",  "Naguabo",  "Naranjito",  "Orocovis",  "Patillas",  "Peñuelas",  "Ponce",  "Quebradillas",  "Rincón",  "Rio Grande" , "Sabana Grande", "Salinas",  "San Germán" , "San Juan" , "San Lorenzo" "San Sebastián" , "Santa Isabel" , "Toa Alta" , "Toa Baja", "Trujillo Alto" , "Utuado",  "Vega Alta" , "Vega Baja" , "Vieques",  "Villalba",  "Yabucoa",  "Yauco"]
   return random.choice(pueblos)

def getInput():
   letter = input("Chose letter")

   If(len(letter)!= 1)
      print("error")