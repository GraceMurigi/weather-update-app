from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
from weather import query_api

app = Flask(__name__)
# app.config['DEBUG'] = True


@app.route('/')
def index():
    return render_template(
        'weather.html',
        data=[{'name':'Nairobi'}, {'name':'Mombasa'}, {'name':'Kisumu'},
        {'name':'Dar es Salaam'}, {'name':'Dodoma'}, {'name':'Kampala'}, 
        {'name':'Mbarara'}, {'name':'Addis Ababa'}, {'name':'Khartoum'}, 
        {'name':'Kigali'}])

@app.route("/result" , methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query_api(select)
    pp(resp)
    if resp:
       data.append(resp)
    # if len(data) != 2:
    #     error = 'Bad Response from Weather API'
    return render_template(
        'result.html',
        data=data,
        error=error)
    
if __name__=='__main__':
    app.run(debug=True)