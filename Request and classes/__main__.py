from speeduser import SpeedUser
import math

# CONST
users_api_url = "https://jsonplaceholder.typicode.com/users"

print("### Question 3 ###\n")


users = SpeedUser.generate(users_api_url)
for user in users:
    print(user)


print("\n### Question 4 ###\n")


retrived_lat = 0
retrived_lng = 0
while True:
    try:
        text = input("Please enter latitude and lngtitude with comma for seperation: ") 
        text = text.strip().split(",")
        retrived_lat = float(text[0])
        retrived_lng = float(text[1])
        break
    except:
        print("You enter wrong values. Please try again")
    
nearest_user = users[0]
distance = lambda lat1, lng1, lat2, lng2: math.sqrt(abs(lat2-lat1)**2 + abs(lng2-lng1)**2) # calculate the 

for i in range(1, len(users)):
    user = users[i]
    u_let = float(user.address["geo"]["lat"])
    u_lng = float(user.address["geo"]["lng"])
    n_let = float(nearest_user.address["geo"]["lat"])
    n_lng = float(nearest_user.address["geo"]["lng"])
    new_u_d = distance(u_let, u_lng, retrived_lat, retrived_lng)
    current_n_d = distance(n_let, n_lng, retrived_lat, retrived_lng)
#    print(f"User: let = {u_let}, lng = {u_lng} | Nearest: let = {n_let}, lng = {n_lng} | d1 = {new_u_d} | d2 = {current_n_d}")
    if (new_u_d < current_n_d):
        nearest_user = user

print(f"Nearest user is: {nearest_user}")