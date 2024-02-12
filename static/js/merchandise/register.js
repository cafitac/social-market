function register() {
    const name = document.getElementById("name").value;
    const description = document.getElementById("description").value;
    const price = document.getElementById("price").value;

    if (name === "" || price === "") {
        alert("상품 이름 또는 상품 가격이 입력되지 않았습니다");
    }

    csrftoken = getCookie('csrftoken')
    fetch("http://localhost:8000/api/merchandise/merchandises", {
        method: "POST",
        body: JSON.stringify({
            name: name,
            description: description,
            price: price,
        }),
        headers: {
            "Content-type": "application/json;",
            "X-CSRFToken": csrftoken,
        },
    })
        .then((response) => {
            if (response.status === 201) {
                window.location.href = "/my-merchandises";
            }
        });
}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}