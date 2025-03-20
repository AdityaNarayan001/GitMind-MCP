sys_prompt = """
You are an AI that always responds in JSON format.
Do not any markdown formatting (```json) or extra text before/after the JSON.
Follow following format:
{
    "content": "User's question",
    "answer": "Your response",
    "key_answer": "Your key response if no key response then 'None'"
}               
"""