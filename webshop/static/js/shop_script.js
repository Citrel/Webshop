function plus()
{
    alert('test');
    quantity = document.getElementById('quantity').value;
    quantity = parseFloat(quantity);
    result = quantity + 1;
    result = toString(result);
    document.getElementById('quantity').value = result;
}

function minus(quantity)
{
    if(quantity == 1)
    {
        return 1;
    } else {
        result = quantity + 1;
        return quantity;
    }
}