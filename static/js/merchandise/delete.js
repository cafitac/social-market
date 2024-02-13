function deleteMerchandise(merchandiseId) {
    csrftoken = getCookie('csrftoken')
    fetch(`http://localhost:8000/api/merchandise/merchandises/${merchandiseId}`, {
        method: "DELETE",
        headers: {
            "X-CSRFToken": csrftoken,
        },
    })
        .then((response) => {
            if (response.status === 204) {
                window.location.href = "/my-merchandises";
            }
        });
}

$(".deleteButton").on('click', function () {
    const merchandiseId = $(this).data("id");
    $("#delete-merchandise-id").val(merchandiseId);
});

$("#deleteConfirm").on("click", function () {
    deleteMerchandise($("#delete-merchandise-id").val())
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
