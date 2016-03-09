# inheritance
 > Classes can inherit functionality from other classes, let’s take a
 > look at how that works. We start with a basic class:

 ```python
class User:
    name = ""

    def __init__(self, name):
        self.name = name

    def printName(self):
        print "Name  = " + self.name

brian = User("brian")
brian.printName()
 ```

 > This creates one instance called brian which outputs its given name.
 > Add another class called Programmer.


```python
class Programmer(User):

    def __init__(self, name):
        self.name = name
    def doPython(self):
        print "Programming Python"
```



> This looks very much like a standard class except than User is given in the
> parameters. This means all functionality of the class User is accesible in the
> Programmer class.

### Full example of Python inheritance:

```python
class User:
    name = ""

    def __init__(self, name):
        self.name = name

    def printName(self):
        print "Name  = " + self.name

class Programmer(User):
    def __init__(self, name):
        self.name = name

    def doPython(self):
        print "Programming Python"

brian = User("brian")
brian.printName()

diana = Programmer("Diana")
diana.printName()
diana.doPython()
```


> The output:
```python
Name  = brian
Name  = Diana
Programming Python
```

> Brian is an instance of User and can only access the method printName.
> Diana is an instance of Programmer, a class with inheritance from User,
> and can access both the methods in Programmer and User.

