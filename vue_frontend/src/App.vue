<template>
  <v-app>
    <v-main class="text-center">
      <h1>Zadanie testowe!</h1>
      <p>Strona pokazuje wykorzystanie Vuetify oraz Django do budowy komponentu kalendarza.</p>
      <Calendar/>
    </v-main>
  </v-app>
</template>

<script>
import Calendar from './components/Calendar';

export default {
  name: 'App',

  components: {
    Calendar,
  },

  data: () => ({
    //
  }),
};
</script>
