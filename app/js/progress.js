function loadProgress() {
    const state = getState();
    document.getElementById('prog-xp').innerText = state.xp;
    document.getElementById('prog-streak').innerText = state.streak;
}
document.addEventListener('DOMContentLoaded', loadProgress);
