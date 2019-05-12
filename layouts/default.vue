<template>
  <div>
    <nav class="navbar navbar-dark navbar-expand-lg fixed-top" id="mainNav">
      <div class="container"><a class="navbar-brand" href="/"><img src="/img/fulllogo.png" height="50px"></a><button data-toggle="collapse" data-target="#navbarResponsive" class="navbar-toggler" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"><i class="fa fa-bars"></i></button>
        <div
            class="collapse navbar-collapse" id="navbarResponsive">
            <ul class="nav navbar-nav ml-auto">
                <li class="nav-item" role="presentation"><nuxt-link class="nav-link" to="/">Home</nuxt-link></li>
                <!-- <li class="nav-item" role="presentation"><a class="nav-link" href="about.html">About us</a></li> -->
                <li class="nav-item" role="presentation" v-if="$cookies.get('_bid')"><nuxt-link class="nav-link" to="/myposts">My Posts</nuxt-link></li>
                <li class="nav-item" role="presentation"><nuxt-link class="nav-link" :to="$cookies.get('_bid')?'/write':'/login'">Write your blog</nuxt-link></li>
                <li class="nav-item" role="presentation" v-if="$cookies.get('_bid')"><button class="btn btn-link btn-sm text-danger" style="padding-top:7px;padding-bottom:7px" @click.prevent="logout">Log Out</button></li>
            </ul>
        </div>
      </div>
    </nav>
    <nuxt style="clear:both" />
    <footer style="clear:both">
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
  </div>
</template>
<script>
export default {
  methods:{
    logout(){
      this.$cookies.remove("_bid")
      location.href="/"
    }
  }
}
</script>

<style>
html {
  font-family: 'Source Sans Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI',
    Roboto, 'Helvetica Neue', Arial, sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
}

*,
*:before,
*:after {
  box-sizing: border-box;
  margin: 0;
}

.button--green {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #3b8070;
  color: #3b8070;
  text-decoration: none;
  padding: 10px 30px;
}

.button--green:hover {
  color: #fff;
  background-color: #3b8070;
}

.button--grey {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #35495e;
  color: #35495e;
  text-decoration: none;
  padding: 10px 30px;
  margin-left: 15px;
}

.button--grey:hover {
  color: #fff;
  background-color: #35495e;
}
</style>
