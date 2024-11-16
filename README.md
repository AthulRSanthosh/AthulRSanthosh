### RecipeBot with Gemini AI

_Overview_

RecipeBot is an interactive chatbot designed to help users generate recipes based on their requests. Using the capabilities of Gemini AI, this project showcases a simple yet powerful way to fetch recipes through conversational inputs.

_Features_

- **Recipe Generation**: Generate recipes for a wide range of dishes based on user input.
- **Conversational Interface**: Chat-based interaction where users can request recipes by name or ingredients.
- **Built with Gemini AI**: Utilizes Google's Gemini AI for generating responses dynamically.

### Installation


1. Install dependencies:
   ```bash
   pip install google-generativeai
   ```

### Configuration

Before running the application, set up your API key:

```python
import google.generativeai as genai

genai.configure(api_key="your-api-key")
```

Replace `"your-api-key"` with your actual API key.

### Running the Chatbot

To start the RecipeBot, run:

```bash
python main.py
```

Once running, you can interact with the bot by typing requests such as:

- "I want a sambar recipe."
- "Give me a recipe with chicken 65."
- "egg curry"

To exit the chatbot, type `exit`.
