let name="fahim"
let age = 23;
var isStudent = true;
let personP = {
    firstName:"Fahimul",
    LastName:"Haque",
    age:23,
}
let colors=["red","green","blue"];
//console.log(name,age,isStudent);
//console.log(personP);
//console.log(colors);

let strNum = "10";
let floatNum = "22.5";

let intVal = parseInt(strNum);
let floatVal = parseFloat(floatNum);
let numVal = Number(strNum);
let strVal = String(100);
//console.log(intVal, floatVal, numVal, strVal);

let a = 10, b = 8, x = true, y = false;
//console.log(a + b, a - b, a * b, a / b, a % b);
//console.log(x && y, x || y, !x);
//console.log(a > b, a < b, a == "10", a === "7", a !== b);
/*
function sum1(a, b) {
    return a + b;
}

console.log(sum1(10, 100));

const sum2 = (a, b) => a + b;

console.log(sum2(10, 100));

let num = 2004;
if (num % 2 === 0) {
    console.log("Even Number");
} else {
    console.log("Odd Number+");
}
for (let i = 1; i <= 10; i++) {
    console.log(i+" ");
}
*/
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    greet() {
        console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
    }
}
let person1 = new Person("Fahim", 23);
person1.greet(); 