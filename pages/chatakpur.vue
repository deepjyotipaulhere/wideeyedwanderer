<template>
    <div>
        <header class="masthead" style="background-image: url('/img/IMG_2309.jpg');background-position: bottom;background-size: cover;">
            <div class="overlay"></div>
            <div class="container">
                <div class="row">
                    <div class="col-md-10 col-lg-8 mx-auto">
                        <div class="site-heading">
                            <h1>Chatakpur</h1>
                            <span class="subheading"><i class="fa fa-map-marker"></i> Chatakpur, Darjeeling, West Bengal, India</span>
                        </div>
                    </div>
                </div>
            </div>
        </header>
        <div class="container">
            <h1>A chilly weekend getaway in the lap of nature</h1>
            <span class="subheading">by Wide Eyed Wanderer</span>
            <br>
            <br>
            <social-sharing :url='"http://www.wideeyedwanderer.in/chatakpur"' inline-template>
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
            <br>
            <div v-html="content"></div>
        </div>
    </div>
</template>

<script>
var SocialSharing = require('vue-social-sharing');
export default {
    head:{
        title: 'Chatakpur, West Bengal - Wide Eyed Wanderer',
        meta: [
            { name: 'twitter:image', content: '/img/IMG_2309.jpg' },
            { name: 'description', content: 'A chilly weekend getaway in the lap of nature' },
            { name: 'og:type', content: 'website' },
            { name: 'og:image', content: '/img/IMG_2309.jpg' },
            { name: 'twitter:card', content: 'summary_large_image' },
        ],
    },
    data(){
        return {
            content:''
        }
    },
    components:{
        SocialSharing
    },
    created(){
        this.load()
    },
    methods:{
        load(){
            this.$axios.get("/chatakpur").then(response=>{
                this.content=response.data.text
            })
        }
    }
}
</script>

<style>

</style>
