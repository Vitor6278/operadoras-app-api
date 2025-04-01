<template>
  <div>
    <h1>Consultas de Operadoras de Saúde</h1>

    <div>
      <label for="searchType">Buscar por:</label>
      <select v-model="searchType" id="searchType">
        <option value="nome">Nome da Operadora</option>
        <option value="registro">Registro ANS</option>
        <option value="cnpj">CNPJ</option>
        <option value="modalidade">Modalidade</option>
      </select>
    </div>

    <input
      v-model="searchQuery"
      :placeholder="getPlaceholder"
      @keyup.enter="performSearch"
    />
    <button @click="performSearch">Buscar</button>

    <div v-if="isLoading" class="loading-feedback">Carregando...</div>

    <table v-if="!isLoading && Array.isArray(operadoras) && operadoras.length > 0">
      <thead>
        <tr>
          <th>Razão Social</th>
          <th>Registro ANS</th>
          <th>CNPJ</th>
          <th>Modalidade</th>
          <th>Relevância</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="operadora in operadoras" :key="String(operadora.Registro_ANS)">
          <td>{{ operadora.Razao_Social }}</td>
          <td>{{ String(operadora.Registro_ANS) }}</td>
          <td>{{ operadora.CNPJ }}</td>
          <td>{{ operadora.Modalidade }}</td>
          <td>{{ String(operadora.Relevancia) }}</td>
        </tr>
      </tbody>
    </table>

    <p v-if="!isLoading && searchPerformed && searchQuery && operadoras.length === 0" class="no-results">
      Nenhum resultado encontrado para "{{ searchQuery }}".
    </p>
  </div>
</template>

<script>
import appLogic from './App.js';
import './App.css';
export default {
  ...appLogic
};
</script>

<style>
@import url(https://fonts.googleapis.com/css?family=Exo:100);

/* Background data (Original source: https://subtlepatterns.com/grid-me/) */
/* Animations */
@-webkit-keyframes bg-scrolling-reverse {
  100% {
    background-position: 50px 50px;
  }
}
@-moz-keyframes bg-scrolling-reverse {
  100% {
    background-position: 50px 50px;
  }
}
@-o-keyframes bg-scrolling-reverse {
  100% {
    background-position: 50px 50px;
  }
}
@keyframes bg-scrolling-reverse {
  100% {
    background-position: 50px 50px;
  }
}
@-webkit-keyframes bg-scrolling {
  0% {
    background-position: 50px 50px;
  }
}
@-moz-keyframes bg-scrolling {
  0% {
    background-position: 50px 50px;
  }
}
@-o-keyframes bg-scrolling {
  0% {
    background-position: 50px 50px;
  }
}
@keyframes bg-scrolling {
  0% {
    background-position: 50px 50px;
  }
}

/* Main styles */
body {
  margin-top: 13.5rem;
  color: #4d4a4a;
  font: 400 16px/1.5 exo, ubuntu, "segoe ui", helvetica, arial, sans-serif;
  text-align: center;
  /* img size is 50x50 */
  background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAIAAACRXR/mAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAAADqYAAAXb5JfxUYAAABnSURBVHja7M5RDYAwDEXRDgmvEocnlrQS2SwUFST9uEfBGWs9c97nbGtDcquqiKhOImLs/UpuzVzWEi1atGjRokWLFi1atGjRokWLFi1atGjRokWLFi1af7Ukz8xWp8z8AAAA//8DAJ4LoEAAlL1nAAAAAElFTkSuQmCC") repeat 0 0;
  -webkit-animation: bg-scrolling-reverse 0.92s infinite;
  /* Safari 4+ */
  -moz-animation: bg-scrolling-reverse 0.92s infinite;
  /* Fx 5+ */
  -o-animation: bg-scrolling-reverse 0.92s infinite;
  /* Opera 12+ */
  animation: bg-scrolling-reverse 0.92s infinite;
  /* IE 10+ */
  -webkit-animation-timing-function: linear;
  -moz-animation-timing-function: linear;
  -o-animation-timing-function: linear;
  animation-timing-function: linear;
}

body::before {
  content: "Intuitive Care";
  font-size: 8rem;
  font-weight: 100;
  font-style: normal;
}
</style>