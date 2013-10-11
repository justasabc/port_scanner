Python Port Scanner 
========
- 2011    - Stephen Gricci
- 2013.10 - justasabc

Usage
----
* show help

`python main.py --help`
* use normal ip

`python main.py localhost`
`python main.py 192.168.1.200`
* use multi-range ip

`python main.py 192.168.1.200-202`
`python main.py 192-193.168-170.1-2.200-202`
* use two kinds of port upper-bound(1024 or 65535)

`python main.py 192.168.1.200 -w`
`python main.py 192.168.1.200 -m`
* show progress bar

`python main.py 192.168.1.200 -p`
* save result fo file

`python main.py 192.168.1.200 -f 1.txt`

Features
----
- Run on windows and linux-compatible platform
- Support general command line arguments
- Support prograss bar while processing
- Allow user to hide progress
- Support multi-range ip scaning
- Allow user to save scaning results to file

TODO
----
- Use multi-threading 
- Support general user interface(GUI)
