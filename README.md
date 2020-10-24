# Repozytorium do zajęć z Flaska z grupą PytKrk4

## Instrukcja obsługi

1. Sklonuj repozytorium
2. Zainstaluj wymagane pakiety używając pliku requirements.txt

```bash
pip install -r requirements.txt
```

3. Postępuj zgodnie z instrukcjami prowadzącego.

## Sugerowane zadania

1. Dla każdego przykładu, przetestować działanie aplikacji napisanej we Flasku przy pomocy modułu requests
2. Napisać prostą aplikację działającą jak webowy kalkulator. Przyjmij następujące założenia:
   - Aplikacja będzie operowała tylko na integerach.
   - Wszystkie zasoby wykorzystują jedynie metodę GET.
   - Dostępne będą cztery podstawowe działania: dodawanie, odejmowanie, mnożenie, dzielenie.
     Każdej operacji powinien odpowiadać osobny zasób.
   - Parametry (czyli argumenty danej operacji matematycznej będą przekazywane w ścieżce.
   - Zasób odpowiadający za wykonanie dzielenia będzie przyjmował dodatkowy parametr (w query stringu), decydujący o tym, czy dzielenie ma zostać wykonane
     dokładnie (`truediv=true`) czy też calkowitoliczbowo (`truediv=false`). Domyślną wartością parametru powinno być `true`.
   - Ręcznie zwróć odpowiedź o statusie 400 (Bad request) w przypadku, gdy zażądano dzielenia przez zero.
     
3. Zmodyfikuj aplikację z powyższego zadania tak, aby otrzymywała argumenty zapisane w JSON-ie, oraz zwracała wynik zakodowany w JSONie.
     - Format wejściowy: `{"arg1": liczba, "arg2": liczba}`, na przykład `{"arg1": 50, "arg2": 30}`, typ operacji jest determinowany przez ścieżkę.
     - Format wyjściowy: `{"arg1": liczba, "arg2": liczba, "operator": operator, "result": rezultat}`. Na przykład: `{"arg1": 20, "arg2": 3, "operator": "-", "result": 17}`.
    
    Tym razem wszystkie zasoby powinny używać metody POST.
    
4. Napisz konsolowego klienta aplikacji z powyższego zadania. Aplikacja powinna otrzymać od użytkownika argumenty działania oraz samo działanie. Następnie,
   powinna wykonać żądanie do napisanej przez Ciebie aplikacji webowej, oraz wyświetlić wynik.
   
5. W przykładzie 17 tworzyliśmy endpointy pozwalające na wykonywanie operacji CRUD na kilku kolekcjach obiektów
   (Genre + dowolny obiekt wybrany przez kursantów w ramach ćwiczenia). Proszę przerobić aplikację z
   przykładu 17 tak, aby endpointy operaujące na różnych modelach zostały zrealizowane przy pomocy blueprintów.
   Na przykład, jeśli mamy endpointy operaujące na Genre i MediaType, należy utworzyć dwa Blueprinty, jeden
   z operacjami dla Genre, drugi z operacjami dla MediaType.
   
6. Aplikacja z przykładu 19 posiada poważną niedoróbkę wydajnościową. Aby zrozumieć na czym polega problem wykonaj
   następujące czynnośći:
   - Ustaw opcję konfiguracyjną `SQLALCHEMY_ECHO` na wartość `True` podczas tworzenia obiektu aplikacji.
   - Odwiedź w przeglądarce endpoint `/albums` (możesz też wysłać żądanie używając modułu `requests`)
   - Zwróć uwagę na logi aplikacji. Czy widzisz na czym polega problem?
   
   Jeżeli udało Ci się zidentyfikować problem, spróbuj wyjaśnić dlaczego powstał, oraz zaproponuj poprawkę.
 
8. Przerobić rozwiązanie z zadania 5 w taki sposób, aby korzystało ono z fabryki do tworzenia obiektku aplikacji.
   
9. Dodać do rozwiązania z zadania 5 testy sprawdzające działanie wybranych endpointów. Pamiętać o używaniu
   albo testowej bazy na dysku, albo bazy w pamięci. Przetestować zarówno endpoint pobierający dane, jak i
   wysyłająćy i usuwający obiekty.
  
10. Przerobić rozwiązanie z zadanie 5. w taki sposób, aby przychodzące dane były walidowane przy pomocy modeli
    Pydantic.
    
11. Przy pomocy Flaska (lub FastAPI) napisać prostą aplikację do obsługi sklepu.
    - Zaprojektować modele bazy danych
    - Zaprojektować API udostępniane przez aplikację. Nie narzucam struktury, ale chciałbym, zeby:
      - Można było dodawać i usuwać produkty. Produkt powinien mieć nazwę, producenta, cenę oraz
        ilość w magazynie.
      - Można było wyszukiwać produkty (np. cena większa/mniejsza niż..., nazwa zawierające....)
      
      Podziel API na dwa Blueprinty:
      - Jeden do obsługi operacji CRUD na produktach
      - Drugi do wyszukiwania
      
    Wymagania opcjonalne (ale wskazane):
    - Testy, najlepiej do każdego endpointa
    - Walidacja przychodzących danych przy pomocy Pydantica
    - Konsolowy klient naszej aplikacji

   
