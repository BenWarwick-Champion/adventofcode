# AoC2020 - Python
This is just a general summary of my thoughts/learnings from each day of participating in the challenge. 

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
### Part 1:
This problem highlighted the usefulness of pythons sets to me. After parsing the inputs into separate groups, a simple function just added each response to a set of questions. The lack of duplicates in sets meant that each set could then be counted as the solution.
### Part 2:
With sets the extension to this problem was straightforward. The questions set was instead composed of the intersection of the sets for each person in the group.

After completing this problem I went onto the r/adventofcode subreddit and saw some far more compact solutions. Feeling inspired I wrote custom_customs_but_smaller.py and managed to reduce each part to a single line using map().

## Day 7: Handy Haversacks
### Part 1:
Solved the first problem using a stack. I first wrote a simple is_shiny() function to check if a bag contained a shiny gold one. A first pass through all the colours allowed me to prime the stack with those colours which directly contained a shiny gold bag. After that I popped each colour off the stack and searched for bags containing that colour adding all results back onto the stack as well as adding to a set. With the stack empty the set holds each unique colour that could hold a shiny gold bag.
### Part 2:
This was the first day where the problem took a little bit more thinking for me as I was not familiar with writing recursive solutions. It is one thing to see that it can be solved recursively and another to write it. Fortunately I was able to write a simple recursive function without too much trouble and in the end I found it more difficult to wrangle the data into the dictionary format which I wanted.

## Day 8: Handheld Halting
### Part 1 & 2:
There was nothing too difficult about this day, simply implementing the instructions as described for both parts.

## Day 9: Encoding Error
### Part 1 & 2:
Again, nothing groundbreaking from this day. Although for part 2 I had a foolish bug for a while where I returned the sum of the first and last elements in the contiguous list before I realised that the question was asking for the sum of the max and min instead.

## Day 10: Adapter Array
### Part 1:
After sorting the array this problem was trivial.

### Part 2:
I fared better writing the recursive function for this problem, unfortunately that was not enough. This time it was necessary to implement memoisation as well to avoid too much recalculation and to get the algorithm to run in reasonable time. After discovering what it was it did not take long to integrate it with my function.

## Day 11: Seating System

## Day 12: Rain Risk

## Day 13: Shuttle Search

## Day 14: Docking Data

## Day 15: Rambunctious Recitation

## Day 16: Ticket Translation

## Day 17: Conway Cubes

## Day 18: Operation Order

## Day 19: Monster Messages

## Day 20: Jurassic Jigsaw

## Day 21: Allergen Assessment

## Day 22: Crab Combat

## Day 23: Crab Cups

## Day 24: Lobby Layout

## Day 25: Combo Breaker
