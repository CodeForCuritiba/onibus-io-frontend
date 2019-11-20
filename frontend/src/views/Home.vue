<template>
  <v-container fluid fill-height class="full-width">
    <v-row align="center" justify="center">
      <v-col cols="12" align="center" justify="center">
        <v-row align="center" justify="center">
          <v-icon size="300">mdi-bus</v-icon>
        </v-row>
      </v-col>
      <v-col cols="12" md="8">
        <v-text-field
          label="Linha"
          placeholder="Busque aqui por código da linha"
          outlined
          append-icon="mdi-magnify"
        ></v-text-field>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'home'
}
</script>
<style scoped>
.full-width {
  width: 100vh;
}
</style>
