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

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2025 iqra-devv

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
