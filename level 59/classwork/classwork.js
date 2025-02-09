const form = document.getElementById("nameform");
const submit = document.getElementById("submit");
submit.addEventListener("click", function (event) {
  event.preventDefault();
  const name1 = form.elements.name;
  console.log(name1.value);
});
