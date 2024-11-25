let HtmlBody = document.querySelector('body');

let randomFunction = function () {
    let randomColor = Math.floor(Math.random() * 16777215).toString(16);
    HtmlBody.style.backgroundColor = "#" + randomColor;
}