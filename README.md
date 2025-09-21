# Lintuhavainto
## Sovelluksen toiminnot
- Sovelluksessa käyttäjät voivat jakaa missä ja milloin ovat havainneet linnun
- Käyttäjä voi lisäksi kirjoittaa lisätietoja
- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sekä ulos
- Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan lintuhavainnot
- Käyttäjä näkee sovellukseen lisätyt havainnot
- Käyttäjä voi hakea lintuhavaintoja hakusanalla

### Sovelluksen puuttuvat ominaisuudet:
- **Käyttäjä voi etsiä havaintoja ajan perusteella**
- Havainnon kuvan lisäys
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

Havaintojen luonti tapahtuu tunnuksilla pääsivulla ```Luo tunnus``` kohdasta.

Viimeisimmät havainnot näkee pääsivun lopusta ja tarkastelemaan niitä painamalla linkeistä.

Jos tehdyn havainnon haluaa poistaa tai muokata: Pääsivun ```Viimeisimmät havainnot``` klikkaa havaintoa, havaintosivulta löytyy painike havainnon muokkaukseen ja poistamiseen.

Havaintoja voidaan hakea ```Etsi havainto``` kohdasta. Hakusanaksi käy ***lintulaji, lähiö tai kaupunki***.
