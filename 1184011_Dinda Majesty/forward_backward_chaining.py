# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 10:38:30 2021

@author: SIMAMORA
"""

#example 1
#kasus = "seorang user ingin berkonsultasi apakah tepat jika ia berinvestasi pada stock IBM"

#A = "memiliki uang $10.000 untuk investasi"
#B = "berusia < 30 tahun"
#C = "tingkat pendidikan pada level college"
#D = "pendapatan minimum pertahun $40.000"
#E = "investasi pada bidang sekuritas (Asuransi)"
#F = "investasi pada saham pertumbuhan (growth stock)"
#G = "investasi pada saham IBM"

#the fact A and B is True
A = True
B = True
C = None
D = None
E = None
F = None
G = None

#forward chaining
while G == None:
    if A and C == True:
        E = True
        print("E is True")
    if D and C == True:
        F = True
        print("F is True")
    if B and E == True:
        F = True
        print("F is True")
    if B == True:
        C = True
        print("C is True")
    if F == True:
        G = True
        print("G is true")

#backward chaining
fact = [{"A":True}, {"B":True}]
stack = [{"G":None}]
new_fact = []

for data_stack in stack:
  for key, value in data_stack.items():
    if key == "G":
        #add F to stack
        stack.append({"F":None})
        print(stack)
    if key == "F":
        #add C and D to stack
        stack.append({"C":None})
        stack.append({"D":None})
        print(stack)
    if key == "C":
        #add E to stack, A = True
        stack.append({"E":None})
        print(stack)
    if key == "E":
        #B is True and no new stack, so lets check the new fact
        if B == True:
            C = True
            new_fact.append({"C":True})
            print(new_fact)
        if A and C == True:
            E = True
            new_fact.append({"E":True})
            print(new_fact)
        if B and E == True:
            F = True
            new_fact.append({"F":True})
            print(new_fact)
        if F == True:
            G = True
            new_fact.append({"G":True})
            print(new_fact)
            print("so the target (G) is True")
            
#example 2
#forward chaining

suggestion_to_users = None

symptoms1 = "meriang"
symptoms2 = "sesak napas"

symptoms_data = [{"value1": "sakit kepala", "value2": "suhu tubuh meningkat", "result": "demam"}, {"value1": "meriang", "value2": "sesak napas", "result": "infeksi virus corona"}, {"value1": "detak jantung melemah", "value2": "tekanan darah menurun", "result": "hipotermia"}]
suggestions = [{"demam": "banyak istirahat dan minum obat"}, {"infeksi virus corona": "vaksinasi dan perkuat sistem imun"}, {"hipotermia": "jaga suhu tubuh tetap normal"}]

symptoms_identifier = None
for data_symptoms in symptoms_data:
  if (symptoms1 == data_symptoms["value1"] or symptoms1 == data_symptoms["value2"]) and (symptoms2 == data_symptoms["value1"] or symptoms2 == data_symptoms["value2"]):
    symptoms_identifier = data_symptoms["result"]
    break

if symptoms_identifier:
  print(symptoms_identifier)
else:
  print("result symproms is not found..")
  
for data_suggestions in suggestions:
  for key, value in data_suggestions.items():
    if key == symptoms_identifier:
      suggestion_to_users = data_suggestions[symptoms_identifier]
      break
  
if suggestion_to_users:
  print(f"direkomendasikan untuk {suggestion_to_users}")
else:
  print("result suggestion to user is not found...")
  
  
#backward chaining
suggestion_to_users = None

symptoms1 = "meriang"
symptoms2 = "sesak napas"

symptoms_data = [{"value1": "sakit kepala", "value2": "suhu tubuh meningkat", "result": "demam"}, {"value1": "meriang", "value2": "sesak napas", "result": "infeksi_virus_corona"}, {"value1": "detak jantung melemah", "value2": "tekanan darah menurun", "result": "hipotermia"}]
suggestions = [{"demam": "banyak istirahat dan minum obat"}, {"infeksi_virus_corona": "vaksinasi dan perkuat sistem imun"}, {"hipotermia": "jaga suhu tubuh tetap normal"}]

  # C => D
for suggestions_data in suggestions:
  for key, value in suggestions_data.items():
    # A & B => C
    for data_symptoms in symptoms_data:
      if data_symptoms["result"] == key:
        if (symptoms1 == data_symptoms["value1"] or symptoms1 == data_symptoms["value2"]) and (symptoms2 == data_symptoms["value1"] or symptoms2 == data_symptoms["value2"]):
          suggestion_to_users = value

if suggestion_to_users:
  print(f"direkomendasikan untuk {suggestion_to_users}")
else:
  print("result suggestion to user is not found...")