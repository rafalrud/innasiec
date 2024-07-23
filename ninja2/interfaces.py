import yaml
from jinja2 import Environment, FileSystemLoader

# Wczytaj plik YAML
with open('interfaces.yaml') as file:
    config = yaml.safe_load(file)

# Przygotuj środowisko Jinja2
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.j2')

# Generuj konfigurację
output = template.render(interfaces=config['interfaces'])

# Zapisz wynik do pliku
with open('configuration.txt', 'w') as output_file:
    output_file.write(output)

print("Konfiguracja została wygenerowana i zapisana w pliku configuration.txt.")