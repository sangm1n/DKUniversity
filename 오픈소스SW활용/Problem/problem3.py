"""
Design and implement a class Country that stores the information on countries s
uch as nation name, capital city, population, and area.
Then write a program that reads in a set of countries and prints
"""


class Country:
    def __init__(self, nation_name, capital_city, population, area):
        self.nation_name = nation_name;
        self.capital_city = capital_city;
        self.population = population;
        self.area = area;
        self.density = round(self.area / self.population, 2);


nation_name = ['Korea', 'USA', 'Japan', 'China', 'Tailand']
capital_city = ['Seoul', 'Washington, D.C', 'Tokyo', 'Beijing', 'Bangkok']
population = [51164435, 326766748, 127185332, 1415045928, 69183173]
area = [100210, 9372610, 377930, 9706961, 513120]

country = []
for i in range(5):
    country.append(Country(nation_name[i], capital_city[i], population[i], area[i]))


def largestArea(country):
    area = []
    for i in range(len(country)):
        area.append(country[i].area)
    large_area = max(area)
    large_area_idx = area.index(large_area)

    print('========== Largest Area Information ==========')
    print('{}, Area is {}\n'.format(
        country[large_area_idx].nation_name, country[large_area_idx].area
    ))


def largestPopulation(country):
    population = []
    for i in range(len(country)):
        population.append(country[i].population)
    large_pop = max(population)
    large_pop_idx = population.index(large_pop)

    print('======= Largest Population Information =======')
    print('{}, Population is {}\n'.format(
        country[large_pop_idx].nation_name, country[large_pop_idx].population
    ))


def largestDensity(country):
    density = []
    for i in range(len(country)):
        density.append(country[i].density)
    large_density = max(density)
    large_density_idx = density.index(large_density)

    print('=== Largest Population Density Information ===')
    print('{}, Population Density is {}\n'.format(
        country[large_density_idx].nation_name, country[large_density_idx].density
    ))


def capitalCity(country):
    print('====== Country Capital City Information ======')

    for i in range(len(country)):
        print('{}, capital city is {}'.format(
            country[i].nation_name, country[i].capital_city
        ))


largestArea(country)
largestPopulation(country)
largestDensity(country)
capitalCity(country)
