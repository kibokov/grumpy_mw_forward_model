import numpy as np
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from urllib.parse import urljoin


def SDSS_footprint(input_stuff):
    
    '''
    coverage RA goes from 0 to 360
    coverage DES goes from -90 to +90
    
    
    Function will return a list of equal length of ras/decs with 1s (in footprint) and 0s (not in footprint)
    '''
    
    ras = input_stuff["ra"]
    session = input_stuff["seesh"]
    decs = input_stuff["dec"]
    url = input_stuff["url"]
    
    data = {"coverageRA":str(ras),"coverageDec":str(decs)}
    res = session.post(url, data=data)

    if "The area you requested" in str(res.content):
        return 1
    else:
        return 0
        
