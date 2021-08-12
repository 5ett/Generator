const nohead = document.querySelector(".form-type");
const title = document.querySelector(".logo");
const menu = document.querySelector(".menu");
const row1 = document.getElementById("proforma-row")
const row2 = document.getElementById("receipts-row")

// const dropdown = document.getElementsById('form-dropdown')
// const navdrop = document.getElementById('tropdown');
// const totem = document.getElementsById('caret');
// const minimenu = document.getElementById('trop-menu') 

const tropes = new TimelineMax();

tropes.fromTo(
    menu, 1, {opacity: 0, x: 30}, {opacity: 1, x:0}
)

tropes.fromTo(
    nohead, 0.6, {opacity: 0, y: -15}, {opacity: 1, y:0}
)

menu.onclick = () => {
    tropes.fromTo(
        menu, 0.2, {opacity: 0, y:-4}, {opacity: 1, y:0}
    )

    if (navdrop.style.cssText=`
        opacity: 0;
    `) {

        tropes.fromTo(
            navdrop, 0.2, {opacity: 0, y:-15}, {opacity: 1, y:0}
        )
    } else{
        tropes.fromTo(
            navdrop, 0.2, {opacity: 1, y:0}, {opacity: 0, y:1}
        )
    }
    
};

const animate2 = new TimelineMax();

animate2.fromTo(
    row1, 1, {opacity: 0, x: 30}, 
    {opacity: 1, x:0}
)

.fromTo(
    row2, 1, {opacity: 0, x: 30}, 
    {opacity: 1, x:0}, "-=0"
);
