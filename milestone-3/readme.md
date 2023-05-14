# Setting up the ChatGPT 
This would require an OpenAI API key which can be obtained from [OpenAI API Key](https://platform.openai.com/account/api-keys). Save the key in a file named `config.json` in `/milestone-2` folder in the format given below.

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
[Notion Report](https://www.notion.so/twistedfate/Milestone-3-ML4SE-Group-B-e317a2e0000b425e88b4b18567e84564)
<br/>
[PDF Report](https://github.com/theashwin/ml4se/blob/main/milestone-3/milestone_3.pdf)
