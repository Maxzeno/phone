 
function filtersAprear() {
  let filters = document.querySelector('#filters');
  if (filters.className.search('d-md-none') != -1){
    filters.setAttribute('class','d-none px-3 mb-2');
  }else if (filters.className.search('d-none') != -1){
    filters.setAttribute('class','d-md-none px-3 mb-2');
  }
}

document.querySelector('#filterIcon').addEventListener('click', filtersAprear);



function emmaNavOpen() {
  document.getElementById('iconSideBar').style.display = 'block';
  document.getElementById('emmaNav').style.left = '0px';
  // document.getElementById('iconSideBar').style.transition = '1s';
  document.getElementById('mainNav').style.backgroundColor = '#0d0f10';
    // document.body.style.backgroundColor = "rgba(0,0,0,0.4)";


}

function emmaNavclose() {
  document.getElementById('iconSideBar').style.display = 'none';
  document.getElementById('emmaNav').style.left = '-250px';
    // document.body.style.backgroundColor = "rgb(255,255,255)";
  document.getElementById('mainNav').style.backgroundColor = '#1a1d20';

}