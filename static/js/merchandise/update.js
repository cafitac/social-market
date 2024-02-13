function updateMerchandise(merchandiseId, data) {
    csrftoken = getCookie('csrftoken')
    fetch(`http://localhost:8000/api/merchandise/merchandises/${merchandiseId}`, {
        method: "PATCH",
        body: JSON.stringify(data),
        headers: {
            'Content-Type': "application/json;",
            "X-CSRFToken": csrftoken,
        },
    })
        .then((response) => {
            if (response.status === 200) {
                window.location.href = "/my-merchandises";
            }
        });
}

function updateMerchandiseStock(merchandiseId, stock) {
    csrftoken = getCookie('csrftoken')
    fetch(`http://localhost:8000/api/merchandise/merchandises/${merchandiseId}/stock`, {
        method: "PATCH",
        body: JSON.stringify({
            count: stock,
        }),
        headers: {
            'Content-Type': "application/json;",
            "X-CSRFToken": csrftoken,
        },
    })
        .then((response) => {
            if (response.status === 200) {
                window.location.href = "/my-merchandises";
            }
        });
}

$(".updateButton").on('click', function () {
    const merchantId = $(this).data("id")
    const name = $(this).data("name");
    const description = $(this).data("description");
    const price = $(this).data("price");
    const stock = $(this).data("stock");

    $("#update-merchandise-id").val(merchantId)

    $("#previousName").val(name);
    $("#updateName").val(name);

    $("#previousDescription").val(description);
    $("#updateDescription").val(description);

    $("#previousPrice").val(price);
    $("#updatePrice").val(price);

    $("#previousStock").val(stock);
    $("#updateStock").val(stock);
});

$("#updateConfirm").on("click", function () {
    const merchandiseId = $("#update-merchandise-id").val()

    let data = {}
    if ($("#previousName").val() !== $("#updateName").val()) {
        data['name'] = $("#updateName").val();
    }
    if ($("#previousDescription").val() !== $("#updateDescription").val()) {
        data['description'] = $("#updateDescription").val();
    }
    if ($("#previousPrice").val() !== $("#updatePrice").val()) {
        data['price'] = $("#updatePrice").val();
    }

    if (!$.isEmptyObject(data)) {
        updateMerchandise(merchandiseId, data)
    }

    if ($("#previousStock").val() !== $("#updateStock").val()) {
        updateMerchandiseStock(merchandiseId, $("#updateStock").val());
    }
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
