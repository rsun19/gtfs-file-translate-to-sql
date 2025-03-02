# GTFS file to Postgres conversion

### Description
This script is focused only on the MBTA GTFS data, released by the Massachusetts Department of Transportation and the MBTA. Attempting to use this script on data from other agencies may result in failure, and thus adjustments to the insertion scripts may be needed. I want to support the conversion from more agencies in the future, so stay tuned for future improvements.

1. Create a virtual environment by running `python -m venv venv`
2. Start the virtual environment
    1. In windows: `venv\Scripts\activate`
    2. In linux/macOS: `source venv/bin/activate`
3. Run the requirements.txt file: `pip install -r requirements.txt`
4. Set your environment variables in `.env` for the database connection
5. Download the GTFS files at https://www.mbta.com/developers/gtfs
6. Run the `create.py` file: `python create.py`
