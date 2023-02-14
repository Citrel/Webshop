function plus()
{
    quantity = document.getElementById('quantity').value;
    quantity = parseFloat(quantity);
    result = quantity + 1;
    result = result.toString();
    document.getElementById('quantity').value = result;
}

function minus(quantity)
{
    quantity = document.getElementById('quantity').value;
    quantity = parseFloat(quantity);

    if(quantity == 1)
    {
        result = result.toString();
        document.getElementById('quantity').value = result;
    } else {
        result = quantity - 1;
        result = result.toString();
        document.getElementById('quantity').value = result;
    }
}