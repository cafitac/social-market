function login(username, password) {
    const body = JSON.stringify({
        username: "username",
        password: "password",
    });
    $.ajax({
        url: "http://localhost:8000/api/auth/login",
        type: "POST",
        success: function (result) {
            console.log(result);
        },
    });
}