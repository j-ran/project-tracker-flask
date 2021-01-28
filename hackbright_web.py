"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github) 
    # unpacking returned row = ['Lucia', 'Racine', 'lracine0']
    # first = row[0] -> 'Lucia'
    # last = row[1] -> 'Racine'
    # github = row[2] -> 'lracine0'


    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github)   

    print("{} is the GitHub account for {} {}".format(github, first, last))

    return html


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""
    first = request.form.get('first')
    last = request.form.get('last')

    Some SQL to INSERT into database

    return html that says operation happened 

    return render_template("student_creation.html",
                            first=first,
                            last=last)
    
@app.route("/student-add-input", methods=['POST'])
def student_add():
    """Add a student."""
    first = request.form.get('first')
    last = request.form.get('last')

    take in the information from the html form

    redirect
        
    
if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
