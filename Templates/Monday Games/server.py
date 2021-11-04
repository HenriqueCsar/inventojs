from flask import Flask, request, render_template, redirect
app=Flask(__name__, template_folder='pages')

#Home server in english language
@app.route("/en/")
def index():
    return render_template('/en/index.html')

#End of server in english language

#From here you can already start developing pages for another language
    
@app.route("/", methods=['GET'])
def redirect_():
    if request.method == 'GET':
        return redirect("/en/")
    else:
        return 'An error has occurred, the administrator has been notified.'


if __name__ == "__main__":
    app.run()
