import urllib
import urllib2
import urlparse
import httplib

## http://the.taoofmac.com/space/blog/2009/08/10/2205

class URLExpander:
  # known shortening services
  shorteners = ['tr.im','is.gd','tinyurl.com','bit.ly','snipurl.com','cli.gs',
                'feedproxy.google.com','feeds.arstechnica.com']
  twofers = [u'\u272Adf.ws']
  # learned hosts
  learned = []
    
  def resolve(self, url, components):
    """ Try to resolve a single URL """
    c = httplib.HTTPConnection(components.netloc)
    c.request("GET", components.path)
    r = c.getresponse()
    l = r.getheader('Location')
    if l == None:
      return url # it might be impossible to resolve, so best leave it as is
    else:
      return l
  
  def query(self, url, recurse = True):
    """ Resolve a URL """
    components = urlparse.urlparse(url)
    # Check weird shortening services first
    if (components.netloc in self.twofers) and recurse:
      return self.query(self.resolve(url, components), False)
    # Check known shortening services first
    if components.netloc in self.shorteners:
      return self.resolve(url, components)
    # If we haven't seen this host before, ping it, just in case
    if components.netloc not in self.learned:
      ping = self.resolve(url, components)
      if ping != url:
        self.shorteners.append(components.netloc)
        self.learned.append(components.netloc)
        return ping
    # The original URL was OK
    return url


