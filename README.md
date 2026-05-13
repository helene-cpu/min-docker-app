# Escape room nettside
### Dette er en enkel nettside hvor brukere kan prøve å løse spennende online escape room oppgaver. I denne oppgaven har jeg satt meg inn i Docker, SQLite og APIer. 

## Prosjektbeskrivelse
### Teknologier brukt:
##### - Python (Flask)
##### - HTML og CSS
##### - SQLite for database
##### - Docker
##### - Flask-WTF


### Funksjoner
##### Bruker kan løse escape room oppgaver
##### Lagring av data i SQL databaser
##### Skjemaer med Flask-WTF
##### Enkel backend med python (Flask)
##### API 
##### Docker for å kjøre prosjektet

### Kjøre programmet lokalt:
#### 1. Installasjoner:
##### Flask
```
pip install flask-sqlalchemy
```
##### Flask-WTF

```
pip install Flask-WTF
```

#### 2. Opprette en database
##### Database + 2 tabeller

#### 3. Lag en requirements.txt
##### inkludere disse punktene:
##### Flask
##### Flask-SQLAlchemy
##### Flask-WTF
##### requests

#### 4. Start applikasjon
##### naviger til prosjektet
##### bygg et image
````
docker build -t my-custom-app .
````
##### Kjør programmet
```
docker run -p 3000:3000 my-custom-app
```

### Kompetansemål:
#### Utvikling: 
##### modellere og opprette databaser for informasjonsflyt i systemer-.
##### beskrive og anvende relevante versjonskontrollsystemer i utviklingsprosjekter.
##### analysere digitale trusler, verdier og sårbarheter og utvikle applikasjoner med innebygget sikkerhet
##### gjøre rede for hensikten med teknisk dokumentasjon og utarbeide teknisk dokumentasjon for IT-løsninger

#### Drift:
##### planlegge og dokumentere arbeidsprosesser og IT-løsninger
##### utforske trusler mot datasikkerhet og gjøre rede for dagens trusselbilde og hvordan truslene kan påvirke en åpen samfunnsdebatt og tilliten til demokratiet
##### planlegge, drifte og implementere IT-løsninger som ivaretar informasjonssikkerhet og gjeldende regelverk for personvern

#### Brukerstøtte: 
##### utøve brukerstøtte og veilede i relevant programvare
##### kartlegge behovet for og utvikle veiledninger for brukere og kunder