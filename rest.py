import requests
from pyassert import *


def get(url, params):
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        json = resp.json()
        print(json)
        if assert_that(resp.ok).is_true():
            print("ok")
            # todo log success

    except requests.exceptions.RequestException as e:
        print("yo")
        # todo log error
        print(e)
    return


def post():
    # todo post method
    return


def put():
    # todo put method
    return


def patch():
    # todo patch method
    return
