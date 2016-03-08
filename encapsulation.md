> Encapsulation
> In an object oriented python program, you can restrict access to methods and
> variables. This can prevent the data from being modified by accident and is
> known as encapsulation.  Let's start with an example.

```python
class Mobile:

    def __init__(self):
        self.__update_software()

    def switch_on(self):
        print 'driving'

    def __update_software(self):
        print 'updating software'

smobile = Mobile()
smobile.switch_on()
#smobile.__updateSoftware()  not accesible from object.

print('-'*100)
```
> Explanation
> The private method  __update_software() can only be called within the class
> itself.  It can never be called from outside the class.


> Private variables
> Variables can be private which can be useful on many occasions.
> Objects can hold crucial data for your application and you do not want that
> data to be changeable from anywhere in the code. An example:

```python
class Mobile:

    __os = 'andriod'
    __name = ""

    def __init__(self):
        self.__os = 'andriod'
        self.__name = "Supercar"

    def switch_on(self):
        print 'Mobile Os is ' + str(self.__os)

smobile = Mobile()
smobile.switch_on()
smobile.__os = 'ios'  > will not change variable because its private
smobile.switch_on()
print('-'*100)
```
> If you want to change the value of a private variable, a setter method is used.
> This is simply a method that sets the value of a private variable.

```python
class Mobile:

    __os = 'andriod'
    __name = ""

    def __init__(self):
        self.__os = 'andriod'
        self.__name = "Supercar"

    def switch_on(self):
        print 'Mobile Os is ' + str(self.__os)

    def set_os(self, os):
        self.__os = os

smobile = Mobile()
smobile.switch_on()
smobile.set_os('ios')
smobile.switch_on()

print('-'*100)
```

> Summary
> To summarize, in Python there are:

Type | Description
--- | ---
public methods      | accessible from anywhere
private methods     | accessible only in their own class. starts with two underscores
public variables    | accessible from anywhere
private variables   | accesible only in their own class or by a method if defined. starts with two underscores
