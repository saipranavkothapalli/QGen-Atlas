from flask import Flask, request, render_template, flash, redirect, url_for,session, Response, render_template_string
from objective import ObjectiveTest
from subjective import SubjectiveTest

app = Flask(__name__)

@app.route('/Answering.html')
def answering_page():
    return render_template('Answering.html')

app.secret_key= 'aica2'

'''
import nltk
import ssl

# Disable SSL verification
ssl._create_default_https_context = ssl._create_unverified_context

# Download NLTK data
nltk.download('all')

'''

@app.route('/')
def index():
	return render_template('index.html')
from flask import render_template

@app.route('/test_generate', methods=["POST"])
def test_generate():
    if request.method == "POST":
        inputText = request.form["itext"]
        testType = request.form["test_type"]
        noOfQues = request.form["noq"]
        gen_type=request.form["generate_type"]
        if testType == "objective":
            objective_generator = ObjectiveTest(inputText,noOfQues)
            question_list, answer_list = objective_generator.generate_test()
            testgenerate = list(zip(question_list, answer_list))  # Convert zip object to list of tuples
            if gen_type=="Q&A":
                return render_template('generatedtestdata.html', cresults = testgenerate)
            else:
                return render_template('Answering.html', cresults = testgenerate)
        elif testType == "subjective":
            subjective_generator = SubjectiveTest(inputText,noOfQues)
            question_list, answer_list = subjective_generator.generate_test()
            testgenerate = list(zip(question_list, answer_list))  # Convert zip object to list of tuples
            if gen_type=="Q&A":
                return render_template('generatedtestdata.html', cresults = testgenerate)
            else:
                return render_template('Answering.html', cresults = testgenerate)
        else:
            flash('Error Occurred!')
            return redirect(url_for('/'))

if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = 5001, debug=True)
    

	