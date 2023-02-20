
# Milestone 1:
## Github Repo Link
https://github.com/theashwin/ml4se

## Team Members
```
Ashwin Patil <anpatil2@illinois.edu>
Chinmay Saraf <csaraf2@illinois.edu>
Kedar Takwane <takwane2@illinois.edu>
Maahi Patel <maahidp2@illinois.edu>
```

## Dataset used for Code Analysis:
- We have used [CodeSearchNet](https://github.com/github/CodeSearchNet) dataset<br>
### Python
- As CodeQL needs .py file for python based code analysis, we extracted random 100 functions from CodeSearchNet dataset using code from [notebook](https://github.com/theashwin/ml4se/blob/main/notebooks/get_data.ipynb)
- The json format of datapoints can be found in [python-data](https://github.com/theashwin/ml4se/blob/main/data/python.json)
- The [folder](https://github.com/theashwin/ml4se/tree/main/data/functions/py) has all .py files considered for the analysis.
### Java
- As CodeQL needs java project for java code analysis, we have imported [hazelcast](https://github.com/hazelcast/hazelcast) repository which is one of the repository used by CodeSearchNet in its dataset.
- We have considered some java files from [hazelcast](https://github.com/hazelcast/hazelcast) in the code analysis. The [folder](https://github.com/theashwin/ml4se/tree/main/data/functions/java) has all .java files considered for the analysis.
- The json format of datapoints can be found in [java-data](https://github.com/theashwin/ml4se/blob/main/data/java.json)


## Code for Data flow:
## Code for Control flow:
## Instructions about how to use the code: 
