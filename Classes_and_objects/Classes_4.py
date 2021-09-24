import random

class colleague:

    def __init__(self, name=None, pet= None):
        self.name = name
        self.pet = pet

    def speak(self):
        phrases = {
            1: "I'm hungry",
            2: "I'm tired",
            3: "I want to go home",
            4: "I want to sleep"
        }
        n = random.randint(1,4)
        print(f"{self.name} : {phrases[n]}")

    def generate():
        names = {
            1: 'Zoe',
            2: 'Keith',
            3: 'Desmond',
            4: 'Gareth'
        }
        n = random.randint(1,4)

        return colleague(names[n])



if __name__ == '__main__':
    c1 = colleague.generate()
    c2 = colleague.generate()
    c3 = colleague.generate()
    c4 = colleague.generate()
    c1.speak()
    c2.speak()
    c3.speak()
    c4.speak()