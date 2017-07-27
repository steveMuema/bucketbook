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
    
    // var span1 = document.createElement("A");
    var edittxt= document.createTextNode("edit");
    
    span1.className = "edit";
    span1.id="editlink";
    span1.appendChild(edittxt);
    // span1.appendChild(link);
    $('A').append(link);
        myNodelist1[i].appendChild(span1);
        }


//     //click "edit" button to open activities modal
    var edit=document.getElementsByClassName("edit");
    var i;
    for(i=0; i<edit.length; i++){
        edit[i].onclick = function (){
        
          };
    }
 
    

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

    //create close element when user adds a new list
    var spanclose = document.createElement("SPAN");
    var txtclose = document.createTextNode("\u00D7");
    spanclose.className = "close";
    spanclose.appendChild(txtclose);
    list.appendChild(spanclose);

    //create edit element when user adds a new list
    var spanEdit = document.createElement("SPAN");
    var createEdit= document.createTextNode("edit");
    spanEdit.className = "edit";
    spanEdit.appendChild(createEdit);
        list.appendChild(spanEdit);

    //create add activity element when user adds a new list
    var spanAdd = document.createElement("A");
    var createAdd= document.createTextNode("add");
    spanEdit.className = "addActivity";
    spanEdit.appendChild(createAdd);
    list.appendChild(spanAdd);
    

    for (i = 0; i < close.length; i++) {
        close[i].onclick = function() {
        var div1 = this.parentElement;
        div1.style.display = "none";
        }
    }
    for(i=0; i<edit.length; i++){
        edit[i].onclick = function(){
        // Get the modal
        var modal = document.getElementById('myModal');

        // Get the button that opens the modal
        var btn = document.getElementById("myBtn");

        // Get the <span> element that closes the modal
        var span = document.getElementsByClassName("close")[0];

        // When the user clicks on the button, open the modal
        btn.onclick = function() {
            modal.style.display = "block";
        }

        // When the user clicks on <span> (x), close the modal
        span.onclick = function() {
            modal.style.display = "none";
        }

        // When the user clicks anywhere outside of the modal, close it
        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
                }
    }         
} 
    }

    
