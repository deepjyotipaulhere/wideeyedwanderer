<template>
  <div>
      <header class="masthead" style="background-image: url('/img/IMG_1522.jpg');background-position: top;background-size: cover;">
          <div class="overlay"></div>
          <div class="container">
              <div class="row">
                  <div class="col-md-10 col-lg-8 mx-auto">
                      <div class="site-heading">
                          <h3 class="display-4" style="font-weight:800">Wide Eyed Wanderer</h3><span class="subheading">Get ready to explore the world in the footsteps of a wanderer</span></div>
                  </div>
              </div>
          </div>
      </header>
      <div class="container">
        <div class="row">
            <div class="col-md-4"></div>
            <div class="col-md-4"><label>Subscribe to newsletter</label>
                <form>
                    <div class="input-group">
                        <div class="input-group-prepend"><span class="input-group-text"><i class="fa fa-envelope-o"></i></span></div><input type="email" required v-model="regemail" class="form-control" placeholder="Enter your email" style="height: 53px;" />
                        <div class="input-group-append"><button class="btn btn-primary" type="button" @click.prevent="register">Go!</button></div>
                    </div>
                </form>
            </div>
            <div class="col-md-4"></div>
        </div>
        <br>
        <div class="row">
            <div class="col-md-10 col-lg-8">
                <div class="post-preview" v-for="(x,i) in posts" :key="i">
                    <nuxt-link :to="'/post?v='+x._id+'&title='+x.title+'&cover='+x.coverphoto">
                        <h2 class="post-title" style="font-weight:bolder !important">{{x.title}}</h2>
                        <h5 class="post-subtitle">{{x.text}}</h5>
                    </nuxt-link>
                    <p class="post-meta">Posted by&nbsp;<a href="#">{{x.name}} on {{new Date(x.date).toDateString()}}</a></p>
                </div>
                <hr>
                <!-- <div class="clearfix"><button class="btn btn-primary float-right" type="button">Older Posts&nbsp;⇒</button></div> -->
            </div>
            <div class="col-md-2 col-lg-4">
                <iframe src="https://www.youtube.com/embed/3GC1Ur3oNMo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="width:100%;height:200px"></iframe>
            </div>
        </div>
      </div>
        <div role="dialog" tabindex="-1" class="modal fade" id="newmodal">
            <div class="modal-dialog modal-dialog-centered" role="document">
                <div class="modal-content" style="background-image:url('https://images.pexels.com/photos/414171/pexels-photo-414171.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260');background-size:cover">
                    <!-- <div class="modal-header">
                        <h4 class="modal-title">Modal Title</h4><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button></div> -->
                    <div class="modal-body" style="padding:2em 1em 1.5em 1em">
                        <button type="button" class="close text-white" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                        <h3 class="text-center text-black">Welcome aboard!</h3>
                        <p class="text-white">From now on, you will receive latest news and blog posts via email. So, start exploring!</p>
                    </div>
                    <!-- <div class="modal-footer"><button class="btn btn-light" type="button" data-dismiss="modal">Close</button><button class="btn btn-primary" type="button">Save</button></div> -->
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default{
    data(){
        return {
            regemail:'',
            posts:[]
        }
    },

    head:{
        meta:[
            { name: 'twitter:image', content: '/img/banner.png' },
            { name: 'description', content: 'A traveller with the urge to explore the world' },
            { name: 'og:type', content: 'website' },
            { name: 'og:image', content: '/img/banner.png' },
            { name: 'twitter:card', content: 'summary_large_image' },
        ]
    },

    created(){
        this.$axios.get("/hit")
        this.$axios.get("/getuserposts/0").then(response=>{
            this.posts=response.data
        })
    },

    methods:{
        register(){
            if(this.regemail!='')
                this.$axios.post("/registernewsletter",{'regemail':this.regemail}).then(response=>{
                    if (response.data=="ok")
                    {
                        $('#newmodal').modal()
                    }
                }).catch(e=>{
                    if (e.response.data=="blank")
                    alert("Please enter your email")
                })
            else
            {}
        }
    }
}
</script>

<style>
</style>
