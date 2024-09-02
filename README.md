# Medicine Recommender System
A web-based application that recommends alternative medicines based on user input. This project uses machine learning models to suggest similar medicines, helping users find alternatives easily.

### Features
- Medicine Search: Type the name of a medicine, and the app will suggest alternatives.
- Recommendation System: Uses a pre-trained model to recommend similar medicines.
- Purchase Links: Direct links to purchase recommended medicines from online pharmacies.
- Responsive Design: The UI is optimized for various screen sizes, ensuring a smooth experience on both desktop and mobile devices.
### Tech Stack
- Backend: Flask
- Frontend: HTML, CSS (Bootstrap), JavaScript
- Machine Learning: Python, Pandas
- Data: Pre-processed medicine data stored in a pickle file
### Project Structure
```
medicine_recommender/
│
├── static/
│   ├── css/
│   │   └── style.css                 # Custom CSS styles
│   └── images/
│       └── medicine-image.jpg        # Image used in recommendations
├── templates/
│   └── index.html                    # Main HTML template
├── app.py                            # Flask application
├── medicine_dict.pkl                 # Pickle file containing medicine data
└── similarity.pkl                    # Pickle file containing similarity data
```
### Installation
To run this project locally, follow these steps:
Clone the repository:
```
git clone https://github.com/Swamibhuvanesan/Alternative-Medicine-Recommendation-System-.git
```
cd medicine-recommender-system
#### Set up a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

#### Install the required packages:
```
pip install -r requirements.txt
```
#### Add the required pickle files:
Ensure medicine_dict.pkl and similarity.pkl are in the root directory.
#### Run the application:
```
python app.py
```
#### Access the application:
Open your browser and navigate to http://127.0.0.1:5000/.
Usage
Select a Medicine: Use the dropdown to select the medicine you want to find alternatives for.
Get Recommendations: Click the "Recommend" button to view similar medicines.
Purchase: Click on the "Buy Now" button to purchase the recommended medicine from an online pharmacy.
### Screenshots

![Screenshot 2024-09-02 203639](https://github.com/user-attachments/assets/8a6f52b5-1bd6-4248-a34b-c19ed4517350)

## Contributing
Contributions are welcome! Please follow these steps:

Fork the project.
Create your feature branch (git checkout -b feature/AmazingFeature).
Commit your changes (git commit -m 'Add some AmazingFeature').
Push to the branch (git push origin feature/AmazingFeature).
Open a Pull Request.
Please make sure to update tests as appropriate.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Contact
Feel free to reach out!
