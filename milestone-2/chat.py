import json

import openai

# GET YOUR OPEN AI API KEY FROM : https://platform.openai.com/account/api-keys
# Save the key in config.json as { "OPENAI_API_KEY": "<KEY>" }

with open("config.json", "r") as file:
	config = json.loads(file.read())

openai.api_key = config["OPENAI_API_KEY"]

messages = [
	{
		"role": "system",
		"content": "Write five inputs and outputs for the function given in the variable 'Code' as table" # 'Inputs' - 'Outputs'
	}
]

while True:
	message = input("Code : ")
	# Input
	"""
	int doMath(int a, int b){ int c = a+b; a++; b = a+c; return (b+a)*c;}
	"""
	# Output
	"""
	| **Input** | **Output** |
	|-----------|------------|
	| a = 2, b = 3   | 80        |
	| a = -1, b = 5  | 30        |
	| a = 0, b = 0   | 0         |
	| a = -6, b = 10 | 224       |
	"""
	# This should be easy to parse and then automate the testing.

	"""
	Code : Exaplin how you arrived at each solution, show as a table
	ChatGPT: Sure, I can show you how I arrived at each output. 
	
	| **Input** | **Output** | **Steps**                                 |
	|-----------|------------|-------------------------------------------|
	| a = 2, b = 3   | 80        | c = 2+3 = 5; a = 3; b = 8; (b+a)*c = 80 |
	| a = -1, b = 5  | 30        | c = -1+5 = 4; a = -1; b = 8; (b+a)*c = 30|
	| a = 0, b = 0   | 0         | c = 0+0 = 0; a = 1; b = 1; (b+a)*c = 0   |
	| a = -6, b = 10 | 224       | c = -6+10 = 4; a = -5; b = 9; (b+a)*c = 224 |
	
	For each input, I followed the steps in the function to compute the corresponding output value. The steps are straightforward: 

	1. Calculate `c = a + b`
	2. Increment `a` by 1
	3. Set `b = a + c`
	4. Compute and return the value of `(b + a) * c`
	
	For example, if `a = 2` and `b = 3`, the first step gives us `c = 2 + 3 = 5`. The second step updates `a` to `a = 3`. The third step sets `b` to `b = a + c = 3 + 5 = 8`. Finally, the fourth step computes `(b + a) * c = (8 + 3) * 5 = 55`, which is the output value for this input.
	"""
	if message:
		messages.append(
			{"role": "user", "content": message},
		)
		chat = openai.ChatCompletion.create(
			model="gpt-3.5-turbo", messages=messages
		)

	reply = chat.choices[0].message.content
	print(f"ChatGPT: {reply}")
	messages.append({"role": "assistant", "content": reply})