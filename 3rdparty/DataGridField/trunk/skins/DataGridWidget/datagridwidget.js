dataGridFieldFunctions = new Object()

var last_suffix = "x";

dataGridFieldFunctions.getInputOrSelect = function(node) {
    /* Get the (first) input or select form element under the given node */
    
    var inputs = node.getElementsByTagName("input");
    if(inputs.length > 0) {
        return inputs[0];
    }
    
    var selects = node.getElementsByTagName("select");
    if(selects.length > 0) {
        return selects[0];
    }

    return null;
}

dataGridFieldFunctions.getWidgetRows = function(currnode) {
	/* Return primary <tr>s of current node's parent DGW */
	tbody = this.getParentElementById(currnode, "datagridwidget-tbody");
	return this.getRows(tbody);
}

dataGridFieldFunctions.getRows = function(tbody) {
	/* Return <tr> rows of <table> element */
    
	var rows = new Array()
	
	child = tbody.firstChild;
	while(child != null) {
		if(child.tagName != null) {
			if(child.tagName.toLowerCase() == "tr") {
				rows = rows.concat(child);
			}
		}
		child = child.nextSibling;
	}
	              
	return rows;   
} 

dataGridFieldFunctions.autoInsertRow = function(e) {
    /* Add a new row when changing the last row 
       (i.e. the infamous auto insert feature)
    
       Check that if this onchange event handler was
       called from the last row. In this case,
       add a new row for DGF.
       
    */

    var currnode = window.event ? window.event.srcElement : e.currentTarget;
    
	// fetch required data structure   
    var tbody = this.getParentElement(currnode, "TBODY");
    var rows = this.getRows(tbody);        
    var lastRow = rows[rows.length-1]; 
    
    var thisRow = this.getParentElementById(currnode, "datagridwidget-row");      
    
    /* Skip the very last row which is a hidden template row */
    if(rows.length-1 ==(thisRow.rowIndex)) {
	    // Create a new row
	    var newtr = this.createNewRow(lastRow);
	                                                        
	    // Put new row to DOM tree before template row        
		lastRow.parentNode.insertBefore(newtr, lastRow);
		
		// update orderindex hidden fields
		this.updateOrderIndex(tbody);	        	    
    }    
}

dataGridFieldFunctions.addRowAfter = function(currnode) {
	/*
		Creates a new row before the clicked row
	*/
	
	// fetch required data structure
    var tbody = this.getParentElementById(currnode, "datagridwidget-tbody"); 
    var thisRow = this.getParentElementById(currnode, "datagridwidget-row"); 

    var newtr = this.createNewRow(thisRow);
        
	thisRow.parentNode.insertBefore(newtr, thisRow);
	
	// update orderindex hidden fields
	this.updateOrderIndex(tbody);	
  
}

dataGridFieldFunctions.addRow = function(id) {
	/* Explitcly add row for given DataGridField 
	
		@param id Archetypes field id for the widget	
	*/
	
	// fetch required data structure
    var tbody = document.getElementById("datagridwidget-tbody-" + id);    
    var rows = this.getRows(tbody);    
    var lastRow = rows[rows.length-1];
        
    var oldRows = rows.length;
                  
    // Create a new row
    var newtr = this.createNewRow(lastRow);
    
    // Put new row to DOM tree before template row        
	newNode = lastRow.parentNode.insertBefore(newtr, lastRow);
	
	// update orderindex hidden fields
	this.updateOrderIndex(tbody);		
      
}

dataGridFieldFunctions.createNewRow = function(tr) { 
	/* Creates a new row 
		   
	   @param tr A row in a table where we'll be adding the new row
	*/
	
    var tbody = this.getParentElementById(tr, "datagridwidget-tbody"); 
    var rows = this.getRows(tbody);   
    
    // hidden template row 
    var lastRow = rows[rows.length-1]; 
	
	var newtr = document.createElement("tr");
    newtr.setAttribute("id", "datagridwidget-row");
    newtr.setAttribute("class", "datagridwidget-row");
    	
	// clone template contents from the last row to the newly created row
	// HOX HOX HOX
	// If f****ng IE clones lastRow directly it doesn't work.
	// lastRow is in hidden state and no matter what you do it remains hidden.
	// i.e. overriding class doesn't bring it visible.
	// In Firefox everything worked like a charm.
	// So the code below is really a hack to satisfy Microsoft codeborgs.
	// keywords: IE javascript clone clonenode hidden element render visibility visual
	child = lastRow.firstChild;
	while(child != null) {
		newchild = child.cloneNode(true);
		newtr.appendChild(newchild);
		child = child.nextSibling;
	}		

    /* CALENDAR */

    // Select all calendar inputs in the cloned row. We must change the id
    // attribute on each input since the calendar popup needs an id to set the
    // values.
    var base_id = '';

    var n = 0;
    var wrapper = jq(newtr).find(".datagrid-calendar-wrapper input").each(function(i) {        
        if (n == 0)
        {
            base_id = this.id;
        }
        this.id = this.id + last_suffix;
        n = n + 1;
    });

    var wrapper = jq(newtr).find(".datagrid-calendar-wrapper select").each(function(i) {        
        this.id = this.id + last_suffix;
    });

    var wrapper = jq(newtr).find(".datagrid-calendar-wrapper a:first").each(function(i) {
        // We need a local variable here
        var xlast_suffix = last_suffix;
        this.onclick = function(){showJsCalendar(base_id+'_month'+xlast_suffix, 
            base_id+xlast_suffix, base_id+'_year'+xlast_suffix, base_id+'_month'+xlast_suffix, 
            base_id+'_day'+xlast_suffix, base_id+'_hour'+xlast_suffix, 
            base_id+'_minute'+xlast_suffix, 2000, 2014);};
    });

    // Modify the onChange functions on each select tag. We must use method 
    // update_date_field_plone25 from Plone 2.5 since there is a problem
    // when attempting to integrate the older calendar widget with Plone 3.
    // The current datagrid widget calendar handling must be refactored.
    var wrapper = jq(newtr).find(".datagrid-calendar-wrapper select").each(function(i) {
        // We need a local variable here
        var xlast_suffix = last_suffix;
        this.onchange = function(){dataGridFieldFunctions.update_date_field_plone25(base_id+xlast_suffix, 
            base_id+'_year'+xlast_suffix, base_id+'_month'+xlast_suffix, 
            base_id+'_day'+xlast_suffix, base_id+'_hour'+xlast_suffix, 
            base_id+'_minute'+xlast_suffix, base_id+'_ampm'+xlast_suffix)};
    });


    /* REFERENCE */

    // Iterate over referencebrowser widgets in this row
    var dummy = jq(newtr).find(".datagrid-reference-wrapper").each(function(i) {        

        // Alias
        var div = this;
        var xlast_suffix = last_suffix;

        // Adjust first hidden input. It also provides us with base_id.
        var elem = jq(div).find("input[type=hidden]");        
        var base_id = elem.attr("id");
        elem.attr("id", base_id + last_suffix);

        // Adjust input that is used to display the label.
        var elem = jq(div).find("input[type=text]");        
        elem.attr("id", base_id + last_suffix + '_label');

        // Retrieve a few variables needed for javascript popup launcher
        var elem = jq(div).find("span.meta");        
        var startup_directory   = elem.attr("startup_directory");
        var at_url              = elem.attr("at_url");
        var fieldRealName       = elem.attr("fieldRealName");

        // Modify the onClick functions
        var elem = jq(div).find("input.searchButton");
        elem.click(function(){
            dataGridFieldFunctions.referencebrowser_openBrowser(startup_directory, base_id+xlast_suffix, at_url, fieldRealName);
        });

    });

    // 'Increment' the suffix
    last_suffix = last_suffix + "x";

    return newtr;	 
}

dataGridFieldFunctions.removeFieldRow = function(node) {
    /* Remove the row in which the given node is found */
    
    var row = this.getParentElementById(node, 'datagridwidget-row');
    var tbody = this.getParentElementById(node, 'datagridwidget-tbody');
    tbody.removeChild(row);
}

dataGridFieldFunctions.moveRowDown = function(currnode){
    /* Move the given row down one */
           
    var tbody = this.getParentElementById(currnode, "datagridwidget-tbody");    
    
    var rows = this.getWidgetRows(currnode);
    
    var row = this.getParentElementById(currnode, "datagridwidget-row");      
    if(row == null) {
    	alert("Couldn't find DataGridWidget row");
    	return;
    }
    
    var idx = null
    
    // We can't use nextSibling because of blank text nodes in some browsers
    // Need to find the index of the row
    for(var t = 0; t < rows.length; t++) {
        if(rows[t] == row) {
            idx = t;
            break;
        }
    }

    // Abort if the current row wasn't found
    if(idx == null)
        return;     
        
    // If this was the last row (before the blank row at the end used to create
    // new rows), move to the top, else move down one.
    if(idx + 2 == rows.length) {
        var nextRow = rows.item[0]
        this.shiftRow(row, nextRow)
    } else {
        var nextRow = rows[idx+1]
        this.shiftRow(nextRow, row)
    }
    
    this.updateOrderIndex(tbody)

}

dataGridFieldFunctions.moveRowUp = function(currnode){
    /* Move the given row up one */
    
    var tbody = this.getParentElementById(currnode, "datagridwidget-tbody");    
    var rows = this.getWidgetRows(currnode);
    
    var row = this.getParentElementById(currnode, "datagridwidget-row");      
    if(row == null) {
    	alert("Couldn't find DataGridWidget row");
    	return;
    }

    var idx = null
    
    // We can't use nextSibling because of blank text nodes in some browsers
    // Need to find the index of the row
    for(var t = 0; t < rows.length; t++) {
        if(rows[t] == row) {
            idx = t;
            break;
        }
    }
    
    // Abort if the current row wasn't found
    if(idx == null)
        return;
        
    // If this was the first row, move to the end (i.e. before the blank row
    // at the end used to create new rows), else move up one
    if(idx == 0) {
        var previousRow = rows[rows.length - 1]
        this.shiftRow(row, previousRow);
    } else {
        var previousRow = rows[idx-1];
        this.shiftRow(row, previousRow);
    }
    
    this.updateOrderIndex(tbody);
}

dataGridFieldFunctions.shiftRow = function(bottom, top){
    /* Put node top before node bottom */
    
    bottom.parentNode.insertBefore(bottom, top)   
}

dataGridFieldFunctions.updateOrderIndex = function (tbody) {

    /* Update the hidden orderindex fields to be in the right order */
    
    var xre = new RegExp(/^orderindex__/)
    var idx = 0;
    var cell;
    
    var rows = this.getRows(tbody); 
    
    /* Make sure that updateOrderIndex doesn't touch 
       the template (last) row */
    for(var i=0; i<rows.length-1; i++) {
    
	    for (var c = 0; (cell = rows[i].getElementsByTagName('INPUT').item(c)); c++) {
	            
	        if (cell.getAttribute('id')) {
	            if (xre.exec(cell.id)) {
	                cell.value = idx;
	            }
	        }           
	        this.updateRadioButtonGroupName(this.getParentElement(cell, "TR"), idx);        
	        idx++;
	    }      
	}
}


dataGridFieldFunctions.updateRadioButtonGroupName = function (row, newIndex) {
	/* Adjust radio button group names after reordering 
	
	   Why we do this, see RadioColumn class comments
	   
	   TODO: If chain onchange -> updateOrderIndex -> updaterRadioButtonGroupName
	   is triggered on Firefox, the value of checked radio button is put to the
	   newly generated row instead of clicked row.
	*/

   var cell;
   var xre = new RegExp(/^radio/)
   var xre2 = new RegExp(/^checkbox/)
   
    for (var c = 0; (cell = row.getElementsByTagName('INPUT').item(c)); c++) {
   	    	    
   	   	if(cell.getAttribute('type')) {
   	   		var type = cell.getAttribute('type');
             if (xre.exec(type) || xre2.exec(type)) {          
            	
				var name = cell.getAttribute("NAME")
				if(name == null) continue;

				// save fieldId + columnId part
				var baseLabel = name.substring(0, name.lastIndexOf("."));				
				// update per row running id
				cell.setAttribute("NAME", baseLabel + "." + newIndex);
			}
   	    }               
	}
}

dataGridFieldFunctions.getParentElement = function(currnode, tagname) {
    /* Find the first parent node with the given tag name */

    tagname = tagname.toUpperCase();
    var parent = currnode.parentNode;

    while(parent.tagName.toUpperCase() != tagname) {
        parent = parent.parentNode;
        // Next line is a safety belt
        if(parent.tagName.toUpperCase() == "BODY") 
            return null;
    }

    return parent;
}

dataGridFieldFunctions.getParentElementById = function(currnode, id) {
    /* Find the first parent node with the given id 
    
    	Id is partially matched: the beginning of
    	an element id matches parameter id string.
    
    	Currnode: Node where ascending in DOM tree beings
    	Id: Id string to look for. 
    	    	
    */
    
    id = id.toLowerCase();
    var parent = currnode.parentNode;

    while(true) {
       
    	var parentId = parent.getAttribute("id");
    	if(parentId != null) {    	
    		 if(parentId.toLowerCase().substring(0, id.length) == id) break;
    	}
    	    
        parent = parent.parentNode;
        // Next line is a safety belt
        if(parent.tagName.toUpperCase() == "BODY") 
            return null;
    }

    return parent;
}

// Method *is* update_date_field_plone from Plone 2.5
dataGridFieldFunctions.update_date_field_plone25 = function(field, year, month, day, hour, minute, ampm) {
    var field  = document.getElementById(field)
    var date   = document.getElementById(date)
    var year   = document.getElementById(year)
    var month  = document.getElementById(month)
    var day    = document.getElementById(day)
    var hour   = document.getElementById(hour)
    var minute = document.getElementById(minute)
    var ampm   = document.getElementById(ampm)

    if (0 < year.value)
    {
        // Return ISO date string
        // Note: This relies heavily on what date_components_support.py puts into the form.
        field.value = year.value + "-" + month.value + "-" + day.value + " " + hour.value + ":" + minute.value
        // Handle optional AM/PM
        if (ampm && ampm.value)
            field.value = field.value + " " + ampm.value
    } 
    else 
    {
        // Return empty string
        field.value = ''
        // Reset widgets
        month.options[0].selected = 1
        day.options[0].selected = 1
        hour.options[0].selected = 1
        minute.options[0].selected = 1
        if (ampm && ampm.options)
            ampm.options[0].selected = 1
    }
}

// function to open the popup window
dataGridFieldFunctions.referencebrowser_openBrowser = function referencebrowser_openBrowser(path, fieldName, at_url, fieldRealName){
    atrefpopup = window.open(path + '/referencebrowser_popup?fieldName=' + fieldName + '&fieldRealName=' + fieldRealName +'&at_url=' + at_url+'&multiValued=0','referencebrowser_popup','toolbar=no,location=no,status=no,menubar=no,scrollbars=yes,resizable=yes,width=500,height=550');
}
