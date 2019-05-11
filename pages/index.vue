<template>
  <div>
      <header class="masthead" style="background-image: url('/img/IMG_1522.jpg');background-position: top;background-size: cover;">
          <div class="overlay"></div>
          <div class="container">
              <div class="row">
                  <div class="col-md-10 col-lg-8 mx-auto">
                      <div class="site-heading">
                          <h1>Coming Soon!</h1><span class="subheading">Get ready to explore the world in the footsteps of a wanderer</span></div>
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
          <div class="row">
              <div class="col-md-10 col-lg-8">
                  <div class="post-preview">
                      <nuxt-link to="/chatakpur">
                          <h2 class="post-title">Chatakpur - A chilly weekend getaway in the lap of nature</h2>
                          <h3 class="post-subtitle">If you are a person looking for a quick weekend getaway from Kolkata and also want to escape the scorching heat and chaos and crowd of the city, wait no more...</h3>
                      </nuxt-link>
                      <p class="post-meta">Posted by&nbsp;<a href="#">Wide Eyed Wanderer on May 10, 2019</a></p>
                  </div>
                  <hr>
                  <div class="clearfix"><button class="btn btn-primary float-right" type="button">Older Posts&nbsp;⇒</button></div>
              </div>
          </div>
      </div>
      <footer>
          <div class="container">
              <div class="row">
                  <div class="col-md-10 col-lg-8 mx-auto">
                      <ul class="list-inline text-center">
                        <li class="list-inline-item"><span class="fa-stack fa-lg"><i class="fa fa-circle fa-stack-2x"></i><i class="fa fa-twitter fa-stack-1x fa-inverse"></i></span></li>
                        <li class="list-inline-item">
                            <a href="https://www.facebook.com/wide.eyed.wanderer123">
                                <span class="fa-stack fa-lg"><i class="fa fa-circle fa-stack-2x"></i><i class="fa fa-facebook fa-stack-1x fa-inverse"></i></span>
                            </a>
                        </li>
                        <li class="list-inline-item">
                            <a href="https://www.youtube.com/channel/UCzZbwxB8Bj5uBzAIhyNpGbw">
                                <span class="fa-stack fa-lg"><i class="fa fa-circle fa-stack-2x"></i><i class="fa fa-youtube fa-stack-1x fa-inverse"></i></span>
                            </a>
                        </li>
                      </ul>
                      <p class="text-muted copyright">Copyright&nbsp;©&nbsp;Wide Eyed Wanderer 2019</p>
                  </div>
              </div>
          </div>
      </footer>
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
            regemail:''
        }
    },

    created(){
        this.$axios.get("/hit")
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
