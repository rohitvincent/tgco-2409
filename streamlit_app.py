import streamlit as st
import requests
import subprocess
import io

# Define the URL of your Flask API endpoint
FLASK_API_URL = "http://localhost:5000/top-spender"

def fetch_top_spenders():
    """Function to fetch top spenders data from the Flask API"""
    try:
        response = requests.get(FLASK_API_URL)
        response.raise_for_status()  # Raise an exception for any unsuccessful status code
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data from Flask API: {e}")
        return None

def display_top_spenders(top_spenders):
    """Function to display top spenders data in Streamlit"""
    if top_spenders:
        st.write("### Top Spenders")
        for spender in top_spenders:
            st.write(f"**Name:** {spender['name']} {spender['surname']}")
            st.write(f"**Total Spent:** ${spender['total_spent']:.2f}")
            st.write("---")
    else:
        st.write("No top spenders data available.")

def run_tests():
    """Function to run tests and capture results"""
    try:
        # Run pytest command and capture the output
        result = subprocess.run(
            ["pytest", "-v","test_app.py"],
            capture_output=True,
            text=True
        )
        # Return the captured stdout (test results)
        return result.stdout
    except Exception as e:
        return f"An error occurred while running tests: {e}"

def main():
    st.title("Top Spenders in Our Store")

    # Create tabs in Streamlit
    tabs = st.tabs(["Top Spenders", "Test Results"])

    with tabs[0]:
        st.write("Fetching top spenders data from the API...")
        top_spenders = fetch_top_spenders()
        if top_spenders:
            display_top_spenders(top_spenders)
        else:
            st.write("Failed to retrieve data.")

    with tabs[1]:
        st.write("### Test Results")
        test_results = run_tests()
        st.code(test_results, language='text')

if __name__ == "__main__":
    main()
