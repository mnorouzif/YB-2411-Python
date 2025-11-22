import openai
import os

OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY


def instructor_chatbot():
    """Command-line AI Itinerary Chatbot."""
    print("Welcome to AI Itinerary recommender! Answer a few questions to get personalized itenary advice.\n")
    
    days = input("How many (days): ")
    location = input("Where is the destination (city name): ")
    age = input("Enter age average: ")
    # fitness_goal = input("What is your fitness goal? (e.g., lose weight, build muscle, endurance, etc.): ")
    
    # Construct prompt
    prompt = f"""
    You are a professional trouist recommender. Provide an itinerary recommendation based on user data.
    
    User Details:
    - days: {days} days
    - destination: {location} city
    - Age: {age} years
    
    Based on your personal information, 
    Then, give a structured itinerary with a name of the place, address and short description for each day seperatly in order with maximom three activities in a day.
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are a professional itinerary recommender."},
                      {"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.7,
            top_p = 0.99

        )
        
        print("\n My Name is Hadi as AI Itinerary expert:")
        print(response["choices"][0]["message"]["content"])
        
    except Exception as e:
        print("Error communicating with OpenAI API:", e)

if __name__ == "__main__":
    instructor_chatbot()