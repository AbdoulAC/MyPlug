<template>

    <v-bottom-navigation r v-model="drawer"  opacity="0"  background-color="white" height="20" fluid elevation="0" flat app >   
            <v-btn :ripple="false">
                <v-icon> mdi-account-cash </v-icon>
            </v-btn>

            <v-spacer>
                     
            </v-spacer>

            <v-btn :ripple="false">
                    <v-icon>  mdi-battery-charging-high  </v-icon>
            </v-btn>
            
            <v-spacer>
                     
            </v-spacer>

             <v-btn :ripple="false" depressed>
                    <v-icon>  mdi-alien </v-icon>
            </v-btn>

    </v-bottom-navigation>


</template>

<script>
export default {
    
}
</script>

<style>

</style>