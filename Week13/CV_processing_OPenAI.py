import openai
import os

OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

def input_file():
    """Helper function to read CV content from a file."""
    file_path = input("Enter the path to your CV file: ")
    try:
        with open(file_path, 'r', encoding='utf-8',errors='ignore') as file:
            content = file.read()
        return content
    except Exception as e:
        print("Error reading file:", e)
        return None
    
def cv_analyzer():
    """Command-line AI CV Analyzer."""
    print("Welcome to AI CV Analyzer! Please provide your CV for analysis.\n")
    
    cv_content = input_file()
    if not cv_content:
        return
    
    # Construct prompt
    prompt = f"""
    You are a professional career advisor. 
    Analyze the following CV and provide feedback on strengths, weaknesses, and suggestions for improvement.
    
    CV Content:
    {cv_content}
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are a professional career advisor."},
                      {"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7
        )
        
        print("\n AI Career Advisor Feedback:")
        print(response["choices"][0]["message"]["content"])
        
    except Exception as e:
        print("Error communicating with OpenAI API:", e)


if __name__ == "__main__":
    cv_analyzer()