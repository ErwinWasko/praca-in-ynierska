document.addEventListener("DOMContentLoaded", function() {
    const toggleDarkMode = document.getElementById('toggle-dark-mode');
    
    let darkMode = false;

    toggleDarkMode.addEventListener('click', () => {
        darkMode = !darkMode;
        document.body.classList.toggle('dark-mode');
        toggleDarkMode.classList.toggle('dark');
    });
});