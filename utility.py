import requests

from output import red_text, yellow_text


def get_geolocation(ip, verbose=False):
    GEOIP_URL = "https://ipinfo.io/{}/json".format(ip.strip())
    if verbose:
        print(yellow_text("{:>16}: Making GEOIP request: {}".format(
            ip, GEOIP_URL)))
    response = requests.get(GEOIP_URL)

    if response.status_code != 200:
        country = red_text("Error! [ {} ]".format(response.status_code))
    else:
        r = response.json()
        country = r['timezone'] if 'timezone' in r else '???'
    return country


def get_initial_url(host, scheme="http", port=80):
    return "{}://{}:{}/".format(scheme, host, port)
