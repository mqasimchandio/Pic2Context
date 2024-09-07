# Gemini Pro 1.5 - AI-Powered Image & Text Analyzer
## Project Overview:
Gemini Pro 1.5 is a Streamlit-based application that leverages Google's Gemini 1.5 AI to analyze images and text. This project reads any uploaded image or text file, understands its context, and provides detailed insights into the content. It can identify different formats like tables, storytelling, question answering, and more.

## Features
### Image Analysis: 
Upload images (JPG, PNG, etc.) and receive detailed explanations of the content.
### Text Analysis: 
Upload text files (TXT, DOCX, PDF) for content analysis.
### Interactive 
Input: 
Input custom prompts to tailor the AI's response.
### Streamlit UI: 
Simple and intuitive user interface for uploading files and getting results.
## How It Works
### Upload a File: 
The application supports images and text files.
### AI Processing: 
Google Gemini 1.5 model is used to analyze the uploaded content.
### Detailed Response: 
The AI generates a comprehensive response, explaining the image, storytelling, or answering questions.
## Technologies Used
### Python: 
Core programming language.
### Streamlit: 
For building the interactive web app interface.
### Google Generative AI: 
Gemini 1.5 API for AI-powered content generation.
### PIL (Python Imaging Library): 
For image processing.
### dotenv:
To load environment variables securely.
## Installation
### Clone the repository:
```
bash
git clone https://github.com/yourusername/your-repo-name.git
```
### Navigate to the project directory:
```
bash
cd your-repo-name
```
### Install the required dependencies:
```
bash
pip install -r requirements.txt
```
### Set up your environment variables:

### Create a .env file in the project directory:

```
bash
touch .env
```
### Add your Google API key in the .env file:
```
bash
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```
### Usage
## Run the Streamlit app:

```
bash
streamlit run app.py
```

## In the web interface:
Upload an image or text file.
Input a custom prompt.
Click "Tell me about the file" to get a detailed response from the AI.
## Example
### Input:
Upload an image of a table.

## AI Response:
The AI will analyze the table, explain the content, and provide further insights.

## File Structure

## app.py:
Main application code.

## requirements.txt:
List of required dependencies.

## .env:
Environment variables file (not uploaded to GitHub).

## images/:
Directory for storing sample images (optional).

## License
This project is licensed under the MIT License.
