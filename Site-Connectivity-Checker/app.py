import urllib3
import csv
import pandas as pd
http = urllib3.PoolManager()

def check_site_availability(web_address):
    try:
        request = http.request('GET', web_address, timeout=10,retries=urllib3.Retry())
        #checking the type of server response

        if request.status == 200:
            return True
        else:
            return False
    except urllib3.exceptions.NewConnectionError:
        return False
    except urllib3.exceptions.ProtocolError:
        return False
    except urllib3.exceptions.ClosedPoolError:
        return False
    except urllib3.exceptions.ConnectTimeoutError:
        return False
    except urllib3.exceptions.MaxRetryError:
        return False
    except urllib3.exceptions.LocationValueError:
        return False
    except urllib3.exceptions.DecodeError:
        return False
    
 
    

# reading the csv data
data = pd.read_csv('websites.csv')
print(data.head())
#Getting the web addresses and saving them into an array

web_addresses = data['Root Domain'].values

for site in web_addresses:
    if check_site_availability(site) :
        print(site+'-----is AVAILABLE')
    else:
        print(site+'-----IS DOWN')
    



