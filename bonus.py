#!/usr/bin/env python

'''
    This script processes a web server access log and allows extraction of
    data from each line.

    It also generates an ascii bar chart of requests per minute, and
    optionally generates an html report around the chart, suitable to run
    hourly from cron.

    - Matthew Ghali, 10/2015
'''


import datetime, sys
from dateutil import parser


class LogLine(object):
    '''
        object that returns useful attributes from an access.log line
    '''
    def __init__(self, line):
        l = line.split()
        self.srcaddr = l[0]
        self.datetime = parser.parse(' '.join([l[3][1:-9], l[3][-8:],
                                              l[4][:-1]]))
        self.unixtime = int(self.datetime.strftime('%s'))
        self.method = l[5][1:]
        self.uri = l[6]
        self.httpvers = l[7][:-1]
        self.httpcode = l[8]
        self.contentlen = l[9]
        self.useragent = ' '.join(l[11:])[1:]


def quantize(requests, incr):
    '''
        given a list of event times, count events per 'incr' intervals.
        returns: (dict) with a key per interval.
    '''
    buckets = dict()
    bucket = requests[0]
    buckets[bucket] = 0

    for t in requests:
        if t < bucket + incr:
            buckets[bucket] += 1
        else:
            bucket = bucket + incr
            buckets[bucket] = 1

    return buckets


def graph(buckets, width):
    '''
        produce a graph from data in dictionary, of 'width' characters wide.
    '''
    maxval = max(buckets.values())
    keylen = 17

    space = len(str(maxval)) + 3
    print ' ' * keylen, 0, '*' * (width - space), maxval

    for bucket in sorted(buckets):
        rval = (buckets[bucket] / float(maxval)) * width
        print datetime.datetime.fromtimestamp(bucket).strftime('%D %T'), '*' * int(rval)


def report(requests):
    '''
        produce an html report from output of the graph() function.
    '''
    reportwidth = 50
    quantizelen = 10

    start_time  = datetime.datetime.fromtimestamp(requests[0]).strftime('%D %T')
    end_time = datetime.datetime.fromtimestamp(requests[-1]).strftime('%D %T')
    buckets = quantize(requests, quantizelen)
 
    print "<html><head>"
    print "<title>", start_time, '-', end_time, "</title>"
    print "</head><body>"
    print "<h1>Web requests for the period", start_time, '-', end_time, "</h1>"
    print "<pre>"
    graph(buckets, reportwidth)
    print "</pre></body></html>"
    


if __name__ == '__main__':
    requests = list()
    with open(sys.argv[1], 'r') as logfile:
        for line in logfile.readlines():
            logline = LogLine(line)
            requests.append(logline.unixtime)

    report(requests)

