"""This is a sample Flask app that demonstrates how to use OpenAI's API to generate 
unit tests for code or file contents"""
import os
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-3.5-turbo"

@app.route("/", methods=["GET", "POST"])
def index():
    """ Generate unit tests from code or file contents
    and display the generated unit tests on the index page"""
    if request.method == "POST":
        file = request.files.get("file")
        code = request.form.get("code")
        if file:
            file_contents = file.read().decode("utf-8")
            unit_tests = generate_unit_tests_from_file(file_contents)
        elif code:
            unit_tests = generate_unit_tests_from_code(code)
        else:
            unit_tests = ""

        return redirect(url_for("index", result=unit_tests))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_unit_tests_from_file(file_contents):
    """ Generate unit tests from file contents"""
    # Process the file contents and generate unit tests
    # Replace the following code with your unit test generation logic
    unit_tests = "These are the generated unit tests from file:\n1. Test 1\n2. Test 2\n3. Test 3"
    return unit_tests


def generate_unit_tests_from_code(code):
    """ Generate unit tests from code using OpenAI's API"""
    prompt = f"Generate unit tests for the following code:\n\n{code}\n\n"
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt},
            ],
        temperature=0,
        n = 3
    )
    unit_tests = [choice['message']['content'] for choice in response.choices]
    return unit_tests


if __name__ == "__main__":
    app.run()
