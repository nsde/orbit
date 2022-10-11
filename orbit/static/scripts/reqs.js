// Save button
document.querySelectorAll(".toggle-star").forEach((item) => {
    item.addEventListener("click", (event) => {
        element = item.querySelector("i.bi");

        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/example-post/save", true);
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhr.send("lorem=ipsum&dolor=sit");

        if (element.getAttribute("class") == "bi bi-star") {
            element.setAttribute("class", "bi bi-star-fill")
        }
        else {
            element.setAttribute("class", "bi bi-star");
        }
    });
});
