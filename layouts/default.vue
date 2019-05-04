<template>
  <div>
    <nav class="navbar navbar-dark navbar-expand-lg fixed-top" id="mainNav">
        <div class="container"><a class="navbar-brand" href="index.html"><img src="/img/fulllogo.png" height="50px"></a><button data-toggle="collapse" data-target="#navbarResponsive" class="navbar-toggler" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"><i class="fa fa-bars"></i></button>
          <div
              class="collapse navbar-collapse" id="navbarResponsive">
              <ul class="nav navbar-nav ml-auto">
                  <li class="nav-item" role="presentation"><a class="nav-link" href="index.html">Home</a></li>
                  <li class="nav-item" role="presentation"><a class="nav-link" href="about.html">About us</a></li>
                  <li class="nav-item" role="presentation"><a class="nav-link" href="contact.html">Contact us</a></li>
                  <li class="nav-item" role="presentation"><a class="nav-link" href="post.html">Blog Post</a></li>
              </ul>
          </div>
        </div>
      </nav>
    <nuxt />
  </div>
</template>

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
