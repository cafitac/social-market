function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    fetch("http://localhost:8000/api/auth/session/login", {
        method: "POST",
        body: JSON.stringify({
            username: username,
            password: password,
        }),
        headers: {
            "Content-type": "application/json;",
        },
    })
        .then((response) => {
            if (response.status === 200) {
                window.location.href = "/";
            }
        });
}