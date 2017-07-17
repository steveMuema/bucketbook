         // Create a "close" button and append it to each list item
var myNodelist = document.getElementsByTagName("LI");
var i;
for (i = 0; i < myNodelist.length; i++) {
    var span = document.createElement("SPAN");
    var txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    myNodelist[i].appendChild(span);
                  }

                
    //create "edit" button and append on each list item
    var myNodelist1= document.getElementsByTagName("LI");
    var i;
    for (i =0; i<myNodelist1.length; i++) {
    
    var span1 = document.createElement("SPAN");
    var edittxt= document.createTextNode("edit");
    span1.className = "edit";
    span1.appendChild(edittxt);
        myNodelist1[i].appendChild(span1);
        }


    //click "edit" button to open activities modal
    // var edit=document.getElementsByClassName("edit");
    // var i;
    // for(i=0; i<edit.length; i++){
    //     edit[i].onclick = function(){
    //     //open activities page
    //     }

    // Click on a close button to hide the current list item
    var close = document.getElementsByClassName("close");
    var i;
    for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
        var div = this.parentElement;
        div.style.display = "none";
    }
    }

    // Add a "checked" symbol when clicking on a list item
    var list = document.querySelector('ul');
    list.addEventListener('click', function(ev) {
    if (ev.target.tagName === 'LI') {
        ev.target.classList.toggle('checked');
    }
    }, false);

    // Create a new list item when clicking on the "Add" button
    function newElement() {
    var list = document.createElement("li");
    var inputList = document.getElementById("addlist").value;
    var txtnode = document.createTextNode(inputList);
    list.appendChild(txtnode);
    if (inputList === '') {
        alert("You must write something!");
    } else {
        document.getElementById("myUL").appendChild(list);
    }
    document.getElementById("addlist").value = "";

    var spanclose = document.createElement("SPAN");
    var txtclose = document.createTextNode("\u00D7");
    spanclose.className = "close";
    spanclose.appendChild(txtclose);
    list.appendChild(spanclose);

    var spanEdit = document.createElement("SPAN");
    var createEdit= document.createTextNode("edit");
    spanEdit.className = "edit";
    spanEdit.appendChild(createEdit);
        list.appendChild(spanEdit);

    for (i = 0; i < close.length; i++) {
        close[i].onclick = function() {
        var div1 = this.parentElement;
        div1.style.display = "none";
        }
    }
    // for(i=0; i<edit.length; i++){
    //     edit[i].onclick = function(){
    //         //open the lists
    //     }
    // }         
} 



