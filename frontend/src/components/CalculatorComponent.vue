<template>
  <div style="display: flex; align-items: center;">
    <input v-model="value1" type="number" placeholder="Wartość 1" />
    <select v-model="operation">
      <option v-for="op in availableOperations" :key="op" :value="op">{{ op }}</option>
    </select>
    <input v-model="value2" type="number" placeholder="Wartość 2" />
    <p style="margin: 0 10px;">=</p>
    <input
      v-if="result !== null"
      v-model="result.value"
      :style="{ color: result.color }"
      type="text"
      readonly
    />
    <p v-if="errorMessage" style="color: red;">{{ errorMessage }}</p>
    <button @click="calculate">Count</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      value1: "",
      value2: "",
      operation: "addition",
      result: { value: "", color: "red" }, // Ustawienie wyniku na obiekt z domyślnymi wartościami
      errorMessage: "",
      availableOperations: [],
    };
  },
  mounted() {
    this.fetchOperations();
  },
  methods: {
    calculate() {
      this.result = { value: "", color: "red" }; // Wyczyszczenie poprzedniego wyniku
      this.errorMessage = ""; // Wyczyszczenie poprzedniego komunikatu o błędzie

      const requestData = {
        x: parseFloat(this.value1),
        y: parseFloat(this.value2),
      };

      axios
        .post(`http://localhost:80/calculate/${this.operation}`, requestData)
        .then((response) => {
          this.result.value = response.data.result;
          if (response.data.color) {
            this.result.color = response.data.color;
          }
        })
        .catch((error) => {
          if (error.response) {
            this.errorMessage = "Something is wrong, maybe check the values.";
            console.error("Błąd podczas obliczeń:", error.response.data.detail);
          } else if (error.request) {
            this.errorMessage = "Something went wrong, please try again.";
            console.error("Błąd podczas obliczeń: Brak odpowiedzi");
          } else {
            this.errorMessage = "Unknown error occurred.";
            console.error("Błąd podczas obliczeń:", error.message);
          }
        });
    },
    fetchOperations() {
      axios
        .get("http://localhost:80/operations")
        .then((response) => {
          this.availableOperations = response.data;
        })
        .catch((error) => {
          console.error("Błąd podczas pobierania operacji:", error.message);
        });
    },
  },
};
</script>
