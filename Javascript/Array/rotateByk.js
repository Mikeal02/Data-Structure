function reverse(nums,start,end)
{
    while(start<end)
    {
        [nums[start], nums[end]] = [nums[end], nums[start]];
        start++;
        end--;
    }
}

const Rotatebyk=(arr,k,dir)=>{
    let n=arr.length;
    if(n===0 || k==0)return arr;
    k=k %n;
    if(dir==="Left")
    {
        reverse(arr,0,k-1);
        reverse(arr,k,n-1);
        reverse(arr,0,n-1);
    }

    else
    {
        reverse(arr,0,n-1);
        reverse(arr,0,k-1);
        reverse(arr,k,n-1);
    }

}

function main()
{
    let arr=[3,4,5,2,7,6,8];
    Rotatebyk(arr,4,"Right");
    console.log(arr);
}

main();