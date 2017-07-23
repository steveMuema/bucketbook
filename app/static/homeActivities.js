 // Create a "close" button and append it to each activity list item
    var myNodelist2 = document.getElementsByTagName("LI");
    
    var j;
    for (j = 0; j < myNodelist2.length; j++) {
    var span2 = document.createElement("SPAN");
    var txt1 = document.createTextNode("\u00D7");
    span2.className = "closeActivity";
    span2.appendChild(txt1);
    myNodelist2[j].appendChild(span2);
    }

    // Click on a close button to hide the current list item
    var closeActivity = document.getElementsByClassName("closeActivity");
    var j;
    for (j = 0; j < closeActivity.length; j++) {
    closeActivity[j].onclick = function() {
        var div2 = this.parentElement;
        div2.style.display = "none";
    }
    }

    // Add a "checked" symbol when clicking on a list item
    var activityList = document.querySelector('ul');
    activityList.addEventListener('click', function(eventActivity) {
    if (eventActivity.target.tagName === 'LI') {
        eventActivity.target.classList.toggle('checked');
    }
    }, false);

// Create a new activity item when clicking on the "Add" button
 function newActivity() {
    var li = document.createElement("li");
    var inputValue = document.getElementById("addActivity").value;
    var t = document.createTextNode(inputValue);
    li.appendChild(t);
    if (inputValue === '') {
        alert("You must write something!");
    } else {
        document.getElementById("myUL1").appendChild(li);
    }
    document.getElementById("addActivity").value = "";

    var span2 = document.createElement("SPAN");
    var txt1 = document.createTextNode("\u00D7");
    span2.className = "closeActivity";
    span2.appendChild(txt1);
    li.appendChild(span2);

     for (i = 0; i < closeActivity.length; i++) {
        closeActivity[i].onclick = function() {
        var div2 = this.parentElement;
        div2.style.display = "none";
        }
    }
 }