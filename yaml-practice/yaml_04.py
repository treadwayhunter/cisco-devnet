# create a yaml file from a dictionary
import yaml

movie_ratings = {
    'Interstellar': 99,
    'Inception': 98,
    'Beauty and the Beast': 98,
    'Gnomeo and Juliet': 10,
    'Dune: Part 1': 98,
    'Dune: Part 2': 99
}

with open('yaml_04.yaml', 'w') as file:
    yaml.dump(movie_ratings, file)

print('Writing to file complete!')