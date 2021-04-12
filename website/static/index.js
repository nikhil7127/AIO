function deleteNote(noteId) {
  fetch("/deleteNote", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/notes";
  });
}


function prev(number) {
if (number>1)
{
number--;
}
  fetch("/stackoverflow", {
    method: "POST",
    body: JSON.stringify({pg:number}),
  }).then((_res) => {
    window.location.href = "/stackoverflow";
  });
}

function next(number) {
if (number<21)
{
number++;
}
  fetch("/stackoverflow", {
    method: "POST",
    body: JSON.stringify({pg:number}),
  }).then((_res) => {
    window.location.href = "/stackoverflow";
  });
}

function sendRequest(link)
{
fetch("/link", {
    method: "POST",
    body: JSON.stringify({ link: link }),
  }).then((_res) => {
    window.location.href = "/specific";
  })
}