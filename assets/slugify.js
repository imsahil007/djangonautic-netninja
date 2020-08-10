var titleinput = document.querySelector('input[name=title]');
var sluginput = document.querySelector('input[name=slug]');


var slugify = (val) => {
    return val.toString().toLowerCase().trim().replace(/&/g,'-and-').replace(/[\s\W-]+/g,'-');
};

titleinput.addEventListener('keyup',(e) => {
    console.log('comign here');
    sluginput.setAttribute( "value", slugify(titleinput.value));
});