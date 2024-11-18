from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# Load recommendation data
df_result = pd.read_csv('datasets/MovieRecommendations.csv')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    search_movie = data.get('movie', None)
    
    if not search_movie:
        return jsonify({'error': 'No movie provided'}), 400
    
    result = df_result[df_result['title'] == search_movie]
    
    if result.empty:
        return jsonify({'error': 'Movie not found'}), 404
    
    recommendations = {
        'FirstRecommendation': result['FirstMovieRecommendation'].values[0],
        'SecondRecommendation': result['SecondMovieRecommendation'].values[0],
        'ThirdRecommendation': result['ThirdMovieRecommendation'].values[0],
        'FourthRecommendation': result['FourthMovieRecommendation'].values[0],
    }
    
    return jsonify(recommendations)

if __name__== '__main__':
    app.run(debug=True)
