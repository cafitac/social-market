$(".updateCartButton").on("click", function () {
    const merchandiseName = $(this).data("merchandise-name");
    $("#merchandise-name").text(merchandiseName);

    const quantity = $(this).data("quantity");
    $("#quantity").val(quantity);

    const cartId = $(this).data("id");
    $("#update-cart-id").text(cartId);
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

$("#updateCartConfirm").on("click", function () {
    const cartId = $("#update-cart-id").text()

    updateCart(cartId, {
        "amount": $("#quantity").val(),
    });
});

function updateCart(cartId, data) {
    csrftoken = getCookie('csrftoken')
    fetch(`http://localhost:8000/api/cart/carts/${cartId}`, {
        method: "PATCH",
        body: JSON.stringify(data),
        headers: {
            'Content-Type': "application/json;",
            "X-CSRFToken": csrftoken,
        },
    })
        .then((response) => {
            if (response.status === 200) {
                window.location.href = "/cart";
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
