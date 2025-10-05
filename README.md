# Lintuhavainto
## Sovelluksen toiminnot
- Sovelluksessa käyttäjät voivat jakaa missä ja milloin ovat havainneet linnun
- Käyttäjä voi lisäksi kirjoittaa lisätietoja
- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sekä ulos
- Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan lintuhavainnot
- Käyttäjä näkee sovellukseen lisätyt havainnot
- Käyttäjä voi hakea lintuhavaintoja hakusanalla
- Käyttäjä voi luokitella linnut luokkiin (sorsalinnut, päiväpetolinnut, jne)
- Käyttäjäsivu näyttää mitä havaintoja käyttäjä on tehnyt

### Sovelluksen puuttuvat ominaisuudet:
- Havainnon kuvan lisäys

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

Kaikki omat havainnot näkee kohdasta ```Omat havainnot```. Muiden havaintoja voi käydä katsomassa niiden käyttäjien sivuilla.

Viimeisimmät havainnot näkee pääsivun lopusta ja tarkastelemaan niitä painamalla linkeistä.

Jos tehdyn havainnon haluaa poistaa tai muokata: Pääsivun ```Viimeisimmät havainnot``` klikkaa havaintoa tai käy omalla käyttäjäsivulla etsimässä havainnon ```Omat havainnot``` kohdasta, havaintosivulta löytyy painike havainnon muokkaukseen ja poistamiseen.

Havaintoja voidaan hakea ```Etsi havainto``` kohdasta. Hakusanaksi käy ***lintulaji, lähiö tai kaupunki***.

Havaintoihin voi laittaa komentteja. Komentteja ei voi vielä muokata tai poistaa.
