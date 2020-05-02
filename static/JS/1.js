let alreadyClicked = false;

function menuButtonOnClick(){
  switch(alreadyClicked){
    case false:
      document.getElementById('menuSubparagraph').style.display='block';
      alreadyClicked = true;
      break;
    case true:
      document.getElementById('menuSubparagraph').style.display='none';
      alreadyClicked = false;
      break;
  }

}