## Cel Projektu

Prosty, konsolowy skrypt w języku Python, stworzony jako mój pierwszy, praktyczny projekt w ramach nauki automatyzacji i interakcji z zewnętrznymi API. 

Głównym celem było stworzenie narzędzia, które rozwiązuje realny, codzienny problem: potrzebę szybkiego i efektywnego sprawdzania cen gier w sklepie Steam bez konieczności manualnego otwierania przeglądarki. Projekt ten jest dowodem mojego dążenia do automatyzacji i optymalizacji powtarzalnych zadań.

## Architektura i Zastosowane Technologie (System Architecture & Tech Stack)

*   **Język:** Python 3
*   **Kluczowe Biblioteki:**
    *   `requests`: Do wykonywania zapytań HTTP i komunikacji z API Steam.
*   **Źródło Danych:** Niedokumentowane publicznie, ale dostępne API wyszukiwarki sklepu Steam. Kluczową częścią projektu było odkrycie i dekonstrukcja tego API w celu pozyskania ustrukturyzowanych danych w formacie JSON.

## Wyzwania i Zdobyta Wiedza (Challenges & Lessons Learned)

Ten z pozoru prosty projekt był dla mnie niezwykle cennym poligonem doświadczalnym, który nauczył mnie:
1.  **Analizy Sieci:** Jak, używając narzędzi deweloperskich w przeglądarce, monitorować ruch sieciowy i identyfikować zapytania API, które są wysyłane "pod maską" przez strony internetowe.
2.  **Pracy z API i formatem JSON:** Jak programistycznie wysyłać zapytania do zewnętrznego serwisu, odbierać odpowiedzi i parsować dane w formacie JSON, by wydobyć z nich konkretne, potrzebne informacje.
3.  **Czystości i Prostoty Kodu:** Jak napisać krótki, czytelny i w pełni funkcjonalny skrypt, który wykonuje jedno, dobrze zdefiniowane zadanie.

> **Uwaga:** To jest projekt "work-in-progress". Przyszłe plany rozwoju obejmują m.in. dodanie obsługi różnych walut, zapisywanie historii cen i implementację powiadomień.
