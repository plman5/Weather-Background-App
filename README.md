This is a project I worked on with a group for my Software Development Foundations class


# weather-background
A simple python script to change your desktop background to the current weather conditions.

## Requirements
- Python 3
- PIL
- requests
- Pandas
- A PositionStack API key (https://positionstack.com/)
- A US Census Bureau API key (https://api.census.gov/data/key_signup.html)

## Usage
1. Clone the repository
2. Install the required packages using `pip install -r requirements.txt`
3. Create a file called censusKey.txt in the same directory as the script and paste your US Census Bureau API key into it
4. Create a file called positionStackKey.txt in the same directory as the script and paste your PositionStack API key into it
5. Run the script using `python web_server.py`
6. Open your browser and navigate to http://localhost:80/

## Notes
- Due to limitations from the US Census, the states of Alaska, Vermont, and West Virginia are not supported, and same goes for many smaller cities in the United States
- The script will not work if either the US Census Bureau, or Position Stack API keys are not provided
- The script uses the 2020/21 census data, and will not automatically switch to new data, should it become available
- There may be some weather conditions that the script is not designed to handle. There was not a definitive list of weather conditions that the API could return, so we had to make some assumptions
