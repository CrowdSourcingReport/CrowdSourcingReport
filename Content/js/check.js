if(typeof(Storage)!=="undefined")
  {
  if (!sessionStorage.viewStatus)
  {
    sessionStorage.viewStatus=0;
  }
}

  if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
    console.log('Script Running');
    if(sessionStorage.viewStatus===0){
      sessionStorage.viewStatus = 1;
      document.getElementById('desktopView').style.visibility = 'visible';
      loaction.reload(true);
    }   
 }
 
 
 function desktop_view(){
  document.getElementById('view_meta').content = "width=1280";  
  document.getElementById('desktopView').style.visibility = 'hidden';
  loaction.reload(true);
}
