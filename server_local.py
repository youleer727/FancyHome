#!/usr/bin/env python2.7

"""
Columbia's COMS W4111.001 Introduction to Databases
Example Webserver

To run locally:

    python server.py

Go to http://localhost:8111 in your browser.

A debugger such as "pdb" may be helpful for debugging.
Read about it online.
"""

import os
import datetime


from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response
from flask import jsonify


tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)


#
# The following is a dummy URI that does not connect to a valid database. You will need to modify it to connect to your Part 2 database in order to use the data.
#
# XXX: The URI should be in the format of: 
#
#     postgresql://USER:PASSWORD@104.196.18.7/w4111
#
# For example, if you had username biliris and password foobar, then the following line would be:
#
#     DATABASEURI = "postgresql://biliris:foobar@104.196.18.7/w4111"
#
DATABASEURI = "postgresql://xl2672:1157@104.196.18.7/w4111" ## cloud
# DATABASEURI = "postgresql://vibrioh:confidence@localhost/PropertyManagement" ## local


#
# This line creates a database engine that knows how to connect to the URI above.
#
engine = create_engine(DATABASEURI)

#
# Example of running queries in your database
# Note that this will probably not work if you already have a table named 'test' in your database, containing meaningful data. This is only an example showing you how to run queries in your database using SQLAlchemy.
#
# engine.execute("""CREATE TABLE IF NOT EXISTS test (
#   id serial,
#   name text
# );""")
# engine.execute("""INSERT INTO test(name) VALUES ('grace hopper'), ('alan turing'), ('ada lovelace');""")


# before request
@app.before_request
def before_request():
    """
    This function is run at the beginning of every web request
    (every time you enter an address in the web browser).
    We use it to setup a database connection that can be used throughout the request

    The variable g is globally accessible
    """
    try:
        g.conn = engine.connect()
    except:
        print "uh oh, problem connecting to database"
        import traceback;
        traceback.print_exc()
        g.conn = None


@app.teardown_request
def teardown_request(exception):
    """
    At the end of the web request, this makes sure to close the database connection.
    If you don't the database could run out of memory!
    """
    try:
        g.conn.close()
    except Exception as e:
        pass









# @app.route is a decorator around index() that means:
#   run index() whenever the user tries to access the "/" path using a GET request
#
# If you wanted the user to go to e.g., localhost:8111/foobar/ with POST or GET then you could use
#
#       @app.route("/foobar/", methods=["POST", "GET"])
#
# PROTIP: (the trailing / in the path is important)
#
# see for routing: http://flask.pocoo.org/docs/0.10/quickstart/#routing
# see for decorators: http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
#
@app.route('/')
def index():
    """
    request is a special object that Flask provides to access web request information:

    request.method:   "GET" or "POST"
    request.form:     if the browser submitted a form, this contains the data in the form
    request.args:     dictionary of URL arguments e.g., {a:1, b:2} for http://localhost?a=1&b=2

    See its API: http://flask.pocoo.org/docs/0.10/api/#incoming-request-data
    """

    # DEBUG: this is debugging code to see what request looks like
    print request.args

    #
    # example of a database query
    #
    # Flask uses Jinja templates, which is an extension to HTML where you can
    # pass data to a template and dynamically generate HTML based on the data
    # (you can think of it as simple PHP)
    # documentation: https://realpython.com/blog/python/primer-on-jinja-templating/
    #
    # You can see an example template in templates/index.html
    #
    # context are the variables that are passed to the template.
    # for example, "data" key in the context variable defined below will be
    # accessible as a variable in index.html:
    #
    #     # will print: [u'grace hopper', u'alan turing', u'ada lovelace']
    #     <div>{{data}}</div>
    #
    #     # creates a <div> tag for each element in data
    #     # will print:
    #     #
    #     #   <div>grace hopper</div>
    #     #   <div>alan turing</div>
    #     #   <div>ada lovelace</div>
    #     #
    #     {% for n in data %}
    #     <div>{{n}}</div>
    #     {% endfor %}
    #
    # context = dict(data = names)
    return render_template("index.html")

# @app.route('/login')
# def login():
#     return render_template("login.html")

@app.route('/buyer')
def buyer():
    cursor = g.conn.execute("SELECT pid, zip, address, bed, bath, square, bdate, bid, water, bus, subway, start, listprice, evalprice, taxde, maintenancefee, aid FROM (SELECT * FROM properties_all P WHERE P.sale = true) P WHERE P.pid = 'prpt238' OR P.pid = 'prpt359' OR P.pid = 'prpt623'")
    cursor2 = g.conn.execute("SELECT * FROM agents_all A WHERE A.agnt_id = 'agnt40' OR A.agnt_id = 'agnt30'")
    print "/buyer was called"
    tuples = []
    tuples2 = []
    for r in cursor:
        tuples.append(r)
    cursor.close()
    for r in cursor2:
        tuples2.append(r)
    cursor2.close()
    context = dict(data = tuples, data2 = tuples2)
    return render_template("buyer.html", **context)

@app.route('/propertiesresult', methods = ['POST'])
def propertiesresult():
    bed = request.form['bed']
    bath = request.form['bath']
    min_square = request.form['min_square']
    max_square = request.form['max_square']
    min_listprice = request.form['min_listprice']
    max_listprice = request.form['max_listprice']
    water = request.form['water']
    taxde = request.form['taxde']
    sale = request.form['sale']
    print "/propertiesresult was called"
    cursor = g.conn.execute("SELECT pid, zip, address, bed, bath, square, bdate, bid, water, bus, subway, start, listprice, evalprice, taxde, maintenancefee, aid FROM (SELECT * FROM properties_all P WHERE P.sale = '"+ sale +"') P WHERE P.bed >= '"+ bed +"' AND P.bath >= '"+ bath +"' AND P.square >= '"+ min_square +"' AND P.square <= '"+ max_square +"' AND P.listprice >= '"+ min_listprice +"' AND P.listprice <= '"+ max_listprice +"' AND P.taxde = '"+ taxde +"' AND P.water = '"+ water +"'")
    tuples = []
    for r in cursor:
        tuples.append(r)
    cursor.close()
    context = dict(data = tuples)
    return render_template("propertiesresult.html", **context)

@app.route('/agentsresult', methods = ['POST'])
def agentsresult():
    pall = request.form['pall']
    psale = request.form['psale']
    psold = request.form['psold']
    min_avglpr = request.form['min_avglpr']
    max_avglpr = request.form['max_avglpr']
    min_avgspr = request.form['min_avgspr']
    max_avgspr = request.form['max_avgspr']
    print "/agentsresult was called"
    cursor2 = g.conn.execute("SELECT * FROM agents_all A WHERE A.pall >= '" + pall + "' AND A.psale >='" + psale + "' AND A.psold >= '" + psold + "' AND A.avglpr >='" + min_avglpr + "' AND A.avglpr <='" + max_avglpr + "' AND A.avgspr >='" + min_avgspr + "' AND A.avgspr <='" + max_avgspr + "'")
    tuples2 = []
    for r in cursor2:
        tuples2.append(r)
    cursor2.close()
    context = dict(data2 = tuples2)
    return render_template("agentsresult.html", **context)

@app.route('/school', methods = ['POST'])
def school():
    pid = request.form['clicked']
    cursor = g.conn.execute("SELECT pid, zip, address, bed, bath, square, bdate, bid, water, bus, subway, start, listprice, evalprice, taxde, maintenancefee, aid FROM properties_all P WHERE P.pid = '" + pid + "'")
    tuples = []
    for r in cursor:
        tuples.append(r)
    cursor.close()
    get_bid = g.conn.execute("SELECT P.bid FROM properties_all P WHERE P.pid = '"+ pid +"'")
    tbid = []
    for r in get_bid:
        tbid.append(r)
    get_bid.close()
    bid = tbid[0][0]
    cursor2 = g.conn.execute("SELECT S.sch_pri, S.sch_mid, S.sch_hi FROM schools S WHERE S.blk_id = '"+ bid +"'")
    tuples2 = []
    for r in cursor2:
        tuples2.append(r)
    cursor.close()
    context = dict(data = tuples, data2 = tuples2)
    return render_template("school.html", **context)

@app.route('/contactagent', methods = ['POST'])
def contactagent():
    aid = request.form['clicked']
    cursor = g.conn.execute("SELECT pid, zip, address, bed, bath, square, bdate, bid, water, bus, subway, start, listprice, evalprice, taxde, maintenancefee, aid FROM properties_all P WHERE P.aid = '"+ aid +"' AND P.sale = true")
    cursor1 = g.conn.execute("SELECT pid, zip, address, bed, bath, square, bdate, bid, water, bus, subway, start, listprice, evalprice, taxde, maintenancefee, aid FROM properties_all P WHERE P.aid = '" + aid + "' AND P.sale = false")
    cursor2 = g.conn.execute("SELECT * FROM agents_all A WHERE A.agnt_id = '" + aid + "'")
    tuples = []
    tuples1 = []
    tuples2 = []
    for r in cursor:
        tuples.append(r)
    cursor.close()
    for r in cursor1:
        tuples1.append(r)
    cursor1.close()
    for r in cursor2:
        tuples2.append(r)
    cursor2.close()
    print tuples2
    context = dict(data = tuples, data1 = tuples1, data2 = tuples2)
    return render_template("contactagent.html", **context)


@app.route('/agentlogin')
def agentlogin():
    return render_template("agentlogin.html")


@app.route('/agent_dashboard', methods=['POST', 'GET'])
def agent_dashboard():
    return render_template("agent_dashboard.html")


@app.route('/agent_dashboard_result', methods=['POST'])
def agent_dashboard_result():
    aid = request.form['agentid']
    print aid
    tuples = []
    tuples1 = []
    tuples2 = []
    cursor = g.conn.execute(
        "SELECT pid, zip, address, bed, bath, square, bdate, bid, water, bus, subway, start, listprice, evalprice, taxde, maintenancefee, aid, ossn, ofname ||' '|| olname AS fullname FROM properties_all P WHERE P.aid = '" + aid + "' AND P.sale = true")
    for r in cursor:
        tuples.append(r)
    cursor.close()
    cursor1 = g.conn.execute(
        "SELECT pid, zip, address, bed, bath, square, bdate, bid, water, bus, subway, start, listprice, evalprice, taxde, maintenancefee, aid, soldprice, ossn, ofname ||' '|| olname AS fullname FROM properties_all P WHERE P.aid = '" + aid + "' AND P.sale = false")
    for r in cursor1:
        tuples1.append(r)
    cursor1.close()
    cursor2 = g.conn.execute("SELECT * FROM agents_all A WHERE A.agnt_id = '{}';".format(aid))
    for r in cursor2:
        tuples2.append(r)
    cursor2.close()
    context = dict(data = tuples, data1=tuples1, data2=tuples2, aid = aid)
    return render_template("agent_dashboard_result.html", **context)


@app.route('/checkvalid', methods=['POST'])
def checkvalid():
    username = request.form['username']
    password = request.form['password']

    # print "SELECT * FROM Agents WHERE agnt_email LIKE '%%{}%%' AND agnt_id LIKE '%%{}%%';".format(username, password)

    # check whether the account exist in the database
    cursor = g.conn.execute(
        "SELECT * FROM Agents WHERE agnt_email LIKE '%%{}%%' AND agnt_id LIKE '%%{}%%';".format(username, password))
    tuples = []
    for r in cursor:
        tuples.append(r)
    cursor.close()

    print "tuples look like:"
    print tuples

    if len(tuples) == 1:

        # exist
        return jsonify(
            username=username,
            password=password,
            state="succeed",
            agentid=password,
            redirect='/agent_dashboard'
        )
    else:
        # doesn't exist
        return jsonify(
            state='failed'
        )

def is_safe(q):
    not_safe = ['DROP TABLE', 'DELETE FROM', 'DROP INDEX', 'DROP FROM', 'DROP DATABASE', 'DELETE TABLE', 'INSERT INTO',
                'TRUNCATE TABLE']
    for elem in not_safe:
        if elem in q.upper() or ('OR' in q.upper() and (("=" in q) or (">" in q) or ("<" in q) or ("!" in q))) or (
                'UPDATE' in q.upper() and 'SET' in q.upper()) or ('SELECT' in q.upper() and 'FROM' in q.upper()):
            return False
    return True

@app.route('/add', methods=['POST'])
def add():
    aid = request.form['aid']
    print aid
    zip = request.form['zip']
    print zip
    address= request.form['address']
    print address
    bed= request.form['bed']
    print bed
    bath= request.form['bath']
    print bath
    size= request.form['size']
    print size
    bdate= request.form['bdate']
    print bdate
    bid= request.form['bid']
    print bid
    water= request.form['water']
    print water
    listprice= request.form['listprice']
    print listprice
    evalprice= request.form['evalprice']
    print evalprice
    taxde= request.form['taxde']
    print taxde
    maintenancefee= request.form['maintenancefee']
    print maintenancefee
    ossn= request.form['ossn']
    print ossn
    ofname= request.form['ofname']
    print ofname
    olname= request.form['olname']
    print olname
    if not is_safe(address) or not is_safe(ofname) or not is_safe(olname):
        msg = 'NO SQL INJECTION PLEASE, or at least we think so.'
        return render_template("error_outside.html", msg=msg)
    count = g.conn.execute("SELECT COUNT(*) from properties")
    for r in count:
        s = r['count']
    count.close()
    s += 1
    pid = 'prpt' + str(s)
    print pid
    now = datetime.datetime.now()
    ldate = now.strftime("%m-%d-%Y")
    print ldate
    engine.execute("insert into properties values (%s,%s,%s,%s,%s,%s,%s,%s)", pid, zip, address, bed, bath, size, bdate, bid)
    print "Insert successful1"
    engine.execute("INSERT INTO Lists VALUES (%s,%s)", aid, pid)
    print "Insert successful2"
    spool = g.conn.execute(
        "SELECT * FROM owners WHERE onr_ssn LIKE '%%{}%%' ".format(ossn))
    ssnl = []
    for r in spool:
        ssnl.append(r)
    spool.close()
    print "tuples look like:"
    print ssnl
    if len(ssnl) == 1:
        ossn += '(1)'
        print ossn
    engine.execute("INSERT INTO Owners VALUES (%s,%s,%s)", ossn, ofname,olname)
    print "Insert successful3"
    engine.execute("INSERT INTO Blongs VALUES (%s,%s)", ossn, pid)
    print "Insert successful4"
    engine.execute("INSERT INTO States(st_start,prpt_id) VALUES (to_date(%s, 'MM/DD/YYYY'),%s)", ldate, pid)
    print "Insert successful5"
    engine.execute("insert into Prices VALUES (%s,NULL,%s,%s,%s,%s)", listprice, evalprice, taxde, maintenancefee, pid)
    print "Insert successful6"
    tuples = []
    tuples1 = []
    tuples2 = []
    cursor = g.conn.execute(
        "SELECT pid, zip, address, bed, bath, square, bdate, bid, water, bus, subway, start, listprice, evalprice, taxde, maintenancefee, aid, ossn, ofname ||' '|| olname AS fullname FROM properties_all P WHERE P.aid = '" + aid + "' AND P.sale = true")
    for r in cursor:
        tuples.append(r)
    cursor.close()
    cursor1 = g.conn.execute(
        "SELECT pid, zip, address, bed, bath, square, bdate, bid, water, bus, subway, start, listprice, evalprice, taxde, maintenancefee, aid, soldprice, ossn, ofname ||' '|| olname AS fullname FROM properties_all P WHERE P.aid = '" + aid + "' AND P.sale = false")
    for r in cursor1:
        tuples1.append(r)
    cursor1.close()
    cursor2 = g.conn.execute("SELECT * FROM agents_all A WHERE A.agnt_id = '{}';".format(aid))
    for r in cursor2:
        tuples2.append(r)
    cursor2.close()
    context = dict(data=tuples, data1=tuples1, data2=tuples2, aid=aid)
    return render_template("agent_dashboard_result.html", **context)




if __name__ == "__main__":
    import click


    @click.command()
    @click.option('--debug', is_flag=True)
    @click.option('--threaded', is_flag=True)
    @click.argument('HOST', default='0.0.0.0')
    @click.argument('PORT', default=8111, type=int)
    def run(debug, threaded, host, port):
        """
        This function handles command line parameters.
        Run the server using

            python server.py

        Show the help text using

            python server.py --help

        """

        HOST, PORT = host, port
        print "running on %s:%d" % (HOST, PORT)
        app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)


    run()