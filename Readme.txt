API endpoints:
##############################################
#######    No authentication required:  #######
##############################################
Register new user:
http://127.0.0.1:8000/api/auth/users/

Get token:
POST 
http://127.0.0.1:8000/api/auth/token/login
parameters: username, password

##############################################
#######    Authentication required:   #######
##############################################

Users:
http://127.0.0.1:8000/api/users
http://127.0.0.1:8000/api/users/{userId}

Bookings:
http://127.0.0.1:8000/api/bookings
http://127.0.0.1:8000/api/bookings/{bookingId}

Menu-items:
http://127.0.0.1:8000/api/menu-items
http://127.0.0.1:8000/api/menu-items/{menuitemId}


