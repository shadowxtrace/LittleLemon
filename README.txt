// Little Lemon Back-End API

- This project is a Django REST Framework API for the Little Lemon restaurant.
- It supports menu management and table bookings with full CRUD functionality and user authentication.

API Endpoints
- Menu
GET     /restaurant/menu/
POST    /restaurant/menu/
PUT     /restaurant/menu/<id>
DELETE  /restaurant/menu/<id>

- Table Booking
GET     /restaurant/booking/
POST    /restaurant/booking/
PUT     /restaurant/booking/<id>
DELETE  /restaurant/booking/<id>

- Authentication
POST    /auth/users/
POST    /auth/token/login/

Use token authentication for protected endpoints.
- You can use any testing client, I use ThunderClient, Insomnia, PostMan, Curl(CLI) all work!

