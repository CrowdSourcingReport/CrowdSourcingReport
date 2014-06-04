
  if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
    console.log('Script Running');
    var ref = document.createElement("a");
    var vie = document.createTextNode("Desktop View");
    ref.appendChild(vie);
    ref.setAttribute("onClick","desktop_view()"); 
    ref.setAttribute("href","#");
    ref.setAttribute("id","desktop-view"); 
    document.getElementById('desktopView').appendChild(ref);
 }
 
 
 function desktop_view(){
  document.getElementById('view_meta').content = "width=1280";  
  var child = document.getElementById('desktop-view')
  document.getElementById('desktopView').removeChild(child);
 }
