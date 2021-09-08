const darkButton = document.getElementById('light');

const body = document.body;

const theme = localStorage.getItem('theme');

if(theme){
    body.classList.add(theme);
    if(theme == 'light'){
        darkButton.innerText = 'dark';
    } else{
        darkButton.innerText = 'light';
    }
}

darkButton.onclick = () => {
    body.classList.replace('light', 'dark');
    localStorage.setItem('theme', 'dark');
};

darkButton.onclick = () => {

    if (body.classList.contains('light')) {

        body.classList.replace('light', 'dark');
        // darkButton.style.cssText = `
        //  background: var(--white);
        // `

        darkButton.innerText = 'light';

        localStorage.setItem('theme', 'dark');

    } else {

        body.classList.replace('dark', 'light');
    //     darkButton.style.cssText = `
    //     background: var(--border-col);
    //    `

    darkButton.innerText = 'dark';

        localStorage.setItem('theme', 'light');
    }
};


if (window.history.replaceState){
    window.history.replaceState( null, null, window.location.href);
};
