if(typeof(Storage)!=="undefined")
  {
  if (!sessionStorage.viewStatus)
  {
    sessionStorage.viewStatus=0;
  }
}
  
  if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
    console.log('Script Running');
    sessionStorage.viewStatus=1;
 }
 
 
 function desktop_view(){
  document.getElementById('view_meta').content = "width=1280";  
  var child = document.getElementById('desktop-view')
  document.getElementById('desktopView').removeChild(child);
 }
