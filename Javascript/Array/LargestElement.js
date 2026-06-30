const largest=arr=>
{
    //Better Solution
    arr.sort((a,b)=>a-b);

    return arr[arr.length-1];

    //Optimal Solution
    // let maxi=arr[0];
    // for(let i =0;i<arr.length;i++)
    // {
    //     if(arr[i]>maxi)
    //     {
    //         maxi=arr[i];
    //     }
    // }
    // return maxi;
}


const arr =[3,2,5,7.1,12,4];

console.log(`The largest element is: ${largest(arr)}`);