const type = document.querySelector(".form-type");
const title = document.querySelector(".logo");
const menu = document.querySelector(".menu");

// const dropdown = document.getElementsById('form-dropdown')
// const navdrop = document.getElementById('tropdown');
// const totem = document.getElementsById('caret');
// const minimenu = document.getElementById('trop-menu') 

const portals = new TimelineMax();

portals.fromTo(
    menu, 1, {opacity: 0, x: 30}, {opacity: 1, x:0}
)

portals.fromTo(
    type, 0.6, {opacity: 0, y: -15}, {opacity: 1, y:0}
)

menu.onclick = () => {
    portals.fromTo(
        menu, 0.2, {opacity: 0, y:-4}, {opacity: 1, y:0}
    )

    if (navdrop.style.cssText=`
        opacity: 0;
    `) {

        portals.fromTo(
            navdrop, 0.2, {opacity: 0, y:-15}, {opacity: 1, y:0}
        )
    } else{
        portals.fromTo(
            navdrop, 0.2, {opacity: 1, y:0}, {opacity: 0, y:1}
        )
    }
    
};
