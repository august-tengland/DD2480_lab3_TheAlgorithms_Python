# Report for assignment 3

The following is the report for Assignment 3 in DD2480, by Group 21

## Project

Name: Nicholas von Butovitsch, Tianyu Deng, August Tengland, Anna Kristiansson, Kaan Ucar

URL: https://github.com/august-tengland/DD2480_lab3_TheAlgorithms_Python

**Summary of TheAlgorithms_Python:**
TheAlgorithms_Python from https://github.com/TheAlgorithms/Python is a series of implemented algorithms and data structures in Python, designed primarily for educational purposes and ease-of-use. 

## Onboarding experience

The project provides all necessary requirements in “requirement.txt”, meaning that we just had to copy the repository and run “pip install -r .\requirements.txt”. The project did not specify which Python 3 version had compatibility with the project however this did not cause us any issues (the group used different versions of python, from 3.8 to 3.11). The requirement list also included the necessary dependencies for running tests (with “doctest” and “pytest”) which meant that we had everything we needed to run and test the different files.  

Since everything went well and the difficulty of the project was satisfactory, after confirming that the project meets the assignment requirements, we decided to pick the project.



## Complexity

In the section below, we detail our experience with analyzing the cyclomatic complexity of project functions using "Lizard" and by hand. We first discuss 10 functions with high complexity (as provided by Lizard), and then provide a table with 6 functions that were also analyzed manually by two people.   

### List of 10 functions with high complexity:


#### \_remove\_repair @ red black tree : 31CC
\_remove\_repair@212-283@.\data_structures\binary_tree\red_black_tree.py  

\_remove\_repair() is a helper function (to the earlier discussed remove() function) that repairs the coloring of a red black tree that might have been ruined by the removal of a node. The function does a number of assertions (comparing nodes with their siblings, parents etc.) and changes colors accordingly.  

The cyclomatic complexity is very high and the function is mainly composed of a number of sequential if statements.  The cyclomatic complexity is somewhat motivated because it mainly depends on the large number of clauses that are present in each “if-statements” (usually 2-4, tied together with “and” or “or”). It is however very difficult to understand what the function and each if-statement concerns, since the code is not commented. This means that there is a value in partitioning the function into smaller ones with meaningful function-names OR providing adequate comments.  

#### points_to_polynomial @ point to polynomials : 21CC
points_to_polynomial @linear_algebra/src/polynom_for_points.py  

This function matches an appropriate polynomial function to a set of two dimensional points given as input. 
Though the cyclomatic complexity of 21 is high, I think it’s mostly justified. First, a lot of complexity in Point to Polynomials is dedicated to raising potential errors and preventing this function from crashing. Then the calculations for the polynomials contributes to raising the complexity more. 

#### remove @ red black tree : 20CC
remove@155-210@@.\data_structures\binary_tree\red_black_tree.py  

The remove() function defines the removal of a given node in an implementation of the “red black tree” data structure. The function recursively travels down the tree until it finds the node to remove, it thereafter alters the positions and colors of all nodes below and around the node so that it can finally be removed easily.  

The complexity of the function is arguably justified, however there is room for improvement. For example, the two steps of finding and removing a node could be partitioned into two separate functions. There is also only one major return statement, at the end of the function, and it is somewhat difficult to comprehend how the branches end up there (meaning that more returns could be added for ease of understanding). Finally, there is a clear distinction between how “red” and “black” tree-nodes are deleted, meaning that these functionalities could also be partitioned into separate functions to reduce complexity. 

#### sol_1 : 20CC  
solution@95-149@.\project_euler\problem_049\sol1.py  

First, it generates all 4 digits prime numbers. Then greedy all of them and use permutation to form new numbers. Use binary search to check if they are prime and include them in a candidate list. After that, bruteforce all passed candidates sequences.
Its cyclomatic complexity should be high because the logic is not simple. The file has some help functions and the solution function has fairly high readability for me. And since we need to follow some steps to solve the problem and there are some nested loops, the solution function should have high complexity in my opinion.  

#### new generation : 19CC
new_generation@25-70@.\cellular_automata\conways_game_of_life.py  

Conway’s Game of Life is a zero-player game, its evolution is determined by its initial state only. So one interacts with the Game of Life by creating an initial configuration and observing how it evolves. The new_generation function generates the next generation of a given state of the game. Essentially, we just need to check each cell of the game and its adjacent neighbors to determine the next state of a cell. Of course there are rules in this game and that's why this function is mainly constituted of boolean statements to determine the next state of a given cell. 
The high cyclomatic complexity comes from the high number of boolean statements, we can reduce this number by breaking down the boolean statements into multiple helper functions but in my opinion it is not a good idea since the code becomes less readable, we would have to check each other function while it is only simple boolean algebra.


#### Quine Mc Cluskey : 17CC
selection@84-144@.\boolean_algebra\quine_mc_cluskey.py  

The Quine McCluskey class is a method used for minimization of Boolean functions. The selection function implements the selection step in the Quine McCluskey algorithm for minimizing boolean functions. The selection step selects a set of prime implicants that can be used to represent the given boolean function with the minimum number of terms.  

The function has two inputs; a two-dimensional “chart” and a list of strings “prime_implicants”. The “chart” stores 1’s and 0’s representing the minterms and doesn't care for the boolean function to be minimized. Each row corresponds to a prime implicant and each column corresponds to a minterm or don’t care.  

The high cyclomatic complexity is arguably unjustified as the function goes through several steps in the function that can be separated into several smaller functions which would improve readability significantly.  

#### hsv to rgb conversion : 17CC  
hsv_to_rgb@15-81@.\conversions\rgb_hsv_conversion.py  

The RGB color model is an additive color model in which red, green and blue light are added together in various ways to reproduce a broad array of colors. Meanwhile, the HSV representation models how colors appear under light using three components : hue, saturation and brightness value. The function converts a color in hsv representation to the rgb one. Essentially, it is just a few value calculations and a switch on the hue_section which is the hue component divided by 60.  

The high cyclomatic complexity comes from the high number of boolean statements, we can reduce this number by breaking down the boolean statements into multiple helper functions but in my opinion it is not a good idea since the code becomes less readable, we would have to check each other function while it is only simple boolean algebra.

#### kg_v : 17CC
kg_v@353-419@.\maths\primelib.py  

Finds the least common multiple of two positive integers. The high cyclomatic complexity is in my opinion justified as the code is readable and aims to tackle one problem with 1 essential algorithm/step. A large part of the complexity comes from checking both numbers are positive integers and iterating through all the prime factors of each number. One could possibly divide this function through refactoring; identifying the prime factors could be put into a separate function.  

#### convert number to words : 16CC  
convert@4-105@.\web_programming\convert_number_to_words.py  

First, it creates some dictionary singles, doubles, teens, placevalue since people count number in words only use some specific collections of words. Then determine whether the given number is 0, and return "zero" if it is. Otherwise, it do a while loop which starts from the lowest digit of the given input number. In the loop, it discusses the case of odd and even digits, as well as some special cases, such as when the digit is 1, 2, or 3.
Its cyclomatic complexity should be high because only one function is used to achieve the required functions. But since the logic of this function is a little bit complex, it should be better if we create some help functions to improve the readability. This will reduce the cyclomatic complexity.


#### Hill Climbing : 16CC 
hill_climbing@86-160@.\searches\hill_climbing.py  

Hill climbing is a greedy local search algorithm that is goal oriented rather than path oriented. It will keep track of which neighbors are already visited and consider which neighbor has the best state and move to this neighbor, until all the neighbors have a lower state, which would mean we have reached the top and then the current state will be returned as the solution state.  

The function hill_climbing is part of the SearchProblem class and this function seems unnecessarily complex. It seems like it could be further divided into one or two helper functions. One example is the for neighbor in neighbors: line (line 124) that contains a lot of if statements, which could make up one of the helper functions. We also have if visualization: (line 152) and here the visualization commands could also be moved out into a helper function.

### Complexity results (Manual and Automatic)
| Function           | Manual CC (Primary) | Manual CC (Secondary) | Lizard CC   | Lizard NLOC |
| ------------------ |---------------------|-----------------------| ----------- | ----------- |
|HSV-RGB Conv.       | 13                  | 13                    | 17          | 62          |
|RB-Tree Delete      | 18                  | 18                    | 19          | 42          |
|Conv. Num to Words  | 15                  | 15                    | 16          | 96          |
|Quine Mc Cluskey    | 17                  | 17                    | 17          | 42          |
|Points to Poly      | 16                  | 16                    | 21          | 86          |
|kg_v\*              | 16                  | 16                    | 17          | 86          |


\*NOTE: Kg_v is included as an extra function since we added tests to it as well (for P+).

**1. Did all methods (tools vs. manual count) get the same result?**  
No, in all cases but one we got different results when calculating CC by hand and when using Lizard. The reason for this seems to be that Lizard calculates CC as the number of decision points + 1, and doesn't concern itself with more then one exit point. Using this reasoning we got the same results as Lizard, however we decided to use the formula "decisions - endpoints + 2" since it's the formula provided in the course.  

**2. Are the results clear?**  
The results are clear in that they are consistent for the different functions and between reviewers (meaning that the formula provided consistent results for different people). It is however hard to determine how the CC-value correlates with actual complexity, especially when the results differs when using different formulas (such as how Lizard does it).  

### Question Regarding Complexity
**1. Are the functions just complex, or also long?**  
Most of the examined functions are complex in NLOC as well as CC, however there are cases where they do not correlate. For example, adding return-statements will increase the lines of code but decrease the cyclomatic complexity, something that is noticable in some of the functions.  '

**2. Are exceptions taken into account in the given measurements?**  
None of the functions that we examined had explicit try-catch clauses to handle exceptions, but instead had if-statements that raised exceptions when evaluated to true. We did however, when deciding upon how CC would be calculated, establish that exception-clauses should be considered as a "decisions" in the regard that they establish new paths for the execution.  

**3. Is the documentation clear w.r.t. all the possible outcomes?**  
No, the documentation in the code is lacking and is also very inconsistent between files. 

## Refactoring

In the section below we detail our refactoring plans for five functions with high CC, as well as where to find the actual refactorings in the project (in the "master" branch, see "master-before-tests" to view the functions before refactoring).  

### Quine Mc Cluskey - Nicholas von Butovitsch

The function has a relatively high cyclomatic complexity of 16 (according to our metric decisions - endpoints + 2). I would argue that it isn’t very justified and can be seen as unnecessarily long as it aims to perform several steps. Therefore, it makes sense to separate it into a few distinct steps. To reduce the cyclical complexity, the selection function can be divided into three separate functions:

essential_primes(chart: list[list[int]]) -> list[str]:   
This function will take a chart as input and returns a list of essential prime implicants. It implements the first step of the selection process described above.

select_remaining(chart: list[list[int]], prime_implicants: list[str]) -> list[str]:    
This function will take a chart and the list of prime implicants as input, and returns a list of remaining prime implicants that are not essential but are still required to be selected.

selection(chart: list[list[int]], prime_implicants: list[str]) -> list[str]:   
This function takes the chart and the list of prime implicants as input, and returns the complete set of prime implicants for the minimized boolean expression. It calls the essential_primes() and select_remaining() functions internally to implement the complete selection.  

This will lower the cyclical complexity significantly, the results are shown in the master branch selection@84-144@.\boolean_algebra\quine_mc_cluskey.py
with a cyclomatic complexity of 6, 7, 5 according to our metric.   

### Convert number to words - Tianyu Deng
The function convert@4-105@.\web_programming\convert_number_to_words.py has high cyclomatic complexity and this leads to poor readability. I refactored the function to reduce cyclomatic complexity. My first idea was to put special cases in a function, but that's not very easy to do. A simpler refactoring is to classify even and odd digits:
The functions convert_when_even_digit and convert_when_odd_digit are used to define the rules for generating words. The special cases are still discussed separately in the functions, that is, when the digits are ones, tens and hundreds. The readability of these two functions is still not high, because the design logic of the functions is not very clear.
Thus, the original function convert only needs to consider whether the number is 0 or not, and then call the two functions mentioned above as help functions in a while loop.
Refactoring reduces cyclomatic complexity of functions. The cyclomatic complexities of the three new functions are 6, 6, 3. The refactored file is located at the master branch .\web_programming\convert_number_to_words.py

### HSV to RGB conversion - Kaan Uçar
In my opinion, the function is quite a simple one and it did not need refactoring, however, to reduce the complexity I simply put the switch on the hue_section (mentioned above) in another function called helper since it is simply a series of if statements. Nevertheless, I need to say that this worsens the readability of the code due to its simplicity beforehand. Additionally, the cyclomatic complexity of the original function is reduced but we simply transferred the complexity from the original function to the helper function.
The refactored file is located at the master branch : hsv_to_rgb@15-81@.\conversions\rgb_hsv_conversion.py 

### Point to Polynomials - Anna Kristiansson
This function had (according to Lizard) a CC of 21. I don’t think the readability was too bad, but you need to have an understanding of how polynomials relate to points in order to be able to read it correctly, which isn’t very handy if you don’t have a lot of time. I refactored this function by moving an extensive while loop out of the main points_to_polynomial(coordinates: list[list[int]]) into a helper function.
Another way to do it is by creating a helper function for the error controls, but I didn’t do this.
You can find the refactored file in the main branch at points_to_polynomial @linear_algebra/src/polynom_for_points.py

### “Remove” in Red Black Tree - August Tengland
The “remove” function in red_black_tree.py had a previous cyclomatic complexity of 19 (using our metric of decisions - endpoints + 2). This complexity is arguably justified however there are a number of ways to decrease it. One of the easiest is to partition the remove() function into two steps (or functions), one which finds the node to remove, and one that alters the tree: 
- remove(self), which recursively searches the tree for the node to remove
- \_remove_this_node(self): which alters the tree for removal of the node as specified by “self”.  

The removal function is also very distinct in how it handles the removal or “red” versus “black” nodes, something that allows for further partitioning:  
- remove(self), which recursively searches the tree for the node to remove  
- \_remove_this_node(self): determines color of node to remove and call further:
- \_remove_red(self,child): Removal of a red node 
- \_remove_red(self,child): Removal of a red node 

After refactoring, the remove() function went from a CC of 19 to 6 (a 68% reduction) and all of the created helper functions also have a CC equal or lesser than 6. 


## Coverage

The section below details our manual and automatic branch coverage of the 5 selected functions.

### Automatic coverage: Coverage.py

In order to evaluate the branch coverage of the existing suites, we used the "coverage.py" tool. 
Coverage.py primarily measures line coverage but you can add a flag so that it also examines branches, 
we found it easy to work with and it integrates well with the different testing methods used in the project (pytest, doctest). 
One issue with coverage.py is that you cannot specify with function to validate, meaning that it analyzes the entire python file that you run. 
It is however possible to add comments to lines and functions that you want to ignore, meaning that you can choose exactly what to check coverage for. 
Another issue with coverage.py, and one that we did not find a good solution for, is that it does not provide a value for only "branch coverage" but rather an aggregate of both branches and lines. This is the value that we provided in our report, but it means that there will almost always be some difference between the automatic and manual branch calculations.  

### Your own coverage tool

We implemented manual branch coverage analysis in the simple way that the assignment suggested: By creating a globally defined list with flags that were set to true for each branch that the program visited. The coverage tool is visible in the branches [coverage-tool-before-test](https://github.com/august-tengland/DD2480_lab3_TheAlgorithms_Python/tree/coverage-tool-before-test) and [coverage-tool-after-test](https://github.com/august-tengland/DD2480_lab3_TheAlgorithms_Python/tree/coverage-tool-after-test). For direct links to the files that used the coverage tool (before new tests):  

[Red Black Tree](https://github.com/august-tengland/DD2480_lab3_TheAlgorithms_Python/blob/coverage-tool-before-test/data_structures/binary_tree/red_black_tree.py)  
  
[RGB-HSV Conversion](https://github.com/august-tengland/DD2480_lab3_TheAlgorithms_Python/blob/coverage-tool-before-test/conversions/rgb_hsv_conversion.py)  

[Convert Number to Words](https://github.com/august-tengland/DD2480_lab3_TheAlgorithms_Python/blob/coverage-tool-before-test/web_programming/convert_number_to_words.py)  

[Quine Mc Cluskey](https://github.com/august-tengland/DD2480_lab3_TheAlgorithms_Python/blob/coverage-tool-before-test/boolean_algebra/quine_mc_cluskey.py)  

[Points to Polynomial](https://github.com/august-tengland/DD2480_lab3_TheAlgorithms_Python/blob/coverage-tool-before-test/linear_algebra/src/polynom_for_points.py)  


### Coverage Results (Before Adding New Tests)

| Function           | Manual BC   | Automatic BC| 
| ------------------ | ----------- | ----------- |
|RGB-HSV Conv.       | 81%         | 87%         |
|RB-Tree Delete      | 52%         | 55%         |
|Conv. Num to Words  | 54%         | 79%         |
|Quine Mc Cluskey    | 61%         | 69%         |
|Points to Poly      | 92%         | 94%         |
|kg_v\*              | N/A         | 3%          |

\*NOTE: We calculated the branch coverage of kg_v using Coverage.py but not manually, since we only wanted to verify that our new test was productive (for P+). 


### Evaluation

**1. How detailed is your coverage measurement?**  
Our coverage measurement only concerns branch coverage and simply provides a percentual value of the number of branches that were covered. Some group members also implemented prints for viewing exactly which branches were covered or not, however analyzing this output requires looking at the code or control flow diagram of the program. We argue that the program does a precise job in what it is designed to do, and the tool can be altered to conform with other types of branches as well.

**2. What are the limitations of your own tool?**  
One issue of the "tool" is that it is not really a tool, but more of a procedure of analysis. A lot of manual labour is required for each function (adding lines that set flags, adding "elses" where they are missing) which introduces the risk of bugs and mistakes. It has also not been defined exactly how one would use the tool in regard to, for example, try-catch clauses which could introduce issues. 

**3. Are the results of your tool consistent with existing coverage tools?**  
No. As previously stated, the Coverage.py tool provides an aggregate of branch and line coverage, meaning that the results are likely to always differ somewhat. We did find that the automatic coverage tool found the same number of total branches as the manual tool. 

## Coverage improvement

New tests were added to increase the branch coverage results of our manual and automatic tools. The tests were added to the following files (and are visible in the master branch of the project):  

#### **Remove - Red Black Tree**  
Four tests commited by August Tengland in master branch  
[remove@.\data_structures\binary_tree\red_black_tree.py](./data_structures/binary_tree/red_black_tree.py)  
The tests are located between lines @659-725@  

#### **hsv to rgb conversion**  
Three new tests committed by Kaan Uçar in master branch   
[hsv_to_rgb@15-81@.\conversions\rgb_hsv_conversion.py](./conversions/rgb_hsv_conversion.py)    
The tests are located between lines @41-46@  

#### **Point to Polynomials**  
Three tests committed by Anna Kristiansson in master branch  
[points_to_polynomial @linear_algebra/src/polynom_for_points.py](./linear_algebra/src/polynom_for_points.py)    
The tests are located between lines @117-122@  

#### **convert number to words**  
Four new tests committed by Tianyu Deng in master branch   
[.\web_programming\convert_number_to_words.py](./web_programming/convert_number_to_words.py)   
The tests are located between lines @92-99@  

One new test committed by Kaan Uçar at master branch   
[.\web_programming\convert_number_to_words.py](./web_programming/convert_number_to_words.py)
The test is located between lines @100-101@  

#### **Quine Mc Cluskey**
Two additional tests committed by Nicholas von Butovitsch in master branch
[selection@84-144@.\boolean_algebra\quine_mc_cluskey.py](./boolean_algebra/quine_mc_cluskey.py) .
The tests are located between lines @125-128@.

#### **kg_v**
Two tests committed by Nicholas von Butovitsch in master branch address 
[kg_v@353-419@.\maths\primelib.py](./maths/primelib.py) 
The tests are located between lines @626-637@


### Coverage Results (After Adding New Tests)

| Function           | Manual BC   | Automatic BC| 
| ------------------ | ----------- | ----------- |
|RGB-HSV Conv.       | 100%        | 100%        |
|RB-Tree Delete      | 79%         | 84%         |
|Conv. Num to Words  | 88%         | 92%         |
|Quine Mc Cluskey    | 94%         | 97%         |
|Points to Poly      | 98%         | 98%         |
|kg_v                | N/A\*       | 82%         |


\*NOTE: We calculated the branch coverage of kg_v using Coverage.py but not manually, since we only wanted to verify that our new test was productive (for P+). 

## Self-assessment: Way of working

We believe that our group is operating in the “Performing” state. We think this because we have established guidelines and conventions in how we perform git commits and branches, which we have to a large extent been able to follow. Our team is adaptive, and been able to work, collaborate and assist each other where needed. The team members have also become more comfortable with one another, for example by eating lunches togheter, which we argue help the collaborative process. In order to achieve the next state “Adjourned” we will need to complete this assignment entirely in order to allow our focus to be on future assignments.

## Overall experience

This has been an informative assignment which has covered some of the basics in code testing. Some of the group members are reading the "software reliablity" course and have already encountered branch coverage, however it was useful to test tools for applying the theory. The group does however conclude that the use of git in this project was subpar, the conventions that were put up were generally good ideas however they were not that well-suited for a project of this scope. If we would've have re-done the assignment, we would probably have used git in a more flexible fashion and relied on other tools for documenting and writing the report.
