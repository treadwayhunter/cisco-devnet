import yaml

with open('yaml_02.yaml', 'r') as file:
    data = yaml.safe_load(file)

print(data)