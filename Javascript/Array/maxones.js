//brute force
const max_ones = (arr) => {};

//Optimal solution
const maxones = (arr) => {
  let maxi = 0;
  let count = 0;
  for (let x of arr) {
    if (x === 1) {
      count++;
      maxi = Math.max(maxi, count);
    } else {
      count = 0;
    }
  }
  return maxi;
};
const arr = [0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1];
console.log(`The maximum consecutive ones are: ${maxones(arr)}`);
