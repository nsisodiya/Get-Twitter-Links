#!/usr/bin/python

import re
import sys 
import urllib2
import xml.dom.minidom
import ExpandUrl

print ExpandUrl.URLExpander().query(sys.argv[1])
