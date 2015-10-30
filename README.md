# Discovery Team task test


Attached is a sample Apache log-file. Using standard command-line tools, parse the file to produce the following:

- The top 10 IPs making the most requests, displaying the IP address and number of requests made
- The top 10 User agents making the most requests - possibly normalizing those
- Top 10 requested pages and the number of requests made for each
- Percentage of successful requests
- Percentage of unsuccessful requests
- Top unsuccessful page requests
- The total number of requests made every minute in the time period covered
- For each of the top 10 IPs, show the top 5 pages requested and the number of requests for each

For bonus points, please explain what you think is going on in this log-file. For extra bonus points, generate an ASCII bar-chart showing the number of requests per minute For super extra bonus points, write a script that would do this every hour and generate a html report.  Reply by email with your command lines used to generate the above reports


## Solutions
Solutions for all command-line tasks can be found in:
 * The [oneliners](../master/oneliners) shell script, annotated by task. 
 * A sample [run of the script](https://travis-ci.org/mattghali/wikimedia) is available via travis-ci.org.
 * A [bonus script](../master/bonus.py) script generates an ascii bar graph of web requests, showing requests per ten-second period (configurable, per minute wasn't very exciting looking) is included.
 * From the log contents, it looks like several hosts are trying repeatedly to probe for a path traversal exploit. That doesn't make sense- either it works the first time, or it doesn't work.


