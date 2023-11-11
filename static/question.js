// function sendAnswer(position) {
// 	let answerPos = ({"position" : position});
// 	let xhr = new XMLHttpRequest();
// 	xhr.open("POST", "/answer", true);
// 	xhr.setRequestHeader('Content-Type', 'application/json');
// 	xhr.send(JSON.stringify(answerPos));
// 	if(xhr.status == 200){
// 		alert("YES")
// 	// 	window.location = "/next"
// 	}
// }

// function addLableFor() {
// 	let btns = document.getElementsByName("answers");
// 	for (var i = 0; i < btns.length; i++) {
// 		let btn = btns[i].getElementsByClassName("myButton")[0]
// 		let checkbox = btn.getElementsByTagName("input")[0]
// 		let lable = btn.getElementsByTagName("label")[0]
// 		lable.htmlFor = "checkbox.id"
// 	}
// }

// function sendAnswer1(position) {
// 	let form = document.createElement('form');
// 	document.body.appendChild(form)
// 	form.method = 'post'
// 	form.action = 
// }