from flask import Flask, g, render_template, request, redirect
import json
import requests
app = Flask(__name__)

@app.route('/')
def index():
    url = 'https://graph.facebook.com/v2.8/' + 'nieieeestudentbranch/events' \
    + '?fields=id%2Cname%2Ccover%2Cstart_time%2Cdescription%2Cplace%2Cticket_uri' \
    + '&access_token=1327383467301154%7CYDfQ94wTelbffydG5XrnanHnqu0'
    json1_str = requests.get(url)
    json1_data = json.loads(json1_str.text)["data"][:4]
    url = 'https://graph.facebook.com/v2.12/374095752666883?fields=photos.fields(source).limit(6)&access_token=1327383467301154%7CYDfQ94wTelbffydG5XrnanHnqu0'
    json1_str = requests.get(url)
    json2_data = json.loads(json1_str.text)["photos"]["data"]
    a=[]
    for x in json2_data:
        a.append(x["source"])
    return render_template('index.html',events=json1_data, glinks=a[:6])

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/roadmap')
def roadmap():
    return render_template('roadmap.html')



#this might need to go
@app.route('/projects')
def projects():
    secret = '?client_id=1a84d3397645fd06d61b&client_secret=de3ce9a9140fcb03f4118a8d5cb641ac0a79563e'
    json1_str = requests.get('https://api.github.com/users/nisbweb/repos' + secret)
    json1_data = json.loads(json1_str.text)
    return render_template('projects.html',projects=json1_data)


@app.route('/events/all')
def events_all():
    url = 'https://graph.facebook.com/v2.8/' + 'nieieeestudentbranch/events' \
    + '?fields=id%2Cname%2Ccover%2Cstart_time%2Cdescription%2Cplace%2Cticket_uri' \
    + '&access_token=1327383467301154%7CYDfQ94wTelbffydG5XrnanHnqu0'
    print url
    json1_str = requests.get(url)
    json1_data = json.loads(json1_str.text)["data"]
    j1 = json1_data[:len(json1_data):2]
    j2 = json1_data[1:len(json1_data):2]
    return render_template('events.html',events1=j1, events2=j2, title="All Events")

@app.route('/events/cs')
def events_cs():
    url = 'https://graph.facebook.com/v2.8/' + 'nieieeecomputersociety/events' \
    + '?fields=id%2Cname%2Ccover%2Cstart_time%2Cdescription%2Cplace%2Cticket_uri' \
    + '&access_token=1327383467301154%7CYDfQ94wTelbffydG5XrnanHnqu0'
    print url
    json1_str = requests.get(url)
    json1_data = json.loads(json1_str.text)["data"]
    j1 = json1_data[:len(json1_data):2]
    j2 = json1_data[1:len(json1_data):2]
    return render_template('events.html',events1=j1, events2=j2, title="Computer Society Events")


@app.route('/events/wie')
def events_wie():
    url = 'https://graph.facebook.com/v2.8/' + 'nieieeewie/events' \
    + '?fields=id%2Cname%2Ccover%2Cstart_time%2Cdescription%2Cplace%2Cticket_uri' \
    + '&access_token=1327383467301154%7CYDfQ94wTelbffydG5XrnanHnqu0'
    print url
    json1_str = requests.get(url)
    json1_data = json.loads(json1_str.text)["data"]
    j1 = json1_data[:len(json1_data):2]
    j2 = json1_data[1:len(json1_data):2]
    return render_template('events.html',events1=j1, events2=j2, title="Women in Engineering Events")

@app.route('/ankura')
def ankura():
    return redirect('http://ankura.nisb.in')

@app.route('/adroit')
def adroit():
    return redirect('http://adroit.nisb.in')

@app.route('/events/feedback')
def events_feedback():
    return render_template('feedback.html')

@app.route('/cs')
def cs():
    return render_template('cs.html')

@app.route('/wie')
def wie():
    return render_template('wie.html')

@app.route('/fg')
def fg():
    return 'Page Under Construction'

@app.route('/gallery')
def gallery():
    url = 'https://graph.facebook.com/v2.12/374095752666883?fields=photos.fields(source).limit(100)&access_token=1327383467301154%7CYDfQ94wTelbffydG5XrnanHnqu0'
    json1_str = requests.get(url)
    json1_data = json.loads(json1_str.text)["photos"]["data"]
    a=[]
    for x in json1_data:
        a.append(x["source"])
    return render_template('gallery.html',links=a)

@app.route('/contact')
def contact():
    return render_template('contact.html')






#redirects
@app.route('/ank18ipl')
def ank18ipl():
    return '<script>window.location = "http://e.nisb.in/register/997011107122033";</script>'




@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', errorcode=404)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
