class solution{
     removedup(arr)
    {
        if(arr.length===0){

            return 0;
        }

        let i=0;
        for(let j=1;j<arr.length;j++)
        {
            if(arr[i]==arr[j])
            {
                continue;
            }
            else{
                i++;
                arr[i]=arr[j];
                
            }
        }
        return i+1;
    }
}

function main()
{
    let arr=[1,1,2,2,2,3,3,4,4];
    let obj= new solution();

    let ans=obj.removedup(arr);
    console.log(ans);
}

main();