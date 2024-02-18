import requests
import random
from selenium import webdriver


def check_repo_number(user_name):
    url = f"https://api.github.com/users/{user_name}/repos"
    response = requests.get(url)
    assert response.status_code == 200, f"Action failed with status code: {response.status_code}"
    repos = response.json()
    assert len(repos) > 5, f"{user_name} has only {len(repos)} in their Github profile"
    print(f"{user_name} has {len(repos)} repositories")


def select_random_name(num_of_names) -> list:
    name_file_path = r"names.json"
    selected_names = []
    with open(name_file_path, 'r') as n:
        names = []
        for line in n:
            name = line.strip().strip(',').strip('"')
            # print(name)
            if name:
                names.append(name)
    for i in range(num_of_names - 1):
        selected_names.append(random.choice(names))
    return selected_names


def agify(names_list) -> None:
    for name in names_list:
        url = f'https://api.agify.io/?name={name}'
        response = requests.get(url)
        assert response.status_code == 200, f"Error, status code {response.status_code}"
        data = response.json()
        age = data.get('age')
        if age:
            print(f"{name} is estimated to be at age {age}.")
        else:
            print(f"couldn't predict {name}'s name.")


def check_num_of_universities(country) -> int:
    url = f'http://universities.hipolabs.com/search?country={country}'
    response = requests.get(url)
    assert response.status_code == 200, f"Error, status code {response.status_code}"
    universities = response.json()
    assert len(universities) >= 5, f"{country} has less then 5 universities"
    return len(universities)


def check_title(url, title):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    dr = webdriver.Chrome(options=options)
    try:
        dr.get(url)
        site_title = dr.title
        # Didn't want to user assert here because it will stop thw program if th titles not match
        # assert site_title == title, f'Titles does not match'
        if site_title == title:
            print("Titles match")
        else:
            print("Title doesn't match")
            print(f"This is the website title: {site_title}")
    finally:
        dr.quit()


# check_title(url="https://www.ycombinator.com/", title='Y-Combinator')
# check_title(url="https://hub.docker.com/", title="Docker HubContainer Image Library | App Containerization")
# username = input("Please Enter username")
# check_repo_number(user_name='avielb')
random_names = select_random_name(4)
agify(names_list=random_names)
# country = input("Enter a country name to check how many universities there is that country")
# print(check_num_of_universities(country=country.title()))
