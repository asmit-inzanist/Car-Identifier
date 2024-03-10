# Car Identifier App

## Prerequisites

- Python 3.x
- Set up a `.env` file with your Gemini API key.
- Install dependencies by running:
  ```bash
  pip install -r requirements.txt



## Description
"Car Identifier" is a Streamlit web application for identifying cars using the Google Generative AI API. It provides informative descriptions and specs for uploaded images of Cars or any other vehicles along with its manufacturing company .

## Features
- Upload images of Cars or any other vehicle.
- Receive informative descriptions,components and specs of the car in a tabular format
- Get info on the car manufacturing company and a google link to the car's purchasing site.

## Usage
1. Visit the application [here]().
2. Upload an image of a Car or a Vehicle .
3. Click on "Tell me about the Car" button.
4. Wait for the AI to process the image and provide info.
5. Review the generated content and explore the insights.

## Dependencies
- `google.generativeai`: Wrapper for the Gemini Generative AI API.
- `dotenv`: For loading environment variables.
- `streamlit`: Framework for creating web applications.
- `PIL`: Python Imaging Library for image processing.

## How to Run
```python
streamlit run your_app_name.py
```

### Developed with ❤ by Asmit.

