class Trobble:

    def __init__(self , name , sex):
        self.name = name
        self.sex = sex
        self.health = 10
        self.age = 0
        self.hunger = 0

    def __str__(self):
        return self.name + ": " + self.sex + ", health " + str(self.health) + ", hunger " + str(self.hunger) + ", age " + str(self.age)

    def next_turn(self):
        if self.health == 0: 
            return
        self.age += 1
        self.hunger += self.age
        self.health = max(0 , self.health - int(self.hunger / 20))
        
    def feed (self):
        self.hunger = max(0 , self.hunger - 25)
    def cure (self):
        self.health = min(10 , self.health + 5)
    def party (self):
        self.health = min(10 , self.health + 2)
        self.hunger += 4
    def is_alive(self):
        return self.health > 0

def get_name():
    return input('Please give your new Trobble a name: ')

def get_sex():
    sex = None
    while sex is None:
        prompt = 'Is your new Trobble male or female? Type "m" or "f" to choose: '
        choice = input(prompt)
        if choice == 'm':
            sex = 'male'
        elif choice == 'f':
            sex = 'female'
    return sex

def get_action(actions):
    while True:
        prompt = f"Type one of {', '.join(actions.keys())} to perform the action, or stop to quit the game: "
        action_string = input(prompt)
        if action_string == 'stop':
            print('Thanks for having played with Trobbles!')
            return
        if action_string not in actions:
            print('Unknown action!')
        else:
            return actions[action_string]
        
def play():
    name = get_name()
    sex = get_sex()
    trobble = Trobble(name, sex)
    actions = {'feed': trobble.feed, 'cure': trobble.cure, 'party' : trobble.party}
    
    while trobble.is_alive():
        print('You have one Trobble named ' + str(trobble))
        if trobble.age % 10 == 0 and trobble.age != 0:
            print(f"Happy Birthday {trobble.name}!")
            trobble.hunger = max(0 , trobble.hunger-5)
        action = get_action(actions)
        if action is None:
            return
        action()
        trobble.next_turn()

    print(f'Unfortunately, your Trobble {trobble.name} has died at the age of {trobble.age}')

#t1 = Trobble('cariciu' , 'elicopter de lupta')

def mate(trobble1, trobble2, name_offspring):
    if (trobble1.age < 4 or trobble2.age < 4 or trobble1.sex == trobble2.sex or trobble1.health == 0 or trobble2.health == 0):
        return 
    else:
        return Trobble(name_offspring , trobble1.sex)

#print(t1.name , t1.sex)
# 
# print(t1)
# 
# for i in range(15):
    # t1.next_turn()
    # print(t1)