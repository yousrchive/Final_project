let loginEl = document.getElementById("login")

function loginChk() {

    let idEl = loginEl.username.value;
    let pwdEl = loginEl.password.value;

    if (!idEl) {
        alert('아이디를 입력해주세요.');
        return;
    }
    if (!pwdEl) {
        alert('비밀번호를 입력해주세요.');
        return;
    }
    document.getElementById('login').submit();
    // alert(`id : ${idEl}\npwd : ${pwdEl}`);
}
