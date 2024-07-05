# Room Service
 
**Flask App:** Defines a simple web server with routes to manage room operations.

**MongoDB Connection:** Connects to a MongoDB database running on localhost.

**Endpoints:**

`GET /room/<room_id>`: Fetches details of a specific room.

`PUT /room/<room_id>/status`: Updates the status of a specific room (e.g., available, occupied).

`PUT /room/<room_id>/pricing`: Updates the pricing of a specific room.