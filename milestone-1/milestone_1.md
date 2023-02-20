
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


## CodeQL Queries and Python scripts
### Python
 - Code for Data flow: [python-data-flow](https://github.com/theashwin/ml4se/tree/main/milestone-1/python/data-flow)
 - Code for Control flow: [python-control-flow](https://github.com/theashwin/ml4se/tree/main/milestone-1/python/control-flow)

### Java
 - Code for Data flow: [java-data-flow](https://github.com/theashwin/ml4se/tree/main/milestone-1/java/data-flow)
 - Code for Control flow: [java-control-flow](https://github.com/theashwin/ml4se/tree/main/milestone-1/java/control-flow)

## Instructions about how to use the code: 

### Setup CodeQL CLI and Visual Studio Extension
1. [Install CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli/using-the-codeql-cli/getting-started-with-the-codeql-cli)
2. [Install VS Code extension and setting it up](https://codeql.github.com/docs/codeql-for-visual-studio-code/setting-up-codeql-in-visual-studio-code/) - Follow all steps mentioned in this link. Please check if the queries are running with given example database 

### Add Database
1. Open VS Code
2. Open CodeQL Window (click QL icon from left panel)
3. Hover on Databases tab - it'll show multiple icons to add database <br/>
    
    a. From Archive <br/>
    b. From Folder <br/>
    c. Download Database <br/>
    d. From Github <br/>
4. For Java, CodeQL needs whole Java Project. So, for this milestone we have used [hazelcast](https://github.com/hazelcast/hazelcast) Java project. Add database in CodeQL using **From Github** option. The VS Code window may pop out to selcting language. Select Java language.
5. For Python, CodeQL needs files with .py extension. For this milestone, we have added data in [folder](https://github.com/theashwin/ml4se/tree/main/data/functions/py). Add this database in CodeQL from **From Folder** option. The VS Code window may pop out to selcting language. Select Python language.
6. Under Databases tab in VS Code, hover on databases and click on **Set Current Database** to query respective database.

### Execute Queries
On VS Code's CodeQL window, through **Command Palette**, open **CodeQL: Quick Query**. This will open ``quick-query.ql`` file.

#### Java
- Control Flow - <br/>
    a. Copy content from [control_flow.ql](https://github.com/theashwin/ml4se/blob/main/milestone-1/java/control-flow/control_flow.ql) and paste it in ``quick-query.ql``. <br/>
    b. Right Click on Editor and select **CodeQL: Run Query on Selected Database**. <br/>

- Data Flow - <br/>
    a. Copy content from [data_flow.ql](https://github.com/theashwin/ml4se/blob/main/milestone-1/java/data-flow/data_flow.ql) and paste it in ``quick-query.ql``. <br/>
    b. Right Click on Editor and select **CodeQL: Run Query on Selected Database**. <br/>

#### Python
- Control Flow - <br/>
    a. Copy content from [control_flow.ql]() and paste it in ``quick-query.ql``. <br/>
    b. Right Click on Editor and select **CodeQL: Run Query on Selected Database**. <br/>

- Data Flow - <br/>
    a. Copy content from [data_flow.ql]() and paste it in ``quick-query.ql``. <br/>
    b. Right Click on Editor and select **CodeQL: Run Query on Selected Database**. <br/>

## Results

### Python
- Code Snippet #1
    1. Code Snippet
    ```
    ```
    2. Data Flow Graph - [link]()
    3. Control Flow Graph - [link]()

- Code Snippet #2
    1. Code Snippet
    ```
    ```
    2. Data Flow Graph - [link]()
    3. Control Flow Graph - [link]()

### Java
- Code Snippet #1
    1. Code Snippet
    ```
    ```
    2. Data Flow Graph - [link]()
    3. Control Flow Graph - [link]()

- Code Snippet #2
    1. Code Snippet
    ```
    ```
    2. Data Flow Graph - [link]()
    3. Control Flow Graph - [link]()