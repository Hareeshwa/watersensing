from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def first():
    return render_template("index.html")


@app.route('/register')
def second():
    return render_template("second.html")

@app.route('/signup')
def signup():
    return render_template("sign_up.html")

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
#new code
import csv

def get_sensor_data(sensor_id):
    # Define the path to your CSV file
    csv_file_path = "C:\\Users\\hareeshwar\\Desktop\\Sample100.csv"


    # Initialize a list to store sensor data
    sensor_data = []

    # Open the CSV file and read data
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Sensor_ID'] == sensor_id:
                sensor_data.append(row)

    return sensor_data


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # Your code to generate the tree-based model goes here
    return render_template('index.html', sensor_data=None)

@app.route('/get_sensor_data', methods=['POST'])
def get_sensor_data_route():
    sensor_id = request.form.get('sensor_id')
    sensor_data = get_sensor_data(sensor_id)
    return render_template('index.html', sensor_data=sensor_data)

if __name__ == '__main__':
    app.run()




