# Semistrukturierte Datenformate

Semistrukturierte Dateiformate sind Datenformate, die eine gewisse Struktur aufweisen, jedoch nicht so streng strukturiert wie zum Beispiel relationale Datenbanken oder tabellarische Datenformate. Im Gegensatz zu rein strukturierten Formaten wie SQL-Datenbanken oder CSV-Dateien erlauben semistrukturierte Formate mehr Flexibilität in Bezug auf die Datenorganisation.

Ein bekanntes Beispiel für ein semistrukturiertes Dateiformat ist JSON (JavaScript Object Notation). In JSON werden Daten in Form von Schlüssel-Wert-Paaren dargestellt, was eine gewisse Struktur bedeutet, aber es erlaubt auch die Verschachtelung von Daten und das Vorhandensein optionaler Felder.

Ein weiteres Beispiel ist XML (eXtensible Markup Language). XML verwendet Tags, die Daten in einer hierarchischen Struktur organisieren. Auch hier gibt es eine festgelegte Struktur, aber im Vergleich zu streng strukturierten Formaten gibt es mehr Spielraum für Anpassungen.

Der Vorteil semistrukturierter Dateiformate liegt darin, dass sie flexibler sind und sich gut für den Austausch von Daten zwischen verschiedenen Systemen eignen, die unterschiedliche Datenstrukturen verwenden können. Dies macht sie besonders nützlich in vielen Anwendungsgebieten, darunter Webentwicklung, Datenübertragung und Konfigurationsdateien.

# Verwendung semistrukturierter Dateiformate als strukturierte Formate

Wenn zum Beispiel JSON oder XML Dateien im Kontext von festen Schemata verwendet betrachtet man sie gerne auch als Streng strukturierte Dateiformate.

In einem streng strukturierten JSON können Daten in einem genau definierten Format vorliegen, und jedes Element hat einen festgelegten Typ.

Beispiel:

```json
{
  "Personen": [
    {
      "Name": "John",
      "Alter": 25,
      "Stadt": "Berlin"
    },
    {
      "Name": "Anna",
      "Alter": 30,
      "Stadt": "München"
    }
  ]
}

```

# Aufgabenstellung:

Gegeben ist eine CSV-Datei mit Informationen zu Büchern. Jede Zeile enthält Titel, Autor, Veröffentlichungsjahr und Genre. Die Aufgabe besteht darin, diese Daten zu analysieren und sie in ein semistrukturiertes JSON-Format umzuwandeln.

CSV-Datei (books.csv):

```csv
Titel, Autor, Veröffentlichungsjahr, Genre
"Die Verwandlung", Franz Kafka, 1915, Roman
"1984", George Orwell, 1949, Dystopie
"To Kill a Mockingbird", Harper Lee, 1960, Roman
"The Catcher in the Rye", J.D. Salinger, 1951, Coming-of-Age
```

1. Lese die CSV-Datei ein und analysiere sie, um zu verstehen, wie die Daten strukturiert sind.

2. Erstelle eine Funktion oder ein Skript, um die Daten in ein JSON-Format zu konvertieren. Jedes Buch sollte ein Objekt im JSON sein, das Titel, Autor, Veröffentlichungsjahr und Genre enthält.
    
3. Berücksichtige dabei, dass das JSON-Format semistrukturiert sein kann. Du könntest beispielsweise optionale Felder für ISBN-Nummern oder Bewertungen hinzufügen.

4. Speichere das resultierende JSON in einer neuen Datei.

Diese Übung ermöglicht es dir, Erfahrung im Umgang mit semistrukturierten und streng strukturierten Datenformaten zu sammeln, sowie in der Verarbeitung von Daten und der Umwandlung zwischen verschiedenen Formaten. Du könntest verschiedene Programmiersprachen wie Python, JavaScript oder eine andere Sprache deiner Wahl verwenden, um diese Aufgabe zu lösen.


