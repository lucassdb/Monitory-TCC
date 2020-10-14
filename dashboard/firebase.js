(function() {
  const config = {
      apiKey: "AIzaSyCCE4yveEuH_09vThP5U1J0Oi3d1-r2muY",
      authDomain: "teste-90925.firebaseapp.com",
      databaseURL: "https://teste-90925.firebaseio.com",
      projectId: "teste-90925",
      storageBucket: "teste-90925.appspot.com",
      messagingSenderId: "267430548654"
    };

  firebase.initializeApp(config);
  const entrada = document.getElementById('entrada');
  const dbRef = firebase.database().ref().child('entrada');
  dbRef.on('value', snap => entrada.innerText = snap.val());
  
  // const saida = document.getElementById('saida');
  // const dbRef = firebase.database().ref().child('saida');
  // dbRef.on('value', snap => saida.innerText = snap.val());
  
  // const momento = document.getElementById('momento');
  // const dbRef = firebase.database().ref().child('momento');
  // dbRef.on('value', snap => momento.innerText = snap.val());

}());
