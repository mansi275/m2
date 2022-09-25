let numberdiv = document.getElementById("number");

let number = 0;

let plus = document.getElementById("increment-btn");
let minus = document.getElementById("decrement-btn");

plus.addEventListener("click", () => {
    ++number;
    numberdiv.innerHTML = number;
})

minus.addEventListener("click", () => {
    if (number > 0){
        --number;
        numberdiv.innerHTML = number;
    }
    else {
        numberdiv.innerHTML = 0;
    }
})