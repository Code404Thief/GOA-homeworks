let user = {
  firstName: "სანდრო",
  lastName: "რუხაძე",
  age: 13,
};
localStorage.setItem("user", JSON.stringify(user));
let storedUser = JSON.parse(localStorage.getItem("user"));
console.log(storedUser.firstName);
storedUser.firstName = "ბანდრო";
localStorage.setItem("user", JSON.stringify(storedUser));
let updatedUser = JSON.parse(localStorage.getItem("user"));
console.log(updatedUser.firstName);
