from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

# Route to serve the ads.txt file
@app.route('/ads.txt')
def ads_txt():
    return send_from_directory('.', 'ads.txt')

# Main converter route
@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            conversion_type = request.form['conversion']

            if conversion_type == 'cgpa_to_percent':
                result = f"{value * 9.5:.2f} %"
            elif conversion_type == 'percent_to_cgpa':
                result = f"{value / 9.5:.2f} CGPA"
            elif conversion_type == 'gpa_to_percent':
                result = f"{(value / 4) * 100:.2f} %"
            elif conversion_type == 'percent_to_gpa':
                result = f"{(value / 100) * 4:.2f} GPA"
            elif conversion_type == 'average_to_percent':
                result = f"{value:.2f} %"
            else:
                result = "Invalid conversion selected."
        except ValueError:
            result = "Please enter a valid number."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
