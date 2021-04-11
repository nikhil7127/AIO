function deleteNote(noteId) {
  fetch("/deleteNote", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/notes";
  });
}

//function prev(number) {
//if (number>1)
//{
//number--;
//}
//  fetch("/stackoverflow", {
//    method: "POST",
//    body: JSON.stringify({pg:number}),
//  }).then((_res) => {
//    window.location.href = "/stackoverflow";
//  });
//}
//
//function deleteNote(number) {
//if (number<21)
//{
//number++;
//}
//  fetch("/stackoverflow", {
//    method: "POST",
//    body: JSON.stringify({pg:number}),
//  }).then((_res) => {
//    window.location.href = "/stackoverflow";
//  });
//}