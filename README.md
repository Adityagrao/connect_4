# Connect 4 API

![Swagger](/media/swagger.PNG)



What Is This?
-------------

This is a simple FastAPI application intended to provide a working example of Connect 4 API. Based on the following Requirements below.

How To Use This
---------------

1. Run `pip install -r requirements.txt` to install dependencies
6. Run `python main.py`
. Navigate to http://localhost:8000 in your browser


Requirements
------------

1. ### Problem Statement 

 - Build a pseudo Backend API that plays Connect 4 with 2 users. You have a matrix of  7 columns with 6 rows. 2 coins of red and yellow color can be dropped in any column. The coin is dropped from above and it gets stacked in the bottommost available row. 
  
 - You have to build an API that validates and checks if a Valid move is made & must show who wins whenever red or yellow connects 4 coins in a row or column or diagonally of the same color. Yellow always go 1st or every valid odd move. Red always goes second or every valid even move.

 

2. ### Minimum Requirement

- Write a backend in the tech stack mentioned below which exposes an API that returns the necessary response.

- When a Request  “START” is sent to the API, it must send a response of “READY” after resetting the game of Connect 4 and starting a fresh game.

-  Whenever a column is sent as a request, Eg. 0, 1, 2, … 6. A coin must be dropped in that column.  the response must be either “Valid” or “Invalid”. Every “Valid” move must be considered as a move. Every “Invalid” move should wait for the next request which is valid.

- Zip all your source code, deployment instructions, screenshots, and upload them.

 

3. ### Advanced

    Along with all the above tasks,

-  Assign a random unique token/username every time “START” is sent to the API. & return this token/username. Parallel games must be possible with the use of this. Every subsequent request needs to be made along with this token/username. 

- Use a Database to store all the moves associated with a token/username. A “GET” request to this API along with said token must fetch all the moves made up to that point.

- The API must return “Yellow wins” or “Red wins” whenever an odd or even “Valid” move connects 4 coins of the same color in a row or column or a diagonal.

 



