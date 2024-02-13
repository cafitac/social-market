function deleteMerchandise(merchandiseId) {
    fetch(`http://localhost:8000/api/merchandise/merchandises/${merchandiseId}`, {
        method: "DELETE",
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
    deleteMerchandise($("#delete-merchandise-id").value)
});
