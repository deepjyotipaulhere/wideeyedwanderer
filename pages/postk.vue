<template>
    <div>
        <header class="masthead" style="background-image: url('/img/IMG_2309.jpg');background-position: bottom;background-size: cover;">
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
            <social-sharing :url='"http://www.wideeyedwanderer.in/post?v="+$route.query.v' inline-template>
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
            <div v-html="content.text"></div>
        </div>
    </div>
</template>

<script>
var SocialSharing = require('vue-social-sharing');
export default {
    head(){
        return{
            // meta: [
            //     { name: 'twitter:image', content: 'http://www.wideeyedwanderer.in/img/IMG_2309.jpg' },
            //     { name: 'description', content: this.content.title },
            //     { name: 'og:type', content: 'website' },
            //     { name: 'og:url', content: process.browser?location.href:'' },
            //     { name: 'og:image', content: 'http://www.wideeyedwanderer.in/img/IMG_2309.jpg' },
            //     { name: 'twitter:card', content: 'summary_large_image' },
            // ],
        }
    },
    data(){
        return {
            content:{}
        }
    },
    mounted(){
        document.title=this.content.title+" - Wide Eyed Wanderer"
        var meta=document.createElement("meta")
        meta.name="twitter:image"
        meta.content="http://www.wideeyedwanderer.in/img/IMG_2309.jpg"
        document.getElementsByTagName('head')[0].appendChild(meta)
        
        var meta=document.createElement("meta")
        meta.name="description"
        meta.content=this.$route.query.title
        document.getElementsByTagName('head')[0].appendChild(meta)

        var meta=document.createElement("meta")
        meta.name="og:type"
        meta.content="website"
        document.getElementsByTagName('head')[0].appendChild(meta)

        var meta=document.createElement("meta")
        meta.name="og:url"
        meta.content=process.browser?location.href:'' 
        document.getElementsByTagName('head')[0].appendChild(meta)

        var meta=document.createElement("meta")
        meta.name="og:image"
        meta.content="http://www.wideeyedwanderer.in/img/IMG_2309.jpg"
        document.getElementsByTagName('head')[0].appendChild(meta)

        var meta=document.createElement("meta")
        meta.name="twitter:card"
        meta.content="summary_large_image"
        document.getElementsByTagName('head')[0].appendChild(meta)

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
            })
        }
    }
}
</script>

<style>

</style>
