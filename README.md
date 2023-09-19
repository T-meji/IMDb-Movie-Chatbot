# IMDb Movie Chatbot (M.A.X!)

**M.A.X! (Movie Advisor Xpert)** is an IMDb movie chatbot that provides information about movies, directors, genres, and more. Users can ask questions related to movies, and M.A.X! will respond with relevant information from the IMDb database.

## Table of Contents

- IMDb Movie Chatbot (M.A.X!)
- Features
- Getting Started
    - Prerequisites
    - Installation
- Usage
- Examples
- Contributing
- License

## Features

- Retrieve movie details (e.g., title, release year, genre).
- Find information about directors and their filmography.
- Discover movies by genre.
- Get movie recommendations based on user preferences.
- Chat with M.A.X! in a conversational format.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed.
- OpenAI account
- Pinecone account
- IMDb movie dataset (You can download it from [Kaggle](https://www.kaggle.com/datasets/davidfuenteherraiz/messy-imdb-dataset)).

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/T-meji/IMDb-Movie-Chatbot.git
   ```


2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Pinecone credentials by creating an `env.py` file with the following content:

   ```python
   # env.py
   openai_api_key = "your_openai_api_key"
   pinecone_api_key = "your_pinecone_api_key"
   pinecone_environment_region = "your_environment_region"
   ```

4. Load the IMDb dataset into your preferred database system and configure the data source in the code.

## Usage

1. Start the M.A.X! web application by running:

   ```bash
   streamlit run core.py
   ```

2. Access the web app in your browser.

3. Enter your movie-related questions in the chatbox and get responses from M.A.X!

## Examples

- **User**: "Tell me about 'The Dark Knight'."

  **M.A.X!**: "The Dark Knight is a 2008 movie directed by Christopher Nolan. It belongs to the Action, Crime, and Drama genres. The movie has a runtime of 152 minutes and an IMDb score of 9.0."

- **User**: "Who directed 'Inception'?"

  **M.A.X!**: "Inception was directed by Christopher Nolan."

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Create a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
