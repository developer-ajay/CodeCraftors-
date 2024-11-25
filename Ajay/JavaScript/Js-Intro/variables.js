const myFirstVariable = "Hello, world!";
console.log(myFirstVariable);

//constant variable
//Type of js variables (let,var,const)

var variable = 10 ;
var variable = 20 ;
console.log(variable);
//var can be redeclared in block scope.

const v1 = 10 ;
// redeclaration or reassignment are not possible in const keyword 
//we'll use let when we need redeclaration of variable

let version = 1.0 ;

version = 1.1 ; 
version = 1.2 ;
console.log(version);

//Use let and const for variable declaration rather than var
//because of the reasons like hoisting,reassignment and block scope.

let number1 = '10';
let number2 = 11;
console.log(typeof number1);
console.log(typeof number2);
console.log(number1+number2);
console.log(Number(number1) + number2);

//Types of Variables
const StringValue = "Ajay Joy"
const NumberValue = 25
const BooleanValue = false 
const firstArray = ["Ajay" , "Joy" , 27 , "Alakode" , true, ["Kakkattil" , "House"] ,{ Wife : "Dona Maria K Jesty"}]
console.log(firstArray);
console.log(firstArray[0]);
console.log(firstArray[5]);
console.log(firstArray[6]);

//Object 
const objectVariable = {
    name : "Ajay",
    age : 27 , 
    place : "Alakode" ,
    District : "Kannur"
}

console.log(objectVariable.name);
console.log(objectVariable['District']);


const nestedObject = {
    object1 :{
        object2 :{
            object3: {
                targeted_value : "Nested Value"
            }
        }
    }
}
console.log(nestedObject.object1.object2.object3.targeted_value);


const fun1 = function (num1 , num2){
   return num1 + num2 
}
result = fun1(10,29)
console.log(result);
