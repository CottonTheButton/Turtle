#!/usr/local/bin/python3
import requests, math
from bs4 import BeautifulSoup


def adult_entertainment():
    pass


def alphabetize(*words):
    lists = sorted(words)
    for entry in lists:
        print(entry)


def corona():
    req = requests.get("https://virusncov.com/")
    source = req.content
    soup = BeautifulSoup(source, "html.parser")

    total_cases_broad = soup.find("h2")
    total_cases = total_cases_broad.find("span")
    death_cases_broad = soup.find(class_="second-count mt-large")
    death_cases = death_cases_broad.find(class_="red-text")
    recovery_cases_broad = soup.find(class_="second-count mt-large")
    recovery_cases = recovery_cases_broad.find(class_="green-text")

    currently_infected_broad = soup.find(class_="firt-div")
    currently_infected = currently_infected_broad.find("span")
    mild_condition = soup.find(class_="pupp-text")
    serious_cases = soup.find(class_="red-text")

    closed_cases_broad = soup.find(class_="firt-div")
    closed_cases = closed_cases_broad.find("span")

    print(f"{soup.find('small').get_text()}\n")

    print(f"Total cases: {total_cases.get_text()}")
    print(f"Closed Cases:{closed_cases.get_text()} cases closed (out of {total_cases.get_text()}).")
    print(f"Number of deaths: {death_cases.get_text()}")
    print(f"Numer of recoveries: {recovery_cases.get_text()}\n")

    print("Active Cases:")
    print(f"There are {currently_infected.get_text()} patients that are currently infected.")
    print(f"{mild_condition.get_text()} are in a not-so-serious condition")
    print(f"{serious_cases.get_text()} are in a serious condition.\n")



def factorial(num):
    print(f"The answer is {math.factorial(int(num))}")


def read(file_name):
    file = open(file_name, 'r')
    print(file.read())

def solve(operator, *numbers):
    numbers_list = list(numbers)
    sum = 0
    for number in numbers_list:
        sum+= int(number)

    print(f"The sum is {sum}")
