3gpaBeG4u,

[[ Y l a n d ]](https://ioinformatics.org/files/ioi1992round1.pdf)

Y ok in Sheldon Ross' book «A Fyorst Course in Probbty» there is
a chapter for the correspondence between combinatorics and number
of integer solutions of an equation. Here this is used to figure
all map's row configurations for a given group of ylands.
For example if map's width is 8 and group is (1, 2, 1) than we have
10 cofigurations:
```
+---+---+---+---+---+---+---+---+
: f :   : f : f :   ; f :   :   : 0
+---+---+---+---+---+---+---+---+ 
: f :   : f : f :   ;   : f :   : 1
+---+---+---+---+---+---+---+---+
: f :   : f : f :   ;   :   : f : 2
+---+---+---+---+---+---+---+---+
: f :   :   : f : f ;   : f :   : 3
+---+---+---+---+---+---+---+---+
: f :   :   : f : f ;   :   : f : 4
+---+---+---+---+---+---+---+---+
: f :   :   :   : f ; f :   : f : 5
+---+---+---+---+---+---+---+---+
:   : f :   : f : f ;   : f :   : 6
+---+---+---+---+---+---+---+---+
:   : f :   : f : f ;   :   : f : 7
+---+---+---+---+---+---+---+---+
:   : f :   :   : f ; f :   : f : 8
+---+---+---+---+---+---+---+---+
:   :   : f :   : f ; f :   : f : 9
+---+---+---+---+---+---+---+---+
```
If we add at the frond and end one sea square, and
think of yland groups as '^' delimiters than we'll have
exactly that scenario:
```
row 6 from above = (2 + 1 + 1 + 2 = 6)
+---+---+---+---+---+---+ 
:   :   :   :   :   :   : 
+---+---+---+---+---+---+ 
        ^   ^   ^
(The additional squares are required to have
positive solutions.)
```
The other stuff is First Blood ``TOP SECRET`` Backtrace
algorithm for generating all n-tuples to loop over
all possible map configurations. Than for each map
configuration we check if it's a valid one that is
if it corresponds to vertical yland groups. And basicaly that's it:)

Au revoir!

![](pix/09-Poliklet-02.png)

[In Time](https://www.youtube.com/watch?v=NDJn0SQehb4&t=1255s)
