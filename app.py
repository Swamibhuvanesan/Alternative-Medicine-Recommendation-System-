from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the medicine dataframe and similarity data from pickle files
medicines_dict = pickle.load(open('medicine_dict.pkl', 'rb'))
medicines = pd.DataFrame(medicines_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(medicine):
    medicine_index = medicines[medicines['Drug_Name'] == medicine].index[0]
    distances = similarity[medicine_index]
    medicines_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_medicines = []
    for i in medicines_list:
        recommended_medicines.append(medicines.iloc[i[0]].Drug_Name)
    return recommended_medicines

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = None
    if request.method == 'POST':
        selected_medicine_name = request.form.get('medicine')
        recommendations = recommend(selected_medicine_name)
    return render_template('index.html', medicines=medicines['Drug_Name'].values, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
