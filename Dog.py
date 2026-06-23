# We will be create a dog 'class' that encases a dog 'object'
# An object is a data type that we create and define

class Dog:
  #classes should be capitalized unlike variables

  #We will now write a constructor. This constructs an object.
  #It is a special method. A method is an operation that we can call
  #We will specify what attributes a dog object has

              #These are parameters. Self referes to the object being created.
              #(its just there)
  def __init__(self, breed, age, weight, is_trained):
  # init stands for initialize
    '''
    We now need to set the attributes of the dog to
    the values of the parameters
    '''
    #self.breed referes to the attribute breed of itself. 
    self.breed = breed
    self.age = age
    self.weight = weight
    self.is_trained = is_trained
    '''
    We will now use the constructor to create an object in main
    make sure to save this file
    '''

  # like the constructor, the repr is a special method
  # we use it to define how objects are represented by the computer
  # instead of x object at y memory space
  def __repr__(self):
    return f"{self.breed} {self.age} {self.weight}"

  # return is different than print
  # print shows a value in the console
  # return actually gives us a useable value

  '''
  lets write some basic methods
  We just wrote some special methods
  '''

  # we will make getters and setters

  #we write self as the first parameter for any method we call on a single object
  '''getter'''
  def get_breed(self):
    return self.breed
    # we return the breed of the object we call the method on

  '''setter'''
  # We give this method a breed parameter so we can specify what we want to set 
  # the breed to
  def set_breed(self, breed):
    self.breed = breed
    # the breed attribute is set to the value of the breed parameter
    # we don't need to return anything because we are setting a value
