#!/usr/bin/python3
"""Downloads SW user and film info"""
import requests
from sys import argv

if __name__ == "__main__":
    try:
        films = {}
        try:
            r = requests.get("https://swapi.co/api/films/")
            for result in r.json().get('results'):
                films[result.get('url')] = result.get('title')
        except Exception:
            pass
        url = "http://swapi.co/api/people/"
        params = {"search": argv[1]}
        response = requests.get(url, params=params)
        d = response.json()
        print("Number of results:", d.get("count"))
        while True:
            for result in d.get("results"):
                print(result.get("name"))
                for film in result.get('films'):
                    print('\t', films.get(film))
            if d.get('next'):
                response = requests.get(d.get('next'))
                d = response.json()
            else:
                break
    except ValueError:
        print("Not a valid JSON")
    except Exception:
        pass
