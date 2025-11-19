class parent:
    def habit(self):
        self.name="saiteja"
        self.about="  playing ganes"
        print("every one had a habit got from there parents{0}-{1}".format(self.about,self.name))
class parent1(parent):
    def habit(self):
        self.name="sampath"
        self.about=" going gym"
        print("every one had a habit got from there aprents{0}-{1}".format(self.about,self.name))
parents=parent()
parents.habit()
parents=parent1()
parents.habit()


    