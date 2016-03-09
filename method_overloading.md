
> In Python you can define a method in such a way that there are multiple ways to call
> it. This is known as method overloading. We do that by setting default values of
> variables. Let us do an example:

```python
class Mobile:

    def get_brand(self, brand=None):

        if brand is not None:
            print brand
        else:
            print 'Generic '

# Create instance
obj = Mobile()

# Call the method
obj.get_brand()

# Call the method with a parameter
obj.get_brand('Samsung')

```

#### Output:

> Hello

> Hello Samsung

> To clarify method overloading, we can now call the method sayHello() in two ways:

```python
obj.get_brand()
obj.get_brand('Samsung')
```

> We created a method that can be called with fewer arguments than it is defined
> to allow. We are not limited to two variables, your method could have more
> variables which are optional.

