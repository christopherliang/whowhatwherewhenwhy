import urllib2, google, bs4, re, utils
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
        
        #looking for who??
        if q[0:3].lower()=="who":
            exp = "[A-Z][a-z]+ [A-Z][a-z]+"
            expForNames = "[A-Z][a-z]+"
        #looking for when??
        else:
            if (q[0:4].lower()=="when"):
                exp="January [1-9]+|February [1-9]+|March [1-9]+|April [1-9]+|May [1-9]+|June [1-9]+|July [1-9]+|August [1-9]+|September [1-9]+|October [1-9]+|November [1-9]+|December [1-9]+"

            #look for something else...? we'll give you a name.
            else:
                exp = "[A-Z][a-z]+"


        result = re.findall(exp,text)
        #resultForNames = re.findall(expForNames, text)

        #finding the most common outcome from result
        answer = utils.findMostCommonElement(result)
        
        #print resultForNames
        #namesList = utils.compareNames(resultForNames)
        
        #print namesList
        print result
        return render_template("answer.html",searching=True,results = answer)

if __name__=="__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=8000)

