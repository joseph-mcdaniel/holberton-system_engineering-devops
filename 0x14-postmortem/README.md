## 0x11. Postmortem

### Summary
* Date: August, 8th, 2017
* Duration of outage: 11:25 pm to 11:40 pm
* Users affected: One
* Root Cause: File configuration error.

### Timeline:
- **11:25 pm PST** - The container was spun with nginx pre-installed.
Installation of curl was successful.
- **11:26 pm PST** - Attempted `curl 0:80` received error:
`curl: (7) Failed to connect to 0 port 80: Connection refused`
- **11:30 pm PST** - Located the file /etc/nginx/sites-enabled/default and
discovered the file had been set to listen on port 8080.
- **11:31 pm PST** - Attempted `curl 0:8080` - successful.
Isolated issue as configuration error.
- **11:35 pm PST** - Wrote bash script to check if nginx is installed,
then using sed to substitute 8080 with 80 in the file:
sed -i 's/8080/80/g' /etc/nginx/sites-enabled/default
- **11:38 pm PST** - Ran script and checked status of nginx
- **11:40 pm PST** - Attempted `curl 0:80` - successful.

### Root Cause and Resolution
* In the file /etc/nginx/sites-enabled/default on line 21, the server is configured to listen to port 8080 instead of port 80
* This can be attributed to human error: Whoever pre-installed nginx in the container edited the file to listen to port 8080
* To resolve this, a script was made that would substitute any instance of 8080 with 80 in the file.

## Preventative Measures
* The script written was designed to be used to ensure that this issue will never happen again. It updates all installed programs, checks if nginx is installed and proceeds to check the file that was the root cause of this issue.
* To address the issue further a curl to check port 80 could be added at the end, another solution would be to grep the file in order to check if the line is formatted correctly.
