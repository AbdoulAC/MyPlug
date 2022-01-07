<template>
    
    <div class="home">

                <div >
                   <v-container fluid>
                       
                            <v-row  class="justify-center">
                                <v-col cols="12" xs="4" sm="4" lg="4" xl="6" class="mx-4 my-4 " v-for="A in Actors" :key="A.Name" >
                                    <transition name="card" >
                                       <v-hover v-slot="{ hover }">
                                            <v-card
                                            :elevation="hover ? 16 : 2"
                                            class="blue-grey lighten-2"
                                            outlined 
                                            id="card"
                                            :class="{ 'on-hover': hover }"
                                            max-width="450"
                                            max-heigth="450"
                                            router to="/views/Cards/Card1"
                                            relative
                                            >
                                                    <v-responsive :aspect-ratio="1/1">
                                                  
                                                    
                                                     <v-img
                                                        class="white--text align-end"
                                                        
                                                        src="../assets/téléchargement.jpg"
                                                        >
                                                        
                                                     </v-img>
                                                    <v-card-title class="black--text font-weight-bold">{{A.Name}}</v-card-title>
                                                    </v-responsive> 
                                            </v-card>   
                                         </v-hover> 
                                    </transition>    
                                </v-col>
                            </v-row>
                      
                   </v-container>
                </div>
         
    </div>

    
</template>

<script>
export default {
    data(){
        return{
            Actors:[
                {Name:'Akira'},
                {Name:'Obito'},
                {Name:'Sanji'},
                {Name:'luffy'},
                {Name:'Blackbeard'},
                {Name:'Naruto'},
                {Name:'Kirua'},
                {Name:'Garp'},
                {Name:'Torino'},
                {Name:'Reyligh'},
                
                ],
            Images:[
                {img:'../assets/images(1).jpg'},
                {img:'../assets/images(1).jpg'},
                {img:'../assets/images.jpg'},
                {img:'../assets/téléchargement (1).jpg'},
                {img:'../assets/téléchargement.jpg'},
                {img:'../assets/Tsunami_by_hokusai_19th_century.jpg'},
            ]
        }

    },
    methods:
    {
        sortby(param)  {
           this.Actors.sort((a,b) => a[param] < b[param] ? -1 : 1)
        },

    
      }
    
 }




</script>


<style>

.v-template{
      
background-image: linear-gradient(to bottom, #ffffff, #fefcfe, #fffafb, #fff7f6, #fdf5f0, #f9f0e7, #f2ecde, #eae8d6, #e2dfc8, #dbd6b9, #d5ccab, #cec39d);
}

.card-enter-active, .card-leave-active{
 transition: opacity 5s ease-in-out, transform 5s ease-in-out;
}


.card-enter-active{
  transition-delay: 5s;
}

 /* when the animation starts*/
.card-enter, .card-leave-to{
opacity: 0;
transform: translateY(50px);
}

/* when it ends, view-leave (1)-> view-leave(0) to en 0.5s vice versa pour enter */
.card-enter-to, .card-leave{
  opacity: 1;
  transform: translateY(0px);
}
</style>