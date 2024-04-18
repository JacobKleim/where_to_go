# where_to_go
 

## Project Description
 - The project "Where to Go" is aimed at creating an interactive map of Moscow, which will present various places of active recreation with detailed descriptions

## Technologies and tools
 - Python 3.9.10

## Demo
 - Web-site address:
 ```
 https://jacobkl.pythonanywhere.com/
 ```
 - Admin panel address. Username and password:
 ```
 https://jacobkl.pythonanywhere.com/admin
 ```
 ```
 admin
 ```


## Setup
 Clone this repository and go to the project folder:
   ```bash
   cd /c/project_folder
   ```
   ```bash
   git clone git@github.com:JacobKleim/where_to_go.git
   ```
   ```bash
   cd /c/project_folder/where_to_go
   ```
## Environment      
 Сreate and activate a virtual environment  
   ```
   python -m venv venv
   ```
   ```bash
   source venv/Scripts/activate
   ```
## Requirements
   Update the Python package manager to the latest version:
   ```
   python -m pip install --upgrade pip
   ```
   Install dependencies:
   ```
   pip install -r requirements.txt
   ``` 
   Create an .env file and populate it with data:
   ```
   SECRET_KEY=django-insecure-=)s$o(p)(enter your key)
   DEBUG=True or False
   ALLOWED_HOSTS=Your website's domain or/and IP address
   ```

## Run
   If necessary, make migrations and start the project:
   ```
   python manage.py migrate
   ```
   ```
   python manage.py runserver
   ```

   If you want to create new objects in the database, you can use a script that uses data from [GitHub](https://github.com/) and takes two parameters: username/project name and folder name in the project. This script collects the location data from the json files folder and creates new objects in the database.
   
   ```
   python manage.py load_place username/project_name folder_name
   ```

   Example json file:
   ```
   {
    "title": "Дизайн-квартал Флакон",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/40457e6b95ee4512d3c980202db6c12b.jpg"
    ],
    "description_short": "Креативный кластер Флакон вырос в целый район благодаря постоянному взаимодействию с горожанами, созданию живого творческого сообщества и внимательному выбору резидентов. ",
    "description_long": "<p>Флакон — место притяжения горожан и туристов. Здесь разместилось множество шоу-румов, студий и мастерских, кафе и и ресторанов, площадок для обучения, концертных и театральных пространств и многое другое. Всего свыше 250 арендаторов. Флакон создан так, чтобы каждый посетитель мог здесь творить, самовыражаться и отдыхать.</p><h3>Особенности креативного кластера</h3><ul><li>Это открытое и доступное пространство без заборов, с коротким проходом от станции метро Дмитровская.</li><li>Инфраструктура удобна и продолжает улучшаться. Есть парковка и велопарковка, каршеринг, пешеходная зона, зелёные зоны для отдыха, спортивные площадки под открытым небом.</li><li>Для резидентов созданы такие рабочие условия, в которых комфортно творить.</li><li>Городские события проходят в новом формате, к ним присоединяются яркие и уникальные проекты из разных областей — культуры, искусства, бизнеса.</li></ul><blockquote class=\"directSpeech\"><p class=\"directSpeech-text\">Наш неспальный район — это атмосфера локального туризма, фестиваля. Настроение, за которым не нужно никуда лететь.</p></blockquote><p>На Флаконе проходят масштабные культурные и фестивальные события. Фестивали страноведения проводятся в формате «дней» разных стран — Франции, Норвегии, Сингапура, Японии и многих других. Также здесь проходят автомобильный фестиваль «Листва», фестивали креативных индустрий и современного искусства. На форуме «Хлебокультура» собираются представители ремесленных пекарен, а на «Ламбада-маркете» — мастера и любители хэнд-мейда.</p><p>Флакон — одно из самых популярных мест для городских мероприятий, выставок, театральных постановок, видео- и фотосъёмок большого масштаба.</p><p>Кафе и шоу-румы Флакона работают с 10:00 до 22:00.</p><p>В ноябре 2019 года стартовала программа лояльности для посетителей.</p>",
    "coordinates": {
        "lng": "37.58440699999958",
        "lat": "55.80563009999988"
    }
   }
   ```

