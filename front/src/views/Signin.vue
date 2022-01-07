<template>
  <v-form
    ref="form"
    v-model="valid"
    lazy-validation
  >
    <v-text-field
      v-model="name"
      :counter="10"
      :rules="nameRules"
      label="Name"
      required
    ></v-text-field>

    <v-text-field
      v-model="email"
      :rules="emailRules"
      label="E-mail"
      required
    ></v-text-field>

    <v-select
      v-model="select"
      :items="items"
      :rules="[v => !!v || 'Item is required']"
      label="Item"
      required
    ></v-select>

    <v-checkbox
      v-model="checkbox"
      :rules="[v => !!v || 'You must agree to continue!']"
      label="Do you agree?"
      required
    ></v-checkbox>

    <v-btn
      :disabled="!valid"
      color="success"
      class="mr-4"
      @click="validate"
    >
      Validate
    </v-btn>

    <v-btn
      color="error"
      class="mr-4"
      @click="reset"
    >
      Reset Form
    </v-btn>

    <v-btn
      color="warning"
      @click="resetValidation"
    >
      Reset Validation
    </v-btn>
  </v-form>
</template>


<script>
export default {

/* 
         <v-bottom-navigation  transparent elevation="0"  opacity="0" height="100">
            <v-app-bar-icon small class="ml-2" @click="drawer=!drawer"></v-app-bar-icon>
            <v-bottom-navigation-title class="black--text">
                <span class="black--text">Hokusai</span>
            </v-bottom-navigation-title>
            <v-spacer></v-spacer>
            <v-btn text elevation="0" small transparent plain opacity="0" v-for="link in links" :key="link.text" router :to="link.route" >
                <v-chip small elevation="0" outlined color="blue-grey lighten-2"> 
                    <span>{{link.text}}</span>
                </v-chip>
            </v-btn>
            <v-btn small transparent>
                <span class="black--text">Sign Out</span>
                <v-icon>mdi-open-in-new</v-icon>
            </v-btn>
        </v-bottom-navigation>
        
        
#$window-transition	
.3s cubic-bezier(.25, .8, .50, 1) !default;

background-image: linear-gradient(to bottom, #869696, #94a1a1, #a1acab, #afb8b7, #bdc3c2, #c7cccb, #d1d5d5, #dbdede, #e4e6e7, #edeeef, #f6f7f7, #ffffff);

blue grey
background-image: linear-gradient(to top, #b0bcbc, #b6c0c0, #bcc4c4, #c2c9c8, #c8cdcc, #ced3d2, #d5d8d8, #dbdede, #e4e6e7, #edeeef, #f6f7f7, #ffffff);



 <v-btn text elevation="0" small transparent plain wrap opacity="0" v-for="link in links" :key="link.text" router :to="link.route" >
                <v-chip small elevation="0" outlined color="blue-grey lighten-2"> 
                    <span>{{link.text}}</span>
                </v-chip>
            </v-btn>




  Drawer-----
  <v-app-bar-nav-icon small class="ml-2" @click="drawer=!drawer"></v-app-bar-nav-icon>
  <v-navigation-drawer v-model="drawer" app transparent >
            <v-list>
                <!-- : is to bind the data to a property-->
                <v-list-item v-for="link in links" :key="link.text" router :to="link.route" >
                    <v-list-item-action>
                        <v-icon role="img" aria-hidden="false" >{{link.icon}}</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title class="black--text">{{link.text}}</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>    
        </v-navigation-drawer>




        ------------
          <v-container class="my-5">
                <v-layout row class="mb-4 pt-4" wrap >
                   
                    <v-flex xs12 md3 xl4>
                        <v-btn small text   @click="sortby('Name')">
                            <v-icon left small > </v-icon>
                            <span>Look</span>
                        </v-btn>
                    </v-flex>
                </v-layout>
               
                    <v-layout  row class="mb-4 pt-4 xs12 md6" wrap >
                        <v-flex v-for="person in Actors" :key="person.Name">
                            <!-- boucle dans le flex sinon la carte prend la longueur de la page-->
                             <v-card flat class="text-xs-center" >
                                <div class=" grey--text">{{person.Name}}</div>        
                                <v-chip small dark >USER</v-chip> 
                              </v-card>
                        </v-flex>
                    </v-layout>
                
                 <v-divider></v-divider>
              </v-container>

              ------
              height="650" width="600"  

              cols="12" md="6"


              ------------------- test image gallery
              :src="`../assets/images(1).jpg${n * 5 + 10}`"
                                                    :lazy-src="`../assets/images(1).jpg${n * 5 + 10}`"
              
           
            <v-app-bar-title class="ml-4 mr-8 black--text" wrap>
                   
                    <span Name="title" class="font-weight-bold">Hokusai</span>
              
            </v-app-bar-title>
           

           -----------------------------------------
            
*/


}
</script>



