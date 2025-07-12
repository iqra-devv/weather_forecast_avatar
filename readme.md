# Weather Forecast Avatar

A Python application that fetches your location and current weather, then recommends an outfit and displays it using a graphical avatar.

## Features

- Automatically detects your city using your IP address.
- Fetches current temperature using [WeatherAPI](https://www.weatherapi.com/).
- Recommends an outfit based on the temperature.
- Draws a graphical avatar with the recommended outfit using the `turtle` library.

## Setup

### 1. Clone the repository

```sh
git clone <your-repo-url>
cd weather_forcast
```

### 2. Install dependencies

```sh
pip install -r requirements.txt
```

### 3. Set up your WeatherAPI key

- Get your API key from [WeatherAPI](https://www.weatherapi.com/).
- place your API key in a `.config` file in the project directory:

```
WEATHER_API_KEY="your_api_key_here"
```

### 4. Run the application

```sh
python main.py
```

## Files

- `main.py`: Main application logic.
- `avatar.py`: Avatar drawing class using turtle graphics.
- `.config`: (Optional) Stores your API key for development.
- `requirements.txt`: Python dependencies.
- `.gitignore`: Files and folders to ignore in version control.

## Notes

- The application will update the weather and outfit recommendation every 4 hours.
- Make sure your API key is kept secure and not committed to version control.

## License
