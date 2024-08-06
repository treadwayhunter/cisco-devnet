import yaml

with open('yaml_03.yaml', 'r') as file:
    data = yaml.safe_load(file)

print(data)