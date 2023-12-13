from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/home")
def index():
    return render_template("home.html")

@app.route('/compare', methods=['POST'])
def compare():
    # Get the uploaded files
    file1 = request.files['csvFile1']
    file2 = request.files['csvFile2']

    # Secure the filenames and save the files
    filename1 = secure_filename(file1.filename)
    filename2 = secure_filename(file2.filename)
    file1.save(os.path.join('/path/to/save', filename1))
    file2.save(os.path.join('/path/to/save', filename2))

    # Read the CSV files
    df1 = pd.read_csv(os.path.join('/path/to/save', filename1))
    df2 = pd.read_csv(os.path.join('/path/to/save', filename2))

    # Compare the two dataframes
    comparison = df1.compare(df2)

    # If comparison is empty, files are identical
    if comparison.empty:
        return "The CSV files are identical."
    else:
        return "The CSV files are not identical. Differences: " + str(comparison)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
