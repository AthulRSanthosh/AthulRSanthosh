import google.generativeai as genai

genai.configure(api_key="api_key") #Kindly add API Key

model = genai.GenerativeModel("gemini-1.5-flash")  

def get_recipe(query):
    try:
        response = model.generate_content(f"Give me a recipe for {query}")

        return response.text

    except Exception as e:
        return f"Oops! Something went wrong: {e}"


def run_chatbot():

    print("Welcome to RecipeBot! Ask me for a recipe by name or ingredients.")

    print("Type 'exit' to quit.\n")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input == "exit":
            print("Goodbye!")
            break

        recipe = get_recipe(user_input)
        print("RecipeBot:", recipe)
        
run_chatbot()
