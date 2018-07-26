# Mars Rover

Solution of the Mars Rover challenge described [here](https://github.com/abdulg/Mars-Rover).

"*A squad of robotic rovers are to be landed by NASA on a plateau on Mars.*

*This plateau, which is curiously rectangular, must be navigated by the rovers so that their on board cameras can get a complete view of the surrounding terrain to send back to Earth.*

*A rover's position is represented by a combination of an x and y co-ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North.*

*In order to control a rover, NASA sends a simple string of letters. The possible letters are 'L', 'R' and 'M'. 'L' and 'R' makes the rover spin 90 degrees left or right respectively, without moving from its current spot.*

*'M' means move forward one grid point, and maintain the same heading.*

*Assume that the square directly North from (x, y) is (x, y+1).*

*Input:*

*Configuration Input: The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be 0,0.*

*Per Rover Input:*

*Input 1: Landing co-ordinates for the named Rover. The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the rover's orientation.*

*Input 2: Navigation instructions for the named rover. i.e a string containing ('L', 'R', 'M').*"

## Some edge cases
* It is not possible to land outside of plateau;
* It is not possible to land on a busy grid position;
* It is not possible to move outside of plateau;
* It is not possible move to a busy grid position, it will reset to the initial position.
* It is not possible to use plateau on negatives positions (0 > x or y )
* Once plateau is defined, it is not possible to overwrite it.

## Usage
* Python 2.7.2 is required, so please install [here](https://www.python.org/downloads/).
* Type on terminal: git clone https://github.com/DayanneAraujo/mars-rover.git
* cd mars-rover
* In order to execute the command line app, run the app.py file
```
python app.py
```
## I/O

**Input Example**
```
Plateau:5 5
Rover1 Landing:1 2 N
Rover1 Instructions:LMLMLMLMM
Rover2 Landing:3 3 E
Rover2 Instructions:MMRMMRMRRM
```
**Expected Example**
```
Rover1:1 3 N
Rover2:5 1 E
```
**Executing the unit tests**
```
python -m unittest discover
```

_enjoy it_

License
----

[MIT](https://opensource.org/licenses/MIT)