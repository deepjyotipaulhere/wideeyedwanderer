<template>
    <div>
        <header class="masthead" :style="{'background-image':'url(http://www.wideeyedwanderer.in/api/getimage/'+content.coverphoto+')', 'background-position':'center', 'background-size':'cover'}">
            <div class="overlay"></div>
            <div class="container">
                <div class="row">
                    <div class="col-md-10 col-lg-8 mx-auto">
                        <div class="site-heading">
                            <h1>{{content.place}}</h1>
                            <span class="subheading"><i class="fa fa-map-marker"></i> {{content.address}}</span>
                        </div>
                    </div>
                </div>
            </div>
        </header>
        <div class="container">
            <h1>{{content.title}}</h1>
            <span class="subheading">by {{content.name}}</span>
            <span class="subheading">published on {{new Date(content.date).toDateString()}}</span>
            <br>
            <br>
            <no-ssr>
            <social-sharing :url='$route.fullpath' inline-template>
                <div>
                    <button>
                        <network network="facebook">
                            <i class="fa fa-fw fa-facebook"></i>
                        </network>
                    </button>
                    <button>
                    <network network="linkedin">
                    <i class="fa fa-fw fa-linkedin"></i>
                    </network>
                    </button>
                    <button>
                    <network network="pinterest">
                    <i class="fa fa-fw fa-pinterest"></i>
                    </network>
                    </button>
                    <button>
                    <network network="reddit">
                    <i class="fa fa-fw fa-reddit"></i>
                    </network>
                    </button>
                    <button>
                    <network network="twitter">
                    <i class="fa fa-fw fa-twitter"></i>
                    </network>
                    </button>
                    <button>
                    <network network="whatsapp">
                    <i class="fa fa-fw fa-whatsapp"></i>
                    </network>
                    </button>
                </div>
            </social-sharing>
            </no-ssr>
            <br>
            <div v-html="content.text"></div>
        </div>
    </div>
</template>

<script>
var SocialSharing = require('vue-social-sharing');
export default {
    head(){
        return{
            title: this.$route.query.title+" - Wide Eyed Wanderer",
            meta:[
                { name: 'og:type', content: 'website' },
                { name: 'og:title', content: this.$route.query.title+" - Wide Eyed Wanderer" },
                { name: 'og:description', content: this.$route.query.title },
                // { name: 'og:url', content: location.href},
                { name: 'og:image', content: 'http://www.wideeyedwanderer.in/api/getimage/'+this.$route.query.cover },

                { name: 'twitter:title', content: this.$route.query.title+" - Wide Eyed Wanderer" },
                { name: 'twitter:description', content: this.$route.query.title },
                { name: 'twitter:image', content: 'http://www.wideeyedwanderer.in/api/getimage/'+this.$route.query.cover },

            ]
            
        }
    },
    data(){
        return {
            content:{}
        }
    },
    mounted(){

    },
    components:{
        SocialSharing
    },
    created(){
        this.load()
    },
    methods:{
        load(){
            this.$axios.get("/getblog/"+this.$route.query.v).then(response=>{
                this.content=response.data
            }).then(()=>{
                this.$axios.get("/view/"+this.$route.query.v)
            })
        }
    }
}
</script>

<style>

</style>
