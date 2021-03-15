"""
Created on Thu Feb 25 11:17:09 2021

@author: Jack
"""


animal = { 
        'hair' : True,
        'milk' : False,
        'meat' : False,
        'pointedteeth' : False,
        'claws' : False,
        'forwardeyes' : False,
        'carnivore' : False,
        'mammal' : False,
        'hooves' : False,
        'ungulate' : False,
        'cud' : True,
        'tawny' : False,
        'darkspots' : True,
        'blackstripes' : False,
        'longneck' : True,
        'tiger' : False,
        'giraffe' : False,
        'zebra' : False,
        'cheetah' : False
        }

new_fact = True

rules_fired = ['facts']

while new_fact == True:
    new_fact = False
    
    # Rule 1
    if animal['hair'] is True and animal['mammal'] is False:
        animal['mammal'] = True
        new_fact = True
        rules_fired.append('R1')
    
    # Rule 2
    if animal['milk'] is True and animal['mammal'] is False:
        animal['mammal'] = True
        new_fact = True
        rules_fired.append('R2')
        
    # Rule 3
    if animal['meat'] is True and animal['carnivore'] is False:
        animal['carnivore'] = True
        new_fact = True
        rules_fired.append('R3')
        
    # Rule 4
    if animal['pointedteeth'] is True and animal['claws'] is True and animal['forwardeyes'] is True and animal['carnivore'] is False:
        animal['carnivore'] = True
        new_fact = True
        rules_fired.append('R4')
        
    # Rule 5
    if animal['mammal'] is True and animal['hooves'] is True and animal['ungulate'] is False:
        animal['ungulate'] = True
        new_fact = True
        rules_fired.append('R5')
        
    # Rule 6
    if animal['mammal'] is True and animal['cud'] is True and animal['ungulate'] is False:
        animal['ungulate'] = True
        new_fact = True
        rules_fired.append('R6')
    
    # Rule 7
    if animal['mammal'] is True and animal['carnivore'] is True and animal['tawny'] is True and animal['darkspots'] is True and animal['cheetah'] is False:
        animal['cheetah'] = True
        new_fact = True
        rules_fired.append('R7')
    
    # Rule 8
    if animal['tawny'] is True and animal['blackstripes'] is True and animal['mammal'] is True and animal['carnivore'] is True and animal['tiger'] is False:
        animal['tiger'] = True
        new_fact = True
        rules_fired.append('R8')
    
    # Rule 9
    if animal['darkspots'] is True and animal['longneck'] is True and animal['ungulate'] is True and animal['giraffe'] is False:
        animal['giraffe'] = True
        new_fact = True
        rules_fired.append('R9')
        
    # Rule 10
    if animal['blackstripes'] is True and animal['ungulate'] is True and animal['zebra'] is False:
        animal['zebra'] = True
        new_fact = True
        rules_fired.append('R10')
        
    if animal['zebra'] is True:
        print('Your animal is a zebra!\n')
        print('Rules fired: ')
        print(rules_fired)
        new_fact = False
        
    elif animal['tiger'] is True:
        print('Your animal is a tiger!\n')    
        print('Rules fired: ')
        print(rules_fired)
        new_fact = False
    
    elif animal['giraffe'] is True:
        print('Your animal is a giraffe!\n')    
        print('Rules fired: ')
        print(rules_fired)
        new_fact = False
    
    elif animal['cheetah'] is True:
        print('Your animal is a cheetah!\n')    
        print('Rules fired: ')
        print(rules_fired)
        new_fact = False
        


