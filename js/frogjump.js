function frogjump(x, y, d)
{
    return Math.ceil((Math.abs(y-x)/d));
}

console.log(frogjump(10, 85, 30));