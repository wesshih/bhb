#!/usr/bin/python 
""">> sqlcl << command line query tool by Tamas Budavari <budavari@pha.jhu.edu>
Usage: sqlcl [options] sqlfile(s)

Options:
        -s url	   : URL with the ASP interface (default: pha)
        -f fmt     : set output format (html,xml,csv - default: csv)
        -q query   : specify query on the command line
        -l         : skip first line of output with column names
        -h	   : show this message"""

formats = ['csv','xml','html']

default_url='http://cas.sdss.org/public/en/tools/search/x_sql.aspx'
default_fmt='csv'

def usage(status, msg=''):
    "Error message and usage"
    print __doc__
    if msg:
        print '-- ERROR: %s' % msg
    sys.exit(status)

def query(sql,url=default_url,fmt=default_fmt):
    "Run query and return file object"
    import urllib
    params = urllib.urlencode({'cmd': sql, 'format': fmt})
    return urllib.urlopen(url+'?%s' % params)    
    
def main(argv):
    "Parse command line and do it..."
    import os, getopt, string
    
    queries = []
    url = os.getenv("SQLCLURL",default_url)
    fmt = default_fmt
    writefirst = 1
    
    # Parse command line
    try:
        optlist, args = getopt.getopt(argv[1:],'s:f:q:lh?')
    except getopt.error, e:
        usage(1,e)
        
    for o,a in optlist:
        if   o=='-s': url = a
        elif o=='-f': fmt = a
        elif o=='-q': queries.append(a)
        elif o=='-l': writefirst = 0
        else: usage(0)
        
    if fmt not in formats:
        usage(1,'Wrong format!')

    # Enqueue queries in files
    for fname in args:
        try:
            queries.append(open(fname).read())
        except IOError, e:
            usage(1,e)

    # Run all queries sequentially
    for qry in queries:
        ofp = sys.stdout
        file = query(qry,url,fmt)
        # Output line by line (in case it's big)
        line = file.readline()
        if line.startswith("ERROR"): # SQL Statement Error -> stderr
            ofp = sys.stderr
        if writefirst:
            ofp.write(string.rstrip(line)+os.linesep)
        line = file.readline()
        while line:
            ofp.write(string.rstrip(line)+os.linesep)
            line = file.readline()


if __name__=='__main__':
    import sys
    main(sys.argv)




