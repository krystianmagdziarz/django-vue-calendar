<template>
    <div class="mt-6">
        <h3>Kalendarz</h3>
        <v-row v-if="loaded">
            <v-col>
              <v-sheet height="500">
                <v-calendar
                  :now="today"
                  :value="today"
                  color="primary"
                >
                  <template v-slot:day="{ date }">
                    <v-row
                      class="fill-height"
                    >
                      <template v-if="date === today && tracked[date]">
                        <v-sheet
                          v-for="(percent, i) in tracked[date]"
                          :key="i"
                          :color="colors[i]"
                          :width="`${percent}%`"
                          height="100%"
                          tile
                        ></v-sheet>
                      </template>
                      <template v-else>
                        <v-sheet
                          v-for="(percent, i) in tracked[date]"
                          :key="i"
                          height="100%"
                          tile
                        ></v-sheet>
                      </template>
                    </v-row>
                  </template>
                </v-calendar>
              </v-sheet>
            </v-col>
          </v-row>
    </div>
</template>

<script>
    export default {
        name: "Calendar",
        data() {
            return {
                today: String,
                type: 'month',
                tracked: {},
                colors: [],
                category: ["Days"],
                days: [],
                loaded: false
            }
        },
        methods: {
            async fetchDays() {
                const res = await fetch('http://localhost:8000/api/calendar');
                return await res.json();
            },
        },
        async mounted() {
            this.days = await this.fetchDays();
            this.loaded = true;
            this.today = this.days["today"];
            Object.entries(this.days["days"]).forEach(([key, value]) => {
                let day_number = parseInt(key.slice(-2));
                let array_value = Array(day_number).fill(0);
                array_value[day_number-1] = 1/day_number*100;
                this.tracked[key] = array_value;
                this.colors.push(value);
            });
            console.log(this.tracked);
        }
    }
</script>

<style scoped>

</style>