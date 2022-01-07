<template >
    <nav>
        <!--including the font on the navbar made it work on every page whereas the contrary wouldn't work-->
       <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP&subset=latin,latin-ext" rel='stylesheet' type='text/css'>
        
       <v-app-bar  
       id="Nav"
       elevation="0"  
      
       height="60" 
       app
       background-color="transparent"
       >
            <v-btn 
            elevation="0"  
            height="25" 
            width="25" 
            fab
            
            class="mr-4" 
            >
                <v-img 
                src="../assets/Hokusai.png" height="25" width="25" >
                </v-img>

            </v-btn>   
            
            
           
           
            <v-tabs 
            right 
            fixed-tabs >
                <v-tabs-slider color="grey lighten-1"></v-tabs-slider>
                 <v-tab 
                 elevation="0"
                 small
                 transparent
                 plain
                 opacity="0"
                 :ripple="false"
                 v-for="link in links" 
                 :key="link.text" 
                 router :to="link.route"
                        >
                            <v-chip small text plain outlined> 
                             <span >{{link.text}}</span>
                             </v-chip>
                 </v-tab>
             </v-tabs>
            
           
            <v-btn small transparent rounded  >
                
                <v-icon>mdi-open-in-new</v-icon>
            </v-btn>
        </v-app-bar>
        <!-- continuer le remplacement des toolbar par appbars-->
        <!-- drawer invisible by default thus the boolean-->
        
    </nav>
</template>

<script>

export default {

    data(){
        return{
            drawer:false,
            links:[
                    {icon:'mdi-snowman', text:'home', route: '/views/Dashboard'},
                    {icon:'mdi-snowman', text:'dash', route: '/'},
                    {icon:'mdi-snowman', text:'About', route: '/views/About'},
                    {icon:'mdi-snowman', text:'team', route: 'Team'},
                 ]
            }
        },
    /*
        lights() {
                @click="lights()"
                if(drawer=="false"){
        
                    document.getElementById('Navbar').querySelector(Navbar).style.color = "Black";
                } 
                else{
                    document.getElementById('Navbar').querySelector(Navbar).style.color = "white";
                }   
            }
    */
    };
 


   

</script>


<style>
.title{
    transform: rotate(90deg);
    display: inline-block;
}
</style>
