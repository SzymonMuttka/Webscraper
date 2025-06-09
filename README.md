# Webscraper

# 🌐 Opis

Aplikacja rozproszona do pobierania danych z witryn internetowych, z graficznym interfejsem użytkownika opartym na Flask.

---

## 📌 Funkcjonalność

- Pobieranie i selekcjonowanie danych ze stron WWW
- Obsługa 4 grup danych:
  - Tytułu strony (`<title>`)
  - Nagłówków H1–H3
  - Odnośników (`<a href>`)
  - Adresów e-mail
- Wieloprocesowe przetwarzanie z wykorzystaniem `multiprocessing` i `asyncio`
- Parsowanie stron z użyciem BeautifulSoup
- Przechowywanie wyników w bazie danych MongoDB
- Interfejs graficzny we Flask z automatycznym odświeżaniem danych
- Całość uruchamiana w kontenerach Docker (GUI, silnik, baza danych)

---

## 🚀 Instrukcja uruchomienia

### 1. Wymagania
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### 2. Uruchomienie aplikacji
docker compose up --build

(GUI będzie dostępne pod adresem: http://localhost:5000)
(MongoDB działa domyślnie na porcie 27017)

---

🧠 Autor: Szymon Muttka 21278
