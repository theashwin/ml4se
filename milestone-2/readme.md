# Setting up the ChatGPT 
This would require an OpenAI API key which can be obtained from [https://platform.openai.com/account/api-keys](OpenAI API Key). Save the key in a file named `config.json` in `/milestone-2` folder in the format given below.

```
{ 
  "OPENAI_API_KEY": "<KEY>" 
}
```

# Installation
```
pip install --upgrade openai
```

# Running the Script

```
python3 gpt.py --lang <LANG> --n <NUM>
```

Here, \<LANG\> can be either 'java' or 'python'. If no argument is passed then the script takes 'java' as the default language. <br/>
\<NUM\> indicates number of data points to be run. It is an integer between 1 to 50 and takes a default value of 5.

- Details of the script execution and what it executes can be found in report mentioned below.

# Report
[Notion Report](https://twistedfate.notion.site/twistedfate/Milestone-2-ML4SE-Group-B-26762fd5356c4623aa29310169cbe1ab)
<br/>
[PDF Report](https://twistedfate.notion.site/twistedfate/Milestone-2-ML4SE-Group-B-26762fd5356c4623aa29310169cbe1ab)
