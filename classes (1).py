class Skills:
    
    def __init__(self, name, atk, typ, pp, category):
        self.name = name
        self.atk = atk
        self.typ = typ
        self.pp = pp  #The remaining times this skill can be used
        self.category = category
        
    def __str__(self):
        """Takes the parameters given when defining the skills and returns this 
        information in human language.
        
        Returns
        -------
        string: string
            String that gives the information of the skill of the Pokemon.
        """
        
        string = "{} is {} {} type skill with power of {}, with {} times left.\n"\
        .format(self.name, self.category, self.typ, self.atk, self.pp)
        
        return string

from my_module import pokemons_skills
    
    
class Pokemon:
    
    def __init__(self, name, typ, atk, hp, 
                 skill_1, skill_2, skill_3, skill_4, temp_skill = 0):
        self.name = name
        self.typ = typ
        self.atk = atk
        self.hp = hp  #Pokemon dies if hp becomes 0
        self.skill_1 = skill_1
        self.skill_2 = skill_2
        self.skill_3 = skill_3
        self.skill_4 = skill_4
        self.temp_skill = temp_skill

    def __str__(self):
        """Gives the information of a Pokemon in human language.
        
        Return
        -------
        info: string
            String that gives the information of the Pokemon.
        """
        
        info = '{} is {}-type Pokemon\n{} has 4 skills:\n{}{}{}{}'\
        .format(self.name, self.typ, self.name, self.skill_1,
                self.skill_2, self.skill_3, self.skill_4)
        
        return info
    
    def attack(self, other):
        """Calculate the type effectiveness of the Pokemons' skills, and 
        uses a formula to determine the damage of a certain skill on a 
        certain Pokemon, and the remaining hp of the Pokemon being attacked.
        Also updates the pp value of the skilled used.
        
        Parameter
        ---------
        other: Pokemon
            The opponent Pokemon that receives the attack.
        
        Return
        -------
        [damage, other_new_hp]: list
            Gives the damage caused by the attacking Pokemon, and the remaining hp of 
            the opponent Pokemon.
        """
        
        #Calculate the type effectiveness
        if self.temp_skill.typ == "Fire" and other.typ in ["Grass"]:
            multi = 1.5
        elif self.temp_skill.typ == "Fire" and other.typ in ["Water", "Fire"]:
            multi = 0.5
        elif self.temp_skill.typ == "Water" and other.typ in ["Fire"]:
            multi = 1.5
        elif self.temp_skill.typ == "Water" and other.typ in ["Grass", "Water", "Electric"]:
            multi = 0.5
        elif self.temp_skill.typ == "Grass" and other.typ in ["Water"]:
            multi = 1.5
        elif self.temp_skill.typ == "Grass" and other.typ in ["Fire", "Grass"]:
            multi = 0.5
        elif self.temp_skill.typ == "Electric" and other.typ in ["Water"]:
            multi = 1.5
        elif self.temp_skill.typ == "Electric" and other.typ in ["Electric", "Grass"]:
            multi = 0.5
        elif self.temp_skill.typ == "Steel" and other.typ in ["Grass"]:
            multi = 1.5
        elif self.temp_skill.typ == "Steel" and other.typ in ["Fire"]:
            multi = 0.5
        else:
            multi = 1
        
        #Determine the damage of the skill, the remaining hp and pp
        damage = int((self.temp_skill.atk + self.atk) * multi)
        other_new_hp = other.hp - damage
        other.hp = other_new_hp
        self.temp_skill.pp -= 1  
        return [damage, other_new_hp]

from my_module.pokemons import pikachu, bulbasaur, charmander, squirtle    
    
import random
        

class Fight():
    
    def getting_started(self):
        """Takes the Pokemon name from the user input, checks if it corresponded 
        with an existing Pokemon.
        If yes, prints the Pokemon information and gives the instruction to move 
        to next stage.
        If not, keeps asking until get a desired name.
        
        Return
        -------
        Pokemon
            The chosen Pokemon instance from the Pokemon class.
        """      
        
        switch = True #Loop breaks if the input name from the user matches the Pokemon name
        
        while switch:
            my_pokemon = input('Choose one: Pikachu, Bulbasaur, Charmander, Squirtle --- ')
            
            if my_pokemon == 'Pikachu':
                switch = False
                print(pikachu)
                print ("Now let's see who's your opponent!")
                return pikachu
            
            elif my_pokemon == 'Bulbasaur':
                switch = False
                print(bulbasaur)
                print ("Now let's see who's your opponent!")
                return bulbasaur
            
            elif my_pokemon == 'Charmander':
                switch = False
                print(charmander)
                print ("Now let's see who's your opponent!")
                return charmander
            
            elif my_pokemon == 'Squirtle':
                switch = False
                print(squirtle)
                print ("Now let's see who's your opponent!")
                return squirtle
            
            else:
                print('Please enter one of the Pokemon names exactly as given.')
       
    def get_opponent(self, my_po): 
        """After the user made his choice, randomly chooses one Pokemon
        from the left three Pokemons as the opponent Pokemon.
        
        Parameter
        ---------
        my_po: Pokemon
            The Pokemon chosen by the user.
        
        Return
        -------
        op_po: Pokemon
            The Pokemon the computer chooses.
        """

        #Ensures the computer doesn't choose the same Pokemon as the user
        pokemons = [pikachu, bulbasaur, charmander, squirtle]
        pokemons = list(filter(lambda x: x.name != my_po.name, pokemons)) 
        op_po = random.choice(pokemons)
        
        opponent = 'Your opponent will be --- ' + op_po.name + '.'
        
        print (opponent)
        
        return op_po
    
    def fight(self, my_po, op_po):
        """The user enters the name of the skill he wanted to use.
        If input is the name of an available skill(pp > 0), 
        the computer takes turn to choose a skill.
        If the input is invalid(wrong spelling or pp < 0), 
        will ask again until get the desired name.
        After both side chooses a skill, calculates damage done by 
        the skills and the remaining hp of both Pokemons.
        If one of the Pokemons has a hp <= 0, the fight ends and the result returned; 
        otherwise, repeat the above procedure to choose skills.
        
        Parameter
        ---------
        my_po: Pokemon
            The Pokemon chosen by the user.
        op_po: Pokemon
            The Pokemon chosen by the computer.
        
        Return
        -------
        result : string
            Gives the result on whether the user wins or loses.
        """
        
        my_po_hp = 1
        op_po_hp = 1
        
        while my_po_hp > 0 and op_po_hp > 0:
            
            #Asks the user to choose a skill to fight
            switch = True  
            
            while switch:
                skill_info = 'skill info:\n{}{}{}{}'.format(my_po.skill_1, my_po.skill_2, my_po.skill_3, 
                                                            my_po.skill_4)
                print(skill_info)
                choose_skill = input('choose one skill --- ')   

                if choose_skill == my_po.skill_1.name and my_po.skill_1.pp > 0:
                    my_po.temp_skill = my_po.skill_1
                    switch = False
                elif choose_skill == my_po.skill_2.name and my_po.skill_2.pp > 0:
                    my_po.temp_skill = my_po.skill_2
                    switch = False
                elif choose_skill == my_po.skill_3.name and my_po.skill_3.pp > 0:
                    my_po.temp_skill = my_po.skill_3
                    switch = False
                elif choose_skill == my_po.skill_4.name and my_po.skill_4.pp > 0:
                    my_po.temp_skill = my_po.skill_4
                    switch = False
                else:
                    print('You enter an invalid skill name or the chosen skill can no longer be used')
                    
            #Choose skill for opponent pokemon
            op_po_skills = [op_po.skill_1, op_po.skill_2, op_po.skill_3, op_po.skill_4]
            op_po_skills = list(filter(lambda x: x.pp > 0, op_po_skills)) 
            op_po.temp_skill = random.choice(op_po_skills)
            
            #Checks the status of both pokemons 
            op_po_status = my_po.attack(op_po)
            damage_on_op_po = op_po_status[0]
            op_po_hp = op_po_status[1]
            
            my_po_status = op_po.attack(my_po)
            damage_on_my_po = my_po_status[0]
            my_po_hp = my_po_status[1]
           
            #Decides if the fight continues
            if op_po_hp <= 0:
                output = 'Opponent pokemon hp -' + str(damage_on_op_po) + \
                '. Opponent pokemon remaining hp:' + str(op_po_hp) + \
                '\n\nYou win!'        
                print (output)
                
                result = 'win'
                return result
                
            elif op_po_hp > 0 and my_po_hp <= 0:
                output = 'Your opponent uses --- ' + op_po.temp_skill.name + \
                '.\nMy pokemon hp -' + str(damage_on_my_po) + \
                '. My Pokemon remaining hp:' + str(my_po_hp) + \
                '\n\nYou lose.'
                print (output)
                
                result = 'lose'
                return result
               
                
            elif op_po_hp > 0 and my_po_hp > 0:    
                output = 'Opponent pokemon hp -' + str(damage_on_op_po) + \
                '. Opponent pokemon remaining hp:' + str(op_po_hp) + \
                '.\nYour opponent uses --- ' + op_po.temp_skill.name + \
                '.\nMy pokemon hp -'+ str(damage_on_my_po) + \
                '. My Pokemon remaining hp:' + str(my_po_hp) + '.\n'
                print (output)
                
        
        
     
        