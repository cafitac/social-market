$(".add-cart").on('click', function () {
    const merchandiseId = $(this).data("merchandise-id");
    const merchandiseName = $(this).data("merchandise-name");

    $("#add-cart-merchandise-id").text(merchandiseId);
    $("#merchandise-name").text(merchandiseName);
});

$("#incrementQuantity").click(function () {
    var quantity = parseInt($("#quantity").val());
    $("#quantity").val(quantity + 1);
});

$("#decrementQuantity").click(function () {
    var quantity = parseInt($("#quantity").val());
    if (quantity > 1) {
        $("#quantity").val(quantity - 1);
    }
});

function addCart(data) {
    csrftoken = getCookie('csrftoken')
    fetch('http://localhost:8000/api/cart/carts', {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            'Content-Type': "application/json;",
            "X-CSRFToken": csrftoken,
        },
    })
        .then((response) => {
            if (response.status === 201) {
                window.location.href = "/cart";
            }
        });
}

$("#addCartConfirm").on("click", function () {
    const merchandiseId = $("#add-cart-merchandise-id").text()
    const quantity = $("#quantity").val()

    console.log(merchandiseId);
    console.log(quantity);

    addCart({
        "merchandise_id": merchandiseId,
        "amount": quantity,
    })
});

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
