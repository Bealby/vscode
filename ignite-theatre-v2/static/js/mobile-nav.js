// Full Screen Overlay Responsive Nav Bar Mobile

function openMenu(){
  document.getElementById("navbar").style.height = "100%";
}

function openMenuArchive(){
  document.getElementById("navbar-archive").style.height = "100%";
}

function openMenuGallery(){
  document.getElementById("navbar-gallery").style.height = "100%";
}

function closeMenu(){
  document.getElementById("navbar").style.height = "0%";
}

function closeMenuGallery (){
  document.getElementById("navbar-gallery").style.height = "0%";
}

function closeMenuArchive (){
  document.getElementById("navbar-archive").style.height = "0%";
}

function closeAllMenu (){
  document.getElementById("navbar-gallery").style.height = "0%";
  document.getElementById("navbar").style.height = "0%";
  document.getElementById("navbar-archive").style.height = "0%";
}