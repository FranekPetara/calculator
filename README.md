# calculator
requirements:

1. docker
2. docker-compose
   
#how to use:

1. In main folder run command:
docker-compose build
2. When build is done run by command:
docker-compose up
3. To use the application, enter into your browser
http://localhost:8080/

Author's comments
aplikacja jest oparta o vue.js i fastApi. Niestety hot reload vue nie dziala w dokerze tak jak powinien mimo różnych konfiguracji. Nie napisałem klasycznej architektury natomiast spróbowałem orginalnego podejścia z dynamicznym ładowaniem endpointów. Dodawanie endpointów działa podobnie jak dodawanie plaginów do aplikacji. Wystarczy dodać dwa pliki od strony backendu i zostaje dodana nowa operacja bez ingerencji w kod aplikacji szczegóły w plikach w folderach operacje i schema. Po wykonaniu tego zadania widzę parę punktów do poprawy ale czas jest skończony...
