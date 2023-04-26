const form = document.querySelector('#form');
const numEjecucionesInput = document.querySelector('#num-ejecuciones');
const contadorDiv = document.querySelector('#contador');

form.addEventListener('submit', e => {
  e.preventDefault();
  const numEjecuciones = parseInt(numEjecucionesInput.value);
  contadorDiv.innerText = numEjecuciones;
  let contador = numEjecuciones;
  const interval = setInterval(() => {
    contador--;
    contadorDiv.innerText = contador;
    if (contador === 0) {
      clearInterval(interval);
      alert('Se han ejecutado todas las veces');
    }
  }, 1000);
});
