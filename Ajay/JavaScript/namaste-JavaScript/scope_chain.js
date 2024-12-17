function a(){
   var b = 10;
   c();
   function c(){
    console.log(b);  
   } 
      
}
a();

//lexical enviornment is created when a function is called
//it is local memory and refrence to outer memory
