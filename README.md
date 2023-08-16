# DataTako

DataTako is an AI-powered web application that allows users to upload data files, visualize the data, and have interactive conversations with an AI model. The application leverages natural language processing and data analysis capabilities to provide insights, answer queries, and facilitate data exploration in a user-friendly manner.
![Screenshot](/assets/screenshot.png "Screenshot")
## Features

- **File Upload**: Users can easily upload their data files through the web interface (csv, json, xlsx, txt are supported).
- **Data Visualization**: The uploaded file is displayed in a tabular format for easy visualization and exploration.
- **AI-powered Conversations**: Users can have interactive conversations with the AI model by entering queries related to the uploaded data.
- **Insights and Answers**: The AI model analyzes the data and provides valuable insights and answers based on the user's queries.
- **User-friendly Interface**: The web application is designed to be intuitive and user-friendly, making it easy for users to interact with and explore their data.

## Installation

1. Clone the repository:
```
git clone https://github.com/your-username/DataTako.git
cd DataTako
```
2. Install the required dependencies in a virtual environment:
```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```
## Usage
1. Set up your OpenAI API key:
- Obtain an API key from OpenAI.
- Create a file at <project-root>/.streamlit/secrets.toml
- Add this line to the new file (replace it with your own api key)
```
OPENAI_API_KEY = "your open api key"
```
2. Run the web application:
```
streamlit run app.py
```
3. Access the application:
- Open your web browser and go to http://localhost:8501 to access the DataTako web application.
4. Upload your data file:
- Click on the "Upload your file" button and select the file you want to analyze.
- The uploaded data will be displayed in a table for visualization.
5. Interact with the AI model:
- Enter your queries in the provided text area.
- Click the "Chat with data" button to interact with the AI model based on the uploaded data.
- The AI model will provide insights and answers related to your queries.



