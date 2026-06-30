function moveZero(arr)
{
    let n=arr.length;
    if(n===0)return arr;
    let j=-1;
    for(let i=0;i<n;i++)
    {
        if(arr[i]===0)
        {
            j=i;
            break;
        }
    }
    if(j===-1)return arr;

    for(let i=j+1;i<n;i++)
    {
        if(arr[i]!==0)
        {
            [arr[i],arr[j]]=[arr[j],arr[i]];
            j++;
        }
    }

    
}

function main()
{
    let arr=[ 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1];
    moveZero(arr);
    console.log(arr);
  
}

main();