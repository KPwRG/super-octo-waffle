arr = [6, 4, 9]
console.log(arr[0]) //index notation, used for arrays
            //key   //value
var user = {'name': "Trey", 'age': 59}
console.log(user['name']) //key notation, used for objects
console.log(user.name) //dot notation, used for objects



var users = [
            {name: "Michael", age:37}, 
            {name: "John", age:30}, 
            {name: "David", age:27}
            ];

// How would you print/log John's age?
// How would you print/log the name of the first object?
// How would you print/log the name and age of each user using a for loop?  Your output should look something like this
// Michael - 37
// John - 30
// David - 27

console.log(users[1].age) //users[1]['age']
console.log(users[0].name) //users[0]['name']

for(var i = 0; i < users.length; i++){
    console.log(users[i].name + " - " + users[i].age)
    console.log(`${users[i].name} - ${users[i].age}`)
}