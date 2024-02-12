$("#merchandise-search-button").on("click", () => {
    q = document.getElementById("merchandise-search-input").value
    window.location.href = `?q=${q}`;
})

$("#merchandise-search-input").on("keypress", (event) => {
    if (event.key === "Enter") {
        q = document.getElementById("merchandise-search-input").value
        window.location.href = `?q=${q}`;
    }
})