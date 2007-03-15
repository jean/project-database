/* <dtml-var "enableHTTPCompression(request=REQUEST, debug=1, js=1)"> (this is for http compression) */

/*
<dtml-let last_modified="_.DateTime()-14"
expires="_.DateTime()+7" >
<dtml-call "REQUEST.RESPONSE.setHeader( 'Content-Type', 'text/javascript' )">
<dtml-call "REQUEST.RESPONSE.setHeader( 'Last-Modified', last_modified.toZone('GMT').rfc822() )">
<dtml-call "REQUEST.RESPONSE.setHeader( 'Cache-Control', 'max-age=36000, must-revalidate' )">
<dtml-call "REQUEST.RESPONSE.setHeader( 'Expires', expires.toZone('GMT').rfc822() )" >
</dtml-let>
Common Javascript functions for Tasty Bookmarks
*/

function toggle_thread(element_id) {
        displaystyle = document.getElementById(element_id).style;
        if (displaystyle.display == 'none') {
          displaystyle.display = 'block';
        } else {
          displaystyle.display = 'none';
        }
        return false;
      }
      function addKeyword(keyword) {
        kwfield = document.edit_form.keywords;
        if (kwfield.value == "") {
          kwfield.value = kwfield.value + keyword;
        }
        else {
          kwfield.value = kwfield.value + ' ' + keyword;
        }
      }
function addNetscapePanel(sidebarLocation) { 
      if ((typeof window.sidebar == "object") && (typeof window.sidebar.addPanel == "function")) 
      { 
         window.sidebar.addPanel ("Tasty Sidebar", 
         sidebarLocation,""); 
      } 
      else 
      { 
         var rv = window.confirm ("This page is enhanced for use with Mozilla.  " 
            + "Would you like to upgrade now?"); 
         if (rv) 
            document.location.href = "http://www.mozilla.org/products/";
      } 
   } 
 function addKeyword(keyword) {
        kwfield = document.edit_form.keywords;
        if (kwfield.value == "") {
          kwfield.value = kwfield.value + keyword;
        }
        else {
          kwfield.value = kwfield.value + ' ' + keyword;
        }
      }
