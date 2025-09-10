
import requests  # pyright: ignore[reportMissingModuleSource]


class CalculatorTool:
  def add(self,a,b):
    return a+b
  def multiply(self,a,b):
    return a*b


class WeatherTool:
  def __init__(self,api_key):
    self.api_key=api_key

  def get_weather(self,city):
    #API call
    url=f"https://api.tomorrow.io/v4/timelines?location={city}&fields=temperature,weatherCode&units=metric&timesteps=1d&apikey={self.api_key}"
    
    try:
      res=requests.get(url)    
      res.raise_for_status()  
      data=res.json()          
    except requests.exceptions.RequestException as e:
      return f"Error fetching weather:{e}"      


    try:
      timelines=data.get('data',{}).get('timelines',[])

      if not timelines:
        return f"No Interval data for {city}"

      intervals=timelines[0].get('intervals',[])
      if not intervals:
        return f"No interval data for {city}."


      try:
        values=intervals[0].get("values",{})
        temperature=values.get("temperature","N/A")
        weathercode=values.get("weatherCode","N/A") # Corrected key to "weatherCode"
      
        return f"The weather in {city} is {weathercode} with {temperature} degree"
      except Exception as e:
        return f"Error reading weather data:{e}"


    except Exception as e:
        return f"Error processing weather data:{e}"


class StringManipulationTool:
    def reverse_string(self,string):
        stri=string.split()[-1]
        return stri[::-1]

    def lowercase_string(self,string):
        return string.lower()
        
     


       

