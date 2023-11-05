

console.log("I like pizza!");
console.log("it's really good");

// window.alert("Alert");

let age;
let firstName = "Bro";
let student = true

age = 21;

console.log(age);


age = age + 1;
console.log(age);
console.log(firstName);
console.log(student);
console.log("You are", age, "years old!");
console.log("Enrolled:", student);

document.getElementById("p1").innerHTML = "Hello " + firstName;
document.getElementById("p2").innerHTML = "Your are " + age + " years old";
document.getElementById("p3").innerHTML = "Enrolled " + student;

console.log(age/3)

let result = 1 + 2 * 3 * (3+4);
console.log(result)

// let username = window.prompt("What's your name?")
// console.log(username)

let username;
document.getElementById("submit_button").onclick = function(){
    username = document.getElementById("name_text").value;
    console.log(username);
    document.getElementById("name_header").innerHTML = username
} 

//
age = "21"
console.log(typeof age)
age = Number(age)
console.log(typeof age)
console.log(String(3.14), typeof(String(3.14)))

//let x = 3.14
// x = Math.round(x);
// x = Math.floor(x);
// x = Math.pow(x,2);
// x = Math.sqrt(x);
// x = Math.abs(x);
// maximum = Math.max(x,y,z);
// x = Math.PI;

//const -> variable cant change



// let a;
// let b;
// let c;

document.getElementById("calculate").onclick = function(){
    a = document.getElementById("a").value;
    b = document.getElementById("b").value;
    a = Number(a);
    b = Number(b);
    c = Math.sqrt(Math.pow(a,2) + Math.pow(b,2))
    document.getElementById("result").innerHTML = "Result: " + String(c)
}

let count=0
document.getElementById("counter").innerHTML = count
document.getElementById("increase").onclick = function(){
    count+=1
    document.getElementById('counter').innerHTML = count
}
document.getElementById("decrease").onclick = function(){
    count-=1
    document.getElementById('counter').innerHTML = count
}

// Random Number

let x 
let y 
let z 

document.getElementById("roll").onclick = function(){
    x = Math.floor(Math.random() * 6) + 1; 
    y = Math.floor(Math.random() * 6) + 1;
    z = Math.floor(Math.random() * 6) + 1;
    document.getElementById("dice1").innerHTML = x
    document.getElementById("dice2").innerHTML = y
    document.getElementById("dice3").innerHTML = z
    
}

//string properties
let userName = "Bro Code"
console.log(userName.length);
console.log(userName.charAt(2));
console.log(userName.indexOf("o"));
console.log(userName.lastIndexOf("o"));

let space_user_name = " Jay      "
console.log(space_user_name)
console.log(space_user_name.trim())
console.log(userName.toUpperCase())
console.log(userName.toLowerCase())

let phonenumber = "123-456-678"

phonenumber = phonenumber.replaceAll("-","")
console.log(phonenumber)

let first_name
let last_name
//slice method
last_name = userName.slice(4);
console.log(last_name)
first_name = userName.slice(0,3)
console.log(first_name)

last_name = userName.slice(userName.indexOf(" ")+1)
first_name = userName.slice(0, userName.indexOf(" "))
console.log(last_name)
console.log(first_name)

//method chaining
let letter = userName.charAt(0).toUpperCase().trim()
console.log(letter)

//if statement
age = 0
if(age >= 18){
    console.log("You are an adult")
}
else if(age <=0 ){
    console.log("You haven't been born yet")
}
else{
    console.log("You are a child")
}

//Check Box
// document.getElementById("Subscript").onclick = function(){
//     if(document.getElementById("subscript_checkbox").checked){
//         document.getElementById("subscript_result").innerHTML = "Subscripted"
//     }
//     else {
//         document.getElementById("subscript_result").innerHTML = "Not Subscripted"
//     }
// }

const visa = document.getElementById("visa")
const master = document.getElementById("master")
const paypal = document.getElementById("paypal")

document.getElementById("Subscript").onclick = function(){
    if(document.getElementById("subscript_checkbox").checked){
        document.getElementById("subscript_result").innerHTML = "Subscripted"
    }
    else {
        document.getElementById("subscript_result").innerHTML = "Not Subscripted"
    }

    if (visa.checked){
        console.log("You are paying with VISA")
        document.getElementById("payment_result").innerHTML ="You are paying with VISA" 
    }else if (master.checked){
        console.log("You are paying wiht Master")
        document.getElementById("payment_result").innerHTML ="You are paying with Master" 
    }else if (paypal.checked){
        console.log("You are paying wiht PayPal")
        document.getElementById("payment_result").innerHTML ="You are paying with VISA" 
    }else {
        console.log("You must select payment method!")
        document.getElementById("payment_result").innerHTML ="You must select payment method!" 
    }
}
