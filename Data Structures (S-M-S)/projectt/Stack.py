class stack():
    stackk=[]
    def push(self,data):
        self.stackk.append(data)
    def pop(self):
        return self.stackk.pop()