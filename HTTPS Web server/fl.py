# connect on http://127.0.0.1:8082 or https://127.0.0.1:8082
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask is running!'

@app.route('/data')
def names():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)

@app.route('/html')
def html():
    pp = '''<HTML>

<HEAD>

<TITLE>Your Title Here</TITLE>

</HEAD>

<BODY BGCOLOR="FFFFFF">

<CENTER><IMG SRC="https://cdn.arstechnica.net/wp-content/uploads/2014/05/more-clouds.jpg" ALIGN="BOTTOM"> </CENTER>

<HR>

<a href="http://somegreatsite.com">Link Name</a>

is a link to another nifty site

<H1>This is a Header</H1>

<H2>This is a Medium Header</H2>

Send me mail at <a href="mailto:support@yourcompany.com">

support@yourcompany.com</a>.

<P> This is a new paragraph!

<P> <B>This is a new paragraph!</B>

<BR> <B><I>This is a new sentence without a paragraph break, in bold italics.</I></B>

<HR>

</BODY>

</HTML> '''
    return pp

if __name__ == '__main__':
    #HTTP
    # app.run(port="8082")
    #HTTPS
    app.run(port="8082", ssl_context=('cert.pem', 'key.pem'))









'''
if you would like to generate new certificates follow these steps

To run https functionality or SSL authentication in flask application you first install "pyOpenSSL" python package using:

 pip install pyopenssl

Next step is to create 'cert.pem' and 'key.pem' using following command on terminal :

 openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 
'''
