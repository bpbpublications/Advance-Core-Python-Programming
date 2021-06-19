class dog():
    def family(self):
        print("I belong to family of Dogs")

class germanShepherd(dog):
    def breed(self):
        print("I am a German Shepherd")

c = germanShepherd()
c.family()
c.breed()
###############################################3
class dog():
    def family(self):
        print("I belong to family of Dogs")

class germanShepherd(dog):
    def breed(self):
        print("I am a German Shepherd")

class husky(dog):
    def breed(self):
        print("I am a husky")    

g = germanShepherd()
g.family()
g.breed()
h = husky()
h.family()
h.breed()
###################################################33
class dog():
    def family(self):
        print("I belong to family of Dogs")

class germanShepherd(dog):
    def breed(self):
        print("I am a German Shepherd")

class husky(dog):
    def breed(self):
        print("I am a husky")

    def family(self):
        print("I am class apart")

g = germanShepherd()
g.family()
g.breed()

h = husky()
h.family()
h.breed()
#########################################################3
class dog():
    def family(self):
        print("I belong to family of Dogs")

class germanShepherd(dog):
    def breed(self):
        print("I am a German Shepherd")

class husky(dog):
    def breed(self):
        print("I am a husky")

    def family(self):
        super().family()
        print("but I am class apart")

g = germanShepherd()
g.family()
g.breed()

h = husky()
h.family()
h.breed()

