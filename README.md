
![logo-removebg-preview (1)](https://github.com/ArchismwanChatterjee/Object-Finder/assets/115975340/2fa6556d-37da-45a1-ab1a-5974f34e6d9c)


# Object-Finder 🔍

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)
![License](https://badgen.net/github/license/micromatch/micromatch)


Object Finder basically detects and lists out the various objects present in an image. 
Click [here](https://object-finder.streamlit.app/) to try out

## How to use:
1. Go through the disclaimer ⚠️ to understand more regarding what type of images will give best results.
2. Upload any image of your choice (upto 200MB)
3. Wait for the image to be uploaded, the dimesions of the image will be updated
4. Click on the button to detect the objects present
5. Wait for few seconds and See the ✨Magic ✨ Happen.

## Installation:

- clone this repository

- Object Finder requires [Python](https://www.python.org/) v3.9+ to run.

- Install the dependencies.

```python
pip install streamlit
pip install google-generativeai
pip install Pillow
pip install python-dotenv # for environment variable
```
- Make sure to create your own generative-ai api-key using Google Cloud Console or Google Makersuite and replace it.

```python
genai.configure(api_key=os.getenv("MY_SECRET_KEY")) # Replace with your own api-key by creating .env file
```
or 
```python
genai.configure(api_key="YOUR APIKEY")  # Replace YOUR APIKEY with the actual value of your apikey 
```

- To run the server
```python
streamlit run "your_file_name"
```

- For Deploying your application refer [Streamlit Community Cloud](https://docs.streamlit.io/streamlit-community-cloud/get-started)

## Development:

Want to contribute? Great!

Object Finder uses streamlit.

checkout *Installation* above to set it up locally.

make sure all changes you make are in the testing branch. 

## Deployment:

The website is deployed using streamlit community cloud ⬇️

[Link](https://object-finder.streamlit.app/) 
