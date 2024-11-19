//this is javascript
console.log("Hello World!");

let userName = "Ajay Joy";
console.log(userName);

//cannot be reserved keyword
//variables shouled be meaningful 
//cannot start with number
//cannot contain spaces
//cannot start with hyphen (-)

const interestRate = 0.3;
//cannot resign a constant
console.log(interestRate);

//Data Types 
//Primitive and Reference
//Primitive are String , Number , Boolean , Null , Undefined , Symbol

let place ="Alakode" // Srtring
let age = 30 // Number
let isApproved = true // Boolean
let firstName = null // Null
let lastName = undefined // Undefined
let selectedColor = Symbol("red") // Symbol
console.log(selectedColor.description)

//Reference Types
//objects
//Arrays
//functions 

//Objects
let person = {
    pName : "Ajay",
    age : 27,
    isStudent: true,
    greet: function () {
        console.log("Hello!");
    }
}

console.log(person);

//Dot notation
console.log(person.pName);

//Bracket notation
person["pName"] = "Mary"
console.log(person["pName"]);

//arrays
let selectedColors = ['red' , 'blue' , 'green' , 'white'];
selectedColors[4] = "black"
console.log(selectedColors);
console.log(typeof(selectedColors));

//functions

/*************  ✨ Codeium Command ⭐  *************/

function greet(userName) {
    console.log("Hello , How are u ....?, " + userName);
    
}

greet(userName);
greet("John");
greet()


function square(num){
    return num * num
}

console.log(square(2));
