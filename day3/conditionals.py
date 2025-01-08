cars=["audi","bmw","subaru","toyota"]


for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())
        
        
        
newcar="Audi"
#if case matters this behaviour is advantageous and if case doesn't matter 
#newcar=="audi"

#if case doesn't matter and yoou just wanto test the value of a variable
print(newcar.lower()=="audi")
print(newcar)
print( newcar=="audi")

requested_topping='mushrooms' 

if requested_topping != 'anchovies':
    print("Hold the anchovies!")
    
answer=17

if answer !=42:
    print("TThat is not the correct answer .Please try again")
    
requested_toppings =['mushrooms','onions','pineapple']
print('mushrooms' in requested_toppings)
print('pepper' in requested_toppings)


banned_users=["andrew","carolina","david"]
user='marie'

if user not in banned_users:
    print(f"{user.title()},you can post a response if you wish.")
    