//Brute force Solution
const two_sum = (arr, target) => {
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      let sum = arr[i] + arr[j];
      if (sum == target) {
        return [i, j];
      }
    }
  }
};

//hashMap solution

const sum_2 = (arr, target) => {
  const mp = new Map();
  for (let i = 0; i < arr.length; i++) {
    let needed = target - arr[i];
    if (mp.has(needed)) {
      return [mp.get(needed), i];
    }
    mp.set(arr[i], i);
  }
};

const sum_two = (arr, target) => {
  arr.sort((a, b) => a - b);
  let i = 0;
  let j = arr.length - 1;
  while (i < j) {
    let sum = arr[i] + arr[j];
    if (sum == target) {
      return [i, j];
    } else if (sum > target) {
      j--;
    } else {
      i++;
    }
  }
};
const arr = [2, 6, 5, 8, 11];
// console.log(two_sum(arr, 11));
console.log(sum_two(arr, 11));
