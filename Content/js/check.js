console.log('Script Running');
  if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
    document.getElementById('desktop-view').style.visibility = 'visible'
 }
 function desktop_view(){
  document.getElementById('view_meta').content = "width=1024";  
  document.getElementById('desktop-view').style.visibility = 'hidden'
 }
 
