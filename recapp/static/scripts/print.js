const name = document.getElementById('owner').innerText;
const photo = document.getElementById('receipt');




$(document).ready(function(){
    $('#printt').click(funtion(){
        domtoimage.toBlob(photo)
        .then(function(blob)){
            window.saveAs(blob, 'name.png')
        };
    })
})
