# Multiple Inheritance
> In languages that use multiple inheritance, the order in which base classes are
> searched when looking for a method is often called the Method Resolution Order,
> or MRO.


* [Explanation by Guido](http://python-history.blogspot.com/2010/06/method-resolution-order.html)

> lets take an example

```python

class O(): pass

class A(O): pass

class B(O): pass

class C(O): pass

class D(O): pass

class E(O): pass

class K1(A, B, C): pass

class K2(D, B, E): pass

class K3(D, A): pass

class Z(K1, K2, K3): pass

```


Image
![alt text][C3_linearization_example]

> the linearization of Z is computed as

```
L(O)  := [O]                                                // the linearization of O is trivially the singleton list [O], because O has no parents

L(A)  := [A] + merge(L(O), [O])                             // the linearization of A is A plus the merge of its parents' linearizations with the list of parents...
       = [A] + merge([O], [O])
       = [A, O]                                             // ...which simply prepends A to its single parent's linearization

L(B)  := [B, O]                                             // linearizations of B, C, D and E are computed similar to that of A
L(C)  := [C, O]
L(D)  := [D, O]
L(E)  := [E, O]

L(K1) := [K1] + merge(L(A), L(B), L(C), [A, B, C])          // first, find the linearizations of K1's parents, L(A), L(B), and L(C), and merge them with the parent list [A, B, C]
       = [K1] + merge([A, O], [B, O], [C, O], [A, B, C])    // class A is a good candidate for the first merge step, because it only appears as the head of the first and last lists
       = [K1, A] + merge([O], [B, O], [C, O], [B, C])       // class O is not a good candidate for the next merge step, because it also appears in the tails of list 2 and 3, but...
       = [K1, A, B] + merge([O], [O], [C, O], [C])          // ...class B qualified, and so does class C; class O still appears in the tail of list 3
       = [K1, A, B, C] + merge([O], [O], [O])               // finally, class O is a valid candidate, which also exhausts all remaining lists
       = [K1, A, B, C, O]

L(K2) := [K2] + merge(L(D), L(B), L(E), [D, B, E])
       = [K2] + merge([D, O], [B, O], [E, O], [D, B, E])    // select D
       = [K2, D] + merge([O], [B, O], [E, O], [B, E])       // fail O, select B
       = [K2, D, B] + merge([O], [O], [E, O], [E])          // fail O, select E
       = [K2, D, B, E] + merge([O], [O], [O])               // select O
       = [K2, D, B, E, O]

L(K3) := [K3] + merge(L(D), L(A), [D, A])
       = [K3] + merge([D, O], [A, O], [D, A])               // select D
       = [K3, D] + merge([O], [A, O], [A])                  // fail O, select A
       = [K3, D, A] + merge([O], [O])                       // select O
       = [K3, D, A, O]

L(Z)  := [Z] + merge(L(K1), L(K2), L(K3), [K1, K2, K3])
       = [Z] + merge([K1, A, B, C, O], [K2, D, B, E, O], [K3, D, A, O], [K1, K2, K3])    // select K1
       = [Z, K1] + merge([A, B, C, O], [K2, D, B, E, O], [K3, D, A, O], [K2, K3])        // fail A, select K2
       = [Z, K1, K2] + merge([A, B, C, O], [D, B, E, O], [K3, D, A, O], [K3])            // fail A, fail D, select K3
       = [Z, K1, K2, K3] + merge([A, B, C, O], [D, B, E, O], [D, A, O])                  // fail A, select D
       = [Z, K1, K2, K3, D] + merge([A, B, C, O], [B, E, O], [A, O])                     // select A
       = [Z, K1, K2, K3, D, A] + merge([B, C, O], [B, E, O], [O])                        // select B
       = [Z, K1, K2, K3, D, A, B] + merge([C, O], [E, O], [O])                           // select C
       = [Z, K1, K2, K3, D, A, B, C] + merge([O], [E, O], [O])                           // fail O, select E
       = [Z, K1, K2, K3, D, A, B, C, E] + merge([O], [O], [O])                           // select O
       = [Z, K1, K2, K3, D, A, B, C, E, O]                                               // done
```

## Example demonstrated in Python

```python
class A(object): pass

class B(object): pass

class C(object): pass

class D(object): pass

class E(object): pass

class K1(A, B, C): pass

class K2(D, B, E): pass

class K3(D, A): pass

class Z(K1, K2, K3): pass

Z.mro()
```
> output
```python
[<class '__main__.Z'>, <class '__main__.K1'>, <class '__main__.K2'>, <class '__main__.K3'>, <class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.E'>, <type 'object'>]

[Z, K1, K2, K3, D, A, B, C, E, <type 'object'>]


```
[References][wiki_link]


[C3_linearization_example]: images/C3_linearization_example.svg.png "Logo Title Text 2"
[wiki_link]: https://en.wikipedia.org/wiki/C3_linearization#example