# Room Service

## Overview
The Room Service is a component of the hotel management system, designed to handle operations related to managing hotel rooms. This includes checking room availability, updating room status, and managing room pricing. The service is built using Flask and uses MongoDB as the backend database.

## Endpoints:

1. `GET /room/<room_id>`: 
    - **Description:** Retrieve detailed information about a room by its ID.
    - **Response:** JSON containing room details.

2. `PUT /room/<room_id>/status`: 
    - **Description:** Change the status of a room (e.g., available, occupied).
    - **Request Body:** {"status": "new_status"}
    - **Response:** Confirmation message.

3. `PUT /room/<room_id>/pricing`: 
    - **Description:** Modify the pricing of a room.
    - **Request Body:** {"price": new_price}
    - **Response:** Confirmation message.