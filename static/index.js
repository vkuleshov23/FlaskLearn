function getBG() {
    return document.getElementById("bg"); 
}

function blurUp() {
    bg = getBG()
        bg.style.filter = "blur(7px)"
}


function blurDown() {
    bg = getBG()
    bg.style.filter = "blur(1px)"
}

function btn(pos) {
    if (pos == 0){
        blurUp()
    } else {
        blurDown()
    }
    // for (var i = 0; i < btns.length; i++) {
    //     let btn = btns[i].getElementsByClassName("myButton")[0]
    //     let checkbox = btn.getElementsByTagName("input")[0]
    //     let lable = btn.getElementsByTagName("label")[0]
    //     lable.htmlFor = "checkbox.id"
    // }
}