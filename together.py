import json
import sys
import os
import importlib.util
sys.path.append('.')
from together import Together

# Import the weather tool from the renamed Tools.py file
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'tools'))
from Tools import GetWeatherTool

key = "tgp_v1_0ljNvqYPTMCc1_VLyNCCUj2Jg3v3P8-lmgOBRYMHJ1c"
client = Together(api_key=key)


### simple chat completion:
def simple_chat():
    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-7B-Instruct-Turbo",
        messages=[
            {
                "role": "user",
                "content": "Explain the theory of relativity in simple terms.",
            }
        ],
    )
    print(response.choices[0].message.content)

# ### A user function to get current weather
# def get_current_weather(location: str, unit: str) -> str:
#     """Get the current weather in a given location"""
#     # This is a mock implementation. In a real scenario, you would call a weather API.
#     if "new york" in location.lower():  # More flexible matching
#         if unit == "celsius":
#             return "The current temperature in New York is 22°C."
#         else:
#             return "The current temperature in New York is 72°F."
#     return "Location not found."

# def current_weather_tool_call(tool_call):
#     params = json.loads(tool_call["function"]["arguments"])  # Parse JSON from function field
#     location = params.get("location", "")
#     unit = params.get("unit", "celsius")
#     return get_current_weather(location, unit)

def chat_with_weather_function_call():
  # Create weather tool instance
  weather_tool = GetWeatherTool()
  
  response = client.chat.completions.create(
      model="Qwen/Qwen2.5-7B-Instruct-Turbo",  # Use Qwen2.5-7B-Turbo model
      messages=[
          {
              "role": "system",
              "content": "You are a helpful assistant that can access external functions. The responses from these function calls will be appended to this dialogue. Please provide responses based on the information from these function calls.",
          },
          {
              "role": "user",
              "content": "What is the current temperature of New York in Celsius?",
          },
      ],
      tools=[
          weather_tool.to_openai_schema()
        ],
    )

  print(f"Tool Calls:\n {json.dumps(response.choices[0].message.model_dump()['tool_calls'], indent=2)}")

  # Execute the tool call using the weather tool class
  tool_call = response.choices[0].message.model_dump()["tool_calls"][0]
  tool_args = json.loads(tool_call["function"]["arguments"])
  weather_result = weather_tool.execute(**tool_args)
  
  print(f"We got the current weather: {weather_result}")







if __name__ == "__main__":
    # simple_chat()
    chat_with_weather_function_call()




