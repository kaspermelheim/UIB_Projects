 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Håkon Tjeldnes
"""

def oppgave1a(numbers):
    ''' Sort ascending, up: (1,2,3) '''
    numbers.sort()
    return numbers
    

def oppgave1b(numbers):
    ''' Sort descending, down: (3,2,1) '''
    numbers.sort(reverse = True)
    return numbers

def oppgave1c(strings):
    ''' Sort ascending by length '''
    
    """ 
    Alternativ metode:
    strings_sorted = sorted(strings, key=len)
    return strings_sorted 
    """
    
    strings.sort(key=len)
    return strings
    
def count_uppercase(s):
    ''' Count number of capital letters in string
    input:
        s: a single string from list
    return:
        Integer number of the number of capital letters in string '''
    capitals = 0
    
    for i in s:
        if i.isupper():
            capitals += 1
    return capitals
    
def oppgave1d(strings):
    ''' Sort descending by number of capital letters '''

    strings.sort(key=lambda s: (count_uppercase(s), len(s)), reverse=True)
    return strings
            

# Basic classes
# Normally use first capital letter in class names
# We need __init__ to create a specific car, else it is just a possible 
# abstraction that is not real yet (what we call an instance or object).
# The underscores like __name__ just means it is an internal function in python, 
#like __init__,  __repr__, __str__ etc. 

#Class Car 2a & 2c
class Car:
  ''' A car class to generalize a format for all cars '''
  #Constructor to initialize
  def __init__(self, company, name, color, engine):
      self.company = company
      self.name = name
      self.color = color
      self.engine = engine
   # method to represent class as a human readable string
  def __repr__(self):
    return("This is a {} {} {}, using a {}".format(self.color,
           self.company, self.name, self.engine))
  

#Class Engine
class Engine:
    ''' An engine class to generalize a format for all engines '''
    #Constructor to initialize
    def __init__(self, name, horsepowers):
        self.name = name
        self.horsepowers = horsepowers
    # method to represent class as a human readable string
    def __repr__(self):
      return('{} engine with {} horsepowers.\n'.format(self.name,
             self.horsepowers))

def get_engine_power(Car):
    ''' return horsepowers of cars '''
    return Car.engine.horsepowers
      
def main():
    # Sorting
    numbers = [4, 1, 2, 5, 2, 1, 6, 8, 0]
    print(oppgave1a(numbers))
    print(oppgave1b(numbers))
    
    strings = ["abc", "a", "AA", "DAabcas", "adesAA", "EFSFDAAAaaa"]
    print(oppgave1c(strings))
    print(oppgave1d(strings))
    
    
    # Basic classes
    print()
    # 2b Create a ferrari and volvo
    ferrari_f40 = Car("ferari","f40","red", Engine("V8", 800)) # <- fill parameters
    volvo_v50 = Car("volvo", "v50", "gray", Engine("V6", 400)) # <- fill parameters
    
    # 2c Print list of cars as human readable
    list_of_cars = [volvo_v50, ferrari_f40]
    print(list_of_cars)
    
    # 2d Now print sorted cars in descending order of engine size
    list_of_cars.sort(key = get_engine_power, reverse = True)
    print(list_of_cars)
    
main()
    