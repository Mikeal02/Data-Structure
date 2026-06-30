const unique=arr=>{

    // Better solution-O(n)
    const n = arr.length;

        // Step 1: Find the maximum element
        const maxi = Math.max(...arr);

        // Step 2: Create hash array and initialize to 0
        const hash = Array(maxi + 1).fill(0);

        // Step 3: Count frequency of each number
        for (let i = 0; i < n; i++) {
            hash[arr[i]]++;
        }

        // Step 4: Find and return the number with frequency = 1
        for (let i = 0; i < n; i++) {
            if (hash[arr[i]] === 1) {
                return arr[i];
            }
        }

        return -1; // fallback
    }
    // Optimal solution- O(1)
//     let n=arr.length;
//     let xor=0;
//     for(let num of arr)
//     {
//         xor^=num;
//     }
//     return xor;
// }

function main()
{
    let arr=[4,1,2,1,2];
    console.log(unique(arr));
}

main();