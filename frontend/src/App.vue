<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-icon>mdi-bus</v-icon>
      <v-toolbar-title class="title ml-1">Onibus.IO</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn href="https://github.com/CodeForCuritiba/onibus-io-frontend" target="_blank" text>
        <v-icon>mdi-github-face</v-icon>
      </v-btn>
    </v-app-bar>
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: 'OnibusIO',
  data: () => ({
    //
  })
}
</script>
