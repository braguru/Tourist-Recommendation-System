import pandas as pd
import folium
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from flask import Flask, render_template, request

app = Flask(__name__)

# import library

# preparing dataset
url = 'https://drive.google.com/file/d/1z2m8QiXQ2FoyOebOOmTBs4VgwzBTUNI5/view?usp=sharing'
url = 'https://drive.google.com/uc?id=' + url.split('/')[-2]
table_data = pd.read_csv(url)

# processing dataframe
data_content_based_filtering = table_data.copy()
data_content_based_filtering['Tags'] = data_content_based_filtering['Category'] + ' ' + data_content_based_filtering[
    'Description_en']
data_content_based_filtering = data_content_based_filtering[
    ['Place_Id', 'Place_Name', 'Tags', 'Category', 'City', 'Description_en', 'Lat', 'Long', 'Rating']]

# process cosine similarity
tv = TfidfVectorizer(max_features=5000)
vectors = tv.fit_transform(data_content_based_filtering.Tags).toarray()
similarity = cosine_similarity(vectors)

# define output
search_format = ""


# Create a function that will return the name of the recommended tourist spot to the user
def recommend_by_content_based_filtering(categories, regions, number_of_locations):
    data_sample = \
        data_content_based_filtering[data_content_based_filtering['Category'] == categories].sample(1).values[0][1]
    data_sample_id = data_content_based_filtering[data_content_based_filtering['Place_Name'] == data_sample].index[0]
    similar_location = similarity[data_sample_id]
    data_sample_list = sorted(list(enumerate(similar_location)), key=lambda x: x[1], reverse=True)[1:100]

    recommended_tourist_site = []
    for i in data_sample_list:
        if data_content_based_filtering.iloc[i[0]].City == regions:
            recommended_tourist_site.append([data_content_based_filtering.iloc[i[0]].Place_Name])

        if len(recommended_tourist_site) >= int(number_of_locations.split()[0]):
            break

    return recommended_tourist_site


# Function to prepare output to be generated with HTML
def makeRecommender(recommendation):
    search_format = ""
    for places in recommendation:
        data = data_content_based_filtering[data_content_based_filtering['Place_Name'] == ' '.join(places)]

        place_name = ' '.join(places)
        place_category = ' '.join(data['Category'].values)
        place_rating = str(data['Rating'].values)
        place_desc = ' '.join(data['Description_en'].values)

        search_format += "<h3><a href='https://www.google.com/search?q=" + str(place_name) + "' target='_blank'>" + str(
            place_name) + " </a></h3>" + "<p><span>Category:</span> " + place_category + ". Rating: " + place_rating + "</p>" + "<span>Description:</span><br><p>" + str(
            place_desc) + "</p><br><br>"
    return search_format


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        input_type = request.form['type']
        input_city = request.form['city']
        input_number = request.form['number']

        ghana_map = folium.Map(location=[8.3101413, -1.6606439], zoom_start=7)

        # Create a function to return the coordinates of recommended tourist sites
        def coordinate_plotter(place):
            data = data_content_based_filtering[data_content_based_filtering['Place_Name'] == ' '.join(place)]
            latitude = data['Lat'].values[0]
            longitude = data['Long'].values[0]

            folium.Marker(
                location=[float(latitude), float(longitude)],
                popup=' '.join(place),
                tooltip=' '.join(place),
                icon=folium.Icon(color='#43BFF5', icon="info-sign"),
            ).add_to(ghana_map)

        # Process tourist destination place
        recommendation = recommend_by_content_based_filtering(input_type, input_city, input_number)

        # Process the map markers coordinates
        for places in recommendation:
            print(places)
            coordinate_plotter(places)

        # Process the output formatting
        formatter = makeRecommender(recommendation)

        map_html = ghana_map._repr_html_()
        return render_template('result.html', recommendation=formatter, map_html=map_html)
    else:
        return render_template('index.html')


@app.route('/hotspot')
def hotspot():
    return render_template('hottest.html')


@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
