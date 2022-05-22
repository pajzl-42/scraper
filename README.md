Engeto Python Academy Project #3

Author: Jan Tásler

E-mail: jan.tasler@gmail.com

Election scraper - zisk volebních dat - popis spuštění skriptu:
1. Pro spuštění je nutné mít nainstalovaný python s balíčky dle dokumentu Requirements.txt
2. Spouštějte příkazem: python main.py "url" "název" (včetně uvozovek), kde:
   1. url je webová adresa územního celku (okresu) - např: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100
   2. název je pojmenování souboru do kterého budete chtít data uložit
3. Pokud zadáte nesprávné argumenty, program se nespustí - budete upozorněni

Pro instalaci Pythonu se obraťte na následující web: https://www.python.org/downloads/

Instalace potřebného balíčku probíhá pomocí pip instalátoru:
1. Spusťte příkazový řádek vašeho operačního systému
2. Zadejte pip install "název balíčku" (bez uvozovek) a potvrďte (Enter)
3. V případě potřeby postupujte dle instrukcí v příkazovém řádku/terminálu



Ukázka funkčnosti programu:
Územní celek Trutnov 
1. Spuštění: python main.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5205" "Trutnov_example"
2. Výsledky jsou zapsány v souboru Trutnov.csv v tomto adresáři

