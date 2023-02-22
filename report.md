# Report for assignment 3

This is a template for your report. You are free to modify it as needed.
It is not required to use markdown for your report either, but the report
has to be delivered in a standard, cross-platform format.

## Project

Name: Nicholas von Butovitsch, Tianyu Deng, August Tengland, Anna Kristiansson, Kaan Ucar

URL: https://github.com/august-tengland/DD2480_lab3_TheAlgorithms_Python

Summary of TheAlgorithms_Python:
TheAlgorithms_Python from https://github.com/TheAlgorithms/Python is a series of implemented algorithms designed to be readily available and easy to use. 

## Onboarding experience

Did it build and run as documented?
    
See the assignment for details; if everything works out of the box,
there is no need to write much here. If the first project(s) you picked
ended up being unsuitable, you can describe the "onboarding experience"
for each project, along with reason(s) why you changed to a different one.

## Complexity

### Complexity results
| Function           | Manual CC (Primary) | Manual CC (Secondary) | Lizard CC   | Lizard NLOC |
| ------------------ |---------------------|-----------------------| ----------- | ----------- |
|HSV-RGB Conv.       | 13                  | 13                    | 17          | 62          |
|RB-Tree Delete      | 18                  | 18                    | 19          | 42          |
|Conv. Num to Words  | 15                  | 15                    | 16          | 96          |
|Quine Mc Cluskey    | 17                  | 17                    | 17          | 42          |
|Points to Poly      | 16                  | 16                    | 21          | 86          |
|kg_v                | 16                  | 16                    | 17          | 86          |


1. Did all methods (tools vs. manual count) get the same result?
2. Are the results clear?
### Question Regarding Complexity
2. Are the functions just complex, or also long?
3. What is the purpose of the functions?
4. Are exceptions taken into account in the given measurements?
5. Is the documentation clear w.r.t. all the possible outcomes?

## Refactoring

Plan for refactoring complex code:

Estimated impact of refactoring (lower CC, but other drawbacks?).

Carried out refactoring (optional, P+):

git diff ...

## Coverage

### Tools

Document your experience in using a "new"/different coverage tool.

How well was the tool documented? Was it possible/easy/difficult to
integrate it with your build environment?

### Your own coverage tool

Show a patch (or link to a branch) that shows the instrumented code to
gather coverage measurements.

The patch is probably too long to be copied here, so please add
the git command that is used to obtain the patch instead:

git diff ...

What kinds of constructs does your tool support, and how accurate is
its output?

### Coverage Results (Before Adding New Tests)

| Function           | Manual BC   | Automatic BC| 
| ------------------ | ----------- | ----------- |
|RGB-HSV Conv.       |             |             |
|RB-Tree Delete      | 52%         | 55%         |
|Conv. Num to Words  | 54%         | 79%         |
|Quine Mc Cluskey    | 61%         | 69%         |
|Points to Poly      | 92%         |             |
|kg_v                | N/A         | 3%          |

### Evaluation

1. How detailed is your coverage measurement?

2. What are the limitations of your own tool?

3. Are the results of your tool consistent with existing coverage tools?

## Coverage improvement

Show the comments that describe the requirements for the coverage.

Report of old coverage: [link]

Report of new coverage: [link]

Test cases added:

git diff ...

### Coverage Results (After Adding New Tests)

| Function           | Manual BC   | Automatic BC| 
| ------------------ | ----------- | ----------- |
|RGB-HSV Conv.       |             |             |
|RB-Tree Delete      | 79%         | 84%         |
|Conv. Num to Words  | 88%         | 92%         |
|Quine Mc Cluskey    | 94%         | 97%         |
|Points to Poly      | 98%         |   %         |
|kg_v                | N/A         | 82%         |

## Self-assessment: Way of working

Current state according to the Essence standard: ...

Was the self-assessment unanimous? Any doubts about certain items?

How have you improved so far?

Where is potential for improvement?

## Overall experience

What are your main take-aways from this project? What did you learn?

Is there something special you want to mention here?
