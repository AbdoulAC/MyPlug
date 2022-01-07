<template>
    <div class="team">
            <h1>Team Page here</h1>
          
            
            <v-container class="my-5">
            
            </v-container>
    
    </div>
 
</template>

<script>
export default {
    data(){
        return{
            Actors:[
                
                ]
        }

    },
    methods:
    {
        sortby(param)  {
           this.Actors.sort((a,b) => a[param] < b[param] ? -1 : 1)
        }
    
    }
}
</script>


<style>

</style>