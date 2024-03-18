from aves import request_json
from string import Template

url = "https://aves.ninjas.cl/api/birds"
response = request_json(url)

# Obtener lista de imágenes, título y descripción
lista_img = [(elemento.get('images', {}).get('main', ''), elemento.get('uid', ''), elemento.get('name', {}).get('spanish', ''), elemento.get('name', {}).get('english', '')) for elemento in response]

# Plantilla para cada tarjeta de ave
card =  """<div class="col-md-4 mb-3">
                <div class="card bird-card">
                    <div class="card-img-container">
                        <img src="$url" class="card-img-top mx-auto d-block h-100" alt="...">
                    </div>
                    <div class="card-body">
                        <h5 class="card-title text-center">$spanish_name</h5>
                        <h6 class="card-subtitle mb-2 text-muted text-center">$english_name</h6>
                    </div>
                </div>
            </div>
    """

# Crear una instancia de Template
img_template = Template(card)

# Construir el cuerpo de la página con las tarjetas
texto_img = ''
for img, uid, spanish_name, english_name in lista_img:
    texto_img += img_template.substitute(url=img, spanish_name=spanish_name, english_name=english_name) + '\n'

# Plantilla HTML
html_template = Template('''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Aves Chile</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <style>
        body {
            background-color: #999;
        }
        h1 {
            padding : 20px;
        }
        .bird-card {
            transition: background-color 0.3s ease;
        }

        .bird-card:hover {
            background-color:  rgb(134, 170, 183);
        }

        .card-img-container {
            height: 200px;
            overflow: hidden;
        }
    </style>
  </head>
  <body>
    <h1 class="text-center">Aves Chilenas</h1>
    <div class="container">
        <div class="row">
            $body
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </body>
</html>
''')

# Rellenar la plantilla HTML con el cuerpo de la página
html = html_template.substitute(body=texto_img)

# Guardar el archivo HTML
with open('index.html', 'w+', encoding='utf-8') as archivo:
    archivo.write(html)
