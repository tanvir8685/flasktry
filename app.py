from flask import Flask ,request, redirect, url_for,session,Response

app=Flask(__name__)
app.secret_key="supersecrect"

@app.route("/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")

        if username=="admin" and password=="123":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
#            return Response ("In valid credentials Try again ",mimetype="text/plain")
#            return Response ()
            html_content = f'''
                <h3>Invalid credentials. Try again.</h3>
                <a href="{url_for('login')}" style="
                    display: inline-block;
                    padding: 8px 16px;
                    background-color: #007bff;
                    color: white;
                    text-decoration: none;
                    border-radius: 4px;
                    font-family: Arial, sans-serif;
                ">Home</a>
                 '''
            return Response(html_content, mimetype="text/html")
    return '''
        <h2>Login Page </h2>
        <form method="POST">
            Username:<input type="text" name="username"><br>
            Password:<input type="text" name="password"><br>
            <input type="submit" value="Login">
        </form>

'''
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f"""
    <h2>Welcome,{session["user"]}?</h2>
    <a href={url_for('logout')}>Log Out </a>

    """
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))