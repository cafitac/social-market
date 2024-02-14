function chargeCredit(chargeAmount, data) {
    csrftoken = getCookie('csrftoken')
    fetch('http://localhost:8000/api/member/users/credit', {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            'Content-Type': "application/json;",
            "X-CSRFToken": csrftoken,
        },
    })
        .then((response) => {
            if (response.status === 200) {
                window.location.href = "/my-page";
            }
        });
}

$("#chargeConfirm").click(function() {
    const chargeAmount = $("#charge-amount").val();
    chargeCredit(chargeAmount, {
        'charge_amount': chargeAmount,
    });
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
