import re
from tools import CalculatorTool,WeatherTool,StringManipulationTool



class CalculatorAgent:
  def __init__(self):
    self.tool=CalculatorTool()
  



  def perform_task(self,request):
    if any(word in request.lower() for word in ["add","plus","+","multiply","*","times"]):
      numbers=list(map(int,re.findall(r'\d+',request)))
      if(len(numbers)<2):
        return "Not Enough for calculation"
      if any(word in request.lower() for word in ["add","+","plus"] ):
        return self.tool.add(*numbers)
      elif any(word in request.lower() for word in ["multiply","*","times"]):
        return self.tool.multiply(*numbers)
    return None


class WeatherAgent:
  def __init__(self,api_key):
    self.tool=WeatherTool(api_key)
  
  def perform_task(self,request):
    if "weather" in request.lower():
      city_match=re.search(r'weather in ([\w\s]+)',request,re.IGNORECASE)
      
      if city_match:
        city=city_match.group(1).strip()
        
        return self.tool.get_weather(city)
      else:
        return "Please specify a city for the weather."
    return None

class StringManipulationAgent:
  def __init__(self):
    self.tool=StringManipulationTool()
  def perform_task(self,request):
    if "reverse" in request.lower():
      return self.tool.reverse_string(request)
    elif "lowercase" in request.lower():
      return self.tool.lowercase_string(request)
    return None



class MasterAgent:
  def __init__(self,api_key):

    self.agents=[CalculatorAgent(),WeatherAgent(api_key),StringManipulationAgent()]

  def perform_task(self,request):
    for agent in self.agents:
      result=agent.perform_task(request)
      if result is not None:
        return result
    return "No agent could handle this request"

