from flask import Flask ,request, redirect, url_for,session,Response

app=Flask(__name__)

@app.route("/",method=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")

        if username=="admin" and password="123":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return Response ("In valid credentials Try again",mimetype="text/plain")