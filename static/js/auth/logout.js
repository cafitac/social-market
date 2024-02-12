function logout() {
    fetch("http://localhost:8000/api/auth/session/logout", {
method: "POST",
    })
        .then((response) => response.json());
}
