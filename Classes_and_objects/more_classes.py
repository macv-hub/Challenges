import random

class colleague:

    def __init__(self, name='',pet=''):
        self.name = name
        self.pet = pet

    def speak(self):

        dict = {
            1 : 'I am sleepy',
            2 : 'I am hungry',
            3 : 'I want to go home',
            4 : 'I am hungry'
        }
        n = random.randint(1,4)
        print(f'{self.name}: {dict[n]}')

    def generate():

        names = {
            1 : 'Fraser',
            2 : 'Zoe',
            3 : 'Desmond',
            4 : 'Keith'
        }
        pets = {
            1 : 'hamster',
            2 : 'snake',
            3 : 'lion',
            4 : 'racoon'
        }
        n = random.randint(1,4)
        m = random.randint(1,4)
        return colleague(names[n], pets[m])

if __name__ == '__main__':

    a1 = colleague('Manuel', 'dog')
    a2 = colleague('Liam', 'cat')
    a1.speak()
    a2.speak()
    a3 = colleague.generate()
    a3.speak()
    a4 = colleague.generate()
    a4.speak()