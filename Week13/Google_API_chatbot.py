from urllib import response
from google import genai

from google.genai import types
import os

API_KEY = "..."



def instructor_chatbot():
    client = genai.Client(api_key=API_KEY)

    """Command-line AI Itinerary Chatbot."""
    print("Welcome to AI Itinerary recommender! Answer a few questions to get personalized itenary advice.\n")
    
    days = input("How many (days): ")
    location = input("Where is the destination (city name): ")
    age = input("Enter your age: ")
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
    Provide a short description for each place.
    Note: two location for visit for each day except first and the last day as travelers need to take a rest just one place to visit. 
    """
    
    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(system_instruction="You are a professional itinerary recommender.",
                                               temperature=0.7, top_p=0.9,),
            contents=[prompt]
            
        )
        
        
        print("\n My Name is Alex as AI Itinerary expert:")
        print(response.text)
        
    except Exception as e:
        print("Error communicating with OpenAI API:", e)

if __name__ == "__main__":
    instructor_chatbot()