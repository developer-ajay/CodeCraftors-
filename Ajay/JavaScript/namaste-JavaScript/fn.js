var x =1 
console.log("x before a and b is ",x);

a();
b();
console.log("x after a and b is ",x);

function a(){
    var x = 10
    console.log("This is a function! ", x);
    
}

function b(){
    var x = 100
    console.log("This is b function! ", x);
    
}