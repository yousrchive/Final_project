let loginEl = document.getElementById("login")

loginEl.onsubmit = () => {
    let idEl = loginEl.username.value;
    let pwdEl = loginEl.password.value;

    // alert(`id : ${idEl}\npwd : ${pwdEl}`);
};