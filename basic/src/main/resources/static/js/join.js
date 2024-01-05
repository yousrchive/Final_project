let joinEl = document.getElementById("join")

function joinChk() {
    let joinIdEl = joinEl.id.value;
    let joinPwdEl = joinEl.password.value;
    let joinaddrEl = joinEl.addr.value;

    if (!joinIdEl) {
        alert('아이디를 입력해주세요.');
        return;
    }
    if (!joinPwdEl) {
        alert('비밀번호를 입력해주세요.');
        return;
    }
    if (!joinaddrEl) {
        alert('거주지를 선택해주세요.');
        return;
    }
    alert("회원가입이 완료되었습니다.");
    document.getElementById('join').submit();
}