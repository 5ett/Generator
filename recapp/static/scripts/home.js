// plaque-lg transition
const plg1 = document.querySelector(".plg-1")
const plg2 = document.querySelector(".plg-2")
const plg3 = document.querySelector(".plg-3")

const tl = new TimelineMax();

// plaque-lg animation
tl.fromTo(
    plg1, 1, {opacity: 0, x: 30}, {opacity: 1, x:0}
)

.fromTo(
    plg2, 0.8, {opacity: 0, x: 30}, {opacity: 1, x:0},
    "-=0.2"
)

.fromTo(
    plg3, 0.8, {opacity: 0, x: 38}, {opacity: 1, x:0},
    "-=0.4"
);

// plaque-sm transition
const plaqueSm = document.querySelector(".psm");

const tll = new TimelineMax();

tll.fromTo(
    plaqueSm, 1.7, {opacity: 0, x: 60}, {opacity: 1, x:0},
    "-=0.3" 
);