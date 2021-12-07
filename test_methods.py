from my_module.classes import Pokemon, Skills

from my_module.pokemons_skills import thunder_shock, iron_tail, quick_attack, thunderbolt, tackle, vine_whip, seed_bomb, take_down, scratch, ember, flamethrower, slash, water_gun, rapid_spin, rapid_spin, waterfall, muddy_water

from my_module.pokemons import pikachu, bulbasaur, charmander, squirtle

import random 

#The data in Skill and Pokemon get changed after execution
#Please restart kernel before run this test
def test_attack(): 
    my_po = pikachu
    op_po = bulbasaur
    my_po.temp_skill = my_po.skill_1
    op_po_status = my_po.attack(op_po)
    assert callable(my_po.attack)
    assert isinstance(my_po.attack(op_po), list)
    assert op_po_status == [31, 149]
    
    
#Because getting_started requires an user input,
#I redefined it here with the user input feeded as a parameter to the function.
#I also eliminated the print() statement since they don't affect the result anyways.
def getting_started_copy(user_input):
    switch = True
    while switch:
        if user_input == 'Pikachu':
            switch = False
        
            return pikachu
            
        elif user_input == 'Bulbasaur':
            switch = False
            
            return bulbasaur
        
        elif user_input == 'Charmander':
            switch = False
            
            return charmander
            
        elif user_input == 'Squirtle':
            switch = False
            
            return squirtle
        
        else:
            print('Please enter one of the Pokemon names exactly as given.')

def test_getting_started_copy():
    assert callable(getting_started_copy)
    assert isinstance(getting_started_copy('Pikachu'), Pokemon)
    assert getting_started_copy('Pikachu') == pikachu
    
    
#Also I redefined the get_opponent function:
def get_opponent_copy(user_input):   
    pokemons = [pikachu, bulbasaur, charmander, squirtle]
    pokemons = list(filter(lambda x: x.name != user_input.name, pokemons)) 
    op_po = random.choice(pokemons)
    opponent = 'Your opponent will be --- ' + op_po.name + '.'
        
    return op_po

def test_get_opponent_copy():
    assert callable(get_opponent_copy)
    assert isinstance(get_opponent_copy(pikachu), Pokemon)
    assert get_opponent_copy(pikachu) != pikachu


#Same for fight function:
def fight_copy(my_po_hp, op_po_hp):
    if op_po_hp <= 0:        
        result = 'win'

        return result
                
    elif op_po_hp > 0 and my_po_hp <= 0:
        result = 'lose'

        return result
                                  
def test_fight_copy():
    assert callable(fight_copy)
    assert fight_copy(1,0) == 'win'
    assert fight_copy(0,1) =='lose'
    assert isinstance(fight_copy(1,0), str)

                 
    