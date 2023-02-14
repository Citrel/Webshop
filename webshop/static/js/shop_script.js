function plus()
{
    quantity = document.getElementById('quantity').value;
    quantity = parseFloat(quantity);
    result = quantity + 1;
    result = result.toString();
    document.getElementById('quantity').value = result;
}

function minus()
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

function like()
{
    heart = document.getElementById('button-like-text').innerHTML;

    if(heart == "&#9825;")
    {
        document.getElementById('button-like-text').innerHTML = "&#9829;";
    } else 
    {
        document.getElementById('button-like-text').innerHTML = "&#9825;";
    }
}