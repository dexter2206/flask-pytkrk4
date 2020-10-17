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
   
5. Napisać we flasku prostą aplikację webową służącą jako baza ksiązek. Dokładne instrukcje zostaną przekazane na zajęciach.
