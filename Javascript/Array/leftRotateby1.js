class solution{
    leftRotate(arr)
    {
        let element=arr[0];
        for(let i=1;i<arr.length;i++)
        {
            arr[i-1]=arr[i];
        }
        arr[arr.length-1]=element;
    }
}

function main()
{
    let arr=[3,4,5,2,7,6,8];
    let obj=new solution();
    obj.leftRotate(arr);
    console.log(arr);
}

main();