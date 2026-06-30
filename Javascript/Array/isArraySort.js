const isSort=arr=>{
    //Brute Force Solution: O(n)
    for(let i=0;i<arr.length-1;i++)
    {
        if(arr[i]>arr[i+1])
        {
            return false;
        }
    }
    return true;
}

function main()
{
    let arr=[1,2,3,6,5]
    if(isSort(arr))
    {
        console.log("The array is sorted:");
    }
    else{
        console.log("The array is not sorted:");
    }
}

main();