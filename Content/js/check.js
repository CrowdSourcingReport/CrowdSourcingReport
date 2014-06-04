console.log('Script Running');
  if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
   console.log('Mobile');
   window.alert('Mobile Browser');
   document.getElementById('view_meta').content = "width=1024";
 }
 else{
   console.log('Desktop');
  window.alert('Desktop or anything else');
 }
