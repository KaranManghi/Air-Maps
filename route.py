from queue import PriorityQueue

class NodeState(object):
    class State(object):
        def __init__(self, value, parent, start = 0, goal = 0):
            self.children = []    
            self.parent = parent 
            self.value = value   
            self.dist = 0        

            if parent:
                self.start = parent.start   
                self.goal = parent.goal    
                self.path = parent.path[:]  
            
                self.path.append(value)     
            else:
                self.path = [value] 
                self.start = start  
                self.goal = goal    

    class State_String(State):
        def __init__(self, value, parent, start = 0, goal = 0 ):
            super(State_String, self).__init__(value, parent, start, goal) # create constructor
            self.dist = self.GetDistance() # override distance variable by calling GetDistance() method 
    
        def GetDistance(self):
            # first check to see if we have reached to our goal, and if we have then simply return 0  
                if self.value == self.goal:
                    return 0
                dist = 0
    
            #Define a loop to go through each letter of the goal
                for i in range(len(self.goal)):
                    letter = self.goal[i] # get the current letter
                    
                    dist += abs(i - self.value.index(letter)) #find index of letter in current value
                                                            #This will give the distance of letter is from its target p
                return dist   # simply return distance
    
    #Define function to generate our children
        def CreateChildren(self):
                #if there are no children then go ahead and generate the children
                # this is just an extra precaution that we don't want to children twice 
    
                if not self.children:
                    for i in range(len(self.goal)-1): # go through every possibilities or every possible arrangement of the letter.
                        val = self.value
    
                        # switching the second letter and the first letter of every pairs of letters
                        # and we track on the beginning and track on the end and then we have a new arrangement of letter in val.
                        val = val[:i] + val[i+1] + val[i] + val[i+2:]
    
                        # create a child and store the value of the child and pass self to store the parent of the child
                        child = State_String(val, self)
                        self.children.append(child) # finally add this child to our children list