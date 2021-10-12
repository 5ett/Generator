const greetings = document.querySelector(".greetings");
const title = document.querySelector(".logo");
const menu = document.querySelector(".menu-acc");
// const navdrop = document.querySelector(".navbar-nav");
const navdrop = document.getElementById('tropdown');

const heads = new TimelineMax();

heads.fromTo(
    menu, 1, {opacity: 0, x: 30}, {opacity: 1, x:0}
)

heads.fromTo(
    greetings, 0.6, {opacity: 0, y: -15}, {opacity: 1, y:0}
)

menu.onclick = () => {
    heads.fromTo(
        menu, 0.2, {opacity: 0, y:-4}, {opacity: 1, y:0}
    )

    if (navdrop.style.cssText=`
         opacity: 1;
     `) {

        navdrop.style.cssText=`
         opacity: 1;
    }

    // heads.fromTo(
    //         navdrop, 0.2, {opacity: 0, y:-15}, {opacity: 1, y:0}
    //     )

    // if (navdrop.style.cssText=`
    //     opacity: 0;
    // `) {

    // //     navdrop.style.cssText=`
    // //     opacity: 1;
    // // `
    //     heads.fromTo(
    //         navdrop, 0.2, {opacity: 0, y:-15}, {opacity: 1, y:0}
    //     )}
    // } else{

    //     navdrop.style.cssText=`
    //     opacity: 0;
    // `
    //     heads.fromTo(
    //         navdrop, 0.2, {opacity: 1, y:0}, {opacity: 0, y:1}
    //     )
    // }

};
