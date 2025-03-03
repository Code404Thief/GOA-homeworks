function summation(arr) {
  let res = 0;
  for (let i = 0; i < arr.length; i++) {
    res += arr[i];
  }
  return res;
}
console.log(summation([1, 2, 3]));

function mix(arr) {
  let minNum = arr[0];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > minNum) {
      minNum = arr[i];
    }
  }
}
let maxNum = arr[0];
for (let i = 0; i < arr.length; i++) {
  if (arr[i] > maxNum) {
    maxNum = arr[i];
  }
}

console.log(mix[(1, 2, 3, 4, 59)]);

function createArr(num1, num2) {
  let num1 = Math.ceil(Math.random() * 100);
  let num2 = Math.ceil(Math.random() * 100);
  const arr = [];
  if (num1 > num2) {
    num2 = num1;
    num1 = num2;
  }
  for (let i = num1; i < num2; i++) {
    arr.push(i);
  }
  return arr;
}
console.log(createArr());

function square(arr) {
  const newArr = [];
  for (let i = 0; i < arr.length; i++) {
    newArr.push(arr[i] * arr[i]);
  }
}
console.log(square([1,2,3,4,5]));