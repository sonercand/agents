from google.adk.tools import ToolContext
import requests

def set_home_location(location: str, tool_context: ToolContext):
    """Sets the customer's home location.

    Only do this if they explicitly tell you to.
    """
    tool_context.state["user:home_location"] = location
    return f"Home location set to {location}."


def add_city(tool_context: ToolContext, city: str):
    """Adds an airport to the itinerary."""
    # 1. Get current itinerary or default to empty list
    itinerary = tool_context.state.get("itinerary", [])

    # 2. Append the new city
    itinerary.append(city)

    # 3. Save it back to session state
    tool_context.state["itinerary"] = itinerary

    return {"status": f"Added {city} to the itinerary."}

def create_itinerary(tool_context: ToolContext):
    """Creates the itinerary based on the airports in the session state."""
    itinerary = list(tool_context.state.get("itinerary", []))
    home_location = tool_context.state.get("user:home_location")

    # If home location exists and isn't already the first stop, prepend it
    if home_location and (not itinerary or itinerary[0] != home_location):
        itinerary.insert(0, home_location)

    legs = []
    # Loop through adjacent pairs to build travel legs
    for i in range(len(itinerary) - 1):
        legs.append({"from": itinerary[i], "to": itinerary[i + 1]})

    return {"itinerary": legs}

def clear_itinerary(tool_context: ToolContext):
    """Clears the current trip itinerary."""
    tool_context.state["itinerary"] = []
    return "Itinerary cleared. Let's start fresh!"

def get_destination_weather(city: str, tool_context: ToolContext):
  """Gets the current weather forecast for a specified city using Open-Meteo."""
  # Step 1: Convert city name to latitude/longitude using Open-Meteo's free geocoding API
  geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
  geo_response = requests.get(geo_url).json()

  if "results" not in geo_response or not geo_response["results"]:
    return f"Could not find coordinates for {city}."

  location_data = geo_response["results"][0]
  lat = location_data["latitude"]
  lon = location_data["longitude"]
  country = location_data.get("country", "")

  # Step 2: Fetch current weather using coordinates
  weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,weather_code"
  weather_response = requests.get(weather_url).json()

  current = weather_response.get("current", {})
  temp = current.get("temperature_2m")
  units = weather_response.get("current_units", {}).get(
      "temperature_2m", "°C"
  )

  return {
      "city": city,
      "country": country,
      "temperature": f"{temp} {units}",
      "status": "Success",
  }