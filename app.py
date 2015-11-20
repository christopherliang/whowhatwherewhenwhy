import urllib2, google, bs4, re
from flask import Flask, render_template, redirect, url_for, request, Response

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def search():
    if request.method == 'GET' :
        searching = False
        return render_template("home.html",searching=False);
    else :
        searching = True
        q= request.form['search']
        r = google.search(q,num=10,start=0,stop=10)
        l=[]
        for result in r:
            l.append(result)

        print l[0]

        u = urllib2.urlopen(l[0])
        page = u.read()
#print page
        soup = bs4.BeautifulSoup(page,'html')
        raw = soup.get_text()
#print raw
        text = re.sub("[\t\n ]"," ",raw)
        print text
        #return render_template("home.html",searching=True,results = text)

if __name__=="__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=8000)

