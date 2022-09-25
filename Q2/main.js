// Setup
let stringCont = document.getElementById("strVar");
let intCont = document.getElementById("intVar");
let sumFuncAns = document.getElementById("sum-func-answer");
let if_elseAns = document.getElementById("if-else-header-answer");

// Variables
let stringVar = "Mansi";
stringCont.innerHTML = stringVar;
let integerVar = 62;
intCont.innerHTML = integerVar;

// Sum function
let sumFunc = (num1, num2) => {
  return num1 + num2;
};

// Setting the output of the function to html content
sumFuncAns.innerHTML = sumFunc(6, 2);

// Decision making
let age = 62;
if (age >= 21) {
  if_elseAns.innerHTML = "Yes!";
} else {
  if_elseAns.innerHTML = "No!";
}

// Loop to print multiples of 3
for (let k = 1; k < 10; k++) {
  document.write(k * 7 + "<br>");
}