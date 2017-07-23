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
                    var t= document.createTextNode("edit");
                    span1.className = "editlist";
                    span1.appendChild(t);
                     myNodelist1[i].appendChild(span1);
                     }


                    //click "edit" button to open activities modal
                    var edit=document.getElementsByClassName("editlist");
                    var i;
                    for(i=0; i<edit.length; i++){
                        edit[i].onclick = function(){
                         var modal = document.getElementById('myModal');

                    // Get the button that opens the modal
                    var div1 = this.parentElement;

                    // Get the <span> element that closes the modal
                    var span1 = document.getElementsByClassName("close1")[0];

                    // When the user clicks on the edit button, open the modal
                    div1.onclick = function() {
                        modal.style.display = "block";
                    }

                    // When the user clicks on <span> (x), close the modal
                    span1.onclick = function() {
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
                    var li = document.createElement("li");
                    var inputValue = document.getElementById("addlist").value;
                    var t = document.createTextNode(inputValue);
                    li.appendChild(t);
                    if (inputValue === '') {
                        alert("You must write something!");
                    } else {
                        document.getElementById("myUL").appendChild(li);
                    }
                    document.getElementById("addlist").value = "";

                    var span = document.createElement("SPAN");
                    var txt = document.createTextNode("\u00D7");
                    span.className = "close";
                    span.appendChild(txt);
                    li.appendChild(span);
                     var span1 = document.createElement("SPAN");
                    var t= document.createTextNode("edit");
                    span1.className = "editlist";
                    span1.appendChild(t);
                     li.appendChild(span1);

                    for (i = 0; i < close.length; i++) {
                        close[i].onclick = function() {
                        var div = this.parentElement;
                        div.style.display = "none";
                        }
                    }
                    for(i=0; i<edit.length; i++){
                        edit[i].onclick = function(){
                           
                         var modal = document.getElementById('myModal');
                         
                    // Get the button that opens the modal
                    var div1 = this.parentElement;

                    // Get the <span> element that closes the modal
                    var span1 = document.getElementsByClassName("close1")[0];

                    // When the user clicks on the edit button, open the modal
                    div1.onclick = function() {
                        var modal1=this.parentElement;
                        modal.style.display = "block";
                    }

                    // When the user clicks on <span> (x), close the modal
                    span1.onclick = function() {
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

        
                
                // Create a "close" button and append it to each activity list item
                    var myNodelist2 = document.getElementsByTagName("LI");
                    
                    var j;
                    for (j = 0; j < myNodelist2.length; j++) {
                    var span2 = modal.createElement("SPAN");
                    var txt1 = modal.createTextNode("X");
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

                // Create a new list item when clicking on the "Add" button
                function newActivity() {
                var listActivity = document.createElement("li");
                
                var inputActivity = document.getElementById("myInput").value;
                var activityTxt = document.createTextNode(inputActivity);
                listActivity.appendChild(activityTxt);
                if (inputActivity === '') {
                    alert("You must write something!");
                } else {
                    document.getElementById("myUL1").appendChild(listActivity);
                }
                document.getElementById("myInput").value = "";

                var div2 = document.createElement("SPAN");
                var txt1 = document.createTextNode("X");
                div2.className = "closeActivity";
                div2.appendChild(txt1);
                listActivity.appendChild(div2);

                for (j = 0; j < closeActivity.length; j++) {
                    closeActivity[j].onclick = function() {
                    var div2 = this.parentElement;
                    div2.style.display = "none";
                    }
                }

                } 