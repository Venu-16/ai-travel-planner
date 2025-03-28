import streamlit as st
import google.generativeai as genai

# Configure Gemini API Key
genai.configure(api_key="AIzaSyCNcDqBuahNOVuu7m20r--UKshLYz9uEnk")


def get_travel_itinerary(user_input):
    """
    Generate a travel itinerary using Gemini API based on user inputs.
    """
    prompt = f"""You are an AI travel planner. Generate a personalized itinerary based on these details:
    {user_input}

    Include:
    - Morning, afternoon, and evening activities
    - Meal recommendations
    - Transportation options
    - Budget-friendly or luxury choices based on user preference
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text if response else "No itinerary generated."


# Streamlit UI
st.title("AI-Powered Travel Planner")
st.write("Plan your perfect trip with AI!")

# User Inputs
starting_location = st.text_input("Starting Location")
destination = st.text_input("Destination")
budget = st.selectbox("Budget", ["Budget", "Mid-range", "Luxury"])
duration = st.slider("Trip Duration (days)", 1, 14, 5)
purpose = st.text_area("Purpose of Travel (e.g., leisure, adventure, work)")
preferences = st.text_area("Any special preferences? (e.g., food, cultural spots, hidden gems)")

# Generate Itinerary
if st.button("Generate Itinerary"):
    user_input = f"Starting: {starting_location}, Destination: {destination}, Budget: {budget}, Duration: {duration} days, Purpose: {purpose}, Preferences: {preferences}"
    itinerary = get_travel_itinerary(user_input)
    st.subheader("Your Personalized Itinerary")
    st.write(itinerary)