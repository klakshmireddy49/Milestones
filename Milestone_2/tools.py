from langchain.tools import Tool
import datetime
import random


# 1️⃣ Calculator Tool
def calculator_tool(expression: str) -> str:
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Invalid mathematical expression."


calculator = Tool(
    name="Calculator",
    func=calculator_tool,
    description="Useful for solving math problems like 5*6 or 12+3.",
)


# 2️⃣ Weather Tool (Simulated API)
def weather_api(city: str) -> str:

    weather_data = {
        "london": "Rainy, 12°C",
        "new york": "Cloudy, 18°C",
        "tokyo": "Sunny, 22°C",
        "hyderabad": "Hot, 34°C",
        "delhi": "Warm, 30°C",
    }

    city = city.lower()

    return weather_data.get(city, "Weather data not available.")


weather_tool = Tool(
    name="WeatherAPI",
    func=weather_api,
    description="Useful for checking the weather of a city.",
)


# 3️⃣ Unit Converter
def unit_converter(input: str):

    try:
        value, unit = input.split()
        value = float(value)

        if unit == "km":
            return f"{value*1000} meters"

        if unit == "m":
            return f"{value/1000} kilometers"

        return "Unsupported unit."

    except:
        return "Invalid conversion format."


unit_converter_tool = Tool(
    name="UnitConverter",
    func=unit_converter,
    description="Useful for converting units like km to meters.",
)


# 4️⃣ Time Tool
def get_time(_: str):

    now = datetime.datetime.now()

    return now.strftime("%Y-%m-%d %H:%M:%S")


time_tool = Tool(
    name="CurrentTime",
    func=get_time,
    description="Useful when user asks about current date or time.",
)


# 5️⃣ Random Fact Tool
def random_fact(_: str):

    facts = [
        "Octopuses have three hearts.",
        "Bananas are technically berries.",
        "The Eiffel Tower grows in summer.",
        "Honey never spoils.",
        "Sharks existed before trees.",
    ]

    return random.choice(facts)


fact_tool = Tool(
    name="RandomFact",
    func=random_fact,
    description="Useful when user asks for an interesting fact.",
)
