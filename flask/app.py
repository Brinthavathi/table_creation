from flask  import Flask, render_template, request
import requests

app=Flask(__name__)

# new_post=[]
# new=[120185]

# @app.route("/")

# def hello_world():
#     url="https://api.mfapi.in/mf/"+str(new[0])

#     resp=requests.get(url)
   
#     return render_template("index.html",data=resp.json().get("data")[0].get("nav"))

sum=[]
some_of=[139619,148921,149383,148404,119354,149368,149366]
@app.route("/",methods=["POST","GET"])
def hello():
    for i in range(len(some_of)):
        url="https://api.mfapi.in/mf/"+str(some_of[i])
        resp=requests.get(url)
        temp2=resp.json().get("meta").get("fund_house")
        new_get=resp.json().get("data")[0].get("nav")
        temp={"id":some_of[i],"fund_house":temp2,"nav":new_get}
        sum.append(temp)
        print(temp)

    return render_template("index.html",data=sum)



if __name__ =="__main__" : 
   app.run(debug=True)  