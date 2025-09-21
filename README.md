# Lintuhavainto
## Sovelluksen toiminnot
- Sovelluksessa käyttäjät voivat jakaa missä ovat havainneet linnun
- Käyttäjä voi lisäksi kirjoittaa lisätietoja
- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään
- Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan lintuhavainnot
- Käyttäjä näkee sovellukseen lisätyt havainnot

### Sovelluksen puuttuvat ominaisuudet:
- Havainnon ajan kirjaaminen
- Havainnon kuvan lisäys
- Käyttäjä voi hakea lintuhavaintoja hakusanalla
- Käyttäjä voi luokitella milloin lintu on havaittu (kuukausi/vuosi)
- Käyttäjäsivu näyttää mitä havaintoja käyttäjä on tehnyt

## Sovelluksen asennus ja käyttö
### Asennus
Vaatii Flaskin asennuksen:
```
$ pip install flask
```
Luo tietokannan taulu:
```
$ sqlite3 database.db < schema.sql
```
Sovelluksen käynnistys:
```
$ flask run
```
### Käyttö
Pääsivulla voi luoda tunnuksen, kirjautua sisään sekä ulos.

Havaintojen luonti tapahtuu tunnuksilla pääsivulla. 

Viimeisimmät havainnot näkee pääsivun lopusta ja tarkastelemaan niitä painamalla linkeistä.

Jos tehdyn havainnon haluaa poistaa tai muokata: Pääsivun havainnoista klikkaa havaintoa, havainto sivulta löytyy painike havainnon muokkaukseen ja poistamiseen.
