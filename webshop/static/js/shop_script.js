function plus(name)
{
    quantity = document.getElementById(name).value;
    quantity = parseFloat(quantity);
    result = quantity + 1;
    result = result.toString();
    document.getElementById(name).value = result;
}

function minus(name)
{
    quantity = document.getElementById(name).value;
    quantity = parseFloat(quantity);

    if(quantity == 1)
    {
        result = result.toString();
        document.getElementById(name).value = result;
    } else {
        result = quantity - 1;
        result = result.toString();
        document.getElementById(name).value = result;
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