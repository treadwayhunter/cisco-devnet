import yaml

with open('yaml_01.yaml', 'r') as file:
    data = yaml.safe_load(file)

print(f'Data: {data}')