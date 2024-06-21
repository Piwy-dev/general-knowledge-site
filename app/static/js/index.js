window.onload = function() {
    /* Language switcher */
    const languageSwitcher = document.getElementById('languageSwitcher');

    languageSwitcher.addEventListener('change', function() {
        const newLanguage = this.value;
        const currentPath = window.location.pathname;
        const newPath = currentPath.replace(/^\/[a-z]{2}\//, '/' + newLanguage + '/');
        window.location.href = newPath;
    });
}
