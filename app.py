from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/survey", methods=["GET", "POST"])
def survey():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        role = request.form.get("role", "").strip()
        satisfaction = request.form.get("satisfaction", "").strip()
        comments = request.form.get("comments", "").strip()

        return redirect(
            url_for(
                "thanks",
                name=name,
                role=role,
                satisfaction=satisfaction,
                comments=comments,
            )
        )

    return render_template("survey.html")


@app.route("/thanks")
def thanks():
    submission = {
        "name": request.args.get("name", "Anonymous"),
        "role": request.args.get("role", "Not provided"),
        "satisfaction": request.args.get("satisfaction", "Not rated"),
        "comments": request.args.get("comments", "No comments provided."),
    }
    return render_template("thanks.html", submission=submission)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
