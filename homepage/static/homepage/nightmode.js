const nightToggle = document.querySelector("#nightToggle");
const body = document.querySelector("body");
const container = document.querySelectorAll(".container, .sidebar");
let isNightmode = false;

nightToggle.addEventListener("click", function () {
    // if nightmode is not toggled
    if (isNightmode === false) {
        body.style.backgroundColor = "#222";
        body.style.color = "white";
        container.forEach(function (c) {
            c.style.backgroundColor = "#bbb";
        })
        isNightmode = true;
    // if nightmode is toggled
    } else {
        body.style.backgroundColor = "white";
        body.style.color = "black";
        container.forEach(function (c) {
            c.style.backgroundColor = "white";
        })
        isNightmode = false;
    }
})