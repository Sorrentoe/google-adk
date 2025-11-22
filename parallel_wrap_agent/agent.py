from google.adk.agents import Agent, ParallelAgent, SequentialAgent
from google.adk.tools import google_search

hotel_agent = Agent(
    name="HotelAgent",
    model="gemini-2.0-flash",
    tools=[google_search],
    description="An agent that searches for hotels and accommodation in a given destination",
    instruction=""" 
      You are a hotel booking specialist. You will be given a destination and travel dates, and you will search for:
    - Popular hotels in the area
    - Different price ranges (budget, mid-range, luxury)
    - Hotel amenities and ratings
    - Location advantages
    Provide a summary of the best accommodation options with brief descriptions.
    ONLY research for hotels and nothing else.
    """,
    output_key="hotel_options"
)


restaurant_agent = Agent(
    name="RestoAgent",
    model="gemini-2.0-flash",
    tools=[google_search],
    description="An agent that finds best cuisine on the given destination",
    instruction="""
         You are a food and dining expert. You will be given a destination and you will search for:
    - Top-rated restaurants and cafes
    - Local cuisine specialties
    - Different dining price ranges
    - Unique dining experiences
    Provide a summary of the best dining options with cuisine types and highlights.
    Only research for restaurants and nothing else.
    """,
    output_key="restaurant_options"
)


activity_agent = Agent(
    name="ActivityAgent",
    model="gemini-2.0-flash",
    tools=[google_search],
    description="An Agent that searches for activities and attractions in a given destination",
    instruction="""
    You are a local activities expert. You will be given a destination and you will search for:
    - Popular tourist attractions
    - Outdoor activities and adventures
    - Cultural experiences and museums
    - Entertainment and nightlife options
    Provide a summary of the best activities with brief descriptions and recommendations.
    Only research for activities and nothing else.
    """,
    output_key="activity_options"
)


parallel_research_agent = ParallelAgent(
    name='TravelPlanningAgent',
    description='A comprehensive system that simultaneously searches for hotels, restaurants, and activities for trip planning',
    sub_agents=[hotel_agent, restaurant_agent, activity_agent],
)




summarizer_agent = Agent(
    name="SummarizerAgent",
    model="gemini-2.0-flash",
    instruction="""
    You are a travel planner assistant. You will be given a destination and travel dates, and you will synthesize the information from the hotel, restaurant, and activity agents to provide a comprehensive travel plan.
    Provide a summary of the best travel plan with brief descriptions and recommendations.
    {hotel_options}
    {restaurant_options}
    {activity_options}  
    """,
    
)


root_agent = SequentialAgent(
    name="TravelPlanningAgent",
    description="A comprehensive system that simultaneously searches for hotels, restaurants, and activities for trip planning",
    sub_agents=[parallel_research_agent, summarizer_agent],
)


