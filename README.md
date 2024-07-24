# Tourist Attraction Recommendation System

This project is a web-based application that recommends tourist attractions in Ghana. It uses content-based filtering and cosine similarity to recommend locations based on user input. The application is built using Flask, Pandas, Folium, and Scikit-Learn.

## Features
- **Input Category and City:** Users can input a category (e.g., nature, historical) and a city to receive tailored recommendations.
- **Recommendation Engine:** Uses TF-IDF Vectorizer and cosine similarity to find and recommend similar tourist spots.
- **Interactive Map:** Displays recommended tourist locations on an interactive map using Folium.
- **Additional Pages:** Includes pages for "Hotspot", "Team", and "Contact".

## Requirements
- Python 3.x
- Flask
- Pandas
- Scikit-Learn
- Folium

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tourist-recommendation.git
   cd tourist-recommendation
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

## Usage
1. **Homepage:** Enter the category, city, and number of locations you want recommendations for.
2. **Recommendation:** View the recommendations and their ratings. Click on the names to search for more information on Google.
3. **Map:** An interactive map showing the recommended locations.

## File Structure
- `app.py`: Main application file.
- `templates/`: Folder containing HTML templates.
  - `index.html`: Home page template.
  - `result.html`: Result page template displaying recommendations and map.
  - `hottest.html`: Placeholder for Hotspot page.
  - `team.html`: Placeholder for Team page.
  - `contact.html`: Placeholder for Contact page.
- `static/`: Folder for static files like CSS and JS (if any).

## How It Works
1. **Data Preparation:** Reads a CSV file containing tourist site data from a Google Drive link.
2. **Content-Based Filtering:** Merges category and description for TF-IDF Vectorization.
3. **Cosine Similarity:** Computes the cosine similarity of the TF-IDF matrix.
4. **Recommendation:** Filters and sorts similar locations by user’s input category and city.
5. **Map Generation:** Uses Folium to generate an interactive map with markers for the recommended locations.

## Routes
- `/`: Home page where user inputs are taken.
- `/hotspot`: Hotspot page template.
- `/team`: Team page template.
- `/contact`: Contact page template.

## Contributing
Feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License.

**Author:** Your Name

Enjoy exploring new places in Ghana with our recommendation system!