# AoC2020

Contains my solutions to the AoC2020 puzzles. 
Most puzzles were completed on the day of release in Python, with the exception of days 19 and 20. Code has not yet been tidied up - you have been warned.

General summary of the Python solutions is below:

## Day 1: Report Repair
### Part 1:
An easy intro to my first AoC problem. I used quite a naive approach where I first added all the input numbers to a set. I then looped through the input numbers again to subtract them from the desired result. I could then check if the result of the subtraction was in the set I had created.
### Part 2:
Effectively used the same approach as part 1 except fixed one of the numbers first to then find the other 2. Nothing more taxing was required so I didn't need to improve on it.

## Day 2: Password Philosophy
### Part 1:
Fairly trivial - created a function that split a line of the input into the required values and applied the rules to return a boolean value.
### Part 2:
Another nice part 2, split each line as before and simply apply the new rules.

## Day 3: Toboggan Trajectory
### Part 1:
Cheesed part of this problem by using some magic numbers to create the slope. The problem specified that the given input would repeat many times to the right so I wrote a tiny function that did just that. Initially I think I just repeated it 10 times and that was more than enough for part 1.
Otherwise I just used a separate function to traverse the slope at the given rate and count the trees returning the desired value.
### Part 2:
Cheesing the slope for part 1 came back to bite me here and resulted in an incorrect first submission because I forgot to extend the slope further to accomodate the longer traversals. Rather than remedy this I just upped the limit to 100x the original input... not the cleanest solution.
Fortunately, because of the way that I had written my tree_counter function for part 1 it was plug and play for part 2, just inputting the different gradients.

Today was also the first day where I learned to use a context manager for reading the input file - great success!

## Day 4: Passport Processing
### Part 1:
Having never been exposed to regex before I ended up writing a very long 100+ line solution for this where each field had a function which checked the rules applicable to that value and returned a boolean for validity. Having now seen others solutions to this and having been forced into learning regex by problems from later days I may return to write a more compact solution to this.
### Part 2:
There was not too much special about this part 2 other than the addition of more rules. For my solution this just meant adding more logic to each of the functions.

## Day 5: Binary Boarding
### Part 1:
Taking inspiration from the name of the problem I created a function which rebuilt the seat code as a binary string and then converted it to an integer. A separate function calculated the "seat id" as described by the problem.
### Part 2:
I took a fairly straighforward approach to the part 2 of this problem. I created a list of all of the seats and then sorted it. This meant that I could iterate through each seat and check for a skipped one - the missing seats at the beginning and end were neutralised.

## Day 6: Custom Customs