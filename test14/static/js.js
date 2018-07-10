function DateSort() {
    document.getElementById("DateSort").style.display = 'block';    //display the div that has complaint sorted according to date
    document.getElementById("AlphaSort").style.display = 'none';    //hide the div that has complaint sorted according to alpha
    document.getElementById("PrioritySort").style.display = 'none'; //hide the div that has complaint sorted according to priority
    document.getElementById("D").style.color = "#ffffff";   //change the color of the (Date)
    document.getElementById("A").style.color = "#9E9E9E";   //change the color of the (alpha)
    document.getElementById("P").style.color = "#9E9E9E";   //change the color of the (priority)
}

function AlphaSort() {
    document.getElementById("DateSort").style.display = 'none'; //hide the div that has complaint sorted according to date
    document.getElementById("AlphaSort").style.display = 'block';   //display the div that has complaint sorted according to alpha
    document.getElementById("PrioritySort").style.display = 'none'; //hide the div that has complaint sorted according to priority
    document.getElementById("D").style.color = "#9E9E9E";   //change the color of the (Date)
    document.getElementById("A").style.color = "#ffffff";   //change the color of the (alpha)
    document.getElementById("P").style.color = "#9E9E9E";   //change the color of the (priority)
}

function PrioritySort() {
    document.getElementById("DateSort").style.display = 'none';     //hide the div that has complaint sorted according to date
    document.getElementById("AlphaSort").style.display = 'none';    //hide the div that has complaint sorted according to alpha
    document.getElementById("PrioritySort").style.display = 'block';    //display the div that has complaint sorted according to priority
    document.getElementById("D").style.color = "#9E9E9E";   //change the color of the (Date)
    document.getElementById("A").style.color = "#9E9E9E";   //change the color of the (alpha)
    document.getElementById("P").style.color = "#ffffff";   //change the color of the (priority)
}