const secondLar=arr=>{
    // Brute Force Solution- O(nLogn)
    // arr.sort((a,b)=>a-b);

    // return arr[arr.length-2];

    //Better Solution- O(2n)
    let maxi=arr[0];
    let max2=-Infinity;

    for(let i=0;i<arr.length;i++)
    {
        if(arr[i]>maxi)
        {
            maxi=arr[i];
        }
    }
    for(let i=0;i<arr.length;i++)
    {
        if(arr[i]>max2 && arr[i]!=maxi)
        {
            max2=arr[i];
        }
    }
    return max2;

}
function main()
{
    let arr=[4,5,2,1,5,6,7,45,3,5,78,56,4];
    console.log(`The second largest element is : ${secondLar(arr)}`);
}

main();