from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)


model = joblib.load('Final.pkl')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():

    if request.method == 'POST':

        try:

            input_data = pd.DataFrame({

                'Hours_Studied': [int(request.form['Hours_Studied'])],

                'Attendance': [int(request.form['Attendance'])],

                'Parental_Involvement': [int(request.form['Parental_Involvement'])],

                'Access_to_Resources': [int(request.form['Access_to_Resources'])],

                'Previous_Scores': [int(request.form['Previous_Scores'])],

                'Internet_Access': [int(request.form['Internet_Access'])],

                'Tutoring_Sessions': [int(request.form['Tutoring_Sessions'])],

                'Teacher_Quality': [int(request.form['Teacher_Quality'])],

                'Peer_Influence': [int(request.form['Peer_Influence'])],

                'Learning_Disabilities': [int(request.form['Learning_Disabilities'])],

                'Parental_Education_Level': [int(request.form['Parental_Education_Level'])]

            })

            print(input_data)

            prediction = model.predict(input_data)

            return render_template(
                'home.html',
                prediction_text=f'Predicted Score: {prediction[0]:.2f}'
            )

        except Exception as e:
            return f"Error: {str(e)}"

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)