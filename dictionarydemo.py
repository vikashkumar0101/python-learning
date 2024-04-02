country = input()  # add new country
visits = int(input())  # nos of visits
list_of_cities = input()

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "stuttgart"]
    }
]


def add_new_country(names, time_visited, cities_visited):
    new_country = {}
    new_country["country"] = names
    new_country["visits"] = time_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


add_new_country(country, visits, list_of_cities)
print(f"I have been to {travel_log[2]["country"]}  and visited {travel_log[2]["visits"]} times")
print(f"And my favourite cities were {travel_log[2]["cities"][0]}")
