function () {
  if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
   window.alert('Mobile Browser');
 }
 else{
  window.alert('Desktop or anything else');
 }
}
