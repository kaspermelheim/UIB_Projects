#Implement LFSR

def lfsr(feedback, state):
    #assert ( len(feedback) &= len(state) )
    newbit = 0 
    for i in range(len(feedback)):
        newbit = (newbit + feedback[i] * state[i]) % 2
        state = [newbit] + state[:-1]
        print(state)
    
feedback = [5,2,1]
state = [1,0,0,1,0]
lfsr(feedback, state)
